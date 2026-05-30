---
page_type: synthesis
updated_at: 2026-05-30
status: active
source_count: 5
learning_status: learning
confidence: 3
difficulty: 4
review_after: 2026-06-13
---

# RAG 与长上下文

## Thesis

长上下文会降低一部分 RAG 工程复杂度，但不会让 RAG 消失。真正的选择不是二选一，而是如何组合检索、摘要、完整文档回填、rerank、元数据过滤和上下文预算。RAPTOR 和 Agentic RAG 分别代表了这一思路在索引层和决策层的具体实现。

## Comparison

| 维度 | 长上下文 | RAG |
| --- | --- | --- |
| 优势 | 减少分块和检索调参，适合少量长文档直接阅读 | 适合大型文档库、可控召回、安全过滤和成本控制 |
| 风险 | 成本、延迟、注意力分散、排序敏感、上下文污染 | 分块失真、召回失败、索引维护和 rerank 成本 |
| 关键控制点 | 文档顺序、上下文压缩、长上下文召回测试 | 检索粒度、合成粒度、混合检索、rerank、元数据 |
| 组合方式 | 接收 RAG 找到的完整文档或摘要层级 | 先检索摘要/候选，再回填长上下文 |

## RAPTOR：分层摘要索引

RAPTOR 是一种递归聚类和总结方案（来自 `RAG vs 长文本.xmind`）：

1. **嵌入原始文档 chunk**，对 chunk 做聚类（UMAP 降维 + GMM 聚类）。
2. **对每个 cluster 生成摘要**，摘要再做 embedding 和聚类。
3. **递归执行**，直到形成覆盖不同抽象层级的层次摘要树。
4. **所有层级的摘要都存入向量数据库**，查询时可以命中不同抽象层级的内容。

RAPTOR 的核心价值：让 RAG 不只能检索细节 chunk，还能在更高抽象层级上检索主题摘要，适合需要跨多个文档做综合判断的查询。

## Agentic RAG 决策环

Agentic RAG 把检索变成带决策节点的多步环路（来自 `Lang Graph 案例学习.xmind`，legacy · not verified）：

```
用户查询 → 判断是否需要检索 → 检索 → 评估文档相关性
    ↓ 不相关                          ↓ 相关
 重写查询 → Web Search               生成答案 → 评估答案质量
                                          ↓ 不满意
                                       重写查询 / 补充检索
```

三种主要 Agentic RAG 变体：
- **Adaptive RAG**：先判断问题是否需要检索，简单问题直接用模型知识。
- **Corrective RAG**：检索后评估文档相关性，不相关时切换到 Web 搜索。
- **Self RAG**：生成后自我评估答案与证据的匹配质量，决定是否需要重试。

## Evidence

- [[sources/RAG/RAG vs 长文本.xmind|RAG vs 长文本]] — 长上下文限制、RAG 保留理由和 RAPTOR/摘要检索方案。
- [[sources/RAG/RAG.xmind|RAG.xmind]] — rerank、hybrid retrieval、检索块/合成块分离和 production RAG 技巧。
- [[sources/RAG/长记忆.xmind|长记忆.xmind]] — 将长期记忆分类连接到上下文长期化问题。
- [[sources/Langchain(Legacy)/Langchain 案例学习.xmind|Langchain 案例学习]] — RAG 应用案例背景（legacy · not verified）。
- [[sources/Langchain(Legacy)/Lang Graph 案例学习.xmind|Lang Graph 案例学习]] — Agentic RAG 的 LangGraph 实现（legacy · not verified）。

## Implications

- 小型、少量、可一次性阅读的资料可以先用长上下文简化系统。
- 大型、多源、权限敏感、需要可追溯证据的资料仍应保留 RAG 控制面。
- 高质量 RAG 不应只优化 embedding；还要优化文档解析、chunk 设计、metadata、rerank 和 answer synthesis。
- 长上下文评估要检查排序、位置偏差和 needle-in-a-haystack 召回，而不是只看窗口大小。
- RAPTOR 适合需要跨文档摘要检索的场景；Agentic RAG 适合准确率优先、允许多步延迟的场景。

## Related Concepts

- [[concepts/RAG|RAG]]
- [[concepts/Agentic RAG|Agentic RAG]]
- [[concepts/分层文档索引|分层文档索引]]
- [[concepts/混合检索与 Rerank|混合检索与 Rerank]]
- [[concepts/Token 和 Embedding|Token 和 Embedding]]
- [[concepts/结构化文档解析|结构化文档解析]]
- [[concepts/上下文工程|上下文工程]]

## My Take

长上下文改变的是 RAG 的设计空间，不是替代 RAG。更实际的路线是：用 RAG 管理大规模候选和可控性，用长上下文承接更完整的局部证据。RAPTOR 和 Agentic RAG 是两个方向的升级：前者在索引层建立多粒度摘要，后者在决策层引入自适应检索逻辑。

## Open Questions

- source 中关于长上下文召回和具体模型表现的资料未联网核验。
- RAPTOR 的聚类参数和中文文档效果需要实测。
- Agentic RAG 在延迟敏感场景的可用性需要基准测试（legacy · not verified）。
