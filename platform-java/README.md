# platform-java —— 治理面微服务

Spring Boot 3 + Spring Cloud Alibaba，阶段二（W17-W24）实现。

## 模块规划

| 模块 | 职责 | 对应 JD 关键词 |
|---|---|---|
| `tenant-service` | 组织/项目/空间、RBAC、数据隔离 | 多租户、权限 |
| `asset-service` | Agent/Prompt/Tool/Workflow 版本管理、环境隔离、灰度、回滚 | 版本管理、灰度发布 |
| `quota-service` | QPS 配额、token 预算、成本分摊报表 | 配额、计量 |
| `audit-service` | 变更/调用审计日志 | 审计 |
| `mcp-registry` | MCP Server 上架/鉴权/版本/调用审计 | MCP 管理 |
| `task-scheduler` | 长任务调度：优先级/背压/超时回收/断点续跑 | 任务编排 |

## 技术栈

- Spring Boot 3 / Spring Cloud Gateway / Nacos
- RocketMQ（异步任务与事件）
- PostgreSQL（MyBatis-Plus）/ Redis
- OpenTelemetry + Prometheus
