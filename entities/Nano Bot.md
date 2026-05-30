---
page_type: entity
updated_at: 2026-05-30
status: active
source_count: 1
---

# Nano Bot

## What It Is

Nano Bot 在本 wiki 中被整理为轻量 Agent Runtime 案例，强调少层次、强契约、文件系统优先和 MessageBus 解耦。

## Role In This Wiki

它提供最小 runtime 骨架：MessageBus、AgentLoop、Context、Memory、Skills、Tools、Session、Sub Agents、Cron 和 Heartbeat。

## Key Facts

- MessageBus 解耦 channels 与 agent。
- AgentLoop 处理控制命令和入站消息，并进入完整对话链路。
- MEMORY.md 全量进入 system，HISTORY.md 作为可 grep 的追加时间线。
- 子代理结果通过 MessageBus 回灌到主流程。

## Related Concepts

- example-of: [[concepts/Agent Runtime|Agent Runtime]]
- implements: [[concepts/Agent MessageBus|Agent MessageBus]]
- related: [[concepts/子代理委派模式|子代理委派模式]]
- related: [[concepts/Agent 记忆|Agent 记忆]]
- related: [[concepts/Agent Skills|Agent Skills]]
- contrasts-with: [[entities/OpenClaw|OpenClaw]]
- contrasts-with: [[entities/Hermes|Hermes]]
- contrasts-with: [[entities/闪极智能体|闪极智能体]]

## Evidence

- [[sources/Agent/变体/Nano Bot .xmind|Nano Bot]]

## Open Questions

- 需要更多实现资料来确认 Nano Bot 的真实项目状态。
