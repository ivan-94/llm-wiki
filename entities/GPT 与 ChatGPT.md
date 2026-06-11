---
page_type: entity
updated_at: 2026-06-11
status: active
source_count: 6
---

# GPT 与 ChatGPT

## What It Is

GPT（Generative Pre-trained Transformer）是 OpenAI 的 decoder-only 自回归生成模型家族；ChatGPT 是在 GPT 基础上经预训练、SFT、奖励模型和强化学习（RLHF）对齐后得到的对话式助手产品。

## Role In This Wiki

在本 wiki 中，GPT 是 decoder-only / 生成模型路线的代表（与 BERT 对照），ChatGPT 则是“base 模型 + SFT + RLHF 对齐”训练管线的典型落地案例，串起自回归生成、解码采样和偏好对齐多个概念。

## Key Facts

- GPT 属于 decoder-only generative model，面向 next-token 生成，关联 GPT、LLM 与“预训练+监督微调”范式（explicit，`Token and Embedding.xmind`）。
- GPT 采用单向语境偏生成连续文本（explicit，`Transformer.xmind`）。
- GPT 用 BPE 分词（explicit，`Token and Embedding.xmind`）。
- ChatGPT 通过分析上下文预测最可能的下一个词，逐词生成连贯回复，底层架构指向 Transformer（explicit，`图解ChatGPT.xmind`）。
- ChatGPT 训练路径含预训练、监督微调、奖励模型和强化学习（PPO）（explicit，`图解ChatGPT.xmind`）。
- `State of GPT` deck（Andrej Karpathy）把 GPT Assistant 训练拆为 Pretraining/SFT/RM/RL 四阶段（explicit，`State of GPT.pdf` 预览，仅前 3 页）。
- ChatGPT memory / Dreaming V3 source 把产品记忆描述为后台合成、持续更新、可审阅的 memory state，重点是 freshness、continuity 和 relevance（explicit/inferred，human source）。

## Related Concepts

- implemented-by: [[concepts/Encoder 与 Decoder 模型|Encoder 与 Decoder 模型]] — decoder-only 的代表实例。
- contrasts-with: [[entities/BERT|BERT]] — 单向生成 vs 双向理解。
- related-concept: [[concepts/自回归语言模型|自回归语言模型]] — GPT 是典型自回归 LM。
- related-concept: [[concepts/RLHF 与偏好对齐|RLHF 与偏好对齐]] — ChatGPT 用 RLHF 对齐。
- related-concept: [[concepts/预训练与微调范式|预训练与微调范式]] — ChatGPT 是四阶段管线案例。

## Evidence

- [[sources/LLM/图解ChatGPT.xmind|图解ChatGPT]]
- [[sources/LLM/Token and Embedding.xmind|Token and Embedding]]
- [[sources/LLM/Transformer/Transformer.xmind|Transformer.xmind]]
- [[sources/LLM/State of GPT - Microsoft Build 2023 RD.pdf|State of GPT]]
- [[human/sources/inbox/cook-tweet/2026-06-05_ChatGPT记忆DreamingV3_OpenAI|ChatGPT 记忆进入 Dreaming V3]]

## Open Questions

- `State of GPT.pdf` 仅 preview 前 3 页，完整训练 recipe 需回原 deck。
- 作者 Andrej Karpathy 的实体页归属其他 wave，本页仅文字提及。
- 具体 GPT 版本（GPT-3.5/4 等）的能力与参数细节超出当前 source。
