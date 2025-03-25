from datetime import datetime
from typing import Optional, Dict, List
from dataclasses import dataclass
from Models.Progress.task import Task

@dataclass
class ProgressRecord:
    """进度记录模型类"""
    id: int
    task_id: int
    stage: str  # 'started', 'milestone', 'completed', 'failed'
    
    
    total_time: int = 1800 # 任务总耗时,单位秒
    total_tokens: int = 50000000 # 总token预算
    total_steps: int = 50 # 总步骤预算
    
    operation_logs: List[str] = field(default_factory=list)  # 操作日志记录
    status_description: Optional[str] = None  # 状态描述
    adjustment_details: Optional[Dict] = None  # 动态调整记录
    
    start_time: datetime = field(default_factory=datetime.now)  # 任务开始时间
    used_time: int = 0  # 已用时间(秒)
    used_tokens: int = 0
    used_steps: int = 0

    remaining_time: Optional[int] = None  # 剩余时间
    remaining_tokens: Optional[int] = None  # 剩余token预算
    remaining_steps: Optional[int] = None  # 剩余步骤预算
    

    
    def add_operation_log(self, log: str):
        """添加操作日志"""
        self.operation_logs.append(log)
        
    def update_status_description(self, description: str):
        """更新状态描述"""
        self.status_description = description
        
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
    

def update_resources(self, tokens_used: int, steps_used: int, task: Optional[Task] = None):
        """更新资源状态
        
        Args:
            tokens_used: 当前步骤消耗的token数量
            steps_used: 当前步骤消耗的步骤数量
            task: 关联的任务对象
        """
        # 计算总耗时
        elapsed_time = int((datetime.now() - self.start_time).total_seconds())
        self.used_time = elapsed_time
        if self.remaining_time is not None:
            self.remaining_time = max(0, self.total_time - elapsed_time)
        
        # 更新token消耗
        self.used_tokens += tokens_used
        if self.remaining_tokens is not None:
            self.remaining_tokens = max(0, self.total_tokens - self.used_tokens)
            
        # 更新步骤消耗
        self.used_steps += steps_used
        if self.remaining_steps is not None:
            self.remaining_steps = max(0, self.total_steps - self.used_steps)
        
        # 更新关联任务状态
        if task:
            task.tokens_used += tokens_used
            task.updated_at = datetime.now()
            
        return self.remaining_time, self.remaining_tokens, self.remaining_steps
