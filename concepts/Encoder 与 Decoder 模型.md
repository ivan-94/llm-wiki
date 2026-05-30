---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 4
learning_status: new
confidence: 2
difficulty: 3
review_after: 2026-06-06
---

# Encoder 与 Decoder 模型

## Definition

Encoder 模型与 Decoder 模型是 Transformer 的两条使用路线：encoder-only（如 BERT）做双向上下文理解与表示，decoder-only（如 GPT）做单向自回归生成；二者还可组合成 encoder-decoder（Seq2Seq）。

## Why It Matters

“该用 BERT 还是 GPT”往往取决于任务是理解还是生成。理解这条分化，是看懂表示模型 vs 生成模型、文本分类选型、以及 MLM vs next-token 训练目标差异的基础。

## Mental Model

读者 vs 作者：encoder 像通读全文做笔记的读者，能双向看上下文，擅长理解与表示；decoder 像逐字往下写的作者，只能看左边已写内容，擅长生成续写。

## Key Claims

- BERT 属于 encoder-only representation model，用 masked language modeling 学双向上下文，适合迁移学习/微调（explicit，`Token and Embedding.xmind`）。
- GPT 属于 decoder-only generative model，面向 next-token 生成（explicit，`Token and Embedding.xmind`）。
- GPT 采用单向语境偏生成连续文本，BERT 采用双向语境和 MLM 偏上下文理解（explicit，`Transformer.xmind`）。
- 表示模型与生成模型都能做文本分类：表示模型可微调分类头或用 embedding 余弦相似度匹配标签（explicit，`实战：文本分类.xmind`）。
- BERT 是常见的 encoder-only 基础模型且有很多变体（explicit，`实战：文本分类.xmind`）。
- encoder-decoder（Seq2Seq）结构常用于机器翻译等任务（explicit，`python 深度学习入门.xmind`）。

## Examples

- `Token and Embedding.xmind` 明确区分 encoder-only representation models 与 decoder-only generative models。
- `实战：文本分类.xmind` 用表示模型（BERT 微调 / embedding 相似度）与生成模型两条路线做分类。
- `python 深度学习入门.xmind` 的 Transformer sheet 用英西翻译演示 encoder-decoder。

## Common Confusions

- decoder-only 不代表“没有理解能力”，只是用单向自回归的方式获得，且更偏生成。
- BERT 的“双向”指能同时看左右上下文，不是指能像 GPT 那样自由生成长文本。
- 文本分类既可用表示模型（更稳、可解释相似度），也可用生成模型（更开放），需按标签体系与延迟权衡。

## Evidence

- [[sources/LLM/Token and Embedding.xmind|Token and Embedding]]
- [[sources/LLM/Transformer/Transformer.xmind|Transformer.xmind]]
- [[sources/LLM/实战：文本分类.xmind|实战：文本分类]]
- [[sources/机器学习/python 深度学习入门.xmind|python 深度学习入门]]

## Relations

- part-of: [[concepts/Transformer|Transformer]] — 两类模型都是 Transformer 的特化路线。
- prerequisite: [[concepts/注意力机制|注意力机制]] — encoder 双向注意力、decoder 因果注意力的差别源于此。
- contrasts-with: [[concepts/自回归语言模型|自回归语言模型]] — decoder-only 即自回归路线，encoder-only 不是。
- implemented-by: [[entities/BERT|BERT]] — encoder-only 代表模型。
- implemented-by: [[entities/GPT 与 ChatGPT|GPT 与 ChatGPT]] — decoder-only 代表模型。
- related-source: [[sources/LLM/实战：文本分类.xmind|实战：文本分类]] — 提供表示/生成两条分类路线证据。
- map-entry: [[maps/LLM 基础学习地图|LLM 基础学习地图]]

## My Understanding

当前理解：encoder 偏理解（双向、MLM、做表示和分类），decoder 偏生成（单向、自回归、续写）。选型先问任务是“看懂”还是“写出”。

## Review Questions

- BERT 和 GPT 分别属于哪种结构，训练目标是什么？
- 表示模型做文本分类有哪两条路径？
- 为什么 encoder 能双向而 decoder 通常只能单向？

## Open Questions

- T5 等 encoder-decoder 大模型与现代统一架构趋势未在当前 source 充分覆盖。
