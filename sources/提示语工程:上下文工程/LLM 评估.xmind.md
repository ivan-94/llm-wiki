---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/提示语工程:上下文工程/LLM 评估.xmind"
source_relpath: "提示语工程:上下文工程/LLM 评估.xmind"
raw_created_at: 2026-01-13T08:45:25.503710+00:00
raw_modified_at: 2026-01-15T10:17:38.492518+00:00
raw_size: 3408702
raw_fingerprint: "size=3408702;birth=2026-01-13T08:45:25.503710+00:00;mtime=2026-01-15T10:17:38.492518+00:00"
raw_snapshot_at: 2026-05-29T22:17:37+00:00
ingested_at: 2026-05-29
status: ingested
---

# LLM 评估.xmind

## Source

- Raw file: [提示语工程:上下文工程/LLM 评估.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/%E6%8F%90%E7%A4%BA%E8%AF%AD%E5%B7%A5%E7%A8%8B%3A%E4%B8%8A%E4%B8%8B%E6%96%87%E5%B7%A5%E7%A8%8B/LLM%20%E8%AF%84%E4%BC%B0.xmind>)
- Raw ref: `raw:提示语工程:上下文工程/LLM 评估.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2026-01-13T08:45:25.503710+00:00`; modified `2026-01-15T10:17:38.492518+00:00`; size `3408702`; snapshot `2026-05-29T22:17:37+00:00`
- Sheets processed: 1/1 (`LLM 评估`)

## Summary

这张图以 Langfuse 为背景整理 LLM 应用评估：区分离线评估和在线评估，解释 Scores、Evaluation Methods、Datasets、Experiments 等概念，并给出本地 SDK 执行评估、建立基线、模型对比和成本/耗时/准确度分析的流程。

## Source Digest

该 source 的主线是把 LLM 评估从“主观试用”推进到“可重复的实验流程”。

第一部分区分离线评估和在线评估。离线评估发生在受控环境中，通常使用整理好的测试数据集，可以接入 CI/CD，适合开发阶段判断 prompt、模型或代码改动是否带来改进或回退。在线评估发生在真实生产流量中，关注成功率、用户满意度、隐式/显式反馈、影子测试和 A/B 测试，优势是能捕捉实验室里没有覆盖的情况。

基本概念部分围绕 Langfuse 的评估对象展开。Score 是可关联到 trace、session、observation 等对象的评分数据；Evaluation Method 是产生评分的方法；Dataset 是输入集合，可带预期输出；Experiment 会遍历 dataset，触发应用，并可对结果执行评估。

评估方法分为自动和人工两类。LLM-as-a-Judge 用一个提示词和模型作为评估器，对 trace 或数据集条目打分并给出推理。人工评估可以通过 Annotation Queues、UI 或 API/SDK 打分完成。Score Analytics 用来检查自动评估和人工标注是否一致，以及观察评分分布和趋势。

数据模型部分强调 Dataset、Dataset Item、Dataset Run、Dataset Run Item、Score、Score Config、Task Function 和 Evaluator Function 的关系。关键点是评估器本质上是函数：接收输入、输出、期望输出和元数据，返回 Evaluation 对象，最终成为 Langfuse 中的 Score。

本地 SDK 流程强调可与单元测试集成：设置本地评估环境，准备 prompt 和数据集，先用简单基准跑通流程，再完善覆盖边界条件的数据集。测试时先用大模型验证数据集和 prompt 是否合理，建立基线，再测试小模型，看成本下降是否值得精度损失。

该 source 对提示语/上下文工程的补充很关键：prompt 和上下文策略不能只靠感觉优化，需要用固定数据集、固定评估器、基线对比和线上反馈闭环验证。

## Key Claims

- 离线评估适合开发阶段的可重复基线和回归检测，在线评估适合捕捉真实使用场景中的问题。
- Langfuse 中的 Score 是评估结果的核心数据对象，可以承载不同维度的指标。
- LLM-as-a-Judge 是“提示词 + 模型”的自动评估器，但需要与人工标注或评分分析校准。
- 评估流程应先跑通小基准，再扩大数据集覆盖边界条件。
- 模型对比应保持数据集不变，切换模型、模型规模或提示词等变量。
- 成本、耗时和准确度应同时进入 LLM 应用评估，而不是只看答案质量。

## External Links

- documentation: [数据模型概览](https://langfuse.com/docs/evaluation/experiments/data-model) — Langfuse experiments data model；not verified.
- documentation: [本地通过 SDK 执行评估](https://langfuse.com/docs/evaluation/experiments/experiments-via-sdk#testing-in-ci-environments) — Langfuse SDK experiments and CI testing；not verified.
- documentation: [和单元测试框架集成](https://langfuse.com/docs/evaluation/experiments/experiments-via-sdk#testing-in-ci-environments) — same Langfuse SDK/CI page linked from unit-test integration branch；not verified.

## Links

- compiled-concept: [[concepts/LLM 评估|LLM 评估]] — 提炼离线/在线评估、Dataset、Experiment、Score 和本地 SDK 评估流程。
- compiled-concept: [[concepts/LLM-as-a-Judge|LLM-as-a-Judge]] — 将“提示词 + 模型”的自动评估器沉淀为独立概念。
- compiled-entity: [[entities/Langfuse|Langfuse]] — source 以 Langfuse 为评估平台参照。
- compiled-synthesis: [[synthesis/公文提示词优化评估清单|公文提示词优化评估清单]] — 提供数据集、指标和模型对比的评估维度。
- map-entry: [[maps/提示语与上下文工程学习地图|提示语与上下文工程学习地图]] — 纳入提示语/上下文学习路径的评估闭环入口。

## Maintenance Notes

- Re-ingested with all-sheets XMind helper on 2026-05-29.
- `xmind export --format markdown` 成功，sheet `LLM 评估` 已处理。
- source 标注“基于 Langfuse”，并包含 Langfuse 官方文档链接；本次未联网核验链接内容和 API 时效性。
