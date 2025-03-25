from Models.Progress.task import Task
from Models.Progress.progress_record import ProgressRecord
from datetime import datetime
import json
import os
from typing import Dict, List, Optional

class ProgressServer:
    """任务管理服务类"""
    
    def __init__(self, task_id: int, task_name: str, description: str):
        """初始化任务管理服务"""
        self.task = Task(
            id=task_id,
            name=task_name,
            description=description,
            status='pending',
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        
        self.progress_record = ProgressRecord(
            id=task_id,
            task_id=task_id,
            stage='started'
        )
    
    def update_progress(self, stage: str, tokens_used: int, steps_used: int, log: Optional[str] = None):
        """更新任务进度状态"""
        self.progress_record.stage = stage
        self.progress_record.update_resources(tokens_used, steps_used, self.task)
        
        if log:
            self.progress_record.add_operation_log(log)
        
        if stage in ['completed', 'failed']:
            self.export_progress()
    
    def export_progress(self):
        """导出进度记录到Outputs目录"""
        output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Outputs', 'reports')
        os.makedirs(output_dir, exist_ok=True)
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"progress_report_{self.task.id}_{timestamp}.toml"
        filepath = os.path.join(output_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(self.progress_record.to_toml())
        
        # 同时导出JSON格式
        json_filename = f"progress_report_{self.task.id}_{timestamp}.json"
        json_filepath = os.path.join(output_dir, json_filename)
        
        with open(json_filepath, 'w', encoding='utf-8') as f:
            json.dump({
                'task': self.task.__dict__,
                'progress': self.progress_record.__dict__
            }, f, indent=2, default=str)

if __name__ == "__main__":
    # 示例用法
    server = ProgressServer(1, "示例任务", "这是一个示例任务")
    server.update_progress('started', 1000, 1, "任务开始")
    server.update_progress('milestone', 5000, 5, "达到第一个里程碑")
    server.update_progress('completed', 10000, 10, "任务完成")