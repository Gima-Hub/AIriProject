import datetime
from pathlib import Path
from .doctor import AiriDoctor
from .repairer import AiriRepairer
from .manager import TaskManager
from ..utils import path_resolver

class AiriHealthCycle:
    def __init__(self, manager: TaskManager):
        self.manager = manager
        self.doctor = AiriDoctor()
        self.repairer = AiriRepairer(manager)
        self.health_dir = path_resolver.get_repo_root() / "note-factory" / "health"
        self.report_file = self.health_dir / "latest_health_report.md"
        self.log_file = self.health_dir / "repair_history.log"
        
        # Ensure health directory exists
        self.health_dir.mkdir(parents=True, exist_ok=True)

    def run(self, auto_repair: bool = True):
        timestamp = datetime.datetime.now().isoformat()
        
        # 1. Diagnostic scan
        results = self.doctor.run_diagnostics()
        
        # 2. Repair if needed and requested
        repaired_items = []
        if results and auto_repair:
            repaired_items = self.repairer.repair(results)
            # Re-scan if repair was done to get the final state
            if repaired_items:
                results = self.doctor.run_diagnostics()
        
        # 3. Log repair history
        if repaired_items:
            self._log_repairs(timestamp, repaired_items)
            
        # 4. Generate latest health report
        self._generate_report(timestamp, results, repaired_items)
        
        return {
            "timestamp": timestamp,
            "issues_found": len(results),
            "items_repaired": len(repaired_items),
            "report_path": self.report_file
        }

    def _log_repairs(self, timestamp, repaired_items):
        with open(self.log_file, "a", encoding="utf-8") as f:
            for item in repaired_items:
                f.write(f"[{timestamp}] REPAIRED: {item}\n")

    def _generate_report(self, timestamp, current_results, recently_repaired):
        content = f"# AIri Health Report\n\n"
        content += f"- **Timestamp:** {timestamp}\n"
        content += f"- **Status:** {'HEALTHY' if not current_results else 'ISSUES_DETECTED'}\n\n"
        
        if recently_repaired:
            content += "## Recently Repaired\n"
            for item in recently_repaired:
                content += f"- [x] {item}\n"
            content += "\n"
            
        content += "## Current Issues\n"
        if not current_results:
            content += "No issues detected.\n"
        else:
            for res in current_results:
                content += f"### [{res.severity}] {res.message}\n"
                if res.fix_suggestion:
                    content += f"- Suggestion: {res.fix_suggestion}\n"
        
        with open(self.report_file, "w", encoding="utf-8") as f:
            f.write(content)
