---
page_type: entity
updated_at: 2026-05-30
status: active
source_count: 4
---

# BERT

## What It Is

BERT 是 Google 提出的 encoder-only Transformer 表示模型，用 masked language modeling（MLM）学习双向上下文表示，擅长理解类任务（分类、表示、迁移学习/微调），有大量变体。

## Role In This Wiki

在本 wiki 中，BERT 是 encoder-only / 表示模型路线的代表，与 decoder-only 的 GPT 形成对照；也是文本分类、WordPiece 分词、Adapters 微调等内容的参照模型。

## Key Facts

- BERT 属于 encoder-only representation model，用 MLM 训练，适合双向上下文理解的迁移学习/微调（explicit，`Token and Embedding.xmind`）。
- BERT 采用双向语境，相比 GPT 的单向更偏上下文理解（explicit，`Transformer.xmind`）。
- BERT 是常见的 encoder-only 基础模型且有很多变体（explicit，`实战：文本分类.xmind`）。
- BERT 用 WordPiece 分词（explicit，`Token and Embedding.xmind`）。
- Adapters 微调常引用 BERT/GLUE 相关数据作为效果参照（explicit，`微调生成模型.xmind`）。
- `BERT 模型微调.xmind` 为 partial 源，仅有主题与一条 PyTorch 微调教程链接，无完整流程（explicit）。

## Related Concepts

- implemented-by: [[concepts/Encoder 与 Decoder 模型|Encoder 与 Decoder 模型]] — encoder-only 的代表实例。
- contrasts-with: [[entities/GPT 与 ChatGPT|GPT 与 ChatGPT]] — 双向理解 vs 单向生成。
- related-concept: [[concepts/Chat Template 与 Tokenizer|Chat Template 与 Tokenizer]] — BERT 用 WordPiece。
- used-in: [[concepts/Token 和 Embedding|Token 和 Embedding]] — 上下文化表示的代表模型。

## Evidence

- [[sources/LLM/Token and Embedding.xmind|Token and Embedding]]
- [[sources/LLM/Transformer/Transformer.xmind|Transformer.xmind]]
- [[sources/LLM/实战：文本分类.xmind|实战：文本分类]]
- [[sources/LLM/Transformer/BERT 模型微调.xmind|BERT 模型微调]]

## Open Questions

- `BERT 模型微调.xmind` 为 partial 占位，BERT 微调的任务类型、数据格式、训练参数需后续 source 补全。
