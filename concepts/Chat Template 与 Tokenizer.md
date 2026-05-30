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

# Chat Template 与 Tokenizer

## Definition

Tokenizer 负责把文本切分成 token 并转成数字编码；Chat Template 是把多轮对话（system/user/assistant 等角色）拼装成模型期望输入格式的模板。每个模型通常自带配套的 tokenizer 和 chat template。

## Why It Matters

喂给模型的不是裸文本，而是被特定 tokenizer 切分、按特定 chat template 拼好的序列。模板或分词器用错，会导致角色错位、特殊 token 缺失、对话格式不被识别，是部署与微调时常见的隐性 bug。

## Mental Model

报关流程：文本先过 tokenizer“拆箱编号”（切 token、加特殊符、转 ID），再过 chat template“按格式打包”（标好谁说的、哪里开始结束），模型才认得这批货。

## Key Claims

- tokenizer 不等于按字切分；不同模型有自己的 tokenizer 和 chat template，开源模型之间没有统一 template 标准（explicit，`大模型.xmind`）。
- GPT 系列用 BPE，BERT 用 WordPiece；分词器训练依赖数据集，训练后模型才知道 token 的意义（explicit，`Token and Embedding.xmind`）。
- 微调数据准备需把指令-响应对套入提示模板，再分词、填充、对齐（explicit，`模型微调.xmind`）。
- 分词被解释为把 token 转为数字表示，不同模型使用不同编码器/解码器（explicit，`模型微调.xmind`）。
- alpaca 数据格式含 instruction、input、output、system、history 等字段，是一种面向微调的对话/指令模板（explicit，`Llama 微调.xmind`）。

## Examples

- `大模型.xmind` 引用 ModelScope SWIFT 的 `template.py` 作为开源模型 chat template 示例。
- `Llama 微调.xmind` 区分 alpaca 与 sharegpt 数据格式，给出 alpaca JSON 字段结构。
- `Token and Embedding.xmind` 用 BPE（GPT）与 WordPiece（BERT）对比说明分词算法差异。

## Common Confusions

- tokenizer 和 chat template 是两件事：前者管“怎么切词转数字”，后者管“怎么排版对话”。
- 没有跨模型统一的 chat template；换模型常需换模板，否则对话结构会被误解析。
- 同一段文本在不同 tokenizer 下的 token 数不同，直接影响上下文占用与计费。

## Evidence

- [[sources/LLM/大模型.xmind|大模型]]
- [[sources/LLM/Token and Embedding.xmind|Token and Embedding]]
- [[sources/LLM/Transformer/模型微调.xmind|模型微调]]
- [[sources/LLM/Transformer/Llama 微调.xmind|Llama 微调]]

## Relations

- prerequisite: [[concepts/Token 和 Embedding|Token 和 Embedding]] — chat template 之前先有 token 与分词。
- used-in: [[concepts/指令微调（SFT）|指令微调（SFT）]] — SFT 数据要套进提示/对话模板再训练。
- enables: [[concepts/自回归语言模型|自回归语言模型]] — chat 模型靠模板把多轮对话变成可自回归续写的序列。
- related-source: [[sources/LLM/大模型.xmind|大模型]] — 提供 tokenizer/chat template 无统一标准的证据。
- map-entry: [[maps/LLM 基础学习地图|LLM 基础学习地图]]

## My Understanding

当前理解：tokenizer 决定文本怎么变数字，chat template 决定对话怎么排版。两者都与模型绑定，换模型要一起换，否则模型“看不懂”输入。

## Review Questions

- BPE 与 WordPiece 分别是哪类模型的分词算法？
- 为什么换模型时常需要换 chat template？
- 微调数据为什么要套进提示模板再分词？

## Open Questions

- 具体模型的 special token、模板语法（如 Jinja chat template）细节需回 raw 或官方文档核验。
