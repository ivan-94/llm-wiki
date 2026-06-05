---
page_type: concept
updated_at: 2026-06-05
status: active
source_count: 4
learning_status: new
confidence: 2
difficulty: 3
review_after: 2026-06-13
---

# LLMOps

## Definition

LLMOps 是把 LLM 应用的开发、测试、评估、部署、监控和持续改进工程化的实践体系。相比传统 MLOps，LLMOps 特别关注 prompt 版本化、数据集管理、LLM-as-a-Judge 评估、trace 观测和在线/离线评估闭环。

## Why It Matters

LLM 应用的输入和输出都有自然语言的不确定性，传统软件工程的测试和监控方法无法直接适用。LLMOps 提供了把 LLM 应用质量变成可测量、可回归、可持续改进目标的工程路径。

## Mental Model

把 LLMOps 想象成"LLM 应用的 DevOps"：开发阶段有 prompt 版本化和数据集，测试阶段有评估器和实验，部署阶段有 trace 和监控，生产阶段有在线评估和反馈闭环——整个链路形成持续改进的质量引擎。

## Key Claims

- explicit（来自 Langchain DevOps.xmind）：LLM 应用因为自然语言输入和模型输出的不确定性，传统软件测试实践需要适配到评估、数据集和反馈闭环。
- explicit（来自 Langchain DevOps.xmind）：LLMOps 的核心组件包括数据集、评估器、离线实验、CI/CD 集成回归和在线质量监控。
- explicit（来自 LLM 评估.xmind）：LLM 评估应该同时看质量、token 成本、延迟和指令遵循度，而不只是答案准确率。
- explicit（来自 Langchain DevOps.xmind）：评估器是接收输入/输出/期望输出并返回分数的函数，可以是人工、AI 辅助或启发式评估。
- inferred：LLMOps 的关键挑战是定义"什么算好"（评分标准）和"什么算差"（失败模式），这需要任务专属的数据集和评估标准，不能套用通用指标。
- inferred（来自 human source）：LLMOps 的反馈对象不只包括 prompt 和应用输出，也可以包括 agent skill 文本；失败样本只有进入测试集、HAT 步骤或 skill 修订，才会变成可复利资产。

## Examples

- Langfuse 的评估闭环：构建数据集 → 运行 prompt 实验 → LLM-as-a-Judge 打分 → 查看评分分布 → 迭代 prompt。
- LangSmith CI 集成（legacy · not verified）：每次 PR 触发数据集评估，score 低于基线则阻止合并。
- 在线评估：在生产 trace 中抽样，用 LLM-as-a-Judge 或人工标注评估输出质量，监控质量漂移。

## Common Confusions

- LLMOps 不等于监控日志；trace 是原材料，评估和反馈才是 LLMOps 的核心价值。
- 离线评估和在线评估不是替代关系；离线评估确保基线，在线评估捕捉真实场景的新问题。
- prompt 版本化不等于 git 版本控制；需要同时版本化 prompt、数据集和评估标准，三者一起才能可重复。

## Evidence

- explicit: [[sources/Langchain(Legacy)/Langchain  DevOps.xmind|Langchain DevOps.xmind]] — 系统描述 LangSmith 作为 LLMOps 平台的数据集、评估、CI 和监控能力（legacy · not verified）。
- explicit: [[sources/提示语工程:上下文工程/LLM 评估.xmind|LLM 评估.xmind]] — 提供 Langfuse 平台的评估流程和指标设计。
- explicit: [[human/sources/inbox/cook-tweet/2026-06-01_AI输出质量控制与Hermes评估循环_EXM7777|AI 输出质量控制与 Hermes 评估循环]] — human source，补充输出质量门和失败样本回写循环。
- explicit: [[human/sources/inbox/cook-tweet/2026-06-03_用SkillOpt训练可进化Agent技能_SkillOpt|用 SkillOpt 训练可进化 Agent 技能]] — human source，补充 skill 文本版本化、数据集和验证门。

## Relations

- contains: [[concepts/LLM 评估|LLM 评估]]
- contains: [[concepts/LLM-as-a-Judge|LLM-as-a-Judge]]
- implemented-by: [[entities/LangSmith|LangSmith]] （legacy · not verified）
- implemented-by: [[entities/Langfuse|Langfuse]]
- enables: [[concepts/提示语工程|提示语工程]] （LLMOps 为 prompt 迭代提供可重复的评估闭环）
- related-source: [[sources/Langchain(Legacy)/Langchain  DevOps.xmind|Langchain DevOps.xmind]]
- map-entry: [[maps/LLM 应用与数据处理学习地图|LLM 应用与数据处理学习地图]]

## My Understanding

LLMOps 的本质是"把感觉变成指标"：不再说"这个 prompt 感觉更好"，而是在固定数据集上跑实验，用评估器打分，看版本 A 和版本 B 谁的指标更好。

## Review Questions

- LLMOps 和传统 MLOps 最大的区别是什么？
- 离线评估和在线评估分别在什么阶段发挥作用？
- 为什么 LLMOps 必须包含数据集版本化？

## Open Questions

- LangSmith 和 Langfuse 的最新 API 和功能边界需要官方文档核验（LangSmith legacy · not verified）。
- 开源 LLMOps 工具栈的成熟度和社区维护状态需要单独调研。
