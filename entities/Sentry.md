---
page_type: entity
updated_at: 2026-05-30
status: active
source_count: 1
---

# Sentry

## What It Is

Sentry 是一个面向应用开发者的异常监控和错误追踪平台，通过结构化异常事件、grouping/去重、release 关联、suspect commit 和 GitHub/DevOps 集成，把生产错误转化为可分派、可追踪、可验证的 Issue 对象。

## Role In This Wiki

在 Agentic Engineering 语境下，Sentry 代表"AI 可消费的异常治理工具"的参照实现：它能把生产报错聚合成结构化任务对象，让 Agent 直接基于 Issue 生成修复 PR，而不是从海量非结构化日志中人工拼凑上下文。

## Key Facts

- 核心产品：异常事件的结构化聚合、grouping/去重，一类错误对应一个 Issue。
- Issue 包含的结构化上下文：error type、message、stack trace、source file/line、environment、release、transaction、request context、tags、user context、breadcrumbs、event frequency、affected users、suspect commit、linked GitHub issue。
- Release + Commit + GitHub 集成：让异常能追溯到代码变更，进入研发工作流。
- 对比阿里云 ARMS/SLS：后者更偏可观测底座（APM/Trace/日志采集），缺少统一的异常对象生命周期管理，需要额外整合才能达到同等闭环。

## Related Concepts

- [[concepts/异常治理闭环|异常治理闭环]] — Sentry 是该闭环的参照实现平台
- [[concepts/Agentic Engineering|Agentic Engineering]] — 动态治理的工具链选型

## Evidence

- [[sources/Vibe/Vibe Coding 随手记/大规模 AI Coding/异常治理.xmind|异常治理.xmind]] — Sentry vs 阿里云 ARMS/SLS 比较，Agent 可消费事故现场字段定义。

## Open Questions

- Sentry 当前产品功能未联网核验；wiki 中的内容只反映 raw source 中记录的观点。
- Sentry 与 Linear/GitHub Issues 的集成细节需要外部核验。
