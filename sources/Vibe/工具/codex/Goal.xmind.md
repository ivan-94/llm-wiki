---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/工具/codex/Goal.xmind"
source_relpath: "Vibe/工具/codex/Goal.xmind"
raw_created_at: 2026-05-12T03:31:20.191861+00:00
raw_modified_at: 2026-05-12T03:39:20.716378+00:00
raw_size: 4392710
raw_fingerprint: "size=4392710;birth=2026-05-12T03:31:20.191861+00:00;mtime=2026-05-12T03:39:20.716378+00:00"
raw_snapshot_at: 2026-05-29T16:06:16.180406+00:00
ingested_at: 2026-05-30
status: ingested
---

# Goal.xmind

## Source

- Raw file: [Vibe/工具/codex/Goal.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/%E5%B7%A5%E5%85%B7/codex/Goal.xmind>)
- Raw ref: `raw:Vibe/工具/codex/Goal.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2026-05-12T03:31:20.191861+00:00`; modified `2026-05-12T03:39:20.716378+00:00`; size `4392710`; snapshot `2026-05-29T16:06:16.180406+00:00`
- Coverage: XMind helper exported all sheets; `sheet_count=1`; sheet `0` titled `画布 1` with 108 topics.

## Summary

这份 XMind 把 Goal Mode 定义为面向 AI Agent 的持续迭代闭环：Agent 执行动作、对结果打分、判断是否达成目标，未达成则继续循环。source 的核心建议是用清晰可量化目标、紧密反馈回路和 Markdown 外部记忆，解决 Agent 不知道何时停止、反馈过慢和长期运行记忆不稳定的问题。

## Source Digest

source 将 Goal Mode 从“给模型一个任务”提升为“设计一个闭环系统”。闭环是否有效，关键不在 prompt 文案多漂亮，而在目标是否可测、反馈是否足够快、历史是否可持久化。模糊目标会导致过早停止或无休止乱改；可量化目标需要明确对象、指标、约束和验证方式，并可转成 checklist。反馈回路越紧，Agent 越能快速判断一次修改是否变好，因此可以通过小模型、子采样数据集、快速验证环境和低成本评分压缩迭代时间。

长期运行时，source 主张不要让 Agent 只依赖上下文记忆，而要把计划、实验结果和实时思考写入文件系统。PLAN.md 承载高层路线，EXPERIMENTS.md 记录实验及成败原因，EXPERIMENT_NOTES.md 保存时间序列思考，三者共同扩展 Agent 的长期工作记忆。最终工作流是先定义量化目标，再建立快速反馈机制，随后提供外部记忆并持续循环，直到可验证目标达成后停止。

## Key Claims

- explicit: Goal Mode 是一个执行动作、评分结果、判断目标、未达成继续循环的 Agent 持续迭代系统。
- explicit: Goal Mode 的核心挑战是“什么时候算完成”。
- explicit: 好目标需要明确对象、可衡量指标、约束条件和可验证结果，否则容易过早停止或无限循环。
- explicit: 紧密反馈回路要求 Agent 快速知道一次修改是否变好，可通过更快测试、小模型、子采样数据集、快速验证环境和降低运行成本实现。
- explicit: PLAN.md、EXPERIMENTS.md 和 EXPERIMENT_NOTES.md 可作为 Goal Mode 的外部记忆，其中 EXPERIMENTS.md 记录实验、结果和成败原因。
- explicit: Prompt 在 Goal Mode 中不只是提要求，而是在设计清晰目标、快速反馈和持久化记忆组成的闭环系统。
- inferred: 这份 source 适合支撑“Agent 闭环”和“目标驱动执行”概念页，而不是只作为 Codex 某个功能的用法说明。

## External Links

- reference-source: [Chris Hayduk post on X](https://x.com/ChrisHayduk/status/2053807198870880743) — root topic links Goal Mode discussion; not verified.

## Links

- compiled-concept candidate: [[concepts/Goal Mode|Goal Mode]] — 可提炼目标、评分、停止条件和持续迭代循环。
- compiled-concept candidate: [[concepts/Agent 反馈回路|Agent 反馈回路]] — 可补充快速反馈、评分质量和迭代成本之间的关系。
- compiled-concept candidate: [[concepts/Agent 外部记忆|Agent 外部记忆]] — 可沉淀 PLAN.md、EXPERIMENTS.md、EXPERIMENT_NOTES.md 的角色分工。
- map-entry candidate: [[maps/Vibe Coding 学习地图|Vibe Coding 学习地图]] — 可作为长任务、自动化研究和 Codex Goal 工作流主题入口。

## Maintenance Notes

- XMind helper 成功导出全部 1 个 sheet。
- 原始 X 链接未联网核验；只记录为 source 中可提取外链。
- source 中三种 Markdown 文件的第三层节点有空标题占位，但有效子节点可读，不影响 ingest。
