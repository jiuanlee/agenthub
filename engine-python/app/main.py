"""AgentHub 编排引擎入口。

阶段一目标（W11-W12）：
- POST /agents/{agent_id}/run  SSE 流式返回 Agent 执行过程
- 基于 LangGraph Postgres Checkpointer 支持中断恢复
"""

from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI(title="AgentHub Engine", version="0.1.0")


@app.get("/health")
async def health() -> dict:
    return {"status": "ok"}


@app.post("/agents/{agent_id}/run")
async def run_agent(agent_id: str, payload: dict):
    """运行 Agent，SSE 流式返回。

    TODO(W11): 接入 LangGraph StateGraph
    TODO(W12): Postgres Checkpointer + thread_id 断点续跑
    TODO(W13): MCP Client 动态工具发现
    TODO(W14): 短期/长期记忆
    """

    async def event_stream():
        yield f"data: agent {agent_id} started, input={payload}\n\n"
        yield "data: [DONE]\n\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")
