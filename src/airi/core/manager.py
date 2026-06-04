import shutil
from pathlib import Path
from ..utils import path_resolver

class TaskManager:
    def __init__(self):
        self.repo_root = path_resolver.get_repo_root()
        self.pending_dir = path_resolver.get_tasks_dir()
        self.active_dir = path_resolver.get_active_tasks_dir()
        self.archive_dir = self.pending_dir / "archive"

    def activate_task(self, task_filename: str) -> Path:
        """Move a task from Pending to Active."""
        source = self.pending_dir / task_filename
        target = self.active_dir / task_filename

        if not source.exists():
            raise FileNotFoundError(f"Task file not found in pending: {source}")
        
        if target.exists():
            raise FileExistsError(f"Task file already active: {target}")

        # Ensure active directory exists
        self.active_dir.mkdir(parents=True, exist_ok=True)

        shutil.move(str(source), str(target))
        self._update_recovery_pointer(task_filename)
        return target

    def archive_task(self, task_filename: str) -> Path:
        """Move a task from Active to Archive."""
        source = self.active_dir / task_filename
        target = self.archive_dir / task_filename

        if not source.exists():
            raise FileNotFoundError(f"Active task file not found: {source}")

        # Ensure archive directory exists
        self.archive_dir.mkdir(parents=True, exist_ok=True)

        shutil.move(str(source), str(target))
        self._update_recovery_pointer()
        return target

    def _update_recovery_pointer(self, task_filename: str = None):
        """Sync ACTIVE_TASK.md with the current active task state."""
        recovery_file = self.repo_root / "recovery" / "ACTIVE_TASK.md"
        active_tasks = list(self.active_dir.glob("TASK_*.md"))
        
        # Use task_filename if provided, otherwise pick the most recent active task
        current_task = None
        if task_filename and (self.active_dir / task_filename).exists():
            current_task = task_filename
        elif active_tasks:
            # Sort by modification time to get the most recent
            active_tasks.sort(key=lambda x: x.stat().st_mtime, reverse=True)
            current_task = active_tasks[0].name

        content = "# ACTIVE_TASK_POINTER\n\n## CURRENT_TASK\n"
        if current_task:
            content += f"- NAME: {current_task}\n"
            content += f"- URL: https://raw.githubusercontent.com/Gima-Hub/AIriProject/refs/heads/main/note-factory/tasks/active/{current_task}\n"
        else:
            content += "- NAME: NONE\n"
            content += "- URL: NONE\n"
        
        import datetime
        content += f"- LAST_SYNC: {datetime.date.today().isoformat()}\n"
        
        recovery_file.parent.mkdir(parents=True, exist_ok=True)
        with open(recovery_file, "w", encoding="utf-8") as f:
            f.write(content)

    def get_status(self):
        """Get the current status of tasks."""
        pending = [f.name for f in self.pending_dir.glob("TASK_*.md")]
        active = [f.name for f in self.active_dir.glob("TASK_*.md")]
        outputs_count = len(list(path_resolver.get_outputs_dir().glob("RESULT_*.md")))
        return {
            "pending": pending,
            "active": active,
            "outputs_count": outputs_count
        }

    def get_result_for_task(self, task_filename: str) -> Path:
        """Find the corresponding RESULT file for a given task filename."""
        # task_filename: TASK_20260522_SOMETHING.md -> 20260522_SOMETHING
        task_id = task_filename.replace("TASK_", "").replace(".md", "")

        outputs_dir = path_resolver.get_outputs_dir()
        results = list(outputs_dir.glob(f"RESULT_{task_id}*.md"))

        if not results:
            raise FileNotFoundError(f"No result file found for task ID: {task_id}")

        # Return the most recent if multiple (though should be unique)
        return sorted(results, key=lambda x: x.stat().st_mtime, reverse=True)[0]

