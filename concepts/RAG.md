---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 6
learning_status: new
confidence: 3
difficulty: 4
review_after: 2026-06-06
---

# RAG

## Definition

RAG（Retrieval-Augmented Generation）是在生成前先从外部知识库检索相关内容，再把检索结果作为上下文交给模型生成答案的架构。

## Why It Matters

RAG 是把模型能力连接到私有资料、最新事实和大规模文档库的常见方法。即使长上下文增强，RAG 仍在成本、延迟、可控性、安全、索引和大型数据集上有价值。

## Mental Model

RAG 是上下文选择系统：先决定哪些资料值得进模型，再决定以什么粒度、顺序和证据形式进入上下文。

## Key Claims

- RAG 通常包含文档加载、分块、embedding、索引、检索、rerank 和生成。
- 长上下文能简化部分 RAG 复杂度，但不等于替代 RAG。
- 生产级 RAG 需要区分检索块和合成块，支持元数据过滤、分层索引、摘要检索和动态块选择。
- Rerank 用候选文档与问题的语义匹配度重新排序检索结果。
- 长期记忆和 RAG 都依赖检索，但记忆更强调会话/用户/经验的生命周期和演化。

## Examples

- `RAG vs 长文本.xmind` 比较长上下文与 RAG，并给出摘要检索再回填完整文档的组合方案。
- `RAG.xmind` 记录 hybrid retrieval、rerank、production RAG 和检索块/合成块分离。
- `Langchain 案例学习.xmind` 提供 RAG 应用案例。
- `长记忆.xmind` 将 RAG 与 Agent memory 的长期上下文问题连接起来。

## Common Confusions

- RAG 不是向量数据库本身；向量库只是索引/检索组件之一。
- chunk 越小不一定越好，检索粒度和生成粒度可以不同。
- 长上下文不是“把所有资料塞进去”，注意力、成本和安全控制仍然存在。

## Evidence

- [[sources/RAG/RAG vs 长文本.xmind|RAG vs 长文本]]
- [[sources/RAG/RAG.xmind|RAG.xmind]]
- [[sources/RAG/长记忆.xmind|长记忆.xmind]]
- [[sources/Langchain(Legacy)/Langchain 案例学习.xmind|Langchain 案例学习]]

## Relations

- builds-on: [[concepts/Token 和 Embedding|Token 和 Embedding]]
- part-of: [[concepts/上下文工程|上下文工程]]
- contrasts-with: [[concepts/LLM 微调|LLM 微调]]
- used-in: [[concepts/Agent 记忆|Agent 记忆]]
- used-in: [[synthesis/RAG 与长上下文|RAG 与长上下文]]
- map-entry: [[maps/LLM 应用与数据处理学习地图|LLM 应用与数据处理学习地图]]

## My Understanding

当前理解：RAG 的核心不是“搜一下”，而是用索引、过滤、重排和上下文预算控制模型看到什么。

## Review Questions

- 检索块和合成块为什么可以不同？
- 长上下文为什么没有完全替代 RAG？
- Rerank 在 RAG 流水线中解决什么问题？

## Open Questions

- RAGFlow、LlamaIndex 等工具当前实现细节未联网核验。
