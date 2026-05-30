---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/工具/mattpocock:skills  ⭐/Matt Pocock Skills.xmind"
source_relpath: "Vibe/工具/mattpocock:skills  ⭐/Matt Pocock Skills.xmind"
raw_created_at: 2026-05-06T02:01:47.711883+00:00
raw_modified_at: 2026-05-11T01:36:50.646395+00:00
raw_size: 666888
raw_fingerprint: "size=666888;birth=2026-05-06T02:01:47.711883+00:00;mtime=2026-05-11T01:36:50.646395+00:00"
raw_snapshot_at: 2026-05-29T16:06:13.711310+00:00
ingested_at: 2026-05-30
status: ingested
---

# Matt Pocock Skills.xmind

## Source

- Raw file: [Vibe/工具/mattpocock:skills  ⭐/Matt Pocock Skills.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/%E5%B7%A5%E5%85%B7/mattpocock%3Askills%20%20%E2%AD%90/Matt%20Pocock%20Skills.xmind>)
- Raw ref: `raw:Vibe/工具/mattpocock:skills  ⭐/Matt Pocock Skills.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2026-05-06T02:01:47.711883+00:00`; modified `2026-05-11T01:36:50.646395+00:00`; size `666888`; snapshot `2026-05-29T16:06:13.711310+00:00`
- Coverage: XMind helper exported all sheets; `sheet_count=1`; sheet `0` titled `skills` with 164 topics.

## Summary

这份 XMind 总结 Matt Pocock 风格的 agent skills 方法论：skill 应该小、易改、可组合，不替代人思考，而是把工程基本功和共享语言固化成可复用流程。它围绕 4 个失败模式组织解决方案：需求没对齐、AI 废话太多、代码跑不通、代码架构变差，并串起 grilling、CONTEXT.md、TDD、diagnose、architecture improvement、PRD、issue、triage 和 GitHub issue 任务管理。

## Source Digest

source 的底层哲学是“工程基本功优先于流程框架”。Skills 的价值不是把 agent 变成自动魔法，而是通过小而可组合的流程，把需求澄清、术语对齐、反馈循环、测试面、调试纪律、架构深度和任务状态管理变成 agent 可以重复执行的协议。它明确把 interface、feedback loop、deletion test、deep module、CONTEXT.md 和 ADR 作为工程协作中的关键抽象。

工作流上，source 从对齐开始：用 `/grill-me` 或 `/grill-with-docs` 逼清决策树，必要时把术语、关系、例子和歧义写入 CONTEXT.md；随后 `/to-prd` 将已聊内容转换成不含文件路径和代码片段的 PRD；再用 `/to-issues` 拆出穿透 schema/API/UI/test 的垂直切片，并可用 `/triage` 分拣 issue、补上下文、写 Agent Brief 和推进状态；开发阶段用 `/tdd` 保持红绿重构，调试阶段用 `/diagnose` 六阶段闭环，架构维护阶段用 `/improve-codebase-architecture` 寻找 deepening opportunities。

source 还把 GitHub Issue 升格为 AI Coding 的协议层：状态、标签、评论、引用和 webhook 分别承担路由、记忆、消息总线、依赖图和自动化触发器职责。Issue 不只是高级 TODO，而是 agent 之间共享任务上下文、记录决策、承载 spike/prototype 和驱动 ready-for-agent 市场的基础设施。

## Key Claims

- explicit: Matt Pocock Skills 的核心哲学是 small、easy to adapt、composable，并保持人的控制权。
- explicit: 4 个失败模式分别是 AI 没理解需求、AI 废话太多、代码跑不通、代码架构变差。
- explicit: `/grill-me` 和 `/grill-with-docs` 用于需求对齐；后者会实时更新 CONTEXT.md 和 ADR。
- explicit: CONTEXT.md 通过术语定义、Avoid 同义词、关系、示例对话和已解决歧义，让 AI 使用项目共享语言。
- explicit: `/diagnose` 被定义为六阶段调试纪律：建立 feedback loop、复现、提出可证伪假设、插桩、修复加回归测试、清理和 post-mortem。
- explicit: `/to-issues` 应拆 tracer-bullet vertical slices，每个 slice 穿透多层并独立可验证、可 demo。
- explicit: GitHub Issue 被描述为 AI 工作流的协议层，Label、Comment、Webhook 和 Reference 分别承担路由、事件日志、触发器和依赖图角色。
- inferred: 这份 source 可作为 Agent workflow/skills 体系的中枢证据，适合连接 Codex CLI、HAT、PRD、issue、TDD 和 diagnose 等多个局部工具页。

## External Links

No external links found in extracted content.

## Links

- compiled-concept: [[concepts/Agent Skills|Agent Skills]] — 可提炼小型、可组合、可适配的工程 skill 设计原则和三分法。
- compiled-entity: [[entities/Matt Pocock|Matt Pocock]] — 提供四失败模式、工程链路和 GitHub 协议层升格。
- updates: [[concepts/Agent 工作流技能编排|Agent 工作流技能编排]] — 提供 PRD、issue、triage、TDD、diagnose 和 PR 的协作链条。
- compiled-synthesis: [[synthesis/GitHub 驱动的 Agent 开发闭环|GitHub 驱动的 Agent 开发闭环]] — 提炼 triage labels、Agent Brief 和 Issue 协议层。
- map-entry: [[maps/Vibe Coding 工具地图|Vibe Coding 工具地图]] — Vibe 工程化 workflow 主入口。

## Maintenance Notes

- XMind helper 成功导出全部 1 个 sheet；未发现 URL。
- source 中包含较多具体 skill 名称和 workflow 名称；后续 compile 时应区分“方法论概念”和“本机已安装 skill 实现”，避免把当前 repo 工具状态误作 raw 明示事实。
