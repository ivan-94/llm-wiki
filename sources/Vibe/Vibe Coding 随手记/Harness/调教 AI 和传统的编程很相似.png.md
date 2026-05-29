---
source_type: image
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/Vibe Coding 随手记/Harness/调教 AI 和传统的编程很相似.png"
source_relpath: "Vibe/Vibe Coding 随手记/Harness/调教 AI 和传统的编程很相似.png"
raw_created_at: 2026-05-11T00:28:35.701619+00:00
raw_modified_at: 2026-05-11T00:28:37.861275+00:00
raw_size: 1699244
raw_fingerprint: "size=1699244;birth=2026-05-11T00:28:35.701619+00:00;mtime=2026-05-11T00:28:37.861275+00:00"
raw_snapshot_at: 2026-05-29T15:54:58.732146+00:00
ingested_at: 2026-05-29
status: ingested
---

# 调教 AI 和传统的编程很相似.png

## Source

- Raw file: [Vibe/Vibe Coding 随手记/Harness/调教 AI 和传统的编程很相似.png](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/Vibe%20Coding%20%E9%9A%8F%E6%89%8B%E8%AE%B0/Harness/%E8%B0%83%E6%95%99%20AI%20%E5%92%8C%E4%BC%A0%E7%BB%9F%E7%9A%84%E7%BC%96%E7%A8%8B%E5%BE%88%E7%9B%B8%E4%BC%BC.png>)
- Raw ref: `raw:Vibe/Vibe Coding 随手记/Harness/调教 AI 和传统的编程很相似.png`
- Type: image
- Status: ingested
- Raw metadata: created `2026-05-11T00:28:35.701619+00:00`; modified `2026-05-11T00:28:37.861275+00:00`; size `1699244`; snapshot `2026-05-29T15:54:58.732146+00:00`
- Coverage: opened with Agent vision at original resolution; image dimensions are `1055x1491`; all visible sections, comparison table, three-layer structure, key concept cards, and summary statement were inspected.

## Summary

这张信息图把 Vibe Coding / Agentic Coding 解释为传统软件工程对象的扩展：代码没有消失，但“工程化对象”从代码本身扩展到 agent 的行为系统，包括 skills、rules、hooks、context、workflow、debug trace、guardrails 和评审测试。核心判断是：调教 AI 不是摆脱工程化，而是把工程化约束迁移到 agent 行为层。

## Source Digest

图片先给出核心观点：写代码的重心正在从手写实现转向设计约束、抽象流程和沉淀可复用能力；代码更像 agent 执行后的产物，真正的工程判断体现在 skills、rules、hooks、context 和 workflow 上。AGENTS.md / CLAUDE.md 被类比为全局变量与全局函数，因为它们全局可见并影响默认行为。

中部表格把传统开发对象映射到 Agentic/Vibe Coding 对象：函数/类/模块对应 skills；函数组合/模块组合对应 skills composition；全局变量/全局函数/框架约定对应 AGENTS.md、CLAUDE.md 和 global instructions；lint/type check/test 对应 hooks、guardrails、evals、policy checks；debugger/breakpoint 对应观察 agent trace、tool calls 和中间产物；refactor 对应抽取通用 skill、改写 instruction、简化 workflow；runtime bug 对应 agent 偏航、tool misuse 和 context 污染；“先写起来再说”对应高权限 Vibe Mode；工程化交付对应受约束 Agent Mode + review + tests + hooks。

下半部分提出三层工程化结构：自由探索层负责用较大权限快速生成、迁移、重构、试错，追求速度与流动性；约束收敛层用 tests、lint、typecheck、hooks、review prompt、diff inspection 把结果拉回可靠区间；经验固化层把反复出现的问题抽成 skills，把反复的错写进 rules，把危险行为放进 hooks，把复杂流程沉淀成 workflow。关键概念卡进一步定义了 skills、instructions、hooks/guardrails 和 debug trace 在行为系统中的角色。

## Key Claims

- explicit: Vibe Coding / Agentic Coding 的一句话定位是“代码没有消失，而是复用与约束的对象，从代码实现扩展到了 Agent 行为系统”。
- explicit: 写代码的重心正在从手写实现转向设计约束、抽象流程和沉淀可复用能力。
- explicit: Skills 被类比为函数：可复用、可组合，也能约束复杂流程。
- explicit: AGENTS.md / CLAUDE.md 被类比为全局变量与全局函数：全局可见，影响默认行为。
- explicit: 传统软件开发中的函数、组合、全局约定、lint/test、debugger、refactor、runtime bug、快速试写和工程交付，都可映射到 agentic coding 中的 skills、composition、instructions、hooks/evals、trace、workflow、context 污染、高权限模式和受约束交付模式。
- explicit: 三层工程化结构包括自由探索层、约束收敛层和经验固化层。
- explicit: Debug Trace 通过观察运行轨迹来修正 agent 偏移，hooks/guardrails 通过运行时保护防止极端错误。
- inferred: 这张图把 Vibe Coding 从“写提示词”提升为“设计和维护 agent 行为系统”的工程范式。
- inferred: 高权限探索模式需要与 tests、review、hooks、diff inspection 等收敛机制配套，否则容易把速度优势转化为不可靠输出。

## External Links

No external links found in extracted content.

## Links

- compiled-concept: [[concepts/Vibe Coding|Vibe Coding]] — 本 source 可支撑 Vibe Coding 与传统软件工程对象的映射关系。
- related: Agent 行为系统 — 本 source 明确把 skills、instructions、hooks、context、workflow 和 trace 视为工程化对象。
- related: Agent Guardrails — 本 source 可补充 hooks、policy checks、evals 和运行时保护的作用。
- map-entry: [[maps/Vibe Coding 学习地图|Vibe Coding 学习地图]] — 可作为 Vibe/Agentic Coding 基础心智模型入口。

## Maintenance Notes

- 视觉内容清晰，未发现外链。
- “调教 AI 和传统的编程很相似”是用户给定 raw 文件名；图片标题实际为“Vibe Coding / Agentic Coding 信息图”。
