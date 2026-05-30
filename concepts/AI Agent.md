---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 12
learning_status: new
confidence: 3
difficulty: 4
review_after: 2026-06-06
---

# AI Agent

## Definition

AI Agent 是一个由模型、上下文、工具、记忆、反馈和控制循环组成的执行系统，能够基于目标感知状态、选择行动、调用工具并根据结果继续迭代。

## Why It Matters

Agent 是 Vibe Coding 和 Agentic Engineering 的核心执行体。理解 Agent 不能停在“LLM + tool calling”，否则会低估上下文、工具接口、记忆、沙箱、状态持久化和协作协议对可靠性的影响。

## Mental Model

Agent Loop 是内核，Harness 是操作系统：模型负责推理，外部工程系统负责给它可见世界、可用能力、可恢复状态和可验证反馈。

## Key Claims

- Agent 主循环可以抽象为感知、决策、行动、反馈；新增能力通常叠加在循环外围。
- workflow 与 agent 的关键差异是控制权：代码预写路径是 workflow，LLM 动态决定下一步是 agent（详见 [[concepts/Workflow 与 Agent 的边界|Workflow 与 Agent 的边界]]）。
- 控制权可以排成谱系——Prompt Chaining、Routing、Parallelization、Orchestrator-Workers、Evaluator-Optimizer 五类控制模式按控制权由弱到强（详见 [[concepts/Agent 控制模式|Agent 控制模式]]）。
- 认知架构上 Agent 可拆为模型（决策器）、工具（行动能力）、编排层（接收信息、推理、指导下一步直到目标达成或停止条件触发）；Agent 与 Model 的差异在知识范围、状态与记忆、原生工具、原生逻辑层。
- Agent 的工程质量主要取决于 harness、上下文、工具设计、记忆、沙箱、安全边界和验证循环。
- 多 Agent 协作不是简单多开模型，而是需要任务图、worktree 隔离、协议化交接、交叉验证和冲突处理（详见 [[concepts/多 Agent 协作协议|多 Agent 协作协议]]）。
- Agent 自主度依赖可操作机制：跨 session 用 Initializer Agent 创建 `feature-list.json`/`init.sh`/初始提交/进度文件再循环续跑，单 session 内用唯一 `in_progress` 和校正提醒防漂移，慢速 I/O 通过后台线程和通知队列接入。
- Agent 成熟度可从补全/IDE、上下文工程、复合工程、MCP/Skills、Harness、后台 Agent 演进到自主 Agent 团队。

## Examples

- `Agent 解构.xmind` 用 Agent Loop、五类控制模式、OpenClaw 五层架构、多 Agent 和记忆机制拆出系统边界。
- `智能体工程的 8 个等级.xmind` 给出从 Tab 补全到自主团队的成熟度路径。
- `Agent.xmind` 提供「模型/工具/编排层」认知架构和 Planning→Executing→Adjusting 工作循环。
- `多智能体.xmind` 提供 ClawTeam 与 oh-my-claude-code 两种多 Agent 协作模型。
- `闪极智能体` 系列把 Agent 放入 AI 眼镜、多模态设备和沙箱运行时场景。

## Common Confusions

- Tool calling 是 Agent 能力的一部分，不等于完整 Agent。
- 多 Agent 不自动带来质量；没有任务边界和合并协议时会增加编排成本。
- Agent 自主度不是减少人工确认，而是让状态、目标、反馈和停止条件可持续。
- `各种 Agent 类型.xmind` 名为「Agent 类型」，实际是 RAG 能力谱系（原生 RAG、ReRank、多模态、Agentic RAG、混合 RAG、Graph RAG），不应被当成通用 Agent 类型学；该证据归 [[concepts/RAG|RAG]]。

## Evidence

- [[sources/Agent/Agent 解构.xmind|Agent 解构.xmind]]
- [[sources/Agent/Agent.xmind|Agent.xmind]]
- [[sources/Agent/Agent_副本.xmind|Agent_副本.xmind]]
- [[sources/Agent/多智能体.xmind|多智能体.xmind]]
- [[sources/Agent/智能体工程的 8 个等级.xmind|智能体工程的 8 个等级]]
- [[sources/Agent/闪极智能体/闪极智能体.xmind|闪极智能体.xmind]]

## Relations

- part-of: [[concepts/Agentic Engineering|Agentic Engineering]]
- enabled-by: [[concepts/Agent Harness|Agent Harness]]
- contains: [[concepts/Agent 控制模式|Agent 控制模式]]
- contrasts-with: [[concepts/Workflow 与 Agent 的边界|Workflow 与 Agent 的边界]]
- uses: [[concepts/Agent 工具调用|Agent 工具调用]]
- uses: [[concepts/Agent 记忆|Agent 记忆]]
- uses: [[concepts/Agent 沙箱|Agent 沙箱]]
- related: [[concepts/多 Agent 协作协议|多 Agent 协作协议]]
- map-entry: [[maps/Agent 学习地图|Agent 学习地图]]

## My Understanding

当前理解：Agent 的本质不是“更聪明的 prompt”，而是一个必须被工程系统承载的长期执行体。

## Review Questions

- Agent Loop 的四个环节是什么？
- 认知架构里模型、工具、编排层各负责什么？
- 五类控制模式按控制权强弱怎么排序？
- workflow 和 agent 的控制权差异是什么？
- 为什么多 Agent 协作需要 worktree、任务图和交接协议？
- Agent 自主度依赖哪些可操作机制（跨 session / 单 session / 慢 I/O）？

## Open Questions

- 不同 Agent runtime 的能力边界和安全模型还需要真实项目对比。
- 多 Agent 自主协作的收益与编排成本缺少稳定量化证据。
