# Codex 周报模板

用于 `human/inbox/codex-weekly/YYYY-MM-DD_to_YYYY-MM-DD_Codex周报.md`。

这是写作结构，不是机械填空模板。Agent 需要基于七天日报事实进行二次综合，重点放在工作流、工作方式、效率、质量和组织化沉淀。

```markdown
---
title: "{week_start} to {week_end} Codex周报"
date: {week_end}
week_start: {week_start}
week_end: {week_end}
type: codex-weekly
generated_at: {generated_at}
ingest_policy: on-request
inbox_status: unread
inbox_created_at: {generated_date}
inbox_read_at:
raw_path:
ingested_at:
archive_reason:
source_kind: codex-report
---

# {week_start} to {week_end} Codex周报

## 工作周报（对上汇报）

<面向上级同步本周推进了什么、结果怎样、风险是什么、下周准备做什么。面向业务和管理语境表达，不展开执行细节，不按天流水账。>

- 本周推进:
  - <2-5 项>
- 当前结果:
  - <已完成、已验证、已产出的内容>
- 风险与问题:
  - <仍未解决的问题、质量风险、流程风险；没有则写“暂无明显阻塞”>
- 下周计划:
  - <1-3 个最重要动作>

## 本周主线

- <主线 1: 一周真正围绕的工作主题>
- <主线 2>
- <主线 3>

## 每日摘要索引

- [[human/inbox/codex-daily/YYYY-MM-DD_Codex日报|YYYY-MM-DD]]: <一句话主题>；信号: <值得带入周报的工作方式、质量、效率或风险信号>
- YYYY-MM-DD: missing; no daily report found.

## 分析与洞察

<不要写成执行记录汇总。先从七天日报里选出最值得解释的张力点、转折、重复摩擦或反事实风险。每个洞察写成一段，解释：事实片段 -> 暴露的问题 -> 背后的机制 -> 这对工作流、工作方式、效率、质量或组织化意味着什么。>

## 启发与下周调整

<只写最值得改变的 2-4 件事。每条建议说明：它来自本周哪个摩擦或信号；下次遇到什么触发条件时启用；它要改变哪类工作方式。>

## 待跟进归并

- [ ] <归并后的后续动作>
  - 来源: [[human/inbox/codex-daily/YYYY-MM-DD_Codex日报|YYYY-MM-DD]]
  - 归并判断: <为什么这些待办属于同一件事>
```
