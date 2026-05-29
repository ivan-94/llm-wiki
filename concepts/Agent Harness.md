---
page_type: concept
updated_at: 2026-05-29
status: active
source_count: 9
learning_status: new
confidence: 2
difficulty: 4
review_after: 2026-06-05
---

# Agent Harness

## Definition

Agent Harness 是围绕 Agent 的执行环境、上下文入口、权限、工具、反馈、验证和观测所构成的工程控制面。

## Why It Matters

Agent 能力越强，越需要 harness 把它限制在可理解、可恢复、可验证的轨道上。没有 harness，Vibe Coding 容易变成一次性生成和人工救火。

## Mental Model

Harness = empower + constrain：给 Agent 足够能力，同时给它边界、仪表盘和验收门。

## Key Claims

- Harness 的目标不是让 Agent 少做事，而是让 Agent 做事时更可控、更可观测、更容易复盘。
- Harness 循环包括收集轨迹、识别失败、优化上下文/工具/权限/测试，再把改进写回 workflow。
- Skills、AGENTS/CLAUDE、hooks、MCP、browser/test tools、worktree 和 HAT 都可以是 harness 组件。
- 浏览器兼容性测试和 HAT 证据让 Agent 不只通过单元测试，还能接近用户路径验收。

## Examples

- `Harness = EMPOWER + CONSTRAIN` 将 harness 拆成赋能和约束两侧。
- `Harness 循环1/2` 用图示表达持续优化闭环。
- `浏览器兼容性测试.xmind` 将 Selenium、云测试和截图证据纳入 Agent 验收。
- `为 Agents 构造并发执行环境` 把隔离 worktree、运行时和 agent task 分派视为 harness。

## Common Confusions

- Harness 不是单个脚本或工具，而是一组环境、协议和反馈机制。
- 增加工具不一定提高质量；工具需要配合权限、上下文和验收标准。

## Evidence

- [[sources/Vibe/Harness Engineering.xmind|Harness Engineering.xmind]]
- [[sources/Vibe/Vibe Coding 随手记/Harness/Agent Harness Engineering.xmind|Agent Harness Engineering]]
- [[sources/Vibe/Vibe Coding 随手记/Harness/Harness = EMPOWER + CONSTRAIN.xmind|Harness = EMPOWER + CONSTRAIN]]
- [[sources/Vibe/Vibe Coding 随手记/Harness/Harness 循环1.png|Harness 循环1]]
- [[sources/Vibe/Vibe Coding 随手记/Harness/Harness 循环2.png|Harness 循环2]]
- [[sources/Vibe/Vibe Coding 随手记/Harness/浏览器兼容性测试.xmind|浏览器兼容性测试]]

## Relations

- enables: [[concepts/Vibe Coding|Vibe Coding]]
- enables: [[concepts/Agentic Engineering|Agentic Engineering]]
- includes: [[concepts/Agent Skills|Agent Skills]]
- map-entry: [[maps/Vibe Coding 学习地图|Vibe Coding 学习地图]]
- map-entry: [[maps/Vibe Coding 工具地图|Vibe Coding 工具地图]]

## My Understanding

当前理解：Agent Harness 是把 Agent 的“能力”转成“可靠交付”的中间层。

## Review Questions

- Harness 为什么同时要 empower 和 constrain？
- Harness 循环中哪些输入最适合用于改进？
- 浏览器/HAT 证据为什么属于 harness？

## Open Questions

- 还需要对不同工具链的 harness 成本做横向比较。
