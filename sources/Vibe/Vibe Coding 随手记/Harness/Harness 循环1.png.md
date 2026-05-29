---
source_type: image
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/Vibe Coding 随手记/Harness/Harness 循环1.png"
source_relpath: "Vibe/Vibe Coding 随手记/Harness/Harness 循环1.png"
raw_created_at: 2026-05-13T11:11:05.895216+00:00
raw_modified_at: 2026-05-13T11:11:05.896917+00:00
raw_size: 1680542
raw_fingerprint: "size=1680542;birth=2026-05-13T11:11:05.895216+00:00;mtime=2026-05-13T11:11:05.896917+00:00"
raw_snapshot_at: 2026-05-29T15:53:55+00:00
ingested_at: 2026-05-29
status: ingested
---

# Harness 循环1.png

## Source

- Raw file: [Vibe/Vibe Coding 随手记/Harness/Harness 循环1.png](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/Vibe%20Coding%20%E9%9A%8F%E6%89%8B%E8%AE%B0/Harness/Harness%20%E5%BE%AA%E7%8E%AF1.png>)
- Raw ref: `raw:Vibe/Vibe Coding 随手记/Harness/Harness 循环1.png`
- Type: image
- Status: ingested
- Raw metadata: created `2026-05-13T11:11:05.895216+00:00`; modified `2026-05-13T11:11:05.896917+00:00`; size `1680542`; snapshot `2026-05-29T15:53:55+00:00`
- Coverage: opened with Agent vision; full infographic inspected; dimensions `1055x1491`; visible text is clear enough for source note.

## Summary

这张图是“调教 Harness: 从写代码到优化 Agent 运行环境”的第二页，重点用“传统软件工程”和“AI 原生工程”的类比说明 harness runtime 的位置，并列出构建 Agent 操作系统所需的 Agents.md、Skills、Tools、规范/建议等组件，以及新的工程能力栈和价值。

## Source Digest

图的上半部分把传统软件工程链路 `Code -> Compiler -> Binary` 类比为 AI 原生工程链路 `Skills / Rules / Tools -> Harness Runtime -> Agent Behavior`。它强调本质变化是从确定性系统转向概率性系统：传统编译器追求逻辑正确性，而 agent harness 需要通过环境约束、组织引导和反馈驱动来塑造行为。

中间部分把正在构建的东西称为 Agent 的“操作系统”：`Agents.md` 像 config + policy，定义角色、目标、规则与约束；`Skills` 像 library，提供知识、经验和解决方案；`Tools` 像 syscall，提供能力接口并扩展 Agent 边界；`规范 & 建议` 像 guardrails，减少跑偏并约束输出质量；这些共同组成 `Harness Runtime`，类似 OS/Runtime，负责整合和调度并驱动 Agent 执行任务。

图还列出新的工程能力栈：Context Engineering 负责组织信息让 Agent 看得懂；Tool Orchestration 负责设计和组合工具提升执行力；Agent Behavior Shaping 负责引导 Agent 做对的事；Runtime Observability 负责观察、追踪、分析 Agent 行为；Workflow Control 负责设计流程、反馈与迭代机制。关键价值包括更可控、更稳定、更高效、更可扩展和可持续进化。

## Key Claims

- explicit: AI 原生工程中的 `Skills / Rules / Tools` 对应新的“代码”，`Harness Runtime` 对应运行时/编译器，输出是 Agent behavior。
- explicit: 本质变化是从确定性系统转向概率性系统，Agent 行为需要环境约束、组织引导和反馈驱动。
- explicit: Agent 的“操作系统”由 Agents.md、Skills、Tools、规范与建议组成，并汇入 Harness Runtime。
- explicit: 新的工程能力栈包括 Context Engineering、Tool Orchestration、Agent Behavior Shaping、Runtime Observability 和 Workflow Control。
- explicit: 优秀 AI Coding 的关注点不只是写好业务代码，而是设计好 Agent 的运行环境。
- inferred: 这张图可作为 Agent Harness 概念中的 runtime 心智模型图，解释为什么规则、skills 和工具不是附属物，而是行为生成链路的一部分。
- inferred: 图中“概率性系统”的说法适合与验证闭环、观测性和反馈驱动形成 synthesis。

## External Links

No external links found in extracted content.

## Links

- compiled-concept candidate: [[concepts/Agent Harness|Agent Harness]] — 可提供从代码到 harness runtime 的类比和组件结构。
- compiled-concept candidate: [[concepts/Agent Runtime|Agent Runtime]] — 可补充 Agent 操作系统、runtime、syscall/library/config 的比喻。
- compiled-concept candidate: [[concepts/Agent 可观测性|Agent 可观测性]] — 图中明确列出 runtime observability 作为新工程能力。
- map-entry candidate: [[maps/Vibe Coding 学习地图|Vibe Coding 学习地图]] — 可纳入 AI coding 从写代码转向优化运行环境的学习路径。

## Maintenance Notes

- 图片视觉清晰；没有明显 URL。
- raw 文件名为“循环1”，但图片正文标注“图二”；后续排序或展示时应以 source note 的 raw 文件名为准，并可在综合页里注明原图编号。
