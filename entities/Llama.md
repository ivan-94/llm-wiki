---
page_type: entity
updated_at: 2026-05-30
status: active
source_count: 2
---

# Llama

## What It Is

Llama 是 Meta 的开源（开放权重）大语言模型家族，是开源微调实践的主力底座；社区围绕它形成了 Alpaca、alpaca-lora、LLaMA-Factory、Ollama 等数据、微调与运行生态。

## Role In This Wiki

在本 wiki 中，Llama 是开源模型微调实战的核心案例：演示指令数据构造（Self-Instruct/Alpaca）、PEFT/LoRA 训练实现、全参训练资源需求和模型导出部署，是把微调各概念落到代码与硬件的载体。

## Key Facts

- 微调示例围绕 Llama/LLaMA 展开：alpaca 数据格式（instruction/input/output/system/history）、sharegpt 格式（explicit，`Llama 微调.xmind`）。
- Alpaca 用 Self-Instruct 生成数据对 LLaMA-7B 做指令微调（explicit，`Llama 微调.xmind`）。
- 全参训练示例需 4×A100 80G；LoRA 示例用 `LlamaForCausalLM` + PEFT `LoraConfig` + Trainer（explicit，`Llama 微调.xmind`）。
- 运行入口包括 Hugging Face Llama 3 博客、Mac 上用 Ollama 运行、unsloth、LLaMA-Factory、AutoTrain（explicit，External Links，not verified）。
- 导出格式列出 GGUF、vLLM、GGML（explicit，`Llama 微调.xmind`）。
- 预训练数据配比以 LLaMA 为例（CommonCrawl/C4/GitHub/Wikipedia/Books/ArXiv/StackExchange）（explicit，`State of GPT.pdf` 预览）。

## Related Concepts

- used-in: [[concepts/LLM 微调|LLM 微调]] — 开源微调主力底座。
- related-concept: [[concepts/PEFT 与 LoRA|PEFT 与 LoRA]] — alpaca-lora 在 Llama 上做 LoRA。
- related-concept: [[concepts/Self-Instruct 与合成数据|Self-Instruct 与合成数据]] — Alpaca 用 Self-Instruct 数据微调 Llama。
- implemented-by: [[entities/Hugging Face|Hugging Face]] — 用 Transformers/PEFT 微调与加载 Llama。

## Evidence

- [[sources/LLM/Transformer/Llama 微调.xmind|Llama 微调]]
- [[sources/LLM/State of GPT - Microsoft Build 2023 RD.pdf|State of GPT]]

## Open Questions

- 各 Llama 版本（2/3 等）的架构差异与许可细节超出当前 source，未联网核验。
- alpaca-lora 等仓库的当前可用性与最佳实践需实验或核验。
