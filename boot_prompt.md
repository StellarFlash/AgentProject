# AgentProject 启动准则

## 核心执行原则

1. **目标导向**：始终以[Mission.yaml](d:\Agent\AgentProject\Mission.yaml)定义的目标为最高优先级
2. **渐进安全**：资源访问暂用本地模拟模式（开发阶段）
3. **可追溯性**：每个决策必须在`Progress/`中记录

## 初始任务规划流程

1. 在`Progress/`中创建：

```plaintext
initial_plan.md    # 使用Markdown表格格式
task_breakdown/    # 子任务分解目录
```

## 目录职责说明

▸ `Models/`  
    - 存储核心数据结构和领域模型  
    - 版本控制要求：每次变更需创建新版本文件

▸ `Tools/`  
    - 内置工具：经过验证的稳定功能  
    - 动态工具：运行时生成的临时工具需标记为[experimental]

▸ `Outputs/`  
    - 最终产物存放于`artifacts/`  
    - 过程快照存放于`snapshots/{timestamp}/`
