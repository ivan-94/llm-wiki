---
page_type: entity
updated_at: 2026-05-30
status: active
source_count: 2
---

# LangSmith

> **Legacy 警告**：本页内容基于 `Langchain(Legacy)` 资料（Langchain DevOps.xmind，截至 2024年5月），legacy · not verified，API 行为以官方文档为准。注意：`LangSmith.xmind` 是占位草稿（partial），本页不引用其内容。

## What It Is

LangSmith 是 LangChain 生态中的 LLM DevOps 平台，覆盖 trace 记录、prompt 协作、数据集管理、评估实验、CI 回归和在线质量监控。它被定位为 LLM 应用开发、调试和持续改进的观测与评估中心。

LangSmith 属于商业闭源产品，小型项目可以试用。它与开源替代方案（如 Langfuse、Phoenix）形成对比，在 LangChain 生态中处于官方推荐地位，但在当前 wiki 中所有功能声明均标注为 legacy · not verified。

## Role In This Wiki

LangSmith 在本 wiki 中作为 LLMOps 平台参照，用于理解数据集、评估器、离线/在线评估、CI 集成和 trace 监控的工程模式。详细 LLMOps 概念见 [[concepts/LLMOps|LLMOps]]。

## Key Facts

- **Trace**：记录 LLM 应用的每次调用链路，作为评估和调试的原材料。
- **Dataset**：输入输出对的结构化集合，可用于评估实验、few-shot 示例和微调素材；支持版本化、导入导出。
- **Evaluator**：接收输入/输出/可选期望输出，返回分数的函数；内置类型包括：
  - 正确性评估：`qa`、`context_qa`（带上下文）、`cot_qa`（链式推理）。
  - criteria 评估：无参考答案时按简洁性、相关性、正确性、连贯性、有害性等标准打分。
  - labeled criteria：有参考标签的标准评估。
  - 字符串距离和嵌入距离：基于相似度的自动评分。
- **Experiment**：遍历 dataset，触发应用，并可对结果执行评估器；支持离线基线比较。
- **CI 回归**：可接入 CI/CD 流程，部署前自动跑数据集评估，防止质量回退。
- **在线评估**：在生产 trace 中抽样，应用 evaluator 打分，监控质量漂移。
- **Prompt Hub**：共享和版本化 prompt 的协作中心（legacy）。

## Related Concepts

- contrasts-with: [[entities/Langfuse|Langfuse]] — 两者都是 LLM 观测/评估平台，LangSmith 是官方闭源产品，Langfuse 是开源替代；详见 [[synthesis/LangSmith 与 Langfuse 可观测性对照（Legacy）|对照综合页]]。
- implements: [[concepts/LLMOps|LLMOps]]
- implements: [[concepts/LLM 评估|LLM 评估]]
- implements: [[concepts/LLM-as-a-Judge|LLM-as-a-Judge]]

## Evidence

- [[sources/Langchain(Legacy)/Langchain  DevOps.xmind|Langchain DevOps.xmind]] — 主要证据，LangSmith 的数据集、评估器、CI、在线评估和 trace 功能（legacy · not verified）。
- [[sources/Langchain(Legacy)/跟踪和监控.xmind|跟踪和监控.xmind]] — 把 LangSmith 定位为商业闭源的开发、调试、监控工具，对比 Phoenix 和 Langfuse（legacy · not verified）。

## Open Questions

- LangSmith 当前功能边界、价格和 API 需要官方文档核验（legacy · not verified）。
- 2025-2026 LangSmith 的功能演变和新增能力未覆盖。
