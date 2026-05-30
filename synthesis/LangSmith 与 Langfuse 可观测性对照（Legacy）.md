---
page_type: synthesis
updated_at: 2026-05-30
status: active
source_count: 3
learning_status: new
confidence: 2
difficulty: 3
review_after: null
---

# LangSmith 与 Langfuse 可观测性对照（Legacy）

> **全程 Legacy 警告**：本页内容基于 `Langchain(Legacy)` 资料（2024年），所有产品功能声明均标注 legacy · not verified，实际能力以官方最新文档为准。

## Thesis

LangSmith 和 Langfuse 都是 LLM 应用可观测性和评估平台，但定位和开源策略不同。LangSmith 是 LangChain 官方配套的商业闭源平台，Langfuse 是开源替代方案，两者功能高度重叠，但在部署灵活性、LangChain 集成深度和社区生态上各有优劣。

## Comparison

| 维度 | LangSmith | Langfuse |
| --- | --- | --- |
| 开源策略 | 商业闭源 | 开源 |
| 定位 | LangChain 官方 DevOps 平台 | LLM 应用通用观测与评估平台 |
| LangChain 集成 | 原生深度集成 | 支持 LangChain tracing 集成 |
| 部署方式 | SaaS | 本地/自托管/SaaS |
| 数据集管理 | 支持（版本化、导入导出） | 支持（Dataset、Dataset Item） |
| 实验与评估 | 支持（Experiment、Evaluator 函数） | 支持（Experiment、Score、Evaluator Function） |
| 内置评估器 | correctness (qa/context_qa/cot_qa)、criteria、labeled criteria、字符串距离、嵌入距离 | LLM-as-a-Judge、人工标注、Score Analytics |
| CI/CD 集成 | 支持离线评估 + CI 回归 | 支持（SDK 集成单元测试框架） |
| 在线评估 | 支持（trace 抽样评估） | 支持（在线 trace 评估） |
| Prompt Hub | 有（prompt 版本化和共享） | 无（待核验） |
| 全局 LangChain 集成 | 原生 | 有（跟踪和监控.xmind 标注"不支持全局集成"，待核验） |
| 用户系统 | 有 | 有（跟踪和监控.xmind 标注 Phoenix 无用户系统，Langfuse 待核验） |
| 价格 | 商业定价，有免费 tier | 开源免费，自托管可控成本 |

*所有功能声明来自 2024 年 raw，legacy · not verified，实际功能以官方文档为准。*

## Evidence

- [[sources/Langchain(Legacy)/Langchain  DevOps.xmind|Langchain DevOps.xmind]] — LangSmith 的数据集、评估器类型、CI 回归和在线评估详细内容（legacy · not verified）。
- [[sources/提示语工程:上下文工程/LLM 评估.xmind|LLM 评估.xmind]] — Langfuse 的 Score、Experiment、LLM-as-a-Judge、Dataset 和 SDK 评估流程。
- [[sources/Langchain(Legacy)/跟踪和监控.xmind|跟踪和监控.xmind]] — 工具选型视角对比 LangSmith（商业闭源）、Phoenix（开源、无用户系统）、Langfuse（开源）。

## Implications

- 如果项目强绑定 LangChain 生态，LangSmith 的 prompt hub 和原生集成会减少配置成本。
- 如果需要自托管或更灵活的 LLM 应用框架支持，Langfuse 的开源策略更可控。
- 两者在评估工程模式（数据集 → 实验 → 评估器 → 结果分析）上高度一致，学一个再迁移另一个成本较低。
- 两者都可以作为 LLMOps 的评估层；CI 集成是 prompt 工程可重复验证的关键环节。

## Related Concepts

- [[concepts/LLMOps|LLMOps]]
- [[concepts/LLM 评估|LLM 评估]]
- [[concepts/LLM-as-a-Judge|LLM-as-a-Judge]]
- [[entities/LangSmith|LangSmith]]
- [[entities/Langfuse|Langfuse]]

## My Take

从学习视角来看，先用 Langfuse 理解评估工程的概念（数据集、评估器、离线/在线评估），再学 LangSmith 补充 LangChain 生态的原生集成细节，是比较高效的路径。两者工程模式一致，重点是建立"评估 = 可重复实验"的工作模式。

## Open Questions

- 所有功能细节需要官方文档核验（legacy · not verified）。
- 2025-2026 两款产品的功能差距是否已缩小，需要最新对比调研。
- Phoenix 作为第三个开源选项，其能力演变和社区活跃度未在当前 wiki 覆盖。
