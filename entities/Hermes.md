---
page_type: entity
updated_at: 2026-05-30
status: active
source_count: 1
---

# Hermes

## What It Is

Hermes 在本 wiki 中被整理为强调学习循环、跨会话记忆、平台网关、自动化和研究轨迹生成的 Agent 系统。

## Role In This Wiki

它作为长期运行 Agent Runtime 的案例，帮助理解会话血缘、SQLite/FTS5、记忆 provider、cron、delegate、batch runner 和训练轨迹生成如何组合。

## Key Facts

- AIAgent 是核心对话循环，负责提示构建、供应商解析、工具调度、压缩、缓存和持久化。
- 会话存储基于 SQLite 与 FTS5，支持压缩前后的会话血缘。
- Cron 会在新 Agent 会话中运行到期任务；delegate_task 创建隔离子 Agent。
- 当前仓库与产品状态未联网核验。

## Related Concepts

- example-of: [[concepts/Agent Runtime|Agent Runtime]]
- related: [[concepts/Agent 记忆|Agent 记忆]]
- related: [[concepts/Agent 反馈回路|Agent 反馈回路]]
- contrasts-with: [[entities/OpenClaw|OpenClaw]]
- contrasts-with: [[entities/Nano Bot|Nano Bot]]

## Evidence

- [[sources/Agent/变体/Hermes.xmind|Hermes]]

## Open Questions

- 需要确认 Hermes Agent 当前实现状态和与 OpenClaw 的真实差异。
