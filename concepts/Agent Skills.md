---
page_type: concept
updated_at: 2026-05-29
status: active
source_count: 16
learning_status: new
confidence: 2
difficulty: 3
review_after: 2026-06-05
---

# Agent Skills

## Definition

Agent Skills 是把可复用工作流、工具调用规则、交接协议和验证步骤封装成 Agent 可读取、可执行、可组合的知识单元。

## Why It Matters

单次提示会丢失上下文和经验；skill 把重复工程流程固化成可复用资产，让不同 Agent 在相似任务中少走弯路。

## Mental Model

Skill 是给 Agent 的“操作手册 + 进入条件 + 验证门禁”。

## Key Claims

- 好的 skill 不只是说明做什么，还要说明何时使用、读哪些文件、怎么验证、哪些边界不能越过。
- 工作流型 skill 可以串起 TDD、triage、PRD、issue、review、HAT 和 PR 交付。
- Helper skill 更像工程脚手架：设置 pre-commit、git guardrails、迁移测试数据、生成练习目录等。
- 图示类 source 适合做学习地图，具体实现仍要回到 skill 文件或工具文档核验。

## Examples

- `Matt Pocock Skills.xmind` 把 skill 体系分成 workflow、helper、setup、review、delivery 等。
- `tdd.png`、`to_prd__to_issue.png`、`triage 分诊.png` 分别说明垂直切片 TDD、PRD 到 issue、分诊状态机。
- `diagnose.png` 强调复现、最小化、假设、仪器化、修复和回归测试闭环。
- `superpower.xmind` 把 skills 作为 Claude Code 的 session-start hook 和 code-reviewer 子 Agent 入口。

## Common Confusions

- Skill 不是普通知识摘要；它应该改变 Agent 下一步行动。
- Skill 越多不一定越好，关键是触发边界清晰、验证成本可承受、与项目上下文匹配。

## Evidence

- [[sources/Vibe/工具/mattpocock:skills  ⭐/Matt Pocock Skills.xmind|Matt Pocock Skills]]
- [[sources/Vibe/工具/mattpocock:skills  ⭐/diagnose.png|diagnose]]
- [[sources/Vibe/工具/mattpocock:skills  ⭐/tdd.png|tdd]]
- [[sources/Vibe/工具/mattpocock:skills  ⭐/to_prd__to_issue.png|to_prd__to_issue]]
- [[sources/Vibe/工具/mattpocock:skills  ⭐/triage 分诊.png|triage 分诊]]
- [[sources/Vibe/工具/mattpocock:skills  ⭐/定制化.xmind|定制化]]
- [[sources/Vibe/工具/superpower.xmind|superpower]]

## Relations

- part-of: [[concepts/Agent Harness|Agent Harness]]
- used-in: [[synthesis/GitHub 驱动的 Agent 开发闭环|GitHub 驱动的 Agent 开发闭环]]
- map-entry: [[maps/Vibe Coding 工具地图|Vibe Coding 工具地图]]

## My Understanding

当前理解：Agent Skills 是把“我希望 Agent 以后这样做”从聊天偏好变成可复读的工程资产。

## Review Questions

- 一个 workflow skill 和 helper skill 的差别是什么？
- 为什么 skill 需要验证命令和触发边界？
- 哪些 skill 适合放在项目级，哪些适合放在用户级？

## Open Questions

- 多 skill 冲突时的优先级和可观测性还需要进一步设计。
