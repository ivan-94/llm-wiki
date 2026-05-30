---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 7
learning_status: new
confidence: 3
difficulty: 4
review_after: 2026-06-13
---

# RAG

## Definition

RAG（Retrieval-Augmented Generation）是在生成前先从外部知识库检索相关内容，再把检索结果作为上下文交给模型生成答案的架构。

## Why It Matters

RAG 是把模型能力连接到私有资料、最新事实和大规模文档库的常见方法。即使长上下文增强，RAG 仍在成本、延迟、可控性、安全、索引和大型数据集上有价值。

## Mental Model

RAG 是上下文选择系统：先决定哪些资料值得进模型，再决定以什么粒度、顺序和证据形式进入上下文。整个流水线分为两个阶段——Indexing（建立索引）和 Retrieval & Generation（检索并生成）。

## 子系统地图

| 子概念 | 解决的问题 |
| --- | --- |
| [[concepts/文档分块|文档分块]] | 切割文档为合适粒度，检索块和合成块可以不同 |
| [[concepts/向量检索|向量检索]] | 语义相似度搜索，RAG 检索主干 |
| [[concepts/混合检索与 Rerank|混合检索与 Rerank]] | 结合向量+关键词召回，再精排 |
| [[concepts/分层文档索引|分层文档索引]] | 摘要层 + chunk 层，解决超大文档集 top-k 稀释问题 |
| [[concepts/查询分析|查询分析]] | 改写/分解/扩展查询，提升召回质量 |
| [[concepts/History-aware RAG|History-aware RAG]] | 多轮对话中改写追问为独立可检索问题 |
| [[concepts/Agentic RAG|Agentic RAG]] | 把检索提升为可自主决策的检索环路 |
| [[concepts/检索评估|检索评估]] | 衡量检索阶段质量，与生成评估分开 |

## Key Claims

- RAG 通常包含文档加载、分块、embedding、索引、检索、rerank 和生成。
- 长上下文能简化部分 RAG 复杂度，但不等于替代 RAG；大型数据库、成本、安全可控性仍让 RAG 有价值。
- 生产级 RAG 需要区分检索块和合成块，支持元数据过滤、分层索引、摘要检索和动态块选择。
- Rerank 用候选文档与问题的语义匹配度重新排序检索结果；混合检索结合向量搜索和关键词全文搜索。
- 长期记忆和 RAG 都依赖检索，但记忆更强调会话/用户/经历的生命周期和演化。
- RAPTOR 是递归聚类和摘要方案，把多层级摘要存入向量数据库，形成覆盖不同抽象层级的层次结构。
- Agentic RAG 把检索变成带决策节点的多步环路，包括 Adaptive RAG、Corrective RAG 和 Self RAG。
- History-aware RAG 先改写追问为独立问题，再执行标准 RAG，解决多轮对话的检索语境依赖问题。

## Examples

- `RAG vs 长文本.xmind` 比较长上下文与 RAG，给出摘要检索后回填完整文档的组合方案。
- `RAG.xmind` 记录 hybrid retrieval、rerank（Cohere rerank/bge-reranker）、production RAG 和检索块/合成块分离。
- `Langchain 案例学习.xmind` 提供带引用 RAG、History-aware RAG 和代码理解 RAG 应用案例（legacy · not verified）。
- `长记忆.xmind` 将长期记忆（mem0）与 RAG 向量检索连接。
- `Lang Graph 案例学习.xmind` 展示 Adaptive RAG、Corrective RAG、Self RAG 的 LangGraph 实现（legacy · not verified）。

## Common Confusions

- RAG 不是向量数据库本身；向量库只是索引/检索组件之一。
- chunk 越小不一定越好，检索粒度和生成粒度可以不同（检索块和合成块分离）。
- 长上下文不是"把所有资料塞进去"，注意力、成本和安全控制仍然存在。
- 向量检索和关键词搜索有各自盲区，生产场景推荐混合检索。
- Agentic RAG 不等于检索更多文档，核心是在决策点引入模型判断。

## Evidence

- explicit: [[sources/RAG/RAG vs 长文本.xmind|RAG vs 长文本]] — 长上下文限制、RAG 保留理由和 RAPTOR/摘要检索方案。
- explicit: [[sources/RAG/RAG.xmind|RAG.xmind]] — 混合检索、Rerank、检索块/合成块分离和生产级 RAG 控制面。
- explicit: [[sources/RAG/长记忆.xmind|长记忆.xmind]] — 长期记忆与向量检索、图关系查询的连接。
- explicit: [[sources/Langchain(Legacy)/Langchain 案例学习.xmind|Langchain 案例学习]] — RAG 应用案例（legacy · not verified）。
- explicit: [[sources/Langchain(Legacy)/Lang Graph 案例学习.xmind|Lang Graph 案例学习]] — Agentic RAG 实现（legacy · not verified）。
- related: [[sources/Langchain(Legacy)/Langchain  组件.xmind|Langchain 组件]] — Retriever 类型和 RAG 组件层（legacy · not verified）。
- related: [[sources/数据处理/结构化文档提取.xmind|结构化文档提取]] — 文档进入 RAG 前的解析质量决定检索质量。

## Relations

- builds-on: [[concepts/Token 和 Embedding|Token 和 Embedding]]
- part-of: [[concepts/上下文工程|上下文工程]]
- contrasts-with: [[concepts/LLM 微调|LLM 微调]]
- contrasts-with: [[synthesis/RAG 与长上下文|RAG 与长上下文]] （长上下文是 RAG 的互补而非替代）
- used-in: [[concepts/Agent 记忆|Agent 记忆]]
- contains: [[concepts/混合检索与 Rerank|混合检索与 Rerank]]
- contains: [[concepts/文档分块|文档分块]]
- contains: [[concepts/向量检索|向量检索]]
- contains: [[concepts/分层文档索引|分层文档索引]]
- contains: [[concepts/查询分析|查询分析]]
- contains: [[concepts/History-aware RAG|History-aware RAG]]
- contains: [[concepts/Agentic RAG|Agentic RAG]]
- contains: [[concepts/检索评估|检索评估]]
- implemented-by: [[entities/LangChain|LangChain]] （Retriever 族，legacy · not verified）
- map-entry: [[maps/LLM 应用与数据处理学习地图|LLM 应用与数据处理学习地图]]

## My Understanding

RAG 的核心不是"搜一下"，而是用索引、过滤、重排和上下文预算控制模型看到什么。生产级 RAG 要设计检索块和合成块两个粒度，并在混合检索、rerank、分层索引和 Agentic 决策环路中找到质量与效率的平衡。

## Review Questions

- 检索块和合成块为什么可以不同？
- 长上下文为什么没有完全替代 RAG？
- Rerank 在 RAG 流水线中解决什么问题？
- History-aware RAG 解决了什么问题，流程是什么？
- Adaptive RAG、Corrective RAG 和 Self RAG 分别在什么决策点引入 Agent 判断？
- RAPTOR 的层次索引是如何构建的？

## Open Questions

- RAGFlow、LlamaIndex 等工具当前实现细节未联网核验。
- 各 Agentic RAG 变体（Adaptive/Corrective/Self）的质量-延迟权衡缺乏实测数据。
