---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Langchain(Legacy)/Langchain  组件.xmind"
source_relpath: "Langchain(Legacy)/Langchain  组件.xmind"
raw_created_at: 2024-04-24T01:18:43.094011+00:00
raw_modified_at: 2024-12-11T06:55:57.737869+00:00
raw_size: 2897880
raw_fingerprint: "size=2897880;birth=2024-04-24T01:18:43.094011+00:00;mtime=2024-12-11T06:55:57.737869+00:00"
raw_snapshot_at: 2026-05-29T22:11:25.083799+00:00
ingested_at: 2026-05-30
status: ingested
---

# Langchain  组件.xmind

## Source

- Raw file: [Langchain(Legacy)/Langchain  组件.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Langchain%28Legacy%29/Langchain%20%20%E7%BB%84%E4%BB%B6.xmind>)
- Raw ref: `raw:Langchain(Legacy)/Langchain  组件.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2024-04-24T01:18:43.094011+00:00`; modified `2024-12-11T06:55:57.737869+00:00`; size `2897880`; snapshot `2026-05-29T22:11:25.083799+00:00`
- Coverage: exported and digested 1 sheet: `画布 1` (307 topics).

## Summary

这份图把 LangChain 拆成组件层理解：Model I/O 负责提示语、模型和解析；Retrieval 负责 RAG 数据进入模型上下文；Callbacks 负责执行过程观测；Memory 负责上下文记忆；Composition 负责把工具、Agent 和 Chain 组合成应用流程。

## Source Digest

本 source 的主线不是单个 API 教程，而是 LangChain 应用的组件化心智模型。Model I/O 层把提示语模板、聊天消息抽象、工具调用、结构化输出和 Output Parser 串起来，说明 LangChain 的价值之一是屏蔽不同模型接口差异，并把提示、模型调用、解析变成可组合节点。

Retrieval 分支把 RAG 拆成文档加载、文本拆分、Embedding、向量库、Retriever 和 Indexing。高信号细节在 Retriever 分类：Vectorstore、ParentDocument、Multi Vector、Self Query、Contextual Compression、Time-Weighted、Multi-Query、Ensemble 和 Long-Context Reorder 分别面向不同召回、压缩、元数据过滤、多查询和长上下文排序问题。这里的重点是：RAG 不是一个单点技术，而是检索策略、索引同步和上下文压缩的组合工程。

Callbacks 分支强调执行过程观测：同步/异步 handler、请求时间回调、构造函数回调、全局监听以及 Python 3.10 以下异步子 Runnable 需要手动传播回调。Composition 分支把 Tools、Agents、AgentExecutor 和 Chains 放在一起：Agent 由决策器、工具、intermediate steps 和执行循环构成，Chain 则是更固定的编排模板，包括 retrieval、SQL/API 请求、结构化输出、数学、文档合并和总结类 chain。

## Key Claims

- explicit: LangChain 组件可粗分为 Model I/O、Retrieval、Callbacks、Memory 和 Composition，每类组件解决不同层面的 LLM 应用编排问题。
- explicit: Prompt 支持简单模板、聊天模板、消息占位符、few-shot 示例、动态示例选择和 partial 变量绑定。
- explicit: ChatModel 抽象了不同模型的消息格式、工具调用格式、流响应、结构化输出和元数据差异。
- explicit: Retrieval 的关键不是“向量库”单点，而是 loader、splitter、embedding、vector store、retriever、indexing 和多种检索器策略的组合。
- explicit: Callbacks 可用于跟踪和记录执行过程，但在部分 RunnableLambda、RunnableGenerator、Tool 异步子调用中需要手动传播配置。
- explicit: AgentExecutor 维护 agent-action-observation 循环，并需要处理不存在工具、工具参数异常、调用异常和过程跟踪。
- inferred: 这份 source 适合作为 LangChain 学习地图的组件总览节点，后续可把 Prompt、Retriever、Callback、AgentExecutor、Chain 分别编译成更小的概念页。

## External Links

- documentation: [LangChain concepts callbacks anchor](https://python.langchain.com/v0.2/docs/concepts/#callbacks) — source 根节点引用的 LangChain v0.2 concepts 页面；not verified.

## Links

- related: [[sources/Agent/LangChain.xmind|Agent/LangChain.xmind]] — 现有 source 与本 source 同属 LangChain 总览和应用编排证据。
- related: [[concepts/提示语工程|提示语工程]] — Model I/O 中的 PromptTemplate、ChatPromptTemplate、few-shot 和 parser 细节可补充提示语工程实践。
- related: [[concepts/上下文工程|上下文工程]] — Retrieval、Memory、Callbacks 和 Composition 都服务于上下文构造、传递和观测。

## Maintenance Notes

- No raw files were modified.
- External links were extracted from the XMind export and were not browsed or verified.
- Batch instruction prohibited index/log/concepts/maps/synthesis updates; this note records source-only ingest.
- Compile candidates: LangChain, LangChain Components, PromptTemplate, ChatModel, Output Parser, Retriever, LangChain Callback, LangChain Agent, AgentExecutor, Chain, RAG, Memory.
