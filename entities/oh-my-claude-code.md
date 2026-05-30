---
page_type: entity
updated_at: 2026-05-30
status: active
source_count: 1
---

# oh-my-claude-code

## What It Is

oh-my-claude-code 在本 wiki 中被整理为围绕 Claude Code 的 Hooks、Skills、Agents 和 State 编排系统。

## Role In This Wiki

它用于理解 Claude Code 内部生态如何通过生命周期 hook、workflow skills、专业 agent 和 `.omc/` 状态目录支撑长任务连续性。

## Key Facts

- 系统由 Hooks、Skills、Agents、State 四个部分构成。
- Agents 覆盖 explore、analyst、planner、critic、executor、verifier 等任务角色。
- `.omc/` 保存 state、notepad、project memory、plans、research 和 logs。
- Skills 在现有智能体上增加 autopilot、team、plan/review 等工作流能力。

## Related Concepts

- example-of: [[concepts/Agent 工作流技能编排|Agent 工作流技能编排]]
- related: [[concepts/Agent Skills|Agent Skills]]
- related: [[concepts/Agent 可观测性|Agent 可观测性]]
- related: [[entities/Claude Code|Claude Code]]
- contrasts-with: [[entities/ClawTeam|ClawTeam]]

## Evidence

- [[sources/Agent/多智能体.xmind|多智能体]]

## Open Questions

- 当前项目状态和与 Claude Code 官方能力的边界未核验。
