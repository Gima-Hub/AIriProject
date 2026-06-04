import json
import datetime
import uuid
from pathlib import Path
from ..utils import path_resolver
from .schema import STATUS_UNKNOWN, RuntimeStateRecord

class RuntimeState:
    def __init__(self):
        self.state_file = path_resolver.get_repo_root() / "note-factory" / "health" / "runtime_state.json"
        self.data = self._load()
        self._mediate_metadata()

    @property
    def locks(self):
        """Read-only alias for repair_locks."""
        return self.data.get("repair_locks", {})

    def to_record(self, source: str = "runtime_state"):
        """Convert current state to a RuntimeStateRecord (MVP Schema)."""
        return RuntimeStateRecord(
            id=self.data.get("id", ""),
            status=self.data.get("status", STATUS_UNKNOWN),
            source=source,
            timestamp=self.data.get("timestamp", ""),
            focus=self.data.get("focus", ""),
            safe_mode=self.data.get("safe_mode", False),
            locks=self.locks,
            uncertainty={
                "audit_note": "Generated via Alias Layer (to_record)",
                "legacy_keys": list(self.data.keys())
            }
        )

    def _load(self):
        if self.state_file.exists():
            try:
                return json.loads(self.state_file.read_text(encoding="utf-8"))
            except:
                pass
        
        return {
            "safe_mode": False,
            "repair_locks": {},  # {action_id: lock_until_timestamp}
            "repair_history": [], # List of {action_id: timestamp, success: bool}
            "anomaly_count": 0,
            "last_daemon_pulse": None
        }

    def _mediate_metadata(self):
        """Inject missing mandatory metadata in memory. Persistence is deferred to explicit save()."""
        if "id" not in self.data:
            self.data["id"] = str(uuid.uuid4())
            
        if "status" not in self.data:
            self.data["status"] = STATUS_UNKNOWN
            
        if "timestamp" not in self.data:
            self.data["timestamp"] = datetime.datetime.now().isoformat()
            
        if "source" not in self.data:
            self.data["source"] = "metadata_mediation_mvp"
            
        if "focus" not in self.data:
            self.data["focus"] = "general_runtime"

    def save(self):
        self.state_file.parent.mkdir(parents=True, exist_ok=True)
        # Update timestamp on every save to reflect latest modification
        self.data["timestamp"] = datetime.datetime.now().isoformat()
        with open(self.state_file, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=2)

    def is_safe_mode(self):
        return self.data.get("safe_mode", False)

    def set_safe_mode(self, enabled: bool):
        self.data["safe_mode"] = enabled
        self.save()

    def record_repair(self, action_id: str, success: bool):
        timestamp = datetime.datetime.now().isoformat()
        self.data["repair_history"].append({
            "action_id": action_id,
            "timestamp": timestamp,
            "success": success
        })
        # Keep only last 100
        self.data["repair_history"] = self.data["repair_history"][-100:]
        self.save()

    def get_repair_count(self, action_id: str, minutes_ago: int = 10):
        threshold = datetime.datetime.now() - datetime.timedelta(minutes=minutes_ago)
        count = 0
        for entry in self.data["repair_history"]:
            if entry["action_id"] == action_id:
                if datetime.fromisoformat(entry["timestamp"]) > threshold:
                    count += 1
        return count
