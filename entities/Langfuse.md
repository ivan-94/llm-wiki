---
page_type: entity
updated_at: 2026-05-30
status: active
source_count: 3
---

# Langfuse

## What It Is

Langfuse 是开源的 LLM 应用观测、追踪（tracing）、数据集、实验和评估平台。它支持本地/自托管部署，提供与 LangChain 等框架的 tracing 集成，是 LLM 应用评估闭环的开源参照系。

与 LangSmith（官方商业）、Phoenix（开源、无用户系统）相比，Langfuse 的优势在于开源可自托管、数据可控，界面接近 LangSmith，详见 [[synthesis/LangSmith 与 Langfuse 可观测性对照（Legacy）|可观测性对照综合页]]。

## Role In This Wiki

Langfuse 在本 wiki 中作为 LLM 评估工程的实现参照，承载 Dataset、Experiment、Score、LLM-as-a-Judge、Annotation Queues、Score Analytics、离线评估和在线 trace 评估等概念。同时作为 LangSmith（legacy）的开源替代参照。

## Key Facts

**Tracing 与 Observability**：
- 支持记录每次 LLM 应用调用的完整 trace，包括输入、输出、中间步骤、token 用量和延迟。
- Trace 可关联到 Session（多轮对话）或 Observation（单次调用步骤）层级。
- 支持 LangChain tracing 集成（来自跟踪和监控.xmind，not verified · 当时标注"不支持全局集成"，需核验）。
- 支持本地部署（Docker）。

**评估（Evaluation）**：
- **Score**：核心评估数据对象，可以关联到 trace、session 或 dataset run item；承载不同维度的评分数据。
- **Dataset**：输入（和可选期望输出）的结构化集合，支持版本化。
- **Dataset Item**：Dataset 中的单条记录。
- **Dataset Run / Dataset Run Item**：一次 Experiment 的运行结果和单条记录的结果。
- **Experiment**：遍历 Dataset，触发应用，并可对结果执行评估器，返回 Score。
- **Evaluator Function**：接收输入/输出/期望输出/元数据，返回 Evaluation 对象（最终成为 Score）。

**评估方法**：
- **LLM-as-a-Judge**：用提示词+模型作为评估器，对 trace 或 dataset 条目打分。
- **人工评估**：通过 Annotation Queues、UI 或 API/SDK 打分。
- **Score Analytics**：检查自动评估和人工标注的一致性，并观察评分分布和趋势。

**SDK 评估流程**：
- 设置本地评估环境 → 准备 prompt 和数据集 → 先用大模型建立基线 → 扩充覆盖边界条件的数据集 → 测试小模型的成本/质量权衡。
- 可接入 CI/CD 单元测试框架。

## 与 LangSmith 的对比

见 [[synthesis/LangSmith 与 Langfuse 可观测性对照（Legacy）|LangSmith 与 Langfuse 可观测性对照（Legacy）]]。

核心差异（legacy · not verified）：
- Langfuse：开源/自托管，界面接近 LangSmith，当时标注 LangChain 全局集成支持不同于 LangSmith 原生集成。
- LangSmith：官方商业产品，与 LangChain 原生深度集成，有 Prompt Hub。

## Related Concepts

- implements: [[concepts/LLM 评估|LLM 评估]]
- implements: [[concepts/LLM-as-a-Judge|LLM-as-a-Judge]]
- implements: [[concepts/LLMOps|LLMOps]]
- contrasts-with: [[entities/LangSmith|LangSmith]]

## Evidence

- [[sources/提示语工程:上下文工程/LLM 评估.xmind|LLM 评估.xmind]] — 主要证据：Dataset、Experiment、Score、LLM-as-a-Judge、SDK 评估流程和离线/在线评估。
- [[sources/Langchain(Legacy)/跟踪和监控.xmind|跟踪和监控.xmind]] — 工具选型对比：Langfuse 与 LangSmith/Phoenix 的 tracing 观测层对比（legacy · not verified）。
- [[sources/Langchain(Legacy)/Langchain  DevOps.xmind|Langchain DevOps.xmind]] — 与 LangSmith 评估器类型对比提供侧面证据（legacy · not verified）。

## Open Questions

- 当前未核验 Langfuse 官方文档；具体 API、版本和字段名需要后续查证。
- 跟踪和监控.xmind 中"不支持全局集成"的说法时效性存疑，需要核验当前能力。
- Langfuse 与其他开源 LLMOps 工具（如 Phoenix、Weave）的功能差距需要最新对比。
