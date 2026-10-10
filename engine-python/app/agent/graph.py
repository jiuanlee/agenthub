"""LangGraph Agent 定义（W11-W12 实现）。

设计要点：
- ReAct 循环：plan -> tool_call -> observe -> plan，最大步数保护
- 状态图节点：planner / tool_executor / memory_writer
- Checkpointer：Postgres（thread_id = 任务 ID，支持断点续跑）
- 工具来源：MCP Client 动态发现 + 内置工具
"""

# TODO(W11): from langgraph.graph import StateGraph
# TODO(W12): from langgraph.checkpoint.postgres import PostgresSaver
