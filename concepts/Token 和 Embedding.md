---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 3
learning_status: new
confidence: 3
difficulty: 4
review_after: 2026-06-06
---

# Token 和 Embedding

## Definition

Token 是语言模型处理文本的离散单位，Embedding 是把 token、句子或文档映射到连续向量空间的表示，用于模型计算语义、上下文和相似度。

## Why It Matters

LLM 的输入、输出、上下文窗口、成本、检索和微调都建立在 token 与 embedding 之上。不了解它们，很难理解 RAG、Transformer、文本分类和上下文工程。

## Mental Model

Token 是切块，Embedding 是坐标：分词器决定文本如何被切成模型可处理的片段，embedding 把片段放进可计算的语义空间。

## Key Claims

- 词袋模型简单但丢失词序、语法和上下文。
- Word2Vec 将词映射到低维稠密向量，使语义相近词在空间中更近。
- BPE、WordPiece 等分词算法会影响词表、特殊 token 和模型输入粒度；GPT 系列用 BPE，BERT 用 WordPiece。
- 分词器训练依赖数据集，训练后模型才知道 token 的意义。
- 上下文化词嵌入由语言模型按句内语境动态生成，区别于 Word2Vec 等静态固定词向量。
- 文本/检索 embedding 把整句、文档或多个 token 压成单个向量，是 RAG 检索常说的 embedding；它与“上下文化词嵌入”是不同用途的两类。

## Examples

- `Token and Embedding.xmind` 梳理词袋、Word2Vec、RNN、Transformer、BERT/GPT 和文本嵌入。
- `Transformer.xmind` 把 token/embedding 放到语言模型发展路线里。
- `实战：文本分类.xmind` 使用 embedding 相似度和生成/表示模型做分类任务。

## Common Confusions

- token 不等于自然语言里的词；一个词可能被拆成多个 token。
- embedding 不只用于 RAG，也用于分类、聚类、语义匹配和模型内部表示。
- 上下文化 embedding（随语境变化）与静态词向量（如 Word2Vec，固定）不是同一层概念。
- 检索 embedding（整段→单向量）与上下文化词嵌入（每个 token 一个随语境的向量）用途不同，别混用。
- BPE 和 WordPiece 是不同模型家族的分词算法，不能默认通用。

## Evidence

- [[sources/LLM/Token and Embedding.xmind|Token and Embedding.xmind]]
- [[sources/LLM/Transformer/Transformer.xmind|Transformer.xmind]]
- [[sources/LLM/实战：文本分类.xmind|实战：文本分类]]

## Relations

- enables: [[concepts/Transformer|Transformer]] — token/向量表示是 Transformer 的输入前提（修正：原 `prerequisite: Transformer` 方向反了）。
- enables: [[concepts/注意力机制|注意力机制]] — 注意力作用在 token 的向量表示上。
- enables: [[concepts/RAG|RAG]] — 检索 embedding 是 RAG 的基础（修正方向；RAG 他人维护，仅互链）。
- enables: [[concepts/Chat Template 与 Tokenizer|Chat Template 与 Tokenizer]] — 分词是 chat template 之前的一步。
- used-in: [[concepts/LLM 微调|LLM 微调]] — 数据准备需分词/对齐。
- map-entry: [[maps/LLM 基础学习地图|LLM 基础学习地图]]

## My Understanding

当前理解：token 和 embedding 是 LLM 把文本变成可计算对象的入口，也是后续上下文、检索和成本控制的共同底层。

## Review Questions

- 词袋、Word2Vec 和上下文化 embedding 的差别是什么？
- BPE 和 WordPiece 在学习路径中为什么重要？
- RAG 中的 embedding 通常表示什么？

## Open Questions

- 不同 embedding 模型的当前能力和价格未联网核验。
