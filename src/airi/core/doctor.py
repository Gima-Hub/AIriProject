import re
from pathlib import Path
from ..utils import path_resolver

class DiagnosticResult:
    def __init__(self, severity: str, message: str, fix_suggestion: str = None):
        self.severity = severity  # INFO, WARN, ERROR
        self.message = message
        self.fix_suggestion = fix_suggestion

    def __str__(self):
        output = f"[{self.severity}] {self.message}"
        if self.fix_suggestion:
            output += f"\n    -> Suggestion: {self.fix_suggestion}"
        return output

class AiriDoctor:
    def __init__(self):
        self.repo_root = path_resolver.get_repo_root()
        self.active_tasks_dir = path_resolver.get_active_tasks_dir()
        self.recovery_file = self.repo_root / "recovery" / "ACTIVE_TASK.md"

    def run_diagnostics(self):
        results = []
        results.extend(self._check_recovery_pointer())
        results.extend(self._check_orphan_tasks())
        results.extend(self._check_result_missing())
        results.extend(self._check_directory_integrity())
        return results

    def _check_recovery_pointer(self):
        results = []
        if not self.recovery_file.exists():
            results.append(DiagnosticResult("ERROR", "ACTIVE_TASK.md missing", "Run 'airi-cli status' to regenerate pointer."))
            return results

        content = self.recovery_file.read_text(encoding="utf-8")
        
        # Extract task name from ACTIVE_TASK.md
        match = re.search(r"- NAME: (.*)", content)
        pointer_task = match.group(1).strip() if match else "UNKNOWN"

        active_tasks = [f.name for f in self.active_tasks_dir.glob("TASK_*.md")]

        if pointer_task == "NONE":
            if active_tasks:
                results.append(DiagnosticResult("WARN", f"ACTIVE_TASK.md is 'NONE' but active tasks exist: {active_tasks}", "Run 'airi-cli activate' or manual fix."))
        else:
            if pointer_task not in active_tasks:
                results.append(DiagnosticResult("ERROR", f"ACTIVE_TASK.md points to stale task: {pointer_task}", "Sync with airi-cli or delete pointer if task was archived."))
            
            # Simple Raw URL check
            url_match = re.search(r"- URL: (.*)", content)
            if url_match:
                url = url_match.group(1).strip()
                if pointer_task != "NONE" and pointer_task not in url:
                    results.append(DiagnosticResult("WARN", "Raw URL in ACTIVE_TASK.md might be inconsistent with task name.", "Run 'airi-cli activate' to resync."))

        return results

    def _check_orphan_tasks(self):
        results = []
        active_tasks = [f.name for f in self.active_tasks_dir.glob("TASK_*.md")]
        
        if not self.recovery_file.exists():
            return results
            
        content = self.recovery_file.read_text(encoding="utf-8")
        match = re.search(r"- NAME: (.*)", content)
        pointer_task = match.group(1).strip() if match else "NONE"

        for task in active_tasks:
            if task != pointer_task:
                results.append(DiagnosticResult("WARN", f"Orphan active task found (not in ACTIVE_TASK.md): {task}", f"Archive if completed: 'airi-cli archive {task}'"))
        
        return results

    def _check_result_missing(self):
        results = []
        # Checks if active tasks (except the ones currently being worked on if possible) have corresponding results
        # For now, just warn about tasks in active without results
        active_tasks = [f.name for f in self.active_tasks_dir.glob("TASK_*.md")]
        outputs_dir = path_resolver.get_outputs_dir()
        
        for task in active_tasks:
            task_id = task.replace("TASK_", "").replace(".md", "")
            results_found = list(outputs_dir.glob(f"RESULT_{task_id}*.md"))
            if not results_found:
                # We don't want to spam this for the very task we are currently doing, 
                # but doctor is often run after a break, so it's a good reminder.
                results.append(DiagnosticResult("INFO", f"No RESULT file yet for active task: {task}", "Create RESULT file when work is done."))
        
        return results

    def _check_directory_integrity(self):
        results = []
        dirs = {
            "tasks": path_resolver.get_tasks_dir(),
            "active_tasks": path_resolver.get_active_tasks_dir(),
            "outputs": path_resolver.get_outputs_dir(),
            "archive": path_resolver.get_tasks_dir() / "archive"
        }

        for name, path in dirs.items():
            if not path.exists():
                results.append(DiagnosticResult("ERROR", f"Required directory missing: {name} ({path})", f"Create directory: mkdir {path}"))
            elif not path.is_dir():
                results.append(DiagnosticResult("ERROR", f"Path exists but is not a directory: {name} ({path})", "Remove file and create directory."))
        
        return results
