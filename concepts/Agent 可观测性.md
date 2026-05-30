---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 4
learning_status: new
confidence: 2
difficulty: 4
review_after: 2026-06-06
---

# Agent 可观测性

## Definition

Agent 可观测性是把 Agent 的输入、计划、工具调用、环境状态、错误、日志、截图、测试结果和人工反馈组织成可读证据，使人类和后续 Agent 能复盘它为什么这样做。

## Why It Matters

Agent 失败时，只有最终 diff 不够。没有轨迹和环境证据，就无法判断是上下文缺失、工具错误、权限问题、目标误解还是测试过拟合。

## Mental Model

可观测性是给 Agent 执行过程装仪表盘和黑匣子。

## Key Claims

- 浏览器截图、日志、测试、错误消息和 HAT artifacts 都是 Agent 可读反馈。
- 多 Agent 并发时，可观测性还包括任务板、收件箱、worktree、tmux/session 和状态文件。
- 好的可观测性要能进入下一轮行动，而不是只给人看。

## Evidence

- [[sources/Vibe/Harness Engineering.xmind|Harness Engineering.xmind]]
- [[sources/Vibe/Vibe Coding 随手记/Harness/Harness 循环1.png|Harness 循环1]]
- [[sources/Vibe/Vibe Coding 随手记/Harness/浏览器兼容性测试.xmind|浏览器兼容性测试]]
- [[sources/Agent/多智能体.xmind|多智能体]]

## Relations

- part-of: [[concepts/Agent Harness|Agent Harness]]
- supports: [[concepts/反捷径证据|反捷径证据]]
- used-in: [[synthesis/Vibe Coding 工程化深度模型|Vibe Coding 工程化深度模型]]

## My Understanding

当前理解：Agent 可观测性不是监控大盘，而是让 Agent 行为有可回放、可比较、可修正的证据。

## Review Questions

- 为什么最终代码 diff 不是足够的 Agent 证据？
- 哪些观测信号最适合自动回写成 harness 改进？

## Open Questions

- 还缺少生产环境 Agent 观测指标的真实案例。
