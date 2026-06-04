import time
import hashlib
import datetime
from pathlib import Path
from .health_cycle import AiriHealthCycle
from .manager import TaskManager
from .runtime_state import RuntimeState
from .validator import RuntimeValidator
from .schema import STATUS_INVALID
from ..utils import path_resolver

class AiriDaemon:
    def __init__(self, manager: TaskManager, interval: int = 10):
        self.manager = manager
        self.health_cycle = AiriHealthCycle(manager)
        self.state = RuntimeState()
        self.validator = RuntimeValidator()
        self.base_interval = interval
        self.current_interval = interval
        self.repo_root = path_resolver.get_repo_root()
        self.log_file = self.repo_root / "note-factory" / "health" / "runtime.log"
        
        self.watch_paths = {
            "recovery": self.repo_root / "recovery",
            "tasks_active": path_resolver.get_active_tasks_dir(),
            "active_task_md": self.repo_root / "recovery" / "ACTIVE_TASK.md"
        }
        
        self.last_hashes = {}

    def _calculate_hash(self, path: Path):
        # ... (unchanged)
        if not path.exists():
            return "MISSING"
        
        if path.is_file():
            return hashlib.md5(path.read_bytes()).hexdigest()
        
        files = sorted(list(path.glob("*")))
        state = "".join([f"{f.name}:{f.stat().st_mtime}" for f in files])
        return hashlib.md5(state.encode()).hexdigest()

    def _log(self, message: str):
        timestamp = datetime.datetime.now().isoformat()
        prefix = "[SAFE_MODE] " if self.state.is_safe_mode() else ""
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {prefix}{message}\n")
        print(f"[*] {prefix}{message}")

    def run(self):
        self._log(f"AIri Daemon started (Base Interval: {self.base_interval}s)")
        
        # Initialize hashes
        for name, path in self.watch_paths.items():
            self.last_hashes[name] = self._calculate_hash(path)

        try:
            while True:
                self._update_pulse()
                self._run_advisory_validation()
                self._check_changes()
                self._adjust_interval()
                time.sleep(self.current_interval)
        except KeyboardInterrupt:
            self._log("AIri Daemon stopping (KeyboardInterrupt)")
        except Exception as e:
            self._log(f"AIri Daemon critical error: {e}")

    def _update_pulse(self):
        self.state.data["last_daemon_pulse"] = datetime.datetime.now().isoformat()
        self.state.save()

    def _run_advisory_validation(self):
        """
        Execute read-only validation and log advisory warning if invalid.
        Strictly isolated: does not affect runtime behavior or state.
        """
        try:
            # 1. Obtain record (ReadOnly Alias Layer)
            record = self.state.to_record(source="daemon_advisory")
            
            # 2. Validate (Pure Evaluator)
            result = self.validator.validate_runtime_state(record)
            
            # 3. Advisory Trigger (Log only if invalid)
            if result.status == STATUS_INVALID:
                safe_mode = self.state.data.get("safe_mode", False)
                anomaly_count = self.state.data.get("anomaly_count", 0)
                msg = (
                    f"[ADVISORY] Runtime state invalid: {result.errors} | "
                    f"Status: {result.status} | "
                    f"SafeMode: {safe_mode} | AnomalyCount: {anomaly_count}"
                )
                self._log(msg)
                
        except Exception as e:
            # 4. Exception Isolation: prevent validator failure from stopping daemon
            self._log(f"[ERROR] Validator failure: {e}")

    def _adjust_interval(self):
        # If in Safe Mode, slow down polling to save resources and prevent spam
        if self.state.is_safe_mode():
            self.current_interval = min(self.base_interval * 6, 60) # Max 60s
        else:
            self.current_interval = self.base_interval

    def _check_changes(self):
        changed_items = []
        for name, path in self.watch_paths.items():
            current_hash = self._calculate_hash(path)
            if current_hash != self.last_hashes[name]:
                self._log(f"Change detected in {name}: {path}")
                self.last_hashes[name] = current_hash
                changed_items.append(name)
        
        if changed_items:
            if self.state.is_safe_mode():
                self._log(f"Changes ignored in Safe Mode: {changed_items}")
                return

            self._log("Triggering auto health cycle...")
            summary = self.health_cycle.run(auto_repair=True)
            self._log(f"Health cycle complete: {summary['items_repaired']} items repaired, {summary['issues_found']} remaining.")
            
            # If issues remain after auto-repair, it might be an anomaly
            if summary['issues_found'] > 0 and summary['items_repaired'] == 0:
                self._log("Persistent issues detected. Evaluating escalation...")
