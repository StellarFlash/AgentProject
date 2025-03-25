from pathlib import Path
from datetime import datetime

class OutputManager:
    @staticmethod
    def get_artifact_path(filename: str) -> Path:
        """获取最终成果存放路径"""
        path = Path("d:/Agent/AgentProject/Outputs/artifacts") / filename
        path.parent.mkdir(exist_ok=True)
        return path

    @staticmethod
    def create_snapshot_dir() -> Path:
        """创建带时间戳的快照目录"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        path = Path(f"d:/Agent/AgentProject/Outputs/snapshots/{timestamp}")
        path.mkdir(parents=True, exist_ok=True)
        return path