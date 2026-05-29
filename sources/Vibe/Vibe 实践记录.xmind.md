---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/Vibe 实践记录.xmind"
source_relpath: "Vibe/Vibe 实践记录.xmind"
raw_created_at: 2025-10-27T04:54:21+00:00
raw_modified_at: 2026-04-29T02:33:46.214836+00:00
raw_size: 643801
raw_fingerprint: "size=643801;birth=2025-10-27T04:54:21+00:00;mtime=2026-04-29T02:33:46.214836+00:00"
raw_snapshot_at: 2026-05-29T16:02:54.870101+00:00
ingested_at: 2026-05-30
status: ingested
---

# Vibe 实践记录.xmind

## Source

- Raw file: [Vibe/Vibe 实践记录.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/Vibe%20%E5%AE%9E%E8%B7%B5%E8%AE%B0%E5%BD%95.xmind>)
- Raw ref: `raw:Vibe/Vibe 实践记录.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2025-10-27T04:54:21+00:00`; modified `2026-04-29T02:33:46.214836+00:00`; size `643801`; snapshot `2026-05-29T16:02:54.870101+00:00`
- Coverage: helper exported all sheets. Sheet count: 3. Sheets: `Vibe 实践记录` (index 0, 260 topics), `里程碑示例` (index 1, 1 topic), `数据索引优化 SOP` (index 2, 1 topic).

## Summary

这份 XMind 是一套 AI 辅助工程实践手册。它把 Vibe 协作落到规格驱动开发、AGENTS/CLAUDE 规则约束、分步里程碑、详细设计、变更请求、模块化、依赖倒置、声明式系统、可观测性、工具使用、沙箱、模板和质量门控上，并附带一个执行器里程碑示例与一个数据索引优化 SOP。

## Source Digest

source 的基本判断是：Vibe 实践不是“直接让 AI 写代码”，而是把传统软件工程流程重新组织为 AI 可执行、可验证、可迭代的规格链路。它从概要设计开始，要求先说明项目背景、目标、用户场景、核心流程、模型设计、系统架构、目录结构、API 设计和验收说明；概要设计不必一次完美，但要让 AI 理解最终目的，而不是只接收开发者压缩过的技术术语。

它明确区分业务设计与 agent 行为约束：概要设计描述业务，AGENTS.md/CLAUDE.md 则约束 AI 的工作方式、命令、环境、代码风格和技术栈。复杂需求通过里程碑拆分，按抽象层级、依赖关系、垂直模块或时间拆成可独立执行和测试的单元；每个里程碑再细化为核心目标、组件、接口、流程、验收和注意事项。简单需求可以使用更轻量的变更请求，直接描述目标、步骤和涉及文件。

工程规则部分把“说到底还是软件工程”作为主线：按领域或特性切片组织代码、把模块当库开发、使用依赖倒置和接口优先来让阶段成果独立可测、用 DDD 分层隔离领域层/应用层/基础设施层/表示层，用声明式文件描述基础设施、环境、CI/CD 和配置，并通过日志、错误信息、CLI、MCP、程序化脚本、主流标准技术、沙箱环境、输出模板和质量门控来放大并约束 AI。附录 sheet 给出了执行器里程碑的组件协议和验收要求，以及 AiDailyReport 索引优化从需求梳理、基准索引、10M 数据验证、EXPLAIN/mysqlslap 到总结报告的 SOP。

## Key Claims

- explicit: Vibe 实践的核心是规格驱动开发和软件工程，而不是单纯依赖 agent 直接编码。
- explicit: 概要设计应覆盖背景目标、用户场景、核心流程、模型、架构、目录、API 和验收，让 AI 理解业务目的。
- explicit: AGENTS.md/CLAUDE.md 应约束 AI 行为、命令、环境、风格和技术栈，但需求问题应回到设计文档，不应全部塞入规则文件。
- explicit: 复杂需求应拆成可独立执行、可独立测试的里程碑，再由里程碑生成详细设计；简单需求可用轻量变更请求。
- explicit: 模块化、依赖倒置、接口优先、DDD 分层、声明式配置、可观测性、CLI/MCP 工具、沙箱与质量门控共同构成 AI 友好的工程环境。
- inferred: 这份 source 是 Vibe Coding 从理念走向工程化交付方法的主干材料，可支撑“规格驱动 AI 开发”和“Agent 友好工程环境”概念页。

## External Links

No external links found in extracted content.

## Links

- compiled-concept-candidate: [[concepts/规格驱动 AI 开发|规格驱动 AI 开发]] — 可沉淀概要设计、里程碑、详细设计、变更请求和验收链路；候选，未创建。
- compiled-concept-candidate: [[concepts/Agent 友好工程环境|Agent 友好工程环境]] — 可承载模块化、依赖倒置、声明式、可观测性、CLI、沙箱和质量门控；候选，未创建。
- map-entry-candidate: [[maps/Vibe Coding 学习地图|Vibe Coding 学习地图]] — 可作为 Vibe 实践工作流的核心节点；候选，未创建。

## Maintenance Notes

- Sheet 1 and sheet 2 are single-topic sheets containing long embedded practice examples; they were read and summarized, but their full component/spec text is not copied into this source note.
- Exported content contains large code-tree examples and SOP paths; exact implementation details should be rechecked against raw when needed.
- Some spellings in raw are preserved conceptually but not normalized here, e.g. `implementions`, `optmize`, and `claude sonnect`.
