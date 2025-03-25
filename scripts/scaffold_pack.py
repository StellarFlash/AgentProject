import zipfile
from datetime import datetime
from pathlib import Path

BASE_DIR = Path("d:\\Agent\\AgentProject")
EXCLUDE_DIRS = {"Logs", "__pycache__"}

def create_project_snapshot():
    """创建项目快照压缩包"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    zip_path = BASE_DIR.parent / f"AgentProject_{timestamp}.zip"
    
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for file in BASE_DIR.rglob("*"):
            if not any(excl in file.parts for excl in EXCLUDE_DIRS):
                zipf.write(file, file.relative_to(BASE_DIR.parent))
    
    return zip_path

if __name__ == "__main__":
    snapshot_path = create_project_snapshot()
    print(f"项目快照已创建: {snapshot_path}")