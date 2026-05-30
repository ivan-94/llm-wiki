---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 3
learning_status: new
confidence: 3
difficulty: 4
review_after: 2026-06-06
---

# 多 Agent 协作协议

## Definition

多 Agent 协作协议是让多个 Agent 从「并发启动」变成「能分工、通信、跟踪、隔离、恢复和验收的团队」所需的一组约定：任务依赖、通信信道、状态真相源、隔离执行环境、观测和交接规则。

## Why It Matters

多 Agent 的难点从来不是「开几个模型」，而是协调。没有协议，幻觉、依赖冲突和重复工作会互相放大；有协议，多个 Agent 才能像团队一样并行推进而不互相踩踏。

## Mental Model

把多 Agent 当成一个远程团队：需要任务看板（依赖）、收件箱（通信）、各自的工位（worktree 隔离）、共享文档（状态真相源）和站会复盘（观测+交叉验证）。缺哪一项，团队就乱。

## Key Claims

- `Agent 解构.xmind`：多 Agent 价值在于异步委派和持久化工件，而非简单多开模型；因此需要 JSONL inbox、worktree 隔离、任务图、交叉验证、深度限制和最小系统提示。
- `多智能体.xmind` 给出两类落地模型：ClawTeam 是「CLI + 文件状态 + tmux/worktree + 看板/收件箱」的外部团队运行时；oh-my-claude-code 是「Hooks + Skills + Agents + State」的 Claude Code 内部编排层。
- ClawTeam 以文件系统为真相源（`~/.clawteam/`），不内置常驻协调服务；任务状态用 pending/in_progress/completed/blocked 和 blocked-by 表达，通信用 inbox send/receive/broadcast。
- 驱动方式不是轮询模型内部状态，而是在 spawn 初始提示中注入身份、任务、协作协议和 worker loop，让 Agent 自己调用 CLI 子命令。
- `Agent_副本.xmind`：多 Agent 协作的早期形态是「现实多人协作的类比」，Reflection 由另一个 Agent 审查相当于 code review。

## Examples

- worker 各自持有独立 git worktree、独立 tmux 窗口、独立身份，减少并行改代码冲突（ClawTeam）。
- oh-my-claude-code 的典型流程链：explore → analyst → planner → critic → executor → verifier，并用 `.omc/` state 在上下文压缩后保持连续性。

## Common Confusions

- 多 Agent ≠ 更快更强；缺任务边界和合并协议时只会增加编排成本。
- 「中心化编排者」不是唯一模式；自主团队可以让 Agent 直接认领任务、标记依赖、解决冲突（见 [[concepts/复合工程（Compound Engineering）|复合工程]] 提到的自主团队阶段）。
- 通信协议和状态真相源是两件事：inbox 解决「怎么传」，文件系统/看板解决「真相在哪」。

## Evidence

- [[sources/Agent/多智能体.xmind|多智能体.xmind]]
- [[sources/Agent/Agent 解构.xmind|Agent 解构.xmind]]
- [[sources/Agent/Agent_副本.xmind|Agent_副本.xmind]]

## Relations

- part-of: [[concepts/AI Agent|AI Agent]]
- enables: [[concepts/子代理委派模式|子代理委派模式]]
- contains: [[concepts/Agent MessageBus|Agent MessageBus]]
- implemented-by: [[entities/ClawTeam|ClawTeam]]
- implemented-by: [[entities/oh-my-claude-code|oh-my-claude-code]]
- related: [[synthesis/GitHub 驱动的 Agent 开发闭环|GitHub 驱动的 Agent 开发闭环]]
- map-entry: [[maps/Agent 学习地图|Agent 学习地图]]
- entity-candidate: paperclip
- entity-candidate: ruflo

## My Understanding

当前理解：多 Agent 能不能用，取决于五件事是否到位——任务依赖、通信、隔离 worktree、状态真相源、观测与交叉验证；少一件，多个 Agent 就从团队退化成噪声。

## Review Questions

- 多 Agent 协作需要哪些控制面？
- ClawTeam 和 oh-my-claude-code 的协作模型差异是什么？
- 为什么 worktree 隔离对并行 Agent 重要？

## Open Questions

- 自主多 Agent 协作的收益与编排成本缺少稳定量化证据。
