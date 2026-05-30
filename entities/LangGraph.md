---
page_type: entity
updated_at: 2026-05-30
status: active
source_count: 2
---

# LangGraph

> **Legacy 警告**：本页内容基于 `Langchain(Legacy)` 资料（截至 2024年7月），legacy · not verified，API 行为以官方文档为准。

## What It Is

LangGraph 是 LangChain 生态中的图式 Agent 运行时框架，用于构建有状态、可循环、多参与者的 LLM 应用。它把 Agent 的控制流建模为显式状态图（StateGraph），支持 checkpoint 持久化、中断恢复、时间旅行和流式事件监听。

相比 LCEL（LangChain Expression Language）的无环管道，LangGraph 支持循环、条件分支、多 Agent 协作和人工干预，适合需要长任务弹性、复杂决策流和可审计执行历史的场景。

## Role In This Wiki

LangGraph 在本 wiki 中作为图式 Agent 编排运行时的典型案例，用于理解"状态机 + 检查点 + 可恢复执行"的 Agent 架构模式。相关概念见 [[concepts/Agent 编排图（Graph-based Agent Runtime）|Agent 编排图]]。

## Key Facts

- **StateGraph**：核心 API，状态通过 channel 定义更新方式，类似 Redux reducer；节点返回局部更新，图根据 channel 合并规则更新全局状态。
- **MessageGraph**：状态约束为只追加的 messages 列表，适合聊天与 Agent 消息循环。
- **Checkpoint**：图状态缓存与持久化机制，支持长任务恢复、时间旅行（回退到历史状态）、撤销/重做和多轮记忆。
- **中断恢复**：支持在特定节点前暂停执行，后续再次 invoke 时从暂停点恢复。Human-in-the-loop 通过此机制实现。
- **stream events**：可监听中间模型输出（chat model token）和工具执行（tool start/end）等中间事件，而不只等待最终结果。
- **底层模型**：类比 Google Pregel 迭代图计算，节点在图中以共享全局状态的方式协作。
- **支持的 Agent 模式**：代码生成反思、多智能体协作、supervisor 编排、层级团队子图、Agentic RAG（Adaptive/Corrective/Self RAG）、planning agents、LLM compiler、Web 导航。

## Related Concepts

- contrasts-with: [[concepts/LCEL（LangChain Expression Language）|LCEL]] — LCEL 偏向简单无环流程，LangGraph 支持循环、状态和复杂决策。
- used-in: [[concepts/Agentic RAG|Agentic RAG]] — LangGraph 是 Adaptive/Corrective/Self RAG 的典型实现框架（legacy）。
- contains: [[concepts/Agent 编排图（Graph-based Agent Runtime）|Agent 编排图]] — LangGraph 是图式 Agent 运行时概念的具体实现。

## Evidence

- [[sources/Langchain(Legacy)/LangGraph.xmind|LangGraph.xmind]] — 主要证据，StateGraph、checkpoint、stream events、中断恢复、时间旅行。
- [[sources/Langchain(Legacy)/Lang Graph 案例学习.xmind|Lang Graph 案例学习.xmind]] — 多种 Agent 模式（代码反思、supervisor、RAG 变体、Web 导航）的 LangGraph 实现。

## Open Questions

- LangGraph 在 2025-2026 的 API 演变和稳定性（legacy · not verified，需要官方文档核验）。
- LangGraph Cloud 和本地部署模式的区别尚未有 wiki 证据。
