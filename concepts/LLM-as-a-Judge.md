---
page_type: concept
updated_at: 2026-05-29
status: active
source_count: 1
learning_status: new
confidence: 2
difficulty: 3
review_after: 2026-06-05
---

# LLM-as-a-Judge

## Definition

LLM-as-a-Judge 是用另一个 LLM 作为评估器，根据输入、输出、期望输出和评分标准，对 LLM 应用结果打分并给出理由的方法。

## Why It Matters

许多 LLM 任务没有简单的精确答案。用 LLM 做裁判可以快速覆盖摘要、写作、分类、问答质量、指令遵循等开放任务，但必须校准和监控一致性。

## Mental Model

它本质上是“评估提示词 + 评估模型 + 数据映射”。评估器不是魔法判官，而是一段可版本化、可实验、可对比的 prompt 程序。

## Key Claims

- LLM-as-a-Judge 可以对 trace 或 dataset item 打分，并输出评分理由。
- 评估器需要明确评分范围、输入变量映射和评分标准。
- 自动裁判应通过人工标注、评分分析或多评估器对比检查可靠性。
- 它适合开放式质量判断，但不应替代确定性校验和领域专家审查。

## Examples

- 对客服回答评分：是否解决问题、是否遵守语气、是否引用正确事实。
- 对公文生成评分：结构是否完整、格式是否符合题材、是否遵循篇幅要求。
- 对提示语迭代做实验：固定数据集，比较旧 prompt 和新 prompt 的裁判分数。

## Common Confusions

- LLM-as-a-Judge 不是线上反馈本身；它可以用于线上 trace 抽样，也可以用于离线数据集。
- 裁判模型越强不代表结果一定可信；评分 prompt 和样本设计同样重要。
- 一个 Score 只能表达一个评分值，多维度评估应拆成多个评估器或多个 score。

## Evidence

- [[sources/提示语工程:上下文工程/LLM 评估.xmind|LLM 评估.xmind]]

## Relations

- part-of: [[concepts/LLM 评估|LLM 评估]]
- implemented-by: [[entities/Langfuse|Langfuse]]
- used-in: [[concepts/提示语工程|提示语工程]]
- related-source: [[sources/提示语工程:上下文工程/LLM 评估.xmind|LLM 评估.xmind]]
- map-entry: [[maps/提示语与上下文工程学习地图|提示语与上下文工程学习地图]]

## My Understanding

现在的理解：LLM-as-a-Judge 是把主观质量判断写成可运行的评估 prompt。它能扩大评估覆盖，但仍需要用人工或统计方式校准。

## Review Questions

- LLM-as-a-Judge 的输入通常包括哪些变量？
- 为什么说评估器本质上是提示词加模型？
- 哪些场景适合自动裁判，哪些不适合？
- 如何检查自动裁判和人工判断是否对齐？

## Open Questions

- 还缺少具体评分 rubric 模板和失败案例。
