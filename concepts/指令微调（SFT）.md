---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 5
learning_status: new
confidence: 2
difficulty: 4
review_after: 2026-06-06
---

# 指令微调（SFT）

## Definition

指令微调（SFT，Supervised Fine-Tuning，监督微调）是在基础模型上用“指令-响应”监督数据继续训练，让模型学会理解任务要求并产生符合期望的回答，从而从续写型 base 模型变成更像助手的 chat 模型。

## Why It Matters

SFT 是把“会语言”的 base 模型变成“会听话做事”的第一步，也是预训练与偏好对齐之间的关键桥梁。理解 SFT 的数据形态与训练目标，是理解 ChatGPT 类助手如何被造出来的核心。

## Mental Model

示范带教：给模型看大量“这样问、应该这样答”的高质量范例，让它模仿人类示范者的回答方式；训练目标仍是预测下一个 token，只是数据换成了指令-响应对。

## Key Claims

- SFT 更新基础模型参数，让模型更好执行特定任务或遵循指令，但仍基于下一个 token 预测目标（explicit，`微调生成模型.xmind`）。
- 指令微调把指令/提示与任务输入一起提供，使模型更像 chatbot、更适合大众交互（explicit，`模型微调.xmind`）。
- SFT 使用人工编写的 prompt-response demonstrations，以 language modeling 方式训练得到 SFT model（explicit，`State of GPT.pdf` 预览）。
- 数据准备需收集高质量、多样、真实的指令-响应对，套入提示模板，分词/填充/对齐并划分训练/测试集（explicit，`模型微调.xmind`）。
- Alpaca 用 Self-Instruct 生成的指令数据对 LLaMA-7B 做指令微调（explicit，`Llama 微调.xmind`）。

## Examples

- `State of GPT.pdf` 预览把 Supervised Finetuning 列为管线第二阶段，用人工 demonstration 训练。
- `Llama 微调.xmind` 用 alpaca 格式（instruction/input/output/system/history）组织指令数据。
- `模型微调.xmind` 把指令微调与“借花献佛”式数据构造并列为两条微调数据路径。

## Common Confusions

- 重要纠错：SFT 是 Supervised Fine-Tuning（监督微调），不是 "Soft Fine-Tuning"；`大模型.xmind` 的派生内容曾误写为 Soft Fine-Tuning。
- SFT 与偏好对齐（RLHF/DPO）不同：SFT 学“怎么答”，对齐学“答得更合人类偏好”。
- SFT 属于训练阶段，与 LoRA/QLoRA（参数高效实现策略）不在同一抽象层，可叠加使用。

## Evidence

- [[sources/LLM/微调生成模型.xmind|微调生成模型]]
- [[sources/LLM/Transformer/模型微调.xmind|模型微调]]
- [[sources/LLM/Transformer/Llama 微调.xmind|Llama 微调]]
- [[sources/LLM/State of GPT - Microsoft Build 2023 RD.pdf|State of GPT]]
- [[sources/LLM/大模型.xmind|大模型]]

## Relations

- part-of: [[concepts/预训练与微调范式|预训练与微调范式]] — SFT 是微调阶段的第一段。
- prerequisite: [[concepts/Chat Template 与 Tokenizer|Chat Template 与 Tokenizer]] — 指令数据要套进对话/提示模板。
- enables: [[concepts/RLHF 与偏好对齐|RLHF 与偏好对齐]] — 对齐通常从 SFT 模型初始化。
- used-in: [[concepts/Self-Instruct 与合成数据|Self-Instruct 与合成数据]] — Self-Instruct 为 SFT 批量造指令数据。
- part-of: [[concepts/LLM 微调|LLM 微调]] — 阶段轴上的核心节点。
- related-source: [[sources/LLM/Transformer/模型微调.xmind|模型微调]] — 提供指令微调与数据准备证据。
- map-entry: [[maps/LLM 基础学习地图|LLM 基础学习地图]]

## My Understanding

当前理解：SFT 用人工示范的“指令-回答”教模型听话，训练目标还是预测下一个 token，只是把 base 模型调成了助手。它是 Supervised Fine-Tuning，别被误写的 "Soft Fine-Tuning" 带偏。

## Review Questions

- SFT 全称是什么，常被误写成什么？
- SFT 的数据形态和训练目标分别是什么？
- SFT 与偏好对齐解决的问题有何不同？

## Open Questions

- 指令数据规模、质量阈值与配比的最佳实践需结合实验，超出当前 source。
