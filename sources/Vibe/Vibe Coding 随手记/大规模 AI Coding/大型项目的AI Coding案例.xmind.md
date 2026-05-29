---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/Vibe Coding 随手记/大规模 AI Coding/大型项目的AI Coding案例.xmind"
source_relpath: "Vibe/Vibe Coding 随手记/大规模 AI Coding/大型项目的AI Coding案例.xmind"
raw_created_at: 2026-05-19T13:54:45.315067+00:00
raw_modified_at: 2026-05-23T06:39:42.596983+00:00
raw_size: 585952
raw_fingerprint: "size=585952;birth=2026-05-19T13:54:45.315067+00:00;mtime=2026-05-23T06:39:42.596983+00:00"
raw_snapshot_at: 2026-05-29T15:59:18.165524+00:00
ingested_at: 2026-05-29
status: ingested
---

# 大型项目的AI Coding案例.xmind

## Source

- Raw file: [Vibe/Vibe Coding 随手记/大规模 AI Coding/大型项目的AI Coding案例.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/Vibe%20Coding%20%E9%9A%8F%E6%89%8B%E8%AE%B0/%E5%A4%A7%E8%A7%84%E6%A8%A1%20AI%20Coding/%E5%A4%A7%E5%9E%8B%E9%A1%B9%E7%9B%AE%E7%9A%84AI%20Coding%E6%A1%88%E4%BE%8B.xmind>)
- Raw ref: `raw:Vibe/Vibe Coding 随手记/大规模 AI Coding/大型项目的AI Coding案例.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2026-05-19T13:54:45.315067+00:00`; modified `2026-05-23T06:39:42.596983+00:00`; size `585952`; snapshot `2026-05-29T15:59:18.165524+00:00`
- Coverage: helper exported all sheets; sheet count `4`; sheets: `画布 1` (37 topics), `实现一个 Xmind CLI` (66 topics), `JSSE: A JavaScript Engine Built by an Agent` (33 topics), `We Ralph Wiggumed WebStreams to make them 10x faster` (5 topics).

## Summary

这份 XMind 收集大型 AI Coding 项目案例，覆盖 Vue Lynx、Cloudflare vinext、XMind CLI、JSSE 和 WebStreams 相关材料。核心学习点集中在架构先行、持久上下文、强反馈循环、行为等价测试、文档/contract first、可执行计划、审计实现、TDD 闭环、人类方向控制和长程任务中的过程干预。

## Source Digest

source 用多个案例说明大型 AI Coding 能否成功，关键不在于一次性 prompt 多强，而在于能否把系统行为、架构约束和反馈回路变成 agent 可持续消费的环境。Vue Lynx 案例强调 Day 1 确定核心架构，把设计讨论、决策日志和实现学习写进源码树，配合上游测试、DevTool/CLI 驱动的 E2E、差异评估和真实 App 压力测试，让跨 session 的 AI 实现不漂移。

Cloudflare vinext 案例强调“行为是资产”：用 Next.js 测试套件作为机械可验证规范，先讨论架构、模块和优先级，再让 AI 分步重写，并通过 TypeScript、lint、AI code review、人类把关和渐进式迁移降低风险。XMind CLI 案例则展示了从 agent 视角反向设计工具的流程：先文档驱动，写产品原则、概念模型、reference、schema、guide，再做技术规划、PLAN.md 拆解、implementation-notes 审计、`/goal` 长程执行、TDD 闭环、过程干预和压缩维护。

JSSE 案例提供更长周期的经验：test262 和 Rust 编译器形成反馈信号，PLAN.md 负责任务跟踪，核心循环是找出对通过率影响最大的下一个功能；但复杂任务仍需要人类干预、会话边界、规划质量和并发 worktree 调度。WebStreams sheet 只有标题和占位分支，信息不足，不能支撑实质性结论。

## Key Claims

- explicit: Vue Lynx 案例认为架构先行、持续上下文注入、上游测试复用、agentic E2E 和差异评估是两周内推进复杂框架适配的重要机制。
- explicit: vinext 案例将成熟项目的测试套件作为规范，要求 AI 生成实现通过等价性测试，而不是只看起来合理。
- explicit: XMind CLI 案例采用文档先行、contract first、PLAN.md、implementation-notes、TDD 闭环和人类过程干预来驱动长程 agent 开发。
- explicit: JSSE 案例显示大型 agent 项目需要结构化测试套件、计划质量、会话边界和过程干预；测试通过率后期会变难。
- explicit: JSSE sheet 记录了 42 天、592 commit、17w lines、302 会话和 4,618.94 美元消耗等规模信息。
- inferred: 这些案例共同指向一个模式：大型 AI Coding 的主工程不是写代码，而是搭建可验证行为、持久上下文和可审计执行循环。

## External Links

- learning-source: [How I Built Vue Lynx with AI in Two Weeks](https://x.com/Huxpro/status/2036993665965416601) — source 用作 Vue Lynx 大型 AI Coding 案例；not verified.
- learning-source: [How we rebuilt Next.js with AI in one week](https://blog.cloudflare.com/vinext/) — source 用作 Cloudflare vinext 行为等价重写案例；not verified.
- learning-source: [JSSE: A JavaScript Engine Built by an Agent](https://p.ocmatos.com/blog/jsse-a-javascript-engine-built-by-an-agent.html) — source 用作 JS engine 长程 agent 项目案例；not verified.
- learning-source: [We Ralph Wiggumed WebStreams to make them 10x faster](https://vercel.com/blog/we-ralph-wiggumed-webstreams-to-make-them-10x-faster) — source 只保留标题和占位分支，尚缺可消化细节；not verified.

## Links

- compiled-concept: [[concepts/大型 AI Coding 案例模式|大型 AI Coding 案例模式]] — 候选概念；本 source 汇总跨案例的架构、上下文、反馈和人类控制模式。
- compiled-concept: [[concepts/行为等价测试|行为等价测试]] — 候选概念；vinext 和 Vue Lynx 案例都强调用现有系统行为或成熟测试作为规范。
- compiled-concept: [[concepts/Agent 原生工具设计|Agent 原生工具设计]] — 候选概念；XMind CLI 案例展示角色反转和 contract first 的工具设计路径。
- map-entry: [[maps/Vibe Coding 学习地图|Vibe Coding 学习地图]] — 候选地图入口；可作为大型 AI Coding 真实案例集合。

## Maintenance Notes

- 本批按用户约束只创建 source note，未实际创建或更新 `concepts/`、`maps/`、`index.md`、`log.md`。
- 导出覆盖 4/4 sheets，未发现 sheet 导出错误。
- `We Ralph Wiggumed WebStreams to make them 10x faster` sheet 只有标题和 `分支主题 1-4` 占位，当前信息不足，后续需要补充 raw 内容或重新整理。
- Vue Lynx 的成本描述含“Claude 部分赠送”但原文括号未闭合；保持为原始记录的语义摘要，未外部核验。
