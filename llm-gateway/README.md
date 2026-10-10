# llm-gateway —— 自研 LLM 网关（Java）

阶段二核心亮点项目，独立于 API 网关。

## 功能规划

- **模型路由**：按能力标签/成本/可用性路由到不同模型提供商
- **降级熔断**：主模型超时/限流 → 自动切换备用模型
- **Key 池管理**：多 Key 轮询、用量均衡、失效摘除
- **双维度限流**：QPS + token 预算（租户级）
- **语义缓存**：相似 prompt 命中缓存，降低成本
- **成本核算**：按租户/Agent/模型维度统计 token 消耗与费用

## 协议

对外暴露 OpenAI 兼容 API（`/v1/chat/completions`），支持 SSE 流式。

## 参考设计

LiteLLM、One-API、Higress AI Gateway
