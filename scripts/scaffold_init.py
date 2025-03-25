import argparse
import shutil
from pathlib import Path

# 更新基础路径引用
BASE_DIR = Path(__file__).parent.parent  # 自动定位项目根目录

def init_project(clean: bool = False):
    required_dirs = [
        "Tools/builtin",
        "Models",
        "Logs",
        "Outputs/artifacts",
        "Outputs/snapshots",
        "Progress/history",
        "Progress/abandoned"
    ]
    
    if clean:
        shutil.rmtree(BASE_DIR, ignore_errors=True)
        BASE_DIR.mkdir()
    
    for dir_path in required_dirs:
        (BASE_DIR / dir_path).mkdir(parents=True, exist_ok=True)
    
    # 创建基础文件模板
    with open(BASE_DIR / "Mission.yaml", "w", encoding="utf-8") as f:
        f.write("objective: \"\"\nconstraints: []\nsuccess_metrics: []")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--clean", action="store_true", help="清除现有项目文件")
    args = parser.parse_args()
    init_project(args.clean)