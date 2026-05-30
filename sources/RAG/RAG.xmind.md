---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/RAG/RAG.xmind"
source_relpath: "RAG/RAG.xmind"
raw_created_at: 2024-09-02T03:00:10.239125+00:00
raw_modified_at: 2025-01-01T00:11:23+00:00
raw_size: 2041638
raw_fingerprint: "size=2041638;birth=2024-09-02T03:00:10.239125+00:00;mtime=2025-01-01T00:11:23+00:00"
raw_snapshot_at: 2026-05-29T22:11:39.974404+00:00
ingested_at: 2026-05-30
status: ingested
---

# RAG.xmind

## Source

- Raw file: [RAG/RAG.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/RAG/RAG.xmind>)
- Raw ref: `raw:RAG/RAG.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2024-09-02T03:00:10.239125+00:00`; modified `2025-01-01T00:11:23+00:00`; size `2041638`; snapshot `2026-05-29T22:11:39.974404+00:00`
- Coverage: exported and digested 1 sheet: `思维导图` (29 topics).

## Summary

这份图聚焦生产级 RAG 的两个方向：Rerank/混合检索用于提升召回结果排序，生产级索引技巧则强调检索块与合成块可以分离、超大文档集需要结构化检索和分层索引、任务可动态决定检索数据块。

## Source Digest

Rerank 分支把“混合检索”定义为向量搜索和关键词全文搜索等多种搜索方式的组合。因为不同检索模式的结果需要合并和归一化，重排序模型会重新计算候选文档与用户问题的语义匹配度，并改善最终给大模型的上下文顺序。source 记录的 rerank 模型例子包括 Cohere rerank 和 bge-reranker。

生产级 RAG 分支来自 LlamaIndex 资料，保留了三个高信号实践。第一，检索块和合成块可以不同：例如用文档摘要或句子做检索块，但把完整文档或句子前后上下文作为合成块。第二，超大文档集里普通 top-k 很难直接生效，需要把数据转换成结构化信息做元数据过滤，或建立“文档摘要 -> 文档具体块”的分层索引。第三，根据任务要求动态检索数据块，说明检索不是固定 top-k，而应随查询目标、上下文预算和回答需要调整。

## Key Claims

- explicit: 混合检索是组合不同搜索方式，例如向量搜索和传统关键词全文搜索。
- explicit: Rerank 会计算候选文档与用户问题的语义匹配度，并据此重新排序。
- explicit: 混合检索结果需要合并和归一化，因此 rerank 可用于改善最终排序。
- explicit: 检索块和合成块可以分离，检索可用摘要或句子，合成可用完整文档或句子前后上下文。
- explicit: 超大文档集需要结构化检索、元数据过滤或分层文档索引，普通 top-k 不一定有效。
- inferred: 这份 source 与“RAG vs 长文本”互补：它补的是生产级 RAG 的索引与排序控制面。

## External Links

- article: [Rerank RAG article](https://luxiangdong.com/2023/11/06/rerank/) — Rerank 分支扩展阅读；not verified.
- documentation: [Production RAG tips](https://docs.llamaindex.ai/en/stable/optimizing/production_rag/) — 生产级 RAG 技巧来源；not verified.

## Links

- compiled-concept: [[concepts/RAG|RAG]] — source 提供混合检索、Rerank、检索块/合成块分离和生产级 RAG 控制面的证据。
- compiled-synthesis: [[synthesis/RAG 与长上下文|RAG 与长上下文]] — source 补充为什么长上下文不能完全替代索引、排序和元数据控制。
- map-entry: [[maps/LLM 应用与数据处理学习地图|LLM 应用与数据处理学习地图]] — source 是 RAG 生产化主题的学习材料。
- related: [[concepts/上下文工程|上下文工程]] — Rerank、分层索引、检索块/合成块分离都用于选择进入模型上下文的信息。
- related: [[sources/RAG/RAG vs 长文本.xmind|RAG vs 长文本.xmind]] — 互补：本 source 覆盖生产级 RAG 控制面，对方覆盖 RAG/长上下文取舍与 RAPTOR。
- related: [[sources/RAG/长记忆.xmind|长记忆.xmind]] — 长期记忆检索依赖向量/图数据库，与本 source 的向量检索和混合检索形成上下游。
- related: [[sources/数据处理/结构化文档提取.xmind|结构化文档提取.xmind]] — 文档进入 RAG 前需要结构化解析，两个 source 在 pipeline 上首尾相接。

## Maintenance Notes

- No raw files were modified.
- External links were extracted from the XMind export and were not browsed or verified.
- The raw contains a placeholder branch `分支主题 3`; no substantive claim was derived from it.
- Batch instruction prohibited index/log/concepts/maps/synthesis updates; this note records source-only ingest.
- Compile candidates: RAG, Rerank, hybrid retrieval, production RAG, retrieval chunk vs synthesis chunk, hierarchical index.
