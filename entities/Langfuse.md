---
page_type: entity
updated_at: 2026-05-29
status: active
source_count: 1
---

# Langfuse

## What It Is

Langfuse 是用于 LLM 应用观测、数据集、实验和评估的工具平台。本 wiki 当前只基于 `LLM 评估.xmind` 记录其评估相关概念。

## Role In This Wiki

它作为 LLM 评估流程的实现参照，承载 Dataset、Experiment、Score、LLM-as-a-Judge、Annotation Queues、Score Analytics 等概念。

## Key Facts

- 支持把评估分数关联到 trace、session、observation 或 dataset run item 等对象。
- 支持离线数据集实验和线上 trace 评估。
- 支持自动评估、人工标注、UI/API/SDK 打分和评分分析。

## Related Concepts

- [[concepts/LLM 评估|LLM 评估]]
- [[concepts/LLM-as-a-Judge|LLM-as-a-Judge]]

## Evidence

- [[sources/提示语工程:上下文工程/LLM 评估.xmind|LLM 评估.xmind]]

## Open Questions

- 当前未核验 Langfuse 官方文档；具体 API、版本和字段名需要后续查证。
