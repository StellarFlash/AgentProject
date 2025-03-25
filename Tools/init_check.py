
### 3. 智能体初始化检查脚本 
from pathlib import Path

REQUIRED_DIRS = [
    "Resources",
    "Tools/builtin",
    "Models",
    "Logs",
    "Outputs/artifacts",
    "Outputs/snapshots"
]

def validate_project_structure():
    """验证项目目录结构完整性"""
    missing = []
    for dir_path in REQUIRED_DIRS:
        if not Path(f"d:/Agent/AgentProject/{dir_path}").exists():
            missing.append(dir_path)
    
    if missing:
        raise RuntimeError(f"缺少必要目录: {missing}")
    print("✅ 项目结构验证通过")