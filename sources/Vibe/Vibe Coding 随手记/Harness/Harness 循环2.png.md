---
source_type: image
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/Vibe Coding 随手记/Harness/Harness 循环2.png"
source_relpath: "Vibe/Vibe Coding 随手记/Harness/Harness 循环2.png"
raw_created_at: 2026-05-13T11:11:03.249088+00:00
raw_modified_at: 2026-05-13T11:11:03.250486+00:00
raw_size: 1494749
raw_fingerprint: "size=1494749;birth=2026-05-13T11:11:03.249088+00:00;mtime=2026-05-13T11:11:03.250486+00:00"
raw_snapshot_at: 2026-05-29T15:53:55+00:00
ingested_at: 2026-05-29
status: ingested
---

# Harness 循环2.png

## Source

- Raw file: [Vibe/Vibe Coding 随手记/Harness/Harness 循环2.png](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/Vibe%20Coding%20%E9%9A%8F%E6%89%8B%E8%AE%B0/Harness/Harness%20%E5%BE%AA%E7%8E%AF2.png>)
- Raw ref: `raw:Vibe/Vibe Coding 随手记/Harness/Harness 循环2.png`
- Type: image
- Status: ingested
- Raw metadata: created `2026-05-13T11:11:03.249088+00:00`; modified `2026-05-13T11:11:03.250486+00:00`; size `1494749`; snapshot `2026-05-29T15:53:55+00:00`
- Coverage: opened with Agent vision; full infographic inspected; dimensions `1055x1491`; visible text is clear enough for source note.

## Summary

这张图是“调教 Harness: 从写代码到优化 Agent 运行环境”的第一页，解释为什么需要 harness 循环：Agent 行为不透明、模型不是问题根源、可控性来自环境设计、Agent 自我优化能力还弱。它给出核心工作流：运行 Agent、观察行为、优化环境、再次运行，形成持续迭代。

## Source Digest

图把 harness 循环的必要性放在四个问题上：Agent 的文件读取、工具使用、推理和遇阻过程不透明；真正影响效果的常常是信息、工具、规范、上下文组织和引导方式，而不是模型本身；可控性来自 harness 的环境设计；Agent 目前还不擅长自己写好 skills、优化自身流程，因此仍需要人类持续介入。

核心工作流是一个四步循环：先在 harness 中运行 Agent 执行真实任务；再观察它读了哪些文件、用了哪些工具、遇到哪些阻塞、做了哪些错误判断；随后基于问题优化 Skills、Agents.md、工具、规范和上下文组织；最后重新运行 Agent，进入下一轮循环。这个循环的目标不是一次性写完代码，而是持续优化 Agent 的行为与执行质量。

图还列出可优化对象：`Skills` 负责整理领域知识、最佳实践和解决方案模板，帮助 Agent 理解与执行；`Agents.md` 定义角色、目标、工作方式、行为准则和约束；`Tools` 提供更强大、更准确、更易用的能力接口；`规范与建议` 提供规则、案例约束、风格指南和注意事项，减少歧义与错误。思维范式从“写代码 -> 跑程序 -> debug -> 重构 -> 更好的代码”转向“编写 Skills/规则/工具 -> 运行 Agent -> 观察轨迹 -> 优化 Harness -> 更可控的 Agent 行为”。

## Key Claims

- explicit: 需要 harness 循环，因为 Agent 行为不透明，需要观察它如何读文件、用工具、推理以及遇到阻塞。
- explicit: 模型不是问题的根源；真正影响效果的是信息、工具、规范、上下文组织和引导方式。
- explicit: 可控性来自环境设计，可以通过优化 harness 缩小不确定性，让 Agent 更可靠地完成任务。
- explicit: harness 循环的四步是运行 Agent、观察行为、优化环境、再次运行。
- explicit: 可优化对象包括 Skills、Agents.md、Tools、规范与建议。
- explicit: 新范式从写代码/debug/重构转向编写 Skills/规则/工具、运行 Agent、观察轨迹、优化 Harness。
- inferred: 这张图把 harness 从静态配置推进为持续迭代流程，适合支撑“AI Coding 验证闭环”或“Agent Harness 工程化框架”。
- inferred: source 暗示有效的 Vibe Coding 需要 trace 或操作轨迹作为反馈输入，而不只是评审最终 diff。

## External Links

No external links found in extracted content.

## Links

- compiled-concept: [[concepts/Agent Harness|Agent Harness]] — 可提供 harness 循环和可优化对象。
- related: Agent 行为塑形 — 图中强调通过观察和环境设计塑造 Agent 行为。
- related: Agent Harness 工程化框架 — 可与 Harness 循环1 和 XMind sources 共同综合成闭环模型。
- map-entry: [[maps/Vibe Coding 学习地图|Vibe Coding 学习地图]] — 可作为从“写代码”转向“调教运行环境”的学习入口。

## Maintenance Notes

- 图片视觉清晰；没有明显 URL。
- raw 文件名为“循环2”，但图片正文标注“图一”；后续排序或展示时应以 source note 的 raw 文件名为准，并可在综合页里注明原图编号。
