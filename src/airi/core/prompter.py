from pathlib import Path

class PromptEngine:
    def __init__(self, repo_root: Path):
        self.repo_root = repo_root
        self.raw_base = "https://raw.githubusercontent.com/Gima-Hub/AIriProject/refs/heads/main"

    def _get_raw_url(self, rel_path: str) -> str:
        return f"{self.raw_base}/{rel_path}"

    def generate_activation_prompt(self, task_path: Path) -> str:
        """Generate prompt for Gemini when a task is activated."""
        rel_path = task_path.relative_to(self.repo_root).as_posix()
        raw_url = self._get_raw_url(rel_path)
        return (
            "# AIri Task Activation\n\n"
            "以下のタスクが有効化されました。詳細を読み取り作業を開始してください。\n"
            "作業完了後は RESULT 形式で報告してください。\n\n"
            f"- Path: `{rel_path}`\n"
            f"- Raw URL: {raw_url}"
        )

    def generate_review_prompt(self, task_path: Path, result_path: Path) -> str:
        """Generate prompt for ChatGPT when a task is ready for review."""
        rel_task = task_path.relative_to(self.repo_root).as_posix()
        rel_result = result_path.relative_to(self.repo_root).as_posix()
        raw_task = self._get_raw_url(rel_task)
        raw_result = self._get_raw_url(rel_result)
        
        return (
            "# AIri Review Request\n\n"
            "作業報告が出力されました。以下のファイルを読み込み、3_CURRENT_STATUS.md への統合判定を行ってください。\n\n"
            f"1. Task Definition:\n   - `{rel_task}`\n   - {raw_task}\n"
            f"2. Work Result:\n   - `{rel_result}`\n   - {raw_result}\n\n"
            "問題がなければ、統合の実行とタスクのアーカイブ化を指示してください。"
        )

    def generate_recovery_prompt(self, active_task_path: Path) -> str:
        """Generate prompt for Gemini to recover session context."""
        rel_path = active_task_path.relative_to(self.repo_root).as_posix()
        raw_url = self._get_raw_url(rel_path)
        return (
            "# AIri Session Recovery\n\n"
            "セッションの復旧が必要です。現在アクティブなタスクを確認し、作業を再開してください。\n\n"
            f"- Active Task: `{rel_path}`\n"
            f"- Raw URL: {raw_url}\n\n"
            "現在の進捗を確認し、次に実施すべきステップを提示してください。"
        )
