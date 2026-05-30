---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 7
learning_status: new
confidence: 2
difficulty: 4
review_after: 2026-06-06
---

# Agent Runtime

## Definition

Agent Runtime 是让 Agent 长时间、跨工具、跨会话、可恢复执行任务的运行系统，通常包含消息循环、上下文构建、工具注册、状态存储、记忆、子代理、调度和权限边界。

## Why It Matters

没有 runtime，Agent 只是一次模型调用；有 runtime，Agent 才能处理长任务、外部事件、工具结果、压缩恢复、定时任务和多入口执行。

## Mental Model

Runtime 是 Agent 的操作系统：负责事件进入、状态保存、工具执行、错误恢复和生命周期管理。

## Key Claims

- 轻量 runtime 可以用 MessageBus、AgentLoop、文件记忆和工具注册表构成。
- 长期运行 runtime 需要会话血缘、压缩恢复、搜索、cron、delegate 和隔离执行环境。
- 本地优先 runtime 关注 workspace、文本记忆、CLI 工具面和 loopback 安全边界。
- 云端 runtime 关注托管环境、setup/agent 阶段、权限、事件流、PR/review 集成和恢复机制。

### 变体分类轴

把已 ingest 的 Agent runtime 变体按设计取向分类，便于选型对照：

| 取向 | 代表 | 核心特征 |
| --- | --- | --- |
| 总线型 / 最小架构 | [[entities/Nano Bot|Nano Bot]] | MessageBus 解耦渠道与 agent，文件记忆（MEMORY.md/HISTORY.md），强契约、少层次 |
| 学习型 / 长期运行 | [[entities/Hermes|Hermes]] | 学习循环创建技能、SQLite+FTS5 会话血缘、cron、delegate、批量轨迹生成 |
| 本地优先 / 极简工具面 | [[entities/OpenClaw|OpenClaw]] | Gateway/Node/Channel 三层、Loopback-first、Read/Write/Edit/Bash、不内置 MCP |
| 设备 Channel / 产品化 | [[entities/闪极智能体|闪极智能体]] | AI 眼镜消息模型、OpenAI 兼容 Gateway+SSE、会话压缩、nsjail 沙箱、Loomos 记忆 |
| 低代码平台 | [[entities/Coze|Coze]] | 可视化编排、托管知识库/渠道，上手快但深度定制弱（见 [[concepts/低代码 Agent 平台 vs 代码优先 Runtime|低代码 Agent 平台 vs 代码优先 Runtime]]） |

- 分类轴可归纳为：架构层次（最小 vs 分层）、是否内置学习闭环、本地优先还是托管、是否绑定设备 Channel、代码优先还是低代码。
- 多数变体共享相同核心部件——MessageBus、AgentLoop、session store、tool registry、记忆、子代理、cron，差异在取向和边界，而非部件清单。

## Evidence

- [[sources/Agent/变体/Nano Bot .xmind|Nano Bot]]
- [[sources/Agent/变体/Hermes.xmind|Hermes]]
- [[sources/Agent/变体/OpenClaw.xmind|OpenClaw]]
- [[sources/Vibe/Vibe Coding 随手记/Harness/云端 Agent 能力探索.xmind|云端 Agent 能力探索]]
- [[sources/Agent/闪极智能体/闪极智能体 2.excalidraw|闪极智能体 2]]
- [[sources/Agent/闪极智能体/闪极智能体-里程碑与计划.xmind|闪极智能体-里程碑与计划]]
- [[sources/Agent/变体/Coze.xmind|Coze]]
- [[sources/Agent/LangChain.xmind|LangChain.xmind]]

## Relations

- part-of: [[concepts/AI Agent|AI Agent]]
- enables: [[concepts/Agent Harness|Agent Harness]]
- contains: [[concepts/Agent 记忆|Agent 记忆]]
- contains: [[concepts/Agent 工具调用|Agent 工具调用]]
- contains: [[concepts/Agent MessageBus|Agent MessageBus]]
- contains: [[concepts/会话分层存储与压缩|会话分层存储与压缩]]
- contrasts-with: [[concepts/低代码 Agent 平台 vs 代码优先 Runtime|低代码 Agent 平台 vs 代码优先 Runtime]]
- implemented-by: [[entities/Nano Bot|Nano Bot]]
- implemented-by: [[entities/Hermes|Hermes]]
- implemented-by: [[entities/OpenClaw|OpenClaw]]
- implemented-by: [[entities/闪极智能体|闪极智能体]]
- related-source: [[synthesis/Agent 系统工程综述|Agent 系统工程综述]]
- map-entry: [[maps/Agent 学习地图|Agent 学习地图]]

## My Understanding

当前理解：Runtime 把 Agent 从“会回答”推进到“能持续执行并留下状态”。

## Review Questions

- Agent Runtime 和 Agent Harness 的边界在哪里？
- 为什么 MessageBus、session store 和 tool registry 是 runtime 核心部件？
- Nano Bot、Hermes、OpenClaw、闪极智能体分别代表哪种 runtime 取向？
- 区分 runtime 变体的分类轴有哪些？

## Open Questions

- 不同 runtime 的最小可用边界还需要通过真实实现对比确认。
