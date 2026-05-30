---
page_type: map
updated_at: 2026-05-30
status: active
scope: Vibe/工具
---

# Vibe Coding 工具地图

## Purpose

整理 Vibe 目录中的 Agent 工具、CLI、skills、远程控制和 GitHub 工作流资料，作为工具学习入口。

## Entry Points

推荐学习起点（按顺序）：
1. [[sources/Vibe/工具/mattpocock:skills  ⭐/核心洞察.png|核心洞察.png]] — 整个 Vibe 工具生态的底层逻辑
2. [[sources/Vibe/工具/mattpocock:skills  ⭐/地图2.png|地图2.png]] — skills 硬依赖图，理解工作流节点关系
3. [[entities/Claude Code|Claude Code]] 和 [[entities/Codex|Codex]] — 双 CLI 底座

## Learning Path

1. 先读 [[concepts/Agent Skills|Agent Skills]] 的三分法（Engineering Workflow / Helper / Lightweight），理解 skill 分类和触发契约。
2. 读 `核心洞察.png` 和 `地图2.png`，理解工作流的整体逻辑和硬依赖关系。
3. 读 [[entities/Claude Code|Claude Code]]，理解六层架构（交互/上下文/定制/执行/编排/治理）。
4. 读 [[entities/Agent Client Protocol|Agent Client Protocol]]，理解 client-agent 协议层与 MCP 的分工。
5. 读 [[synthesis/GitHub 驱动的 Agent 开发闭环|GitHub 驱动的 Agent 开发闭环]]，把 GitHub 六层 + triage labels + Agent Brief 串起来。
6. 按场景深入：远程控制 → `tmux.png`/`远程控制.xmind`；知识管理 → Obsidian；长任务 → Codex Goal Mode。

## Tool Clusters

### 协议与 CLI 底座
- ACP: [[sources/Vibe/工具/ACP.xmind|ACP]]（client-agent 协议）、[[entities/Agent Client Protocol|Agent Client Protocol]]
- Claude Code: [[sources/Vibe/工具/Claude Code/解构 Claude Code.xmind|解构 Claude Code]]、[[sources/Vibe/工具/Claude Code/claude code cli.png|cli.png]]、[[sources/Vibe/工具/Claude Code/claude-code-cli-cheatsheet|cheatsheet]]
- Codex: [[sources/Vibe/工具/codex/cli.png|cli.png]]、[[sources/Vibe/工具/codex/Goal.xmind|Goal.xmind]]

### 三大 Skills 框架
- Matt Pocock: [[sources/Vibe/工具/mattpocock:skills  ⭐/Matt Pocock Skills.xmind|Matt Pocock Skills]]、[[entities/Matt Pocock|Matt Pocock]]
- Superpowers: [[sources/Vibe/工具/superpower.xmind|superpower]]（partial）、[[entities/Superpowers|Superpowers]]
- GStack: [[sources/Vibe/工具/AI 软件工厂 GStack.xmind|AI 软件工厂 GStack]]、[[entities/GStack|GStack]]

### GitHub-HAT 工作流
- GitHub: [[sources/Vibe/工具/Github 原住民.xmind|Github 原住民]]
- HAT: [[sources/Vibe/工具/mattpocock:skills  ⭐/定制化.xmind|定制化]]（hat-prepare/hat-run）
- 看板: [[sources/Vibe/工具/mattpocock:skills  ⭐/看板管理.xmind|看板管理]]（编排 UI 候选）

### 远程与运行时
- Remote: [[sources/Vibe/工具/tmux.png|tmux.png]]、[[sources/Vibe/工具/远程控制.xmind|远程控制]]、[[concepts/远程 Agent 控制栈|远程 Agent 控制栈]]
- 并发执行: [[sources/Vibe/工具/mattpocock:skills  ⭐/为 Agents 构造并发执行环境.xmind|为 Agents 构造并发执行环境]]

### 知识管理
- Obsidian: [[sources/Vibe/工具/Obsidian.xmind|Obsidian.xmind]]、[[entities/Obsidian|Obsidian]]

## Key Concepts

- [[concepts/AI 软件工厂|AI 软件工厂]] — 工具生态的抽象概念
- [[concepts/Agent 工作流技能编排|Agent 工作流技能编排]] — 工作流节点编排
- [[concepts/Agent Brief|Agent Brief]] — triage 产物，进入 ready-for-agent 的必要条件
- [[concepts/Vertical Slice Issue|Vertical Slice Issue]] — issue 的结构要求
- [[concepts/CONTEXT.md 领域语言|CONTEXT.md 领域语言]] — 项目语言契约
- [[concepts/Skill 触发契约|Skill 触发契约]] — skill 可用性控制面

## Open Gaps

- CLI flags、ACP transport 演进、Claude Code、Codex 等当前产品状态未联网核验。
- `.xmind-backups` 下的 Obsidian 备份 source 只用于维护，不参与主学习路径。
- 看板管理是设计草案，实际 `agent-board` CLI/App 状态未验证。
