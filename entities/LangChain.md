---
page_type: entity
updated_at: 2026-05-30
status: active
source_count: 10
---

# LangChain

> **Legacy 警告**：本页内容基于 `Langchain(Legacy)` 资料（2024年），legacy · not verified，API 行为以官方最新文档为准。LangChain 生态变化较快，以下内容仅供学习 LLM 应用工程早期抽象之用。

## What It Is

LangChain 是构建 LLM 应用的框架/生态，提供模型接入、提示语模板、检索组件、编排抽象、服务化和观测工具。当前 wiki 所有 LangChain 相关资料来自 `Langchain(Legacy)` 目录（2024年），作为历史学习材料和工具谱系记录。

## Role In This Wiki

LangChain 在本 wiki 中作为 LLM 应用工程早期抽象的参照系：LCEL/Runnable 是理解 LLM 应用编排的模式基础；LangGraph 展示了图式 Agent 运行时的设计方式；LangServe 展示了 LLM 应用服务化的思路；LangSmith 展示了 LLMOps 和评估闭环的工程实践。

细节下沉到子实体/概念页：
- LCEL 编排语言：[[concepts/LCEL（LangChain Expression Language）|LCEL]]
- 图式 Agent 运行时：[[entities/LangGraph|LangGraph]] / [[concepts/Agent 编排图（Graph-based Agent Runtime）|Agent 编排图]]
- Runnable 服务化：[[entities/LangServe|LangServe]] / [[concepts/Runnable 服务化|Runnable 服务化]]
- LLMOps 平台：[[entities/LangSmith|LangSmith]]

## LangChain 生态分层

- **Core**：基础协议和 LCEL，提供流式、异步、并行、跟踪和组合能力。
- **Community**：模型接入（ChatModel/LLM）、检索（Retriever/VectorStore/DocumentLoader/TextSplitter/Embedding）、工具和 Agent 组件。
- **LangChain 包**：高级编排策略，包括 chain、agent 和 retrieval strategy。
- **LangGraph**：图式 Agent 运行时，支持有状态循环和 checkpoint（见 [[entities/LangGraph|LangGraph]]）。
- **LangServe**：把 Runnable 暴露为 REST API（见 [[entities/LangServe|LangServe]]）。
- **LangSmith**：LLMOps 平台，覆盖 trace、评估、数据集和 CI（见 [[entities/LangSmith|LangSmith]]）。

## Key Facts

（LCEL 和 Runnable 细节见 [[concepts/LCEL（LangChain Expression Language）|LCEL]]）
- LangChain 应用覆盖 RAG、结构化提取、工具 Agent、SQL/CSV 问答、文本总结、聊天机器人、请求分析等模式（详见 [[synthesis/LangChain 应用模式目录（Legacy）|LangChain 应用模式目录]]）。
- LangGraph 使用 StateGraph + checkpoint + 条件边构建有状态 Agent，支持中断恢复和时间旅行（legacy · not verified）。
- LangServe 基于 FastAPI 和 Pydantic，暴露 invoke/stream/batch/playground 端点（legacy · not verified）。
- LangSmith 提供 trace 记录、数据集管理、评估实验、CI 回归和在线监控（legacy · not verified）。
- tracing/observability 选项包括 LangSmith（官方商业）、Langfuse（开源）、Phoenix（开源），详见 [[synthesis/LangSmith 与 Langfuse 可观测性对照（Legacy）|可观测性对照综合页]]。

## Related Concepts

- implemented-by: [[concepts/RAG|RAG]]
- contains: [[concepts/LCEL（LangChain Expression Language）|LCEL]]
- contains: [[entities/LangGraph|LangGraph]]
- contains: [[entities/LangServe|LangServe]]
- contains: [[entities/LangSmith|LangSmith]]
- related-source: [[sources/Langchain(Legacy)/Langchain.xmind|Langchain.xmind]]
- related-source: [[sources/Langchain(Legacy)/LangGraph.xmind|LangGraph.xmind]]
- related-source: [[sources/Langchain(Legacy)/Langchain  表达式语言.xmind|Langchain 表达式语言]]
- used-in: [[maps/LLM 应用与数据处理学习地图|LLM 应用与数据处理学习地图]]

## Evidence

- [[sources/Langchain(Legacy)/Langchain.xmind|Langchain.xmind]] — 生态总览和分层。
- [[sources/Langchain(Legacy)/Langchain  组件.xmind|Langchain 组件]] — 组件层详细说明（Model I/O/Retrieval/Callbacks/Memory/Composition）。
- [[sources/Langchain(Legacy)/Langchain  表达式语言.xmind|Langchain 表达式语言]] — LCEL Runnable 完整接口。
- [[sources/Langchain(Legacy)/LangGraph.xmind|LangGraph.xmind]] — 图式 Agent 运行时。
- [[sources/Langchain(Legacy)/LangServe.xmind|LangServe.xmind]] — Runnable 服务化。
- [[sources/Langchain(Legacy)/Langchain  DevOps.xmind|Langchain DevOps.xmind]] — LangSmith 评估和 DevOps。
- [[sources/Langchain(Legacy)/跟踪和监控.xmind|跟踪和监控]] — tracing 选型对比。
- [[sources/Langchain(Legacy)/Langchain 案例学习.xmind|Langchain 案例学习]] — 应用模式案例。
- [[sources/Langchain(Legacy)/Lang Graph 案例学习.xmind|Lang Graph 案例学习]] — LangGraph Agent 模式案例。

## Open Questions

- `Langchain(Legacy)` 资料的版本状态和当前 LangChain/LangGraph API 需要后续联网核验。
- LangChain 在 2025-2026 是否仍是主流 LLM 应用框架，或有其他框架替代，需要最新信息。
