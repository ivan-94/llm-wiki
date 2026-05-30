---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 3
learning_status: new
confidence: 2
difficulty: 3
review_after: 2026-06-10
---

# 反馈工程（Feedback Engineering）

## Definition

反馈工程是把 Agent 的执行结果与预期目标之间的差距压缩成可循环的信号——通过设计可量化目标、快速反馈机制和外部记忆，让 Agent 知道何时完成、在哪里失败、以及下一步应如何调整。

## Why It Matters

Agent 最常见的失控模式是"不知道何时算完成"或"改了但不知道变好还是变坏"。反馈工程解决的不是模型能力问题，而是**信号设计问题**：如果没有可测目标和紧密反馈，再好的模型也会漫无目的地循环或过早停止。

## Mental Model

把 Agent 看作控制系统：Feedback Engineering 是这个控制系统的传感器层，决定控制回路的响应速度和精确度。

```
目标定义 → 执行 → 打分 → 偏差检测 → 调整 → 继续/停止
```

## Key Claims

- 好目标需要明确对象、可衡量指标、约束条件和可验证结果；模糊目标导致过早停止或无限循环。
- 反馈回路越紧，迭代越快：可通过更快测试、小模型替代、子采样数据集、快速验证环境压缩迭代成本。
- 长期运行的 Agent 应把计划、实验结果和思考写入文件系统（PLAN.md / EXPERIMENTS.md），而不是只依赖上下文记忆。
- 评分函数本身也是设计对象：过软的评分会掩盖问题，过硬的评分会阻碍进展。
- 反馈工程与 [[concepts/Agent Harness|Agent Harness]] 紧密耦合：harness 提供工具和约束，反馈工程提供判断"做得好不好"的机制。

## Examples

- Codex Goal Mode：Agent 执行动作 → 打分 → 判断目标是否达成 → 未达成则继续迭代。
- TDD 中的测试套件：绿灯/红灯是最简单的二值反馈信号，让 Agent 知道修改是否变好。
- HAT（Hand Acceptance Test）：用户路径验收作为最终反馈，补充自动化测试无法覆盖的语义边界。

## Common Confusions

- 反馈工程 ≠ 评估（Evaluation）：评估通常是离线的、批量的；反馈工程关注在线的、实时的、可循环的信号。
- 测试通过 ≠ 反馈充分：测试只验证当前实现能通过 happy path，不能证明语义正确、路径收敛或反例失败——这是 L4 证据机制的核心风险。
- 目标越具体不等于越好：过于细化的目标会让 Agent "局部过拟合"，忽略意图层（L0）的更高目标。

## Evidence

- [[sources/Vibe/工具/codex/Goal.xmind|Goal.xmind]] — Goal Mode 明确定义可量化目标、紧密反馈回路和外部记忆的三要素。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/diagnose.png|diagnose.png]] — `/diagnose` 六阶段把反馈闭环（复现→假设→仪器化→修复→回归）明确化。
- [[sources/Vibe/Vibe Coding 随手记/大规模 AI Coding/大型需求的偏移根因与控制.xmind|大型需求的偏移根因与控制]] — 支撑反馈不足导致偏移的机制分析。

## Relations

- part-of: [[concepts/Agent Harness|Agent Harness]] — 反馈信号是 harness 控制面的组成部分。
- enables: [[concepts/Agent 反馈回路|Agent 反馈回路]] — 反馈工程是反馈回路的设计视角。
- related: [[concepts/Agentic Engineering|Agentic Engineering]] — 反馈工程是 Agentic Engineering 的 L4 证据层核心机制。
- implemented-by: [[entities/Codex|Codex]] — Codex Goal Mode 是反馈工程的具体实现案例。
- map-entry: [[maps/Vibe Coding 工具地图|Vibe Coding 工具地图]]

## My Understanding

反馈工程的精髓是"让 Agent 自己知道做得好不好"——不是通过更多 prompt 告诉它该怎么做，而是通过更好的信号设计让它能自我校正。

## Review Questions

- 为什么模糊目标会导致 Agent 过早停止或无限循环？
- PLAN.md / EXPERIMENTS.md 作为外部记忆，主要解决什么问题？
- 反馈工程和传统 LLM 评估（Evaluation）的核心区别是什么？
- 紧密反馈回路有哪些常见的工程手段？

## Open Questions

- 多 Agent 协作场景下，反馈信号如何在 sub-agent 与父 agent 之间传递而不损耗精度？
