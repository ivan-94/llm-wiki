---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 3
learning_status: new
confidence: 2
difficulty: 3
review_after: 2026-06-06
---

# Agent 全局记忆

## Definition

Agent 全局记忆是跨会话、跨任务保留的项目事实、用户偏好、工作流约定、环境入口和验证规则。

## Why It Matters

没有全局记忆，每次 Agent 都要重新探索项目；有全局记忆，重复踩坑可以变成长期约束，后续会话能复用前人的路径。

## Mental Model

全局记忆是 Agent 的长期项目导航图。

## Key Claims

- 全局记忆应保存稳定事实，不应塞入易漂移的临时状态。
- AGENTS.md、CLAUDE.md、MEMORY.md、docs、skills 和 maps 都可以承担全局记忆的一部分。
- 有效全局记忆需要索引和边界，否则会变成上下文噪声。

## Evidence

- [[sources/Vibe/Spec/AGENTS.md 全局记忆.xmind|AGENTS.md 全局记忆]]
- [[sources/Vibe/Harness Engineering.xmind|Harness Engineering.xmind]]
- [[sources/Agent/变体/Hermes.xmind|Hermes]]

## Relations

- implemented-by: [[concepts/AGENTS.md 设计模式|AGENTS.md 设计模式]]
- part-of: [[concepts/上下文工程|上下文工程]]
- related: [[concepts/Agent 记忆|Agent 记忆]]

## My Understanding

当前理解：全局记忆不是“记住所有东西”，而是把稳定、可复用、可验证的上下文放到下一次任务能找到的位置。

## Review Questions

- 全局记忆和会话记忆有什么差别？
- 哪些信息不应该进入全局记忆？

## Open Questions

- 全局记忆的自动更新和过期机制还需要更多实践证据。
