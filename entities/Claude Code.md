---
page_type: entity
updated_at: 2026-05-29
status: active
source_count: 4
---

# Claude Code

## What It Is

Claude Code 在本 wiki 中被整理为一个终端优先的 agentic coding 工具和工作流平台，覆盖 CLI、memory、skills、hooks、SubAgent、Agent Teams、SDK、MCP 和 dynamic workflows。

## Role In This Wiki

它是 Vibe 工具链和 Agentic Engineering 的核心参照之一，用来观察如何把自然语言交互、项目上下文、权限、自动化和多 Agent 编排结合起来。

## Key Facts

**六层架构（来自 `解构 Claude Code.xmind`）：**

| 层 | 核心内容 |
| --- | --- |
| 交互层 | 自然语言对话、slash commands、`@` 文件引用、`#` 记忆、`!` shell、多模态、计划模式 |
| 上下文层 | CLAUDE.md、`.claude/rules/`、全局/项目配置、MCP、渐进式披露原则 |
| 定制层 | 自定义 commands、output-styles、sub-agents、hooks、memory、agent-memory |
| 执行层 | 无头模式、TypeScript SDK、Python SDK、流式/单次模式、GitHub CI 集成 |
| 编排层 | SubAgent（独立上下文/工具限制/专门提示）、Agent Teams（独立实例互沟通）、动态工作流（JS 脚本持有循环和中间结果） |
| 治理层 | 权限控制、hooks 生命周期、session 管理、worktree 并发、JSONL 日志、slop-scan |

**关键设计原则：**
- 渐进式披露：根 CLAUDE.md 只放普适规则和指针，细节放 docs/rules/skills/commands/agents。
- SubAgent vs Agent Teams：SubAgent 向主 Agent 汇报，Teams 是独立实例互沟通；前者适合功能专业化，后者适合多维度协作。
- 计划模式：适合代码探索、复杂改动规划和安全审查，在修改前先制定并确认计划。

**被增强路线：**
- oh-my-claude-code：Hooks/Skills/Agents/State 生命周期管理。
- Superpowers：session-start hook 注入工作流框架 + 子代理评审。
- GStack：slash commands 质量门禁套件（`/ship`/`/review`/`/codex`/`/canary`）。

## Related Concepts

- related: [[concepts/Agent Skills|Agent Skills]]
- related: [[concepts/Agent Harness|Agent Harness]]
- related: [[concepts/Agentic Engineering|Agentic Engineering]]
- related: [[concepts/上下文工程|上下文工程]] — CLAUDE.md 和渐进式披露是上下文工程的核心实践
- implemented-by: [[entities/Superpowers|Superpowers]] — session-hook 注入增强框架
- implemented-by: [[entities/GStack|GStack]] — slash commands 质量门禁套件
- implemented-by: [[entities/oh-my-claude-code|oh-my-claude-code]] — Hooks/Agents/State 生命周期管理
- contrasts-with: [[entities/Codex|Codex]] — Codex 主打云端托管容器和 Goal Mode 闭环，Claude Code 主打终端优先和 SDK 定制

## Evidence

- [[sources/Vibe/工具/Claude Code/解构 Claude Code.xmind|解构 Claude Code]]
- [[sources/Vibe/工具/Claude Code/claude code cli.png|claude code cli.png]]
- [[sources/Vibe/工具/Claude Code/claude-code-cli-cheatsheet|claude-code-cli-cheatsheet]]
- [[sources/Vibe/Vibe Coding 随手记/大规模 AI Coding/claude code 大型项目落地.PNG|claude code 大型项目落地]]

## Open Questions

- CLI flags、SubAgent、Agent Teams 和 dynamic workflows 当前官方状态需要后续核验。
