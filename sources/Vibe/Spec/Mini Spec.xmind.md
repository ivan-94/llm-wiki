---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/Spec/Mini Spec.xmind"
source_relpath: "Vibe/Spec/Mini Spec.xmind"
raw_created_at: 2025-09-29T04:21:27.842664+00:00
raw_modified_at: 2025-10-27T03:09:20.998598+00:00
raw_size: 494900
raw_fingerprint: "size=494900;birth=2025-09-29T04:21:27.842664+00:00;mtime=2025-10-27T03:09:20.998598+00:00"
raw_snapshot_at: 2026-05-29T15:53:28.781618+00:00
ingested_at: 2026-05-29
status: ingested
---

# Mini Spec.xmind

## Source

- Raw file: [Vibe/Spec/Mini Spec.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/Spec/Mini%20Spec.xmind>)
- Raw ref: `raw:Vibe/Spec/Mini Spec.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2025-09-29T04:21:27.842664+00:00`; modified `2025-10-27T03:09:20.998598+00:00`; size `494900`; snapshot `2026-05-29T15:53:28.781618+00:00`
- Coverage: helper exported and read all `1` sheet: `Mini Spec`.

## Summary

这份 XMind 定义 Mini Spec：一种面向小功能、bug fix 和局部重构的轻量规格文档，用来在正式 PRD/设计/任务流程过重时，为开发者和 LLM 提供精细上下文、范围边界、验收标准、技术蓝图和执行计划。

## Source Digest

该 source 的核心是把“小型迭代”也规格化，但不引入完整规格书流程的重量。Mini Spec 适合开发者主导的小团队或独立开发场景，目标是给 LLM 足够精细的上下文边界：哪些文件会改、哪些函数/类相关、什么明确不做、有哪些外部输入、验收标准如何表达、技术方法和依赖是什么、前后端结构如何变化、具体执行步骤如何拆。

资料将 Mini Spec 与全局记忆绑定：局部迭代需要 AGENTS.md/CLAUDE.md 等全局规则来提供项目视角，避免 LLM 在局部 patch 中破坏架构、风格或验证约定。模板推荐用 `Feature-ID`、目标、Context & Scope、Acceptance Criteria、Implementation Sketch 和执行计划组织；验收标准可用 GIVEN/WHEN/THEN 或“触发条件 -> 行为 -> 状态变更”的折中格式。

该 source 适合编译“Mini Spec”“轻量规格”“LLM 精细上下文边界”等概念，并可与 AGENTS.md 全局记忆 source 组成 Vibe Spec 学习路径。

## Key Claims

- explicit: Mini Spec 面向小功能、缺陷修复和局部重构，避免正规规格书、设计、任务流程对小迭代过重。
- explicit: Mini Spec 主要面向开发者，适合小团队和独立开发者降低沟通成本。
- explicit: 为了约束 LLM 做精细化修改，Mini Spec 需要指定精细上下文和范围边界。
- explicit: 局部迭代仍需要 AGENTS.md/CLAUDE.md 等全局记忆提供项目基本准则和全局视角。
- explicit: Mini Spec 文件可按功能目录下 `/specs/SOME_SPEC_YYYYMMDD.md` 组织。
- explicit: 模板包括 Feature-ID、目标、Context & Scope、Affected Files、Key Functions/Classes、Out of Scope、外部输入、Acceptance Criteria、Implementation Sketch、依赖、结构设计和执行计划。
- explicit: 验收标准可以使用 GIVEN/WHEN/THEN，或“触发条件 -> 行为 -> 状态变更”的格式。
- inferred: Mini Spec 的主要价值是把模糊小需求转成可验收、可约束、可执行的 Agent 工作单元。

## External Links

- reference: [context-engineering-intro PRP example](https://github.com/coleam00/context-engineering-intro/blob/main/PRPs/EXAMPLE_multi_agent_prp.md) — source 参考；not verified.

## Links

- compiled-concept: Mini Spec — 本 source 提供轻量规格的适用场景、模板和验收边界。
- compiled-concept: LLM 精细上下文边界 — 资料强调受影响文件、关键函数、范围外事项和外部输入。
- compiled-concept: Agent 工作单元 — Mini Spec 将小需求整理成可执行、可验证的工作单元。
- map-entry: Vibe Spec 学习地图 — 适合与 AGENTS.md 全局记忆共同组织 Spec 类资料。

## Maintenance Notes

- helper `export_xmind_source.py` 返回 `ok: true`、`sheets_error: ""`，无 sheet 缺失。
- 该 source 含模板示例，但没有真实项目落地案例；后续编译时可补充实际 Mini Spec 样例。
