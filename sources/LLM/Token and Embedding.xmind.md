---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/LLM/Token and Embedding.xmind"
source_relpath: "LLM/Token and Embedding.xmind"
raw_created_at: 2025-01-22T05:47:55.329653+00:00
raw_modified_at: 2025-01-22T12:07:17.052162+00:00
raw_size: 5654423
raw_fingerprint: "size=5654423;birth=2025-01-22T05:47:55.329653+00:00;mtime=2025-01-22T12:07:17.052162+00:00"
raw_snapshot_at: 2026-05-29T22:09:33.493587+00:00
ingested_at: 2026-05-30
status: ingested
---

# Token and Embedding.xmind

## Source

- Raw file: [LLM/Token and Embedding.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/LLM/Token%20and%20Embedding.xmind>)
- Raw ref: `raw:LLM/Token and Embedding.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2025-01-22T05:47:55.329653+00:00`; modified `2025-01-22T12:07:17.052162+00:00`; size `5654423`; snapshot `2026-05-29T22:09:33.493587+00:00`
- Coverage: Exported and read 1 sheet: `思维导图`.

## Summary

这张图梳理了从词袋模型、Word2Vec、RNN 到 Transformer 的表示学习演进，并把 tokenization、上下文化词嵌入和文本嵌入放到 LLM 基础概念中解释。

## Source Digest

source 的主线是“文本如何被模型表示”。它先从词袋模型讲起：词袋把文档转成词频向量，简单但丢失词序和语义关系；随后转向 Word2Vec，用分布式假设把词映射到稠密向量空间，适合度量语义相似度，但仍难处理多义词、词序和上下文。再往后，RNN 通过循环结构保留历史信息，可以处理序列和词序，但长序列信息会衰减，因此引入注意力机制，让模型能按任务需要访问过去隐藏状态。

Transformer 部分强调它成为主流语言模型架构的原因：自注意力支持并行化、任意距离 token 关系、显式位置编码、多头注意力、残差连接和层归一化。图中还区分了 Encoder-only representation models 与 Decoder-only generative models：BERT 代表前者，通过 masked language modeling 学习双向上下文表示，更适合迁移学习和任务微调；GPT 代表后者，面向生成式 next-token 预测，并与大规模 LLM 训练范式关联。

最后，source 把 Token 和 Embedding 作为 LLM 输入/输出表示的核心接口：tokenization 包括分割方式、词表大小、特殊 token 和算法选择，示例包括 GPT 使用的 BPE 与 BERT 使用的 WordPiece；上下文化词嵌入由语言模型根据句内语境动态生成；文本嵌入则用单个向量表示句子、文档或多个 token，是 RAG 检索场景常说的 embedding。

## Key Claims

- explicit: 词袋模型把文档表示为词汇表计数向量，但忽略词序、语法和上下文。
- explicit: Word2Vec 基于分布式假设，把词映射到固定维度稠密向量空间，使语义相近词在空间中更接近。
- explicit: RNN 能利用循环结构保存历史信息，相比 Word2Vec 更能考虑上下文和词序，但传统 RNN 难处理长序列。
- explicit: 注意力机制让模型能直接访问过去隐藏状态，并按任务需要关注输入序列的不同部分。
- explicit: Transformer 的优势包括自注意力并行化、长距离依赖建模、位置编码、多头注意力、残差连接、层归一化和模块化结构。
- explicit: BERT 属于 Encoder-only representation model，使用 masked language modeling 训练，更适合需要双向上下文理解的迁移学习/微调任务。
- explicit: GPT 属于 Decoder-only generative model，图中将其与 Generative Pre-trained Transformer、LLM 和“预训练 + 监督微调”训练范式关联。
- explicit: GPT 系列使用 BPE，BERT 使用 WordPiece；分词器训练依赖数据集，训练后模型才知道 token 的意义。
- explicit: RAG 场景中的 embedding 通常指把句子、文档或多个 token 表示为单一向量的 text embedding。
- inferred: 该 source 可以作为后续 LLM 基础学习地图中的“表示学习与 Transformer 前置概念”入口。

## External Links

No external links found in extracted content.

## Links

- compiled-concept: [[concepts/Token 和 Embedding|Token 和 Embedding]] — source 提供 token、embedding、Word2Vec、BPE/WordPiece 和 text embedding 的学习证据。
- compiled-concept: [[concepts/Transformer|Transformer]] — source 把表示学习演进连接到 Transformer、BERT 和 GPT。
- map-entry: [[maps/LLM 基础学习地图|LLM 基础学习地图]] — source 是 LLM 基础学习路径中的表示学习入口。

## Maintenance Notes

- XMind export succeeded for all discovered sheets.
- “扩展阅读”只列出 `Hands on Large Language Models` 书名，没有可见 URL，未写入 External Links。
