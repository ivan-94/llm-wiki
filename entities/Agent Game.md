---
page_type: entity
updated_at: 2026-05-30
status: active
source_count: 1
---

# Agent Game

## What It Is

Agent Game 是一个基于文件系统设计的文字游戏项目，以"repo 即世界、文件即记忆、agent 即游戏引擎、commit 即时间线"为核心哲学，将文字 RPG 游戏的世界状态、人物、章节、历史、规则和技能全部建模为 git 仓库中的 Markdown 文件，由 Agent 读取和维护。

## Role In This Wiki

Agent Game 是 Agentic Engineering 的一个典型案例：它展示了如何用文件系统作为 Agent 可读写的状态层，通过 AGENTS.md 作为规则引擎，append-only 日志作为不可篡改历史，以及 hooks 约束 Agent 行为，构成一个能长期稳定运行的 Agent 应用。该项目揭示的设计范式（索引/状态/历史/规则四要素）可以迁移到任何需要 Agent 在持久化状态中工作的系统。

## Key Facts

- 核心哲学：`repo = world`；`files = memory`；`agent = engine`；`commit = timeline`。
- 目录职责分工：`map/`、`characters/`、`chapters/`、`factions/` 存储世界事实；`states/` 下包含当前状态、玩家档案、偏好记忆、不可变历史日志（`logs.jsonl`）和核心机制。
- `AGENTS.md` 作为规则引擎：覆盖游戏规则、哲学、运行方式、加载、存档、结算、行文和交互。
- `hooks/` 包含强制存档逻辑和随机变量介入，防止 Agent 一味顺从玩家。
- `logs.jsonl` 要求线性插入、不可修改，支持 grep 和工具查询写入。
- GitHub repository: [github.com/ivan-94/agent-game](https://github.com/ivan-94/agent-game)（not verified）

## Architectural Insights

从 Agent Game 可以提炼的文件系统状态管理范式：
- 索引文件（可导航）+ 当前状态文件（精确） + 历史日志（append-only）+ 规则文件（AGENTS.md）+ hooks（行为约束）= Agent 可稳定运行的持久化状态系统。

## Related Concepts

- [[concepts/Agent Harness|Agent Harness]] — Agent Game 是 harness 中 state layer 和 guardrail layer 的极简实现
- [[concepts/Agentic Engineering|Agentic Engineering]] — 长期运行 Agent 应用的工程化案例
- [[concepts/Agent 并发执行环境|Agent 并发执行环境]] — 两者都关注 Agent 的文件系统状态管理

## Evidence

- [[sources/Vibe/Vibe Coding 随手记/文件系统/Agent Game.xmind|Agent Game.xmind]] — 完整设计文档，包括目录职责、状态文件、日志、hooks 和规则引擎。

## Open Questions

- GitHub 仓库当前状态未联网核验。
- 游戏实际运行效果和 Agent 稳定性的案例数据需要后续补充。
