import shutil
from pathlib import Path

CLEAN_TARGETS = [
    "Logs/*.log",
    "Outputs/snapshots/*",
    "__pycache__",
    "*.tmp",
    "Progress/*.md",
    "Progress/task_breakdown/*",
    "!Progress/README.md",
    "!Progress/demo_progress_tracking.md"
]

def clean_project():
    """清理临时文件和日志"""
    base = Path("d:\\Agent\\AgentProject")
    for pattern in CLEAN_TARGETS:
        for path in base.glob(pattern):
            if path.is_file():
                path.unlink()
            elif path.is_dir():
                shutil.rmtree(path)

if __name__ == "__main__":
    clean_project()
    print("项目清理完成")