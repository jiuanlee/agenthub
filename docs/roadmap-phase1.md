# 阶段一任务清单（W9-W16）：Agent 运行时端到端跑通

## W9 Python 速成 + 环境搭建
- [ ] Python：asyncio、类型注解、FastAPI、Pydantic
- [ ] FastAPI 实现 OpenAI 兼容 API 转发服务（SSE 流式）
- [ ] 注册至少两家模型 API Key（为网关降级埋伏笔）

## W10 LLM 应用基础
- [ ] 跑通 Function Calling 全流程
- [ ] 流式输出、token 统计、重试与超时
- [ ] 博客：《Function Calling 的协议细节与坑》
- [ ] 产出：命令行小 Agent，可调用 2 个本地工具

## W11-W12 LangGraph 编排引擎核心
- [ ] StateGraph、节点/边、条件路由、Checkpointer
- [ ] ReAct 循环：规划→工具→观察→再规划，最大步数保护
- [ ] 接入 Postgres Checkpointer，实现中断恢复（断点续跑原型）
- [ ] 产出：engine v0.1，`POST /agents/{id}/run`（SSE）

## W13 MCP 实战
- [ ] 精读 MCP 协议规范（tools/resources/prompts）
- [ ] 自研 MCP Server（如数据库查询工具，带参数校验+权限标记）
- [ ] 引擎接入 MCP Client，动态发现并调用工具

## W14 记忆系统
- [ ] 短期记忆：会话窗口 + 超限摘要压缩
- [ ] 长期记忆：事实抽取 → Embedding → pgvector → 运行时召回注入
- [ ] 跨会话记忆测试

## W15 RAG
- [ ] 入库管线：解析 → chunking（固定 vs 语义对比）→ Embedding → pgvector
- [ ] 检索：向量 + BM25 混合 + Rerank（bge-reranker）
- [ ] RAG 封装为 MCP 工具，Agent 自主决定何时检索

## W16 可观测 + 端到端联调 + 复盘
- [ ] Langfuse：完整 trace、token、成本
- [ ] OpenTelemetry → Prometheus：QPS/延迟/失败率
- [ ] 里程碑演示：发起任务→流式执行→工具调用→kill 服务→重启恢复→完成
- [ ] 博客：《从零构建生产级 Agent 运行时》+ 踩坑清单

## 每周固定动作
- [ ] 全程使用 Cursor/Claude Code 辅助开发（AI 原生工作流谈资）
- [ ] 周末 1h 刷 LangGraph/vLLM Issues 找贡献点
- [ ] W12 起 Go 每周 2-3h（目标：能读网关类项目源码）

## 验收标准（能自信回答）
1. Agent 执行到第 7 步服务挂了怎么恢复？（检查点+幂等重放）
2. 怎么防止 Agent 无限调用工具烧钱？（步数上限+token 预算+熔断）
3. MCP 和 Function Calling 的关系？（协议层 vs 能力层）
