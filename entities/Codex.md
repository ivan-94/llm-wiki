---
page_type: entity
updated_at: 2026-05-30
status: active
source_count: 3
---

# Codex

## What It Is

Codex 在本 wiki 中被整理为 OpenAI 的 coding agent / CLI / 云端执行能力谱系，用于研究终端工作流、非交互执行、云端环境、SDK、MCP 和 GitHub workflow 集成。

## Role In This Wiki

它是 Vibe Coding 工具链和 Agent Runtime 的重要参照，用来观察从本地 CLI 到云端托管容器再到自动化 workflow 的能力分层。

## Key Facts

- CLI source 覆盖安装登录、交互会话、权限/沙箱、配置、AGENTS.md、MCP 和脚本化执行。
- 云端 source 将 Codex 拆成托管容器、Cloud Environments、setup/agent 阶段、SDK、App Server、MCP 和 GitHub Action。
- Goal source 将 Codex 相关 Goal Mode 解释为目标、评分、停止条件和外部记忆组成的闭环。
- Codex 产品细节高度时间敏感，本页未联网核验当前状态。

## Related Concepts

- example-of: [[concepts/Agent Runtime|Agent Runtime]]
- related: [[concepts/Agent 反馈回路|Agent 反馈回路]]
- related: [[concepts/AGENTS.md 设计模式|AGENTS.md 设计模式]]
- contrasts-with: [[entities/Claude Code|Claude Code]]

## Evidence

- [[sources/Vibe/工具/codex/cli.png|Codex CLI]]
- [[sources/Vibe/工具/codex/Goal.xmind|Goal]]
- [[sources/Vibe/Vibe Coding 随手记/Harness/云端 Agent 能力探索.xmind|云端 Agent 能力探索]]

## Open Questions

- 需要基于官方文档核验当前 CLI、云端环境、SDK 和 Goal Mode 状态。
