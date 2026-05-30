---
page_type: entity
updated_at: 2026-05-30
status: active
source_count: 3
---

# Hugging Face

## What It Is

Hugging Face 是 LLM 生态的开源平台与工具链，提供 Transformers 库、模型/数据集 Hub、PEFT、Trainer、AutoTrain 等组件，是加载、微调、运行和分享模型的事实标准入口之一。

## Role In This Wiki

在本 wiki 中，Hugging Face 主要作为微调与运行工具链出现：Llama 微调用它的 Transformers + PEFT(LoRA) + Trainer 组织训练，并通过其博客/文档作为模型运行和安装入口。`Hugging face transformers.xmind` 当前为 partial 占位，仅作待补全资料入口。

## Key Facts

- `Llama 微调.xmind` 用 Hugging Face Transformers、PEFT 的 `LoraConfig`、`transformers.Trainer` 和 data collator 组织 alpaca-lora 训练（explicit）。
- Hugging Face 的 Llama 3 博客、Transformers 安装文档、AutoTrain 被列为运行/微调入口（explicit，`Llama 微调.xmind` External Links，not verified）。
- `大模型.xmind` 把 Hugging Face 列为微调工具之一（explicit）。
- `Hugging face transformers.xmind` 目前仅有标题与占位分支，无实质内容（explicit，partial 源）。

## Related Concepts

- implemented-by: [[concepts/PEFT 与 LoRA|PEFT 与 LoRA]] — Transformers/PEFT 提供 LoRA 实现。
- used-in: [[concepts/LLM 微调|LLM 微调]] — 作为主要微调工具链。
- used-in: [[concepts/指令微调（SFT）|指令微调（SFT）]] — Trainer/数据流程支撑 SFT。
- related-source: [[sources/LLM/Transformer/Llama 微调.xmind|Llama 微调]] — 提供 Transformers+PEFT+Trainer 实操证据。

## Evidence

- [[sources/LLM/Transformer/Llama 微调.xmind|Llama 微调]]
- [[sources/LLM/大模型.xmind|大模型]]
- [[sources/LLM/Transformer/Hugging face transformers.xmind|Hugging face transformers]]

## Open Questions

- `Hugging face transformers.xmind` 为 partial 占位，Hub、Pipeline、Tokenizer、部署等细节需后续 source 或官方文档补全。
- External Links 中的 Hugging Face 文档/博客均未联网核验。
