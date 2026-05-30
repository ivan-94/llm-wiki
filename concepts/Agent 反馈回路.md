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

## Harness Loop Four Steps

Harness 的反馈回路在 Agent 反馈回路上增加了工程化层：
1. **Collect**：收集 Agent 执行的日志、测试报告、HAT 结果和 review 反馈。
2. **Identify**：分析失败来自哪个控制点缺失（上下文、工具、权限、验收标准）。
3. **Optimize**：把改进写入 AGENTS/CLAUDE、skill、hook、linter 或 runtime 约束。
4. **Embed**：让改进自动生效，下次不需要人工重新提醒。

## Long-Task Entry Points

长时间运行任务需要特殊的反馈回路设计：
- **Goal Mode / `/ralph-loop`**：通过 CLI 或 task runner 启动可持续循环，直到目标达成或超时。
- 长任务应把计划、实验状态和实时思考写入文件系统（不只依赖上下文窗口）。
- 中间检查点（checkpoint）让人类在不中断任务的情况下观察进度。

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
