---
page_type: entity
updated_at: 2026-05-30
status: active
source_count: 1
---

# Superpowers

## What It Is

Superpowers 是一个面向 Claude Code 的 agentic skills framework 兼软件开发方法论：通过目标澄清、规格书编写、计划、子代理驱动执行、TDD 和代码评审，把 AI 编码从一次性对话变成受约束的工程工作流。

## Role In This Wiki

Superpowers 是 Claude Code 增强路线中强调"session-start hook 注入 + 子代理评审"的代表工具，与 GStack（slash commands 质量门禁套件）和 Matt Pocock Skills（可组合 GitHub 闭环工作流）构成三种不同增强路线的对比。

## Key Facts

**核心工作流（基本 workflow）：**
1. `brainstorming` — 发散目标
2. `using-git-worktrees` — 隔离执行环境
3. `writing-plans` — 生成足够明确的实现计划
4. `subagent-driven-development` / `executing-plans` — 子代理逐项完成
5. `test-driven-development` — TDD，红/绿重构约束
6. `requesting-code-review` — 触发 code-reviewer 子代理评审
7. `finishing-a-development-branch` — 收尾和清理

**四条方法论原则：**
1. 永远先写测试（YAGNI + DRY + TDD）
2. 系统化流程优于临时猜测
3. 简洁优先降低复杂度
4. 证据胜过宣称

**Claude Code 集成方式：**
- 通过 `hooks/session-start` 注入 `using-superpowers` skill，强制引导整体工作流。
- 注册 `agents/code-reviewer.md` 子 Agent 做代码评审。

**Skills 库分类：**
- 工作流技能：基本 workflow 的各阶段
- 测试 skills：TDD、verification-before-completion
- Debugging skills：systematic-debugging
- 协作 skills：dispatching-parallel-agents、receiving-code-review
- 元 skills：using-superpowers、writing-skills

## Related Concepts

- implements: [[concepts/AI 软件工厂|AI 软件工厂]] — Superpowers 是 AI 软件工厂的 session-hook 注入形态实现。
- related: [[concepts/Agent Skills|Agent Skills]] — Superpowers 把 skills 升格为可编排、可审查的 agent workflow 框架。
- contrasts-with: [[entities/GStack|GStack]] — GStack 侧重质量门禁 slash commands，Superpowers 侧重 session-hook 注入 + 子代理评审。
- contrasts-with: [[entities/Matt Pocock|Matt Pocock]] — Matt 侧重可组合性和 GitHub 闭环，Superpowers 侧重固化工作流和测试约束。
- contrasts-with: [[entities/oh-my-claude-code|oh-my-claude-code]] — oh-my-claude-code 以 Hooks/Agents/State 为核心，Superpowers 以 skills 框架和 TDD 约束为核心。

## Evidence

- [[sources/Vibe/工具/superpower.xmind|superpower.xmind]] — 主要来源；覆盖工作流、方法论原则、Claude Code 集成方式和 skills 库分类。

## Maintenance Notes

- Source 状态为 `partial`：`brainstorming`、`writing planning`、`systematic-debugging`、`test-driven-development`、`writing-skills` 等子 sheet 基本只有标题或空节点，相关技能细节待后续补充。
- 需要后续核验 Superpowers 的实际 GitHub 仓库状态和当前活跃维护情况。

## Open Questions

- Superpowers 的公开仓库和当前维护状态未在 source 中提供 URL，需后续核验。
- 与 Claude Code 官方 SubAgent 能力的边界区分还需要进一步研究。
