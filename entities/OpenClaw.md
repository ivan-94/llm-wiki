---
page_type: entity
updated_at: 2026-05-30
status: active
source_count: 3
---

# OpenClaw

## What It Is

OpenClaw 在本 wiki 中被整理为本地优先、Loopback-first、Unix 哲学导向的个人 Agent 系统案例。

## Role In This Wiki

它是 Agent Runtime 和本地优先 Agent 产品形态的样本，用于比较 Gateway/Node/Channel、文本记忆、workspace、skills、CLI、自动化和多 Agent 隔离。

## Key Facts

- 核心架构由 Gateway、Node、Channel 三层组成。
- Loopback-first 默认不开放外网端口，远程访问通过 Tailscale 或 SSH 转发。
- Daily Log、MEMORY.md、workspace、skills 和 CLI 构成文本优先的可扩展环境。
- 当前产品和外部链接未联网核验。

## Related Concepts

- example-of: [[concepts/Agent Runtime|Agent Runtime]]
- related: [[concepts/Agent 记忆|Agent 记忆]]
- related: [[concepts/Agent 记忆生命周期|Agent 记忆生命周期]]
- related: [[concepts/Agent Skills|Agent Skills]]
- related: [[concepts/Agent 沙箱|Agent 沙箱]]
- contrasts-with: [[entities/Hermes|Hermes]]
- contrasts-with: [[entities/Nano Bot|Nano Bot]]
- contrasts-with: [[entities/闪极智能体|闪极智能体]]

## Evidence

- [[sources/Agent/变体/OpenClaw.xmind|OpenClaw]]
- [[sources/Agent/变体/OpenClaw橙皮书-从入门到精通-v1.3.1.pdf|OpenClaw 橙皮书]]
- [[sources/Agent/Agent 解构.xmind|Agent 解构]]

## Open Questions

- 需要更多当前项目资料来确认 OpenClaw 实际能力和版本状态。
