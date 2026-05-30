---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 2
learning_status: new
confidence: 2
difficulty: 3
review_after: 2026-06-06
---

# LLM Benchmark 评估

## Definition

LLM Benchmark 评估是用标准化测试集（如 ARC、HellaSwag、MMLU、TruthfulQA）和偏好排名（如 Elo）衡量模型能力的方式，常与人工评估、测试集评估并列，用于横向比较模型或微调前后的效果。

## Why It Matters

微调会改变模型行为、也可能损伤通用能力，必须客观评估。Benchmark 提供可复现、可横比的能力标尺，是“刷榜”、模型选型和判断微调是否有效的常见依据。

## Mental Model

标准化考试：用一套公认题库给不同模型出同样的题，按得分排名；Elo 则像棋手对弈积分，靠相互比较定高低。

## Key Claims

- 评估可包含人类评估、测试集评估，以及 ARC、HellaSwag、MMLU、TruthfulQA、Elo 排名等 benchmark 或偏好排名（explicit，`模型微调.xmind`）。
- 微调会改变模型权重、可能带来意外行为或通用能力下降，因此需要客观评估（explicit，`大模型.xmind`）。
- 表示模型分类等任务也可用准确率类指标衡量（inferred，结合 `实战：文本分类.xmind`）。
- benchmark 之外，工程上还应看 token 成本、耗时和指令遵循度（inferred，与本 wiki `LLM 评估` 一致）。

## Examples

- `模型微调.xmind` 列出 ARC、HellaSwag、MMLU、TruthfulQA、Elo 排名作为评估维度。
- `大模型.xmind` 强调微调后需要客观评估以防通用能力下降。

## Common Confusions

- 术语核验：`模型微调.xmind` 写作 `HelloSwag`，常见 benchmark 名应为 HellaSwag；编译时已按通用名采用，未联网核验。
- 本页是 benchmark/能力标尺视角，与他人维护的 [[concepts/LLM 评估|LLM 评估]]（面向应用质量、数据集、Experiment、Score、线上反馈）互补，不重复其内容。
- 跑分高不等于实际任务好用；benchmark 可能与目标任务分布不一致。

## Evidence

- [[sources/LLM/Transformer/模型微调.xmind|模型微调]]
- [[sources/LLM/大模型.xmind|大模型]]

## Relations

- contrasts-with: [[concepts/LLM 评估|LLM 评估]] — benchmark 标尺 vs 应用级评估流程（他人维护，仅互链）。
- used-in: [[concepts/LLM 微调|LLM 微调]] — 微调前后用 benchmark 客观对比。
- related-source: [[sources/LLM/Transformer/模型微调.xmind|模型微调]] — 提供 benchmark 列表证据。
- map-entry: [[maps/LLM 基础学习地图|LLM 基础学习地图]]

## My Understanding

当前理解：Benchmark 是给模型出标准化考卷打分排名（ARC/MMLU/HellaSwag/TruthfulQA/Elo），用来横比模型和验证微调没把通用能力练废；但跑分高不等于任务好用。

## Review Questions

- 列举几个常见 LLM benchmark 及其作用。
- 为什么微调后必须做客观评估？
- benchmark 评估和应用级 LLM 评估有什么区别？

## Open Questions

- 各 benchmark 的具体题型、覆盖能力和局限需联网或专门资料核验；`HelloSwag` 拼写存疑。
