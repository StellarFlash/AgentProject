# 机房管理演示案例

## 机房资源监控

```yaml
server_room:
  name: 主数据中心机房
  location: 3楼A区
  status: 运行中
  
  # 环境监控
  environment:
    temperature: 22.5°C
    humidity: 45%
    power_status: 正常
    
  # 设备清单
  equipment:
    - type: 服务器
      count: 42
      status: 38在线/4维护
    - type: 网络设备
      count: 15
      status: 全部在线
    - type: 存储设备
      count: 8
      status: 7在线/1故障

  # 告警规则
  alerts:
    - metric: temperature
      threshold: >30°C
      severity: 紧急
    - metric: humidity
      threshold: <30% or >70%
      severity: 警告
    - metric: power_status
      threshold: 异常
      severity: 紧急

## 任务追踪示例

复用现有任务追踪规范，展示机房维护任务：

```yaml
project: 机房运维
  modules:
    - name: 日常维护
      tasks:
        - name: 空调系统检查
          status: 已完成
          completed_at: 2023-11-15 09:00:00
        - name: 网络设备巡检
          status: 进行中
          updated_at: 2023-11-16 14:00:00
    - name: 故障处理
      tasks:
        - name: 存储设备修复
          status: 未开始
          dependencies: [备件到货]
```