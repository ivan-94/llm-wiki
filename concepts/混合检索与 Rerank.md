---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 2
learning_status: new
confidence: 2
difficulty: 3
review_after: 2026-06-13
---

# 混合检索与 Rerank

## Definition

混合检索是把向量语义搜索与关键词全文搜索等多种检索模式组合使用，再通过 Rerank 模型对候选文档重新打分排序，以提升最终送入模型的上下文质量。

## Why It Matters

单一检索方式存在各自盲区：向量搜索擅长语义相似，关键词搜索擅长精确术语匹配。混合检索结合两者，Rerank 再用更精准的语义匹配度对候选列表重排，使模型拿到的上下文既召回率高又排序准。

## Mental Model

把检索分两轮：第一轮是宽召回（hybrid = 向量 + BM25），第二轮是精排（rerank 模型重新计算相关度）。最终送入上下文的是第二轮排完的 top-k。

## Key Claims

- explicit（来自 RAG.xmind）：混合检索是组合不同搜索方式，例如向量搜索和传统关键词全文搜索。
- explicit（来自 RAG.xmind）：Rerank 会计算候选文档与用户问题的语义匹配度，并据此重新排序。
- explicit（来自 RAG.xmind）：混合检索结果需要合并和归一化，因此 rerank 可用于改善最终排序。
- explicit（来自 RAG.xmind）：Rerank 模型例子包括 Cohere rerank 和 bge-reranker。
- inferred：Rerank 通常作为"轻量精排"而不是生成步骤，它接收候选集并返回打分列表，不扩展候选范围。

## Examples

- 向量搜索先检索语义接近的 top-50，关键词搜索同时检索精确匹配的候选，两路合并后送入 Rerank 模型，取最终 top-5 作为上下文。
- Cohere rerank API：把问题和候选文档列表发给 Rerank 接口，返回按相关度降序的文档列表。
- bge-reranker：开源 Rerank 模型，可本地部署作为第二阶段精排。

## Common Confusions

- Rerank 不是替代检索，而是对已召回候选重排；召回阶段丢失的文档无法靠 Rerank 找回。
- 混合检索增加了合并、归一化和 Rerank 计算成本，需要和召回质量提升之间权衡。
- Rerank 分数和 embedding 相似度是不同数值，不能直接混用作为过滤阈值。

## Evidence

- explicit: [[sources/RAG/RAG.xmind|RAG.xmind]] — 直接提供混合检索定义和 Rerank 模型例子。
- related: [[sources/Langchain(Legacy)/Langchain  组件.xmind|Langchain 组件.xmind]] — 提到 Ensemble Retriever 和 Long-Context Reorder 作为检索策略组合案例。

## Relations

- part-of: [[concepts/RAG|RAG]]
- enables: [[concepts/向量检索|向量检索]]
- contrasts-with: [[concepts/向量检索|向量检索]] （向量检索是混合检索的一个分支，单独时有局限）
- used-in: [[concepts/Agentic RAG|Agentic RAG]]
- related-source: [[sources/RAG/RAG.xmind|RAG.xmind]]
- map-entry: [[maps/LLM 应用与数据处理学习地图|LLM 应用与数据处理学习地图]]

## My Understanding

混合检索+Rerank 是生产 RAG 的标配：单纯向量检索在准确术语匹配上容易失败，单纯关键词搜索在语义扩展上弱；Rerank 弥合了两路召回的打分空间差异，让模型拿到的候选列表排序更贴近真实相关性。

## Review Questions

- 混合检索相比单一向量检索的优势是什么？
- Rerank 在 RAG 流水线中处于哪个阶段？它接收什么，输出什么？
- 为什么合并多路召回结果需要归一化？

## Open Questions

- 混合检索的最优召回比例（向量：关键词）在不同任务下如何调配？
- Rerank 延迟对 RAG 响应时间的影响尚未有量化数据。
