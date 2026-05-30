---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 4
learning_status: new
confidence: 2
difficulty: 4
review_after: 2026-06-06
---

# RLHF 与偏好对齐

## Definition

偏好对齐是在 SFT 之后，用“人类偏好”信号继续调整模型，使输出更符合人类期望、更安全有用。RLHF（基于人类反馈的强化学习）是经典路线：先训练奖励模型，再用强化学习（如 PPO）优化模型；DPO 是绕开完整 RL 的简化路线。

## Why It Matters

SFT 让模型会答，但“答得好不好、是否符合人类偏好”需要偏好信号。对齐阶段是 ChatGPT 类助手“好用且不离谱”的关键，也是理解 RM、PPO、DPO 关系的核心。

## Mental Model

打分校准：先让人对模型的多个回答排序，训练一个“奖励模型”当裁判，再让模型在裁判打分下不断调整，往“人更喜欢”的方向走；DPO 则跳过裁判和强化学习，直接用“被选中 vs 被拒绝”的样本对比来调。

## Key Claims

- 偏好微调在 SFT 之后把输出偏好引入训练，使输出更符合人类偏好（explicit，`微调生成模型.xmind`）。
- PPO 路线通常先训练奖励模型，再用强化学习优化，使输出不偏离预期奖励过多（explicit，`微调生成模型.xmind`）。
- 奖励模型用人工 comparison 数据训练，类似二分类，用于评估生成质量、引导输出更符合人类期望（explicit，`图解ChatGPT.xmind` / `State of GPT.pdf`）。
- 强化学习阶段从 SFT 初始化并使用奖励模型，使生成 token 最大化 reward（explicit，`State of GPT.pdf` 预览）。
- DPO 用参考模型与可训练模型在 accepted/rejected 样本上的 token 级对数概率差异直接优化偏好，简化了完整 RL 流程（explicit，`微调生成模型.xmind`）。

## Examples

- `图解ChatGPT.xmind` 用预训练→SFT→奖励模型→PPO 还原 ChatGPT 对齐路径（PPO 节点导出不完整）。
- `State of GPT.pdf` 预览把 Reward Modeling 与 Reinforcement Learning 列为管线后两阶段。
- `微调生成模型.xmind` 把 alignment、RLHF、PPO、RM、DPO 放在同一条偏好对齐链上对比。

## Common Confusions

- RLHF 不是单一算法，而是“RM + RL（如 PPO）”的组合流程。
- DPO 是 PPO/RLHF 的简化替代，不需要单独训练奖励模型或跑完整强化学习。
- 对齐发生在 SFT 之后，处理的是“偏好/安全”，不是“是否会做任务”（那是 SFT 的事）。

## Evidence

- [[sources/LLM/微调生成模型.xmind|微调生成模型]]
- [[sources/LLM/图解ChatGPT.xmind|图解ChatGPT]]
- [[sources/LLM/State of GPT - Microsoft Build 2023 RD.pdf|State of GPT]]
- [[sources/LLM/大模型.xmind|大模型]]

## Relations

- part-of: [[concepts/预训练与微调范式|预训练与微调范式]] — 对齐是管线最后阶段。
- prerequisite: [[concepts/指令微调（SFT）|指令微调（SFT）]] — 对齐通常从 SFT 模型初始化。
- part-of: [[concepts/LLM 微调|LLM 微调]] — 阶段轴上的偏好对齐节点。
- related-source: [[sources/LLM/微调生成模型.xmind|微调生成模型]] — 提供 RLHF/PPO/RM/DPO 对比证据。
- map-entry: [[maps/LLM 基础学习地图|LLM 基础学习地图]]

## My Understanding

当前理解：对齐是“SFT 之后让模型答得更合人意”。RLHF = 训奖励模型 + 强化学习优化；DPO 直接用偏好样本对比简化掉强化学习。

## Review Questions

- RLHF 包含哪两个主要部件？
- 奖励模型的训练数据是什么形态？
- DPO 相比 PPO/RLHF 省掉了什么？

## Open Questions

- PPO/DPO 的算法细节、超参与稳定性需回 raw 或专门资料；`图解ChatGPT.xmind` 的 PPO 节点导出不完整。
