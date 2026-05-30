---
page_type: entity
updated_at: 2026-05-30
status: active
source_count: 1
---

# ClawTeam

## What It Is

ClawTeam 在本 wiki 中被整理为 CLI + 文件状态 + tmux/subprocess + worktree + 看板/收件箱的多 Agent 团队运行时案例。

## Role In This Wiki

它用于理解多智能体工程中任务板、worker 身份、blocked-by 依赖、inbox 通信、独立 worktree 和终端观测如何组成协作控制面。

## Key Facts

- worker 通常有独立 git worktree、tmux 窗口和身份。
- 任务状态包括 pending、in_progress、completed、blocked 和依赖关系。
- 通信通过 inbox send/receive/broadcast，观测通过 board、tmux 和 Web 面板。
- 状态以文件系统为真相源，而不是依赖中心化常驻服务。

## Related Concepts

- example-of: [[concepts/Agent Runtime|Agent Runtime]]
- related: [[concepts/Agent 可观测性|Agent 可观测性]]
- related: [[concepts/Agent 工作流技能编排|Agent 工作流技能编排]]
- contrasts-with: [[entities/oh-my-claude-code|oh-my-claude-code]]

## Evidence

- [[sources/Agent/多智能体.xmind|多智能体]]

## Open Questions

- ClawTeam 当前仓库和命令状态未联网核验。
