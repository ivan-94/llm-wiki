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

用三个正交的轴定位任何一次微调：

- 阶段轴（训练目标）：预训练（会语言）→ 指令微调 SFT（会按任务做事）→ 偏好对齐 RLHF/DPO（更合人类偏好）。
- 参数轴（更新范围）：全参数微调（贵）↔ PEFT/Adapters/LoRA/QLoRA（只训少量参数，省资源）。
- 数据轴（数据来源/形态）：无标注预训练语料、人工指令-响应对、Self-Instruct/Alpaca 式合成数据、偏好（accepted/rejected）数据。

一次具体微调 = 选一个阶段目标 × 选一种参数策略 × 配一种数据，三轴独立组合（例如“用 LoRA 在合成指令数据上做 SFT”）。

## Key Claims

- 阶段轴：预训练学下一个 token 预测、基础模型不一定听指令；SFT 用指令数据让模型会做任务；偏好微调在 SFT 后引入偏好，路线含 RLHF/PPO/RM 和 DPO。
- 参数轴：全参数微调成本高；PEFT、Adapters、LoRA、QLoRA 通过只训练少量参数降低资源需求，QLoRA 再加量化省显存。
- 数据轴：无标注数据→预训练，指令-响应对→SFT，偏好数据→对齐；Self-Instruct/Alpaca 提供低成本合成指令数据。
- 三轴正交：SFT/对齐是阶段，LoRA/QLoRA 是参数策略，二者可叠加（如 LoRA 做 SFT），不在同一抽象层。
- Llama 微调材料把三轴落到实操：指令数据构造、Self-Instruct、LoRA/PEFT、Alpaca、LLaMA-Factory 和模型导出格式。

## Examples

- 阶段轴：`微调生成模型.xmind` 拆分预训练、SFT、偏好微调、PPO 和 DPO。
- 参数轴：`微调生成模型.xmind` / `Llama 微调.xmind` 排出全参→Adapters→LoRA→QLoRA 成本阶梯。
- 数据轴：`Llama 微调.xmind` 关注 Self-Instruct/Alpaca 指令数据构造与工具链。
- `模型微调.xmind` 和 `BERT 模型微调.xmind`（partial）提供不同模型家族的微调入口。
- `大模型.xmind` 给出微调/RAG/继续训练/对齐的选型分流（并含 SFT 误写为 Soft Fine-Tuning 的待纠错点）。
- `State of GPT` PDF 预览提供 GPT 助手训练流程的早期可视线索（仅前 3 页）。

## Common Confusions

- 微调不是让模型“学习所有知识”的唯一方式；很多知识型任务更适合 RAG 或工具调用（见 [[concepts/模型工程（知识注入）|模型工程（知识注入）]]）。
- SFT、RLHF、DPO 和 LoRA 不在同一抽象层：前者是训练目标/阶段（阶段轴），后者是参数高效实现策略（参数轴）。
- QLoRA 的核心是量化降低显存，不等于无损微调。
- 术语纠错：SFT 是 Supervised Fine-Tuning（监督微调），不是 "Soft Fine-Tuning"；`大模型.xmind` 的派生内容曾把 SFT 误写为 Soft Fine-Tuning，本 wiki 统一采用 Supervised Fine-Tuning。

## Evidence

- [[sources/LLM/微调生成模型.xmind|微调生成模型]]
- [[sources/LLM/Transformer/Llama 微调.xmind|Llama 微调]]
- [[sources/LLM/Transformer/模型微调.xmind|模型微调]]
- [[sources/LLM/Transformer/BERT 模型微调.xmind|BERT 模型微调]]
- [[sources/LLM/大模型.xmind|大模型]]
- [[sources/LLM/State of GPT - Microsoft Build 2023 RD.pdf|State of GPT]]

## Relations

- prerequisite: [[concepts/Transformer|Transformer]] — 微调建立在 Transformer 架构上。
- prerequisite: [[concepts/Token 和 Embedding|Token 和 Embedding]] — 数据准备依赖分词与表示。
- part-of: [[concepts/预训练与微调范式|预训练与微调范式]] — 微调是该范式的后段。
- contains: [[concepts/指令微调（SFT）|指令微调（SFT）]] — 阶段轴节点。
- contains: [[concepts/RLHF 与偏好对齐|RLHF 与偏好对齐]] — 阶段轴节点。
- contains: [[concepts/PEFT 与 LoRA|PEFT 与 LoRA]] — 参数轴节点。
- contains: [[concepts/Self-Instruct 与合成数据|Self-Instruct 与合成数据]] — 数据轴节点。
- enables: [[concepts/模型量化|模型量化]] — QLoRA 等用量化降本。
- used-in: [[concepts/LLM Benchmark 评估|LLM Benchmark 评估]] — 微调前后用 benchmark 客观评估。
- contrasts-with: [[concepts/RAG|RAG]] — 参数注入 vs 检索注入（他人维护，仅互链）。
- contrasts-with: [[concepts/模型工程（知识注入）|模型工程（知识注入）]] — 微调是参数层知识注入。
- related-source: [[sources/LLM/微调生成模型.xmind|微调生成模型]] — 主要阶段化证据。
- map-entry: [[maps/LLM 基础学习地图|LLM 基础学习地图]]

## My Understanding

当前理解：微调是在模型权重层面改变行为的路线，应和 RAG、prompt、tool calling 一起按任务需求选择，而不是默认优先。

## Review Questions

- 预训练、SFT、偏好微调分别解决什么？
- LoRA 和 QLoRA 为什么属于参数高效微调？
- DPO 相比 PPO/RLHF 简化了什么？

## Open Questions

- 具体模型、数据集和训练工具当前最佳实践需要联网或实验核验。
