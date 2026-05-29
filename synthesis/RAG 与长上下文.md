---
page_type: synthesis
updated_at: 2026-05-30
status: active
source_count: 5
learning_status: learning
confidence: 3
difficulty: 4
review_after: 2026-06-06
---

# RAG 与长上下文

## Thesis

长上下文会降低一部分 RAG 工程复杂度，但不会让 RAG 消失。真正的选择不是二选一，而是如何组合检索、摘要、完整文档回填、rerank、元数据过滤和上下文预算。

## Comparison

| 维度 | 长上下文 | RAG |
| --- | --- | --- |
| 优势 | 减少分块和检索调参，适合少量长文档直接阅读 | 适合大型文档库、可控召回、安全过滤和成本控制 |
| 风险 | 成本、延迟、注意力分散、排序敏感、上下文污染 | 分块失真、召回失败、索引维护和 rerank 成本 |
| 关键控制点 | 文档顺序、上下文压缩、长上下文召回测试 | 检索粒度、合成粒度、混合检索、rerank、元数据 |
| 组合方式 | 接收 RAG 找到的完整文档或摘要层级 | 先检索摘要/候选，再回填长上下文 |

## Evidence

- [[sources/RAG/RAG vs 长文本.xmind|RAG vs 长文本]] 提供长上下文限制、RAG 保留理由和 RAPTOR/摘要检索方案。
- [[sources/RAG/RAG.xmind|RAG.xmind]] 提供 rerank、hybrid retrieval、检索块/合成块分离和 production RAG 技巧。
- [[sources/RAG/长记忆.xmind|长记忆.xmind]] 将长期记忆分类连接到上下文长期化问题。
- [[sources/Langchain(Legacy)/Langchain 案例学习.xmind|Langchain 案例学习]] 提供 RAG 应用案例背景。

## Implications

- 小型、少量、可一次性阅读的资料可以先用长上下文简化系统。
- 大型、多源、权限敏感、需要可追溯证据的资料仍应保留 RAG 控制面。
- 高质量 RAG 不应只优化 embedding；还要优化文档解析、chunk 设计、metadata、rerank 和 answer synthesis。
- 长上下文评估要检查排序、位置偏差和 needle-in-a-haystack 召回，而不是只看窗口大小。

## Related Concepts

- [[concepts/RAG|RAG]]
- [[concepts/Token 和 Embedding|Token 和 Embedding]]
- [[concepts/结构化文档解析|结构化文档解析]]
- [[concepts/上下文工程|上下文工程]]

## My Take

长上下文改变的是 RAG 的设计空间，不是替代 RAG。更实际的路线是：用 RAG 管理大规模候选和可控性，用长上下文承接更完整的局部证据。

## Open Questions

- source 中关于长上下文召回和具体模型表现的资料未联网核验。
