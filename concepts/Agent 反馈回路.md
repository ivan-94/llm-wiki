---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 3
learning_status: new
confidence: 2
difficulty: 4
review_after: 2026-06-06
---

# Agent 反馈回路

## Definition

Agent 反馈回路是 Agent 执行动作、观察结果、评分或验证、调整计划并继续迭代的闭环机制。

## Why It Matters

复杂任务无法靠一次生成完成。反馈回路决定 Agent 是盲目继续，还是能基于测试、日志、评分、人类反馈和外部记忆逐步收敛。

## Mental Model

目标 + 行动 + 评分 + 记忆 = 可持续迭代。

## Key Claims

- 好目标需要对象、指标、约束和可验证结果。
- 反馈越快，Agent 越能降低单次尝试成本并快速修正方向。
- 长任务应把计划、实验和实时思考写入文件系统，而不是只依赖上下文窗口。
- 反馈回路应能沉淀为规则、测试、skill、hook 或 runtime 约束。

## Evidence

- [[sources/Vibe/工具/codex/Goal.xmind|Goal.xmind]]
- [[sources/Vibe/Harness Engineering.xmind|Harness Engineering.xmind]]
- [[sources/Vibe/Vibe Coding 随手记/Harness/Harness 循环2.png|Harness 循环2]]

## Relations

- part-of: [[concepts/Agent Harness|Agent Harness]]
- enables: [[concepts/Agent 可观测性|Agent 可观测性]]
- used-in: [[synthesis/Vibe Coding 工程化深度模型|Vibe Coding 工程化深度模型]]

## My Understanding

当前理解：反馈回路把 Agent 从“执行一次”变成“能自己发现偏差并继续收敛”。

## Review Questions

- 什么样的目标适合 Goal Mode？
- 为什么长期运行需要外部记忆文件？

## Open Questions

- Goal Mode 的真实产品状态和命令细节未核验。
