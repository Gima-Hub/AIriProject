import os
from pathlib import Path

def get_repo_root() -> Path:
    """Find the git repository root."""
    current = Path.cwd()
    for parent in [current] + list(current.parents):
        if (parent / ".git").exists():
            return parent
    return current

def get_tasks_dir() -> Path:
    return get_repo_root() / "note-factory" / "tasks"

def get_active_tasks_dir() -> Path:
    return get_tasks_dir() / "active"

def get_outputs_dir() -> Path:
    return get_repo_root() / "note-factory" / "outputs"
