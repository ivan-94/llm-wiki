---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 2
learning_status: new
confidence: 2
difficulty: 4
review_after: 2026-06-06
---

# Self-Instruct 与合成数据

## Definition

Self-Instruct 是一种用语言模型自己批量生成指令微调数据的方法：从少量人工种子任务出发，让现有 LM 迭代生成新指令与实例，再经多样性过滤回填任务池，从而低成本造出大规模合成训练数据。

## Why It Matters

高质量指令-响应数据是 SFT 的瓶颈，人工标注昂贵。Self-Instruct/蒸馏式合成数据（如 Alpaca 用 ChatGPT 造数据）让小团队也能造出可用的指令数据集，是开源模型快速获得指令能力的关键路径。

## Mental Model

滚雪球造题：先给几道人工范题当种子，让大模型照着出更多新题和答案，把不重复的好题塞回题库，再用更大的题库继续出题，越滚越多。

## Key Claims

- Self-Instruct 从有限人工 seed tasks 出发，用现有 LM 迭代生成新指令和实例，经分类判断、实例生成、过滤、处理、重格式化（explicit，`Llama 微调.xmind`）。
- 非分类任务用 input-first 生成输入和输出，分类任务用 output-first 生成 class label 对应输入（explicit，`Llama 微调.xmind`）。
- 新指令需与种子池指令的 ROUGE-L 小于 0.7 才加入，且排除涉及图像等 LM 无法处理的指令（explicit，`Llama 微调.xmind`）。
- Alpaca 升级了 Self-Instruct：用 text-davinci-003、批量生成 20 条指令、取消分类/非分类差异、每条只生成一个实例（explicit，`Llama 微调.xmind`）。
- “借花献佛”式做法：选大模型擅长的任务，规划约 1000 个输入，用大模型生成输出再人工优化，用于微调小模型（explicit，`模型微调.xmind`）。

## Examples

- `Llama 微调.xmind` 保留了 seed task、分类判断 prompt、ROUGE-L 多样性过滤等完整细节。
- `模型微调.xmind` 用 Alpaca 基于 ChatGPT 生成 Q&A 数据作为合成数据例子。

## Common Confusions

- 合成数据不是免费午餐：质量、版权/许可、与教师模型同质化等风险存在，raw 未展开。
- ROUGE-L < 0.7 过滤是为保证多样性，不是质量评分。
- Self-Instruct 造的是“训练数据”，与推理时的 few-shot 提示是两回事。

## Evidence

- [[sources/LLM/Transformer/Llama 微调.xmind|Llama 微调]]
- [[sources/LLM/Transformer/模型微调.xmind|模型微调]]

## Relations

- used-in: [[concepts/指令微调（SFT）|指令微调（SFT）]] — Self-Instruct 为 SFT 批量造指令数据。
- part-of: [[concepts/LLM 微调|LLM 微调]] — 数据轴上的合成数据节点。
- implemented-by: [[entities/Llama|Llama]] — Alpaca 在 LLaMA-7B 上用 Self-Instruct 数据微调。
- related-source: [[sources/LLM/Transformer/Llama 微调.xmind|Llama 微调]] — 提供 Self-Instruct 流程与 Alpaca 升级证据。
- map-entry: [[maps/LLM 基础学习地图|LLM 基础学习地图]]
- entity-candidate: Alpaca — Self-Instruct 数据 + LLaMA-7B 指令微调的代表项目，暂作候选不单独建页。

## My Understanding

当前理解：Self-Instruct 用大模型给自己出题造数据，靠种子任务起步、ROUGE-L 去重保多样性；Alpaca 是它的简化高效版，用 ChatGPT 造数据微调 LLaMA。

## Review Questions

- Self-Instruct 如何保证生成指令的多样性？
- 分类任务和非分类任务的实例生成方向有何不同？
- Alpaca 对原始 Self-Instruct 做了哪些简化？

## Open Questions

- 合成数据的版权、许可与质量控制风险在 raw 中未展开，需补充。
