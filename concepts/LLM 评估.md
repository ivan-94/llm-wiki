---
page_type: concept
updated_at: 2026-05-29
status: active
source_count: 1
learning_status: new
confidence: 2
difficulty: 4
review_after: 2026-06-05
---

# LLM 评估

## Definition

LLM 评估是用数据集、实验、评分方法和线上反馈来衡量 LLM 应用输出质量、成本、耗时和稳定性的过程。

## Why It Matters

提示语、上下文策略和模型选择都需要验证。没有评估，优化只能依赖主观感受；有了固定数据集和基线，才能判断改动是提升还是回退。

## Mental Model

把 LLM 应用当成一个可测试函数：输入来自数据集，应用产生输出，评估器给出分数，实验记录不同版本之间的差异。

## Key Claims

- 离线评估适合开发和 CI/CD，在线评估适合真实流量中的质量监控。
- Dataset 和 Experiment 让评估可重复，Score 让结果可比较。
- 自动评估可以提高覆盖面，但需要和人工标注或评分分析对齐。
- 模型对比时应固定数据集，切换模型、prompt 或上下文策略等变量。
- 评估指标不应只看准确度，还要看 token 成本、耗时和指令遵循度。

## Examples

- 先用简单数据集跑通 prompt、任务函数和评估器，再补充边界条件。
- 先用大模型验证数据集与任务设计，再测试小模型是否能以可接受质量降低成本。
- 用线上 trace 抽样做 LLM-as-a-Judge 或人工标注，观察生产场景下的问题分布。

## Common Confusions

- 单元测试和 LLM 评估不是互斥关系；本地 SDK 评估可以接入测试框架。
- LLM-as-a-Judge 不是客观真理，它也是一个需要校准的评估器。
- 线上评估不能替代离线评估；真实流量能发现新问题，但不一定可重复。

## Evidence

- [[sources/提示语工程:上下文工程/LLM 评估.xmind|LLM 评估.xmind]]

## Relations

- implemented-by: [[entities/Langfuse|Langfuse]]
- contains: [[concepts/LLM-as-a-Judge|LLM-as-a-Judge]]
- used-in: [[concepts/提示语工程|提示语工程]]
- used-in: [[concepts/上下文工程|上下文工程]]
- related-source: [[sources/提示语工程:上下文工程/LLM 评估.xmind|LLM 评估.xmind]]
- map-entry: [[maps/提示语与上下文工程学习地图|提示语与上下文工程学习地图]]

## My Understanding

现在的理解：LLM 评估给 prompt 和上下文优化提供反馈闭环。它把“感觉变好了”转成“在同一批数据和指标下表现如何”。

## Review Questions

- 离线评估和在线评估分别适合什么阶段？
- Dataset、Experiment、Score 之间是什么关系？
- 为什么先用大模型跑基线，再测小模型？
- 自动评估为什么还需要人工标注或一致性分析？

## Open Questions

- 当前 source 以 Langfuse 为线索，还需要官方文档或项目实践补充 API 与数据模型细节。
- 不同评估指标的权重如何设置，需要结合具体任务。
