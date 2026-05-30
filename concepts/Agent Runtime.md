---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 5
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

## Evidence

- [[sources/Agent/变体/Nano Bot .xmind|Nano Bot]]
- [[sources/Agent/变体/Hermes.xmind|Hermes]]
- [[sources/Agent/变体/OpenClaw.xmind|OpenClaw]]
- [[sources/Vibe/Vibe Coding 随手记/Harness/云端 Agent 能力探索.xmind|云端 Agent 能力探索]]
- [[sources/Agent/闪极智能体/闪极智能体 2.excalidraw|闪极智能体 2]]

## Relations

- part-of: [[concepts/AI Agent|AI Agent]]
- enables: [[concepts/Agent Harness|Agent Harness]]
- contains: [[concepts/Agent 记忆|Agent 记忆]]
- contains: [[concepts/Agent 工具调用|Agent 工具调用]]
- related-source: [[synthesis/Agent 系统工程综述|Agent 系统工程综述]]

## My Understanding

当前理解：Runtime 把 Agent 从“会回答”推进到“能持续执行并留下状态”。

## Review Questions

- Agent Runtime 和 Agent Harness 的边界在哪里？
- 为什么 MessageBus、session store 和 tool registry 是 runtime 核心部件？

## Open Questions

- 不同 runtime 的最小可用边界还需要通过真实实现对比确认。
