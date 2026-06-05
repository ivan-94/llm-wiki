---
page_type: entity
updated_at: 2026-06-05
status: active
source_count: 2
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
- human source 补充：Hermes 也可被理解为承载 eval loop 的 agent runtime 原语集合，用 skills、memory、cron、approval 和生产样本监控把输出质量门持续化。
- 当前仓库与产品状态未联网核验。

## Related Concepts

- example-of: [[concepts/Agent Runtime|Agent Runtime]]
- related: [[concepts/Agent 记忆|Agent 记忆]]
- related: [[concepts/会话分层存储与压缩|会话分层存储与压缩]]
- related: [[concepts/子代理委派模式|子代理委派模式]]
- related: [[concepts/Agent 反馈回路|Agent 反馈回路]]
- contrasts-with: [[entities/OpenClaw|OpenClaw]]
- contrasts-with: [[entities/Nano Bot|Nano Bot]]
- contrasts-with: [[entities/闪极智能体|闪极智能体]]

## Evidence

- [[sources/Agent/变体/Hermes.xmind|Hermes]]
- [[human/sources/inbox/cook-tweet/2026-06-01_AI输出质量控制与Hermes评估循环_EXM7777|AI 输出质量控制与 Hermes 评估循环]] — human source，补充 Hermes 作为评估循环载体的候选证据；外部事实未联网核验。

## Open Questions

- 需要确认 Hermes Agent 当前实现状态和与 OpenClaw 的真实差异。
