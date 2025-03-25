from datetime import datetime
from typing import List, Optional, Dict, Set
from dataclasses import dataclass, field

@dataclass
class Task:
    """任务模型类"""
    id: int
    name: str
    description: str
    status: str  # 'pending', 'in_progress', 'completed', 'failed'
    created_at: datetime
    updated_at: datetime
    completed_at: Optional[datetime] = None
    tokens_used: int = 0
    dependencies: List[int] = field(default_factory=list)  # 依赖的其他任务ID
    adjustments: List[Dict] = field(default_factory=list)  # 动态调整记录
    parent_id: Optional[int] = None  # 父任务ID
    children_ids: Set[int] = field(default_factory=set)  # 子任务IDs
    priority: int = 0  # 任务优先级
    
    def update_status(self, new_status: str):
        """更新任务状态"""
        self.status = new_status
        self.updated_at = datetime.now()

    def add_dependency(self, task_id: int):
        """添加任务依赖"""
        if task_id not in self.dependencies:
            self.dependencies.append(task_id)
            self.updated_at = datetime.now()
            
    def add_child(self, child_task_id: int):
        """添加子任务"""
        self.children_ids.add(child_task_id)
        self.updated_at = datetime.now()
        
    def remove_child(self, child_task_id: int):
        """移除子任务"""
        if child_task_id in self.children_ids:
            self.children_ids.remove(child_task_id)
            self.updated_at = datetime.now()
            
    def set_parent(self, parent_task_id: int):
        """设置父任务"""
        self.parent_id = parent_task_id
        self.updated_at = datetime.now()
        
    def to_toml(self) -> str:
        """将对象属性递归导出为TOML格式字符串"""
        import toml
        
        def process_value(value):
            """递归处理各种类型的值"""
            if hasattr(value, 'to_toml'):
                return process_value(value.to_toml())
            elif isinstance(value, (list, tuple, set)):
                return [process_value(v) for v in value]
            elif isinstance(value, dict):
                return {k: process_value(v) for k, v in value.items()}
            elif isinstance(value, datetime):
                return value.isoformat()
            else:
                return value
        
        data = {}
        for field_name, field_value in self.__dict__.items():
            if not field_name.startswith('_'):
                data[field_name] = process_value(field_value)
        
        return toml.dumps(data)