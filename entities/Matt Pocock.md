---
page_type: entity
updated_at: 2026-06-01
status: active
source_count: 8
---

# Matt Pocock

## What It Is

Matt Pocock 是一位 TypeScript 教育者和方法论作者，在本 wiki 中主要作为 AI Agent skills 工程流程方法论的代表人物。他设计了一套以"小而可组合"为核心的 Agent skills 体系，涵盖从需求对齐（/grill）到 PRD（/to-prd）、issue 拆解（/to-issues）、分诊（/triage）、TDD（/tdd）、调试（/diagnose）、架构改进（/improve-codebase-architecture）、交叉 review（/cross-review）、HAT 验收、PR 创建和合并的完整工程链路。

## Role In This Wiki

Matt Pocock Skills 体系是本 wiki 工作流技能编排内容的核心来源，他的 GitHub 驱动开发闭环方法为 `synthesis/GitHub 驱动的 Agent 开发闭环` 提供了 triage labels、Brief 和 Issue-as-protocol 等核心概念。

## Key Facts

- Skills 设计原则：small（小）、easy to adapt（易改）、composable（可组合），保持人的控制权。
- 四失败模式诊断：AI 没理解需求 → `/grill`；AI 废话太多 → CONTEXT.md 对齐；代码跑不通 → `/tdd`/`/diagnose`；架构变差 → `/improve-codebase-architecture`。
- GitHub Issue 升格为 AI 协作协议层：Label、Comment、Webhook、Reference 分别承担路由、事件日志、触发器和依赖图角色。
- CONTEXT.md 是核心工具：通过术语定义、Avoid 同义词、关系和示例对话让 Agent 使用项目共享语言。
- 个人工程流程完整链路：setup → grill → prototype → to-prd → to-issues → triage → tdd/diagnose/cross-review → hat → pr → merge。
- 并发执行模式：父 Agent 探索规划并协调 sub-agent，子 Agent 在隔离 worktree 中执行 TDD；父 Agent 合并、cross-review 并准备 HAT。

## Related Concepts

- implemented-by: [[concepts/Agent Skills|Agent Skills]] — Matt Pocock Skills 体系定义了 skill 三分法和设计原则。
- enables: [[concepts/Agent 工作流技能编排|Agent 工作流技能编排]] — 其工程链路是工作流技能编排的主要参照。
- contributes-to: [[synthesis/GitHub 驱动的 Agent 开发闭环|GitHub 驱动的 Agent 开发闭环]] — triage labels、Brief 和 Issue 协议层的主要来源。
- related: [[entities/GStack|GStack]] — 另一路 CLI-native + slash commands 实现路线，与 Matt Pocock 的 skills 方法论形成对比。
- contrasts-with: [[entities/Superpowers|Superpowers]] — Superpowers 更侧重 session-start hook 注入和子代理评审，Matt 更侧重 skill 可组合性和 GitHub 闭环。

## Evidence

### 2026-06-01 扩展技能 source

- [[sources/Vibe/工具/mattpocock:skills  ⭐/Ext HAT - Hand Acceptance Test Prepare验收测试准备hat-prepare.xmind|Vibe/工具/mattpocock:skills  ⭐/Ext HAT - Hand Acceptance Test Prepare验收测试准备hat-prepare.xmind]] — 2026-06-01 raw diff refresh补充的 Matt Pocock 扩展工作流证据。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/Ext HAT - Hand Acceptance Test Run验收测试执行hat-run.xmind|Vibe/工具/mattpocock:skills  ⭐/Ext HAT - Hand Acceptance Test Run验收测试执行hat-run.xmind]] — 2026-06-01 raw diff refresh补充的 Matt Pocock 扩展工作流证据。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/Ext 上下文检查agent-context-audit.xmind|Vibe/工具/mattpocock:skills  ⭐/Ext 上下文检查agent-context-audit.xmind]] — 2026-06-01 raw diff refresh补充的 Matt Pocock 扩展工作流证据。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/Ext 流程控制setup-agent-workflow.xmind|Vibe/工具/mattpocock:skills  ⭐/Ext 流程控制setup-agent-workflow.xmind]] — 2026-06-01 raw diff refresh补充的 Matt Pocock 扩展工作流证据。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/我的流程.xmind|Vibe/工具/mattpocock:skills  ⭐/我的流程.xmind]] — 2026-06-01 raw diff refresh补充的 Matt Pocock 扩展工作流证据。

- [[sources/Vibe/工具/mattpocock:skills  ⭐/Matt Pocock Skills.xmind|Matt Pocock Skills]] — 完整方法论体系，包括四失败模式、工程链路和 GitHub 协议层升格。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/我的流程.xmind|我的流程]] — 个人端到端工程流程，覆盖 setup 到 merge 的全链路。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/定制化.xmind|定制化]] — HAT 体系、context audit 和流程治理的具体 skill 实现。

## Open Questions

- Matt Pocock 方法论的公开 GitHub 仓库和具体 skill 实现状态未在 source 中提供 URL，需要后续核验。
