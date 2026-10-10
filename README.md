# AgentHub —— 企业级 Agent 应用平台

支持 Agent 的创建、编排、发布、运行、监控和治理的多租户平台。
Java（治理面）+ Python（编排面）异构微服务架构实战项目。

## 系统架构

```
控制台前端 (React)
       │
API 网关 (Spring Cloud Gateway)  ── 认证/租户解析/全局限流/审计埋点
       │
 ├─ 租户治理服务 (Java)   ── 组织/空间、RBAC、数据隔离
 ├─ Agent 资产管理 (Java) ── Agent/Prompt/Tool 版本管理、灰度发布、回滚
 ├─ 配额计量服务 (Java)   ── QPS 配额、token 预算、成本分摊
 └─ 审计日志服务 (Java)   ── 变更/调用全量留痕
       │ 发布指令
LLM 网关 (Java 自研) ── 模型路由/降级熔断/Key 池/缓存/token 成本核算
       │ OpenAI 兼容协议
Agent 编排引擎 (Python + LangGraph)
 ├─ ReAct 循环 / 工具调用 (MCP)
 ├─ 短期记忆（窗口+摘要压缩）/ 长期记忆 (pgvector)
 └─ 长任务状态机：检查点 → 暂停/恢复/重试/幂等/补偿
       │ MCP 协议              │ MQ 异步任务
MCP Server 注册中心 (Java)   RocketMQ + 任务调度器（优先级/背压/超时回收）

存储: PostgreSQL(业务) | Redis(会话/限流) | pgvector(记忆/RAG) | MinIO(文件)
可观测: OpenTelemetry → Prometheus/Grafana(系统) + Langfuse(LLM 链路)
```

## 目录结构

```
platform-java/     # 治理面微服务（Spring Boot 3 + Spring Cloud Alibaba）
llm-gateway/       # 自研 LLM 网关（Java）
engine-python/     # Agent 编排引擎（FastAPI + LangGraph）
deploy/            # Docker Compose / K8s 部署
 docs/             # 架构设计与学习路线文档
```

## 开发路线

- [x] 项目脚手架搭建
- [ ] 阶段一（W9-W16）：Agent 运行时端到端跑通 → 详见 [docs/roadmap-phase1.md](docs/roadmap-phase1.md)
- [ ] 阶段二（W17-W24）：治理全家桶 + LLM 网关 + 压测
- [ ] 阶段三（W25-W28）：K8s 部署 + 全链路可观测 + 评测体系

## 快速开始

```bash
cd deploy && docker compose up -d          # 基础设施：PG/pgvector、Redis、MinIO、Langfuse
cd engine-python && pip install -r requirements.txt
uvicorn app.main:app --reload              # 启动编排引擎
```
