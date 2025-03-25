
# AgentProject 智能体协作平台

## 项目目的
为生产级智能体提供标准化工作框架，实现：
- 任务目标的可视化管理
- 执行过程的可追溯性
- 工具与资源的安全隔离
- 跨智能体的协同作业

## 架构概览
```plaintext
AgentProject/
├── Mission.yaml       # 战略目标定义
├── Progress/          # 任务进度追踪
├── Resources/         # 安全凭证管理
├── Tools/             # 功能工具库
├── Models/            # 数据模型定义
├── Logs/              # 执行过程记录
└── Outputs/           # 成果输出目录
```

## 目录作用详解
### 1. Mission.yaml
- **作用**：定义智能体的核心KPI和约束条件
- **示例**：
  ```yaml
  objective: "创建用户管理系统"
  constraints:
    - "使用SQLite数据库"
  success_metrics:
    - "完成用户CRUD接口"
  ```

### 2. Progress/
- 包含：
  - `current_plan.md`：当前执行方案
  - `history/`：历史版本存档
- **更新频率**：每个任务阶段至少更新一次

### 3. Outputs/
- 子目录：
  - `artifacts/`：最终交付物（数据库/报告等）
  - `snapshots/`：关键节点状态快照
  - `reports/`：自动生成的JSON/HTML报告

## 快速启动指南
### 通过命令行初始化项目
```powershell
# 1. 克隆仓库
git clone https://github.com/yourrepo/AgentProject.git d:\Agent\AgentProject

# 2. 初始化目录结构
cd d:\Agent\AgentProject
mkdir Resources Tools Models Logs Outputs Progress

# 3. 创建Mission文件
@"
objective: \"示例任务\"
constraints: []
success_metrics: []
"@ | Out-File -Encoding utf8 Mission.yaml

# 4. 启动智能体
python Tools/builtin/agent_launcher.py
```

## 注意事项
1. 安全规范：
   - 所有凭证必须通过`Resources/.secrets_template.json`配置
   - 禁止在代码中硬编码敏感信息

2. 版本控制：
   ```bash
   git add Mission.yaml Progress/ Models/
   git commit -m "更新任务进度"
   ```

3. 日志查看：
   ```powershell
   Get-Content d:\Agent\AgentProject\Logs\execution.log -Tail 50 -Wait
   ```

## 典型工作流
1. 编辑`Mission.yaml`定义目标
2. 在`Progress/`创建执行计划
3. 通过`Tools/`下的工具完成任务
4. 最终产物输出到`Outputs/artifacts/`

## 目录说明
▸ `scripts/`  
   - 项目脚手架脚本  
   - CI/CD自动化脚本  
   - 维护工具  

▸ `Tools/`  
   - 业务功能实现  
   - 智能体操作工具集


## 脚手架工具使用指南

### 1. 初始化项目
```powershell
# 基本初始化（保留现有文件）
python d:\Agent\AgentProject\scripts\scaffold_init.py

# 强制清理后初始化（删除所有现有文件）
python d:\Agent\AgentProject\scripts\scaffold_init.py --clean
```


### 2. 项目打包
```powershell
# 创建带时间戳的压缩包
python d:\Agent\AgentProject\scripts\scaffold_pack.py

# 输出示例：
# 项目快照已创建: d:\Agent\AgentProject_20231120_1430.zip
```


### 3. 清理项目
```powershell
# 清除临时文件和日志
python d:\Agent\AgentProject\scripts\scaffold_clean.py

# 清理目标包括：
# - 所有.log文件
# - 快照目录内容
# - Python缓存文件
```

### 高级用法
#### 自定义排除目录（修改scaffold_pack.py）
```python
EXCLUDE_DIRS = {
    "Logs", 
    "__pycache__",
    "temp"  # 新增排除目录
}
 ```

#### 定时自动打包（Windows任务计划）
```powershell
# 创建每日打包任务
schtasks /create /tn "AgentProjectDailyPack" /tr "python d:\Agent\AgentProject\scripts\scaffold_pack.py" /sc daily /st 18:00
```

### 注意事项
1. 打包时会自动跳过：
   - 日志文件
   - Python编译缓存
   - Git/SVN元数据
2. 使用 --clean 参数前请确认备份重要数据
3. 建议在CI/CD流程中集成这些脚本