---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 3
learning_status: new
confidence: 2
difficulty: 4
review_after: 2026-06-13
---

# LLM 评估

## Definition

LLM 评估是用数据集、实验、评分方法和线上反馈来衡量 LLM 应用输出质量、成本、耗时和稳定性的过程。

## Why It Matters

提示语、上下文策略和模型选择都需要验证。没有评估，优化只能依赖主观感受；有了固定数据集和基线，才能判断改动是提升还是回退。LLM 评估是 LLMOps 的核心质量反馈环。

## 两种评估层的区分

| 层 | 目标 | 工具参照 |
| --- | --- | --- |
| **应用评估**（本页主题） | 衡量特定 LLM 应用在特定任务上的输出质量 | Langfuse、LangSmith（legacy） |
| **模型 Benchmark** | 衡量基础模型在标准化基准上的能力边界 | 见 [[concepts/LLM Benchmark 评估|LLM Benchmark 评估]] |

两者不可混淆：模型 Benchmark 反映模型基础能力，应用评估反映特定 prompt/上下文/任务的系统质量。

## Mental Model

把 LLM 应用当成一个可测试函数：输入来自数据集，应用产生输出，评估器给出分数，实验记录不同版本之间的差异。Evaluator = 函数，接收输入/输出/期望输出，返回分数。

## Key Claims

- 离线评估适合开发和 CI/CD，在线评估适合真实流量中的质量监控；两者互补而非替代。
- Dataset 和 Experiment 让评估可重复，Score 让结果可比较。
- 自动评估（LLM-as-a-Judge）可以提高覆盖面，但需要和人工标注或评分分析对齐。
- 模型对比时应固定数据集，切换模型、prompt 或上下文策略等变量。
- 评估指标不应只看准确度，还要看 token 成本、耗时和指令遵循度。
- LangSmith 内置评估器类型（legacy · not verified）：correctness 类（qa/context_qa/cot_qa）、criteria、labeled criteria、字符串距离、嵌入距离。
- criteria 评估在没有标准答案时，根据简洁性、相关性、正确性、连贯性、有害性等维度打分。
- CI 回归是防止 prompt/上下文改动带来质量退步的工程安全网，在部署前对数据集运行评估。

## Examples

- 先用简单数据集跑通 prompt、任务函数和评估器，再补充边界条件（先用大模型验证基线，再测小模型）。
- 用线上 trace 抽样做 LLM-as-a-Judge 或人工标注，观察生产场景下的问题分布。
- Langfuse 流程：构建 Dataset → 设计 Evaluator 函数 → 运行 Experiment → 查看 Score 分布 → 迭代 prompt。
- LangSmith 流程（legacy · not verified）：Dataset 绑定 Evaluator → 触发 Experiment → 对比新旧版本 Score → CI 门控合并。
- RAG 专项评估：检索阶段用 context_qa 评估文档相关性，生成阶段用 qa 评估答案正确性，分层诊断失败来源。

## Common Confusions

- 单元测试和 LLM 评估不是互斥关系；本地 SDK 评估可以接入测试框架。
- LLM-as-a-Judge 不是客观真理，它也是一个需要校准的评估器。
- 线上评估不能替代离线评估；真实流量能发现新问题，但不一定可重复。
- 应用评估（Langfuse/LangSmith）和模型 Benchmark（MMLU/HumanEval 等）是不同层面的评估，结论不能互换。

## Evidence

- explicit: [[sources/提示语工程:上下文工程/LLM 评估.xmind|LLM 评估.xmind]] — 基于 Langfuse 的离线/在线评估、Dataset、Experiment、Score 和本地 SDK 评估流程。
- explicit: [[sources/Langchain(Legacy)/Langchain  DevOps.xmind|Langchain DevOps.xmind]] — LangSmith 的数据集、评估器类型（correctness/criteria/labeled criteria）、CI 回归和在线监控（legacy · not verified）。
- related: [[sources/Langchain(Legacy)/跟踪和监控.xmind|跟踪和监控.xmind]] — LangSmith 与 Langfuse 的工具选型对比（legacy · not verified）。

## Relations

- contrasts-with: [[concepts/LLM Benchmark 评估|LLM Benchmark 评估]] （应用评估 vs 模型能力基准）
- implemented-by: [[entities/Langfuse|Langfuse]]
- implemented-by: [[entities/LangSmith|LangSmith]] （legacy · not verified）
- contains: [[concepts/LLM-as-a-Judge|LLM-as-a-Judge]]
- part-of: [[concepts/LLMOps|LLMOps]]
- used-in: [[concepts/提示语工程|提示语工程]]
- used-in: [[concepts/上下文工程|上下文工程]]
- related-source: [[sources/提示语工程:上下文工程/LLM 评估.xmind|LLM 评估.xmind]]
- map-entry: [[maps/提示语与上下文工程学习地图|提示语与上下文工程学习地图]]

## My Understanding

LLM 评估给 prompt 和上下文优化提供反馈闭环。它把"感觉变好了"转成"在同一批数据和指标下表现如何"。关键是建立"数据集固定、变量单一、基线可比"的实验模式，而不是每次拿几条样例对比。

## Review Questions

- 离线评估和在线评估分别适合什么阶段？
- Dataset、Experiment、Score 之间是什么关系？
- 为什么先用大模型跑基线，再测小模型？
- 自动评估为什么还需要人工标注或一致性分析？
- LLM 应用评估和模型 Benchmark 的区别是什么？
- criteria 评估和 correctness 评估分别适合什么场景？

## Open Questions

- 当前 source 以 Langfuse 为线索，还需要官方文档或项目实践补充 API 与数据模型细节。
- LangSmith 评估器功能细节需要官方文档核验（legacy · not verified）。
- 不同评估指标的权重如何设置，需要结合具体任务。
