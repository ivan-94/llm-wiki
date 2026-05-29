---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 7
learning_status: new
confidence: 3
difficulty: 5
review_after: 2026-06-06
---

# LLM 微调

## Definition

LLM 微调是在预训练基础模型之上，用监督数据、偏好数据或参数高效方法调整模型，使其更适合特定任务、指令风格、领域或人类偏好。

## Why It Matters

微调是把通用语言模型适配到具体行为和领域的关键方法。它连接训练阶段、任务数据、偏好对齐、成本控制和部署格式。

## Mental Model

预训练让模型会语言，SFT 让模型会按任务做事，偏好微调让模型更符合人类偏好；PEFT/LoRA/QLoRA 是降低微调成本的工程路径。

## Key Claims

- 预训练阶段主要学习下一个 token 预测，基础模型不一定会遵循指令。
- SFT 用任务/指令数据让模型更会执行特定任务。
- 偏好微调在 SFT 后把输出偏好引入训练，常见路线包括 RLHF/PPO/RM 和 DPO。
- 全参数微调成本高，PEFT、Adapters、LoRA、QLoRA 通过只训练少量参数降低资源需求。
- Llama 微调材料强调指令数据构造、Self-Instruct、LoRA/PEFT、Alpaca、LLaMA-Factory 和模型导出格式。

## Examples

- `微调生成模型.xmind` 拆分预训练、SFT、偏好微调、PEFT、LoRA、QLoRA、PPO 和 DPO。
- `Llama 微调.xmind` 关注开源模型指令微调数据与工具链。
- `模型微调.xmind` 和 `BERT 模型微调.xmind` 提供不同模型家族的微调入口。
- `State of GPT` PDF 预览提供 GPT 助手训练流程的早期可视线索。

## Common Confusions

- 微调不是让模型“学习所有知识”的唯一方式；很多知识型任务更适合 RAG 或工具调用。
- SFT、RLHF、DPO 和 LoRA 不在同一抽象层：前者是训练目标/阶段，后者是参数高效实现策略。
- QLoRA 的核心是量化降低显存，不等于无损微调。

## Evidence

- [[sources/LLM/微调生成模型.xmind|微调生成模型]]
- [[sources/LLM/Transformer/Llama 微调.xmind|Llama 微调]]
- [[sources/LLM/Transformer/模型微调.xmind|模型微调]]
- [[sources/LLM/Transformer/BERT 模型微调.xmind|BERT 模型微调]]
- [[sources/LLM/State of GPT - Microsoft Build 2023 RD.pdf|State of GPT]]

## Relations

- builds-on: [[concepts/Transformer|Transformer]]
- builds-on: [[concepts/Token 和 Embedding|Token 和 Embedding]]
- contrasts-with: [[concepts/RAG|RAG]]
- related-source: [[sources/LLM/微调生成模型.xmind|微调生成模型]]
- map-entry: [[maps/LLM 基础学习地图|LLM 基础学习地图]]

## My Understanding

当前理解：微调是在模型权重层面改变行为的路线，应和 RAG、prompt、tool calling 一起按任务需求选择，而不是默认优先。

## Review Questions

- 预训练、SFT、偏好微调分别解决什么？
- LoRA 和 QLoRA 为什么属于参数高效微调？
- DPO 相比 PPO/RLHF 简化了什么？

## Open Questions

- 具体模型、数据集和训练工具当前最佳实践需要联网或实验核验。
