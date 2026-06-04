from pathlib import Path
from .manager import TaskManager
from .doctor import DiagnosticResult
from .runtime_state import RuntimeState

class AiriRepairer:
    def __init__(self, manager: TaskManager):
        self.manager = manager
        self.state = RuntimeState()

    def repair(self, diagnostic_results: list[DiagnosticResult]) -> list[str]:
        if self.state.is_safe_mode():
            return ["[SYSTEM] Repair blocked: System is in Runtime Safe Mode. Manual intervention required."]

        repaired_items = []
        
        for res in diagnostic_results:
            if res.severity in ["ERROR", "WARN"]:
                # Check for repair loop before dispatching
                action_id = self._get_action_id(res)
                if self.state.get_repair_count(action_id) >= 3:
                    self.state.set_safe_mode(True)
                    error_msg = f"[ESCALATION] Repair loop detected for: {action_id}. Entering Safe Mode."
                    repaired_items.append(error_msg)
                    return repaired_items

                repair_msg = self._dispatch_repair(res)
                if repair_msg:
                    repaired_items.append(repair_msg)
                    self.state.record_repair(action_id, success=True)
        
        return repaired_items

    def _get_action_id(self, result: DiagnosticResult) -> str:
        # Generate a stable ID for the diagnostic message to track repeats
        # Example: "Required directory missing: tasks" -> "missing_dir_tasks"
        msg = result.message
        if "ACTIVE_TASK.md missing" in msg: return "missing_active_task_md"
        if "points to stale task" in msg: return "stale_pointer"
        if "ACTIVE_TASK.md is 'NONE'" in msg: return "none_state_mismatch"
        if "Required directory missing" in msg:
            dir_name = msg.split(":")[1].split("(")[0].strip()
            return f"missing_dir_{dir_name}"
        if "Orphan active task" in msg: return "orphan_task"
        return "unknown_action"

    def _dispatch_repair(self, result: DiagnosticResult) -> str:
        # Match diagnostic messages and apply fixes
        msg = result.message
        
        if "ACTIVE_TASK.md missing" in msg:
            self.manager._update_recovery_pointer()
            return "Regenerated missing ACTIVE_TASK.md"
        
        if "points to stale task" in msg:
            self.manager._update_recovery_pointer()
            return f"Synchronized stale pointer in ACTIVE_TASK.md"
            
        if "ACTIVE_TASK.md is 'NONE' but active tasks exist" in msg:
            self.manager._update_recovery_pointer()
            return "Synchronized ACTIVE_TASK.md with existing active tasks"

        if "Required directory missing" in msg:
            # Extract path from message: "Required directory missing: name (path)"
            try:
                path_str = msg.split("(")[1].split(")")[0]
                Path(path_str).mkdir(parents=True, exist_ok=True)
                return f"Recreated missing directory: {path_str}"
            except Exception as e:
                return f"Failed to recreate directory: {e}"

        if "Orphan active task found" in msg:
            # We don't archive automatically to be safe, but we can resync the pointer
            # to include the most recent active task if NONE was set incorrectly.
            # If there are multiple, manual intervention is better, but here we resync.
            self.manager._update_recovery_pointer()
            return "Resynchronized ACTIVE_TASK.md pointer (Orphan task handled by sync)"

        return None
