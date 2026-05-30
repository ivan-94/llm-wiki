---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/Vibe Coding.xmind"
source_relpath: "Vibe/Vibe Coding.xmind"
raw_created_at: 2025-09-23T23:06:25.200539+00:00
raw_modified_at: 2025-09-28T07:09:54.335934+00:00
raw_size: 2460520
raw_fingerprint: "size=2460520;birth=2025-09-23T23:06:25.200539+00:00;mtime=2025-09-28T07:09:54.335934+00:00"
raw_snapshot_at: 2026-05-29T16:02:55.149572+00:00
ingested_at: 2026-05-30
status: ingested
---

# Vibe Coding.xmind

## Source

- Raw file: [Vibe/Vibe Coding.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/Vibe%20Coding.xmind>)
- Raw ref: `raw:Vibe/Vibe Coding.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2025-09-23T23:06:25.200539+00:00`; modified `2025-09-28T07:09:54.335934+00:00`; size `2460520`; snapshot `2026-05-29T16:02:55.149572+00:00`
- Coverage: helper exported all sheets. Sheet count: 1. Sheets: `d` (index 0, 98 topics).

## Summary

这份 XMind 为 Vibe Coding 建立入门框架：先定义“氛围编程”，再把它与更结构化的 AI Assisted Engineering 区分开，最后列出上下文、规划、文档、视觉输入、测试、调试指令、TDD、任务管理与上下文工程等实践要点。

## Source Digest

source 认为 Vibe Coding 是一种依赖高层次提示、接受 AI 建议、关注整体“氛围”而非实现细节的轻量开发方式。它能快速推进功能应用的前 70%，但最后 30% 会暴露工程知识不足：修一个 bug 引入其他 bug、维护性和安全性隐藏成本、初学者收益递减，以及数据库凭据泄露等安全风险。

材料把更成熟的方向命名为 AI Assisted Engineering：保留 Vibe Coding 的创造力，但加入规格、严谨性和人机协作。它要求开发者仍能评估 AI 输出、引导 AI、验证结果，并认识到高级 AI 与技术/非技术人员组合会带来能力扩展、开发流程重排、新信任模型和软件民主化。

实践部分强调“上下文就是一切”：相关代码、架构设计、错误日志、期望输出、约束和需求会直接决定 AI 输出质量。推荐工作流包括先规划再编码、提供正确且最新的文档、用 Figma/截图/浏览器等视觉上下文辅助前端开发、小步测试、调试前明确目标与报错、使用 TDD，以及用 claude-task-master、RooCode、vibe-kanban 等工具管理复杂任务。最后，source 把上下文工程描述为从静态 prompt 转向动态信息组装的信息系统。

## Key Claims

- explicit: Vibe Coding 能快速实现功能雏形，但如果缺少工程能力，后续修复、维护、安全和验证成本会显著上升。
- explicit: AI Assisted Engineering 比 Vibe Coding 更结构化，强调规格、严谨性、人机协作、可维护性和安全性。
- explicit: AI 输出质量与上下文质量和相关性成正比，关键上下文包括代码、架构、日志、示例、约束和需求。
- explicit: 实践上应先规划、补充正确文档、利用视觉上下文、每次改动后测试，并在调试前说明期望与错误信息。
- inferred: 这份 source 适合编译为 Vibe Coding 总论页，并与提示语工程、上下文工程、AI 辅助工程形成学习路径。

## External Links

- further-reading: [Beyond Vibe Coding](https://beyond.addy.ie/) — source 列为扩展阅读；not verified.
- further-reading: [aicodeguide](https://github.com/automata/aicodeguide) — source 列为扩展阅读；not verified.
- further-reading: [awesome-vibe-coding](https://github.com/filipecalegario/awesome-vibe-coding?tab=readme-ov-file) — source 列为扩展阅读；not verified.
- tool-reference: [claude-task-master](https://github.com/eyaltoledano/claude-task-master) — source 列为任务管理工具；not verified.
- tool-reference: [RooCode](https://docs.roocode.com/) — source 列为任务管理/多模式工具；not verified.
- tool-reference: [vibe-kanban](https://github.com/BloopAI/vibe-kanban) — source 列为任务管理工具；not verified.

## Links

- compiled-concept: [[concepts/Vibe Coding|Vibe Coding]] — 可沉淀定义、风险、最佳实践和与 AI Assisted Engineering 的区别。
- map-entry: [[maps/Vibe Coding 学习地图|Vibe Coding 学习地图]] — 可作为 Vibe 主题总入口。

## Maintenance Notes

- The only sheet title is `d`, which is not semantically descriptive; content root is `Vibe Coding`.
- Branches `./实战` and `./方法论` appear as relative pointers, not actual URLs in exported content.

- Link cleanup candidate: related: AI 辅助工程 — 可承载规格、严谨性、人机协作和信任模型。.
