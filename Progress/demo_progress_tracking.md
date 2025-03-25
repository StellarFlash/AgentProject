# 智能体任务进度追踪规范

## 任务结构

- 采用树状层级结构管理任务
- 根节点为项目名称
- 中间节点为任务组/模块
- 叶子节点为具体可执行任务

## 任务节点属性

```yaml
name: 任务名称
description: 任务描述
status:  # 任务状态
  - 未开始
  - 进行中
  - 已完成
  - 已废弃
created_at: YYYY-MM-DD HH:MM:SS  # 创建时间
updated_at: YYYY-MM-DD HH:MM:SS  # 最后更新时间
completed_at: YYYY-MM-DD HH:MM:SS  # 完成时间
tokens_used: 0  # 消耗的token数量
dependencies: []  # 依赖的其他任务

# 动态调整记录
adjustments:
  - timestamp: YYYY-MM-DD HH:MM:SS
    action: 操作类型(新增/删除/修改)
    details: 变更详情
```

## 示例结构

```yaml
project: AgentProject
  modules:
    - name: 核心模块开发
      tasks:
        - name: 用户模型实现
          status: 已完成
          completed_at: 2023-11-15 14:30:00
          tokens_used: 1250
    - name: 工具集成
      tasks:
        - name: 数据库操作工具
          status: 进行中
          updated_at: 2023-11-16 09:15:00
          tokens_used: 780
        - name: 输出管理器
          status: 未开始
```
