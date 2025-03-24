from pydantic import BaseModel

class Task(BaseModel):
    """任务核心数据模型"""
    id: str
    description: str
    dependencies: list[str]
    status: str  # pending, in_progress, completed