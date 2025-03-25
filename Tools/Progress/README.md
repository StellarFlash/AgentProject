# 进度控制服务使用指南

## 1. 启动ProgressServer服务

```python
from Tools.ProgressServer import ProgressServer

# 初始化服务
server = ProgressServer(task_id=1, task_name="示例任务", description="任务描述")
```

## 2. 使用progress_control.py更新任务状态

通过命令行调用progress_control.py脚本更新任务进度：

```bash
python progress_control.py \
  --task-id 1 \
  --task-name "示例任务" \
  --description "任务描述" \
  --stage started \
  --tokens-used 100 \
  --steps-used 5 \
  --log "任务已开始"
```

可用阶段(stage)选项: started, milestone, completed, failed

## 3. 记录格式说明

- 任务ID: 唯一标识符
- 任务名称: 任务描述名称
- 阶段: 当前进度状态
- 已使用token数: 消耗的计算资源
- 已使用步骤数: 执行步骤数
- 日志: 操作记录

## 4. 常见用例示例

### 用例1: 任务开始
```bash
python progress_control.py --task-id 1 --task-name "数据分析" --description "处理用户数据" --stage started --tokens-used 0 --steps-used 0 --log "任务初始化"
```

### 用例2: 里程碑更新
```bash
python progress_control.py --task-id 1 --task-name "数据分析" --description "处理用户数据" --stage milestone --tokens-used 500 --steps-used 3 --log "完成数据清洗"
```

### 用例3: 任务完成
```bash
python progress_control.py --task-id 1 --task-name "数据分析" --description "处理用户数据" --stage completed --tokens-used 1200 --steps-used 8 --log "生成最终报告"
```