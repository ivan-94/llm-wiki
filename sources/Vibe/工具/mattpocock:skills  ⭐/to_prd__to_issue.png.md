---
source_type: image
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/工具/mattpocock:skills  ⭐/to_prd__to_issue.png"
source_relpath: "Vibe/工具/mattpocock:skills  ⭐/to_prd__to_issue.png"
raw_created_at: 2026-05-05T12:51:44.680397+00:00
raw_modified_at: 2026-05-05T12:51:44.680994+00:00
raw_size: 1868215
raw_fingerprint: "size=1868215;birth=2026-05-05T12:51:44.680397+00:00;mtime=2026-05-05T12:51:44.680994+00:00"
raw_snapshot_at: 2026-05-29T16:07:40+00:00
ingested_at: 2026-05-30
status: ingested
---

# to_prd__to_issue.png

## Source

- Raw file: [Vibe/工具/mattpocock:skills  ⭐/to_prd__to_issue.png](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/%E5%B7%A5%E5%85%B7/mattpocock%3Askills%20%20%E2%AD%90/to_prd__to_issue.png>)
- Raw ref: `raw:Vibe/工具/mattpocock:skills  ⭐/to_prd__to_issue.png`
- Type: image
- Status: ingested
- Raw metadata: created `2026-05-05T12:51:44.680397+00:00`; modified `2026-05-05T12:51:44.680994+00:00`; size `1868215`; snapshot `2026-05-29T16:07:40+00:00`
- Coverage: Vision ingest of the full 864x1821 vertical infographic; PRD sections, issue fields, quality criteria, split strategy, and warning panel were inspected.

## Summary

这张图描述从想法到可执行 issue 的两步转化：先用 `to-prd` 把对话、想法或需求收敛成 PRD，再用 `to-issues` 按用户可见行为拆成 vertical slice issues。它强调 issue 必须可抓取、可交付、可验收，且验收标准不清时应回到 PRD 澄清。

## Source Digest

图中将 PRD 视为需求收敛产物，包含 Problem Statement、Goals、Non-goals、User Stories、Functional Requirements、Technical Constraints、Testing Decisions、Out of Scope 和 Further Notes。PRD 的作用是先明确问题、目标、边界、用户场景、功能要求、技术约束和测试决策，避免直接把模糊想法切成任务。

从 PRD 到 issues 的拆分原则是 vertical slice，而不是按 frontend/backend/database 等技术层横切。每个 issue 的模板包含 Summary、Current behavior、Desired behavior、Acceptance criteria、Out of scope 和 Dependencies。底部进一步给出好 issue 的标准：独立可实现、可验证、范围小、行为化描述、耐重构、不依赖文件行号。拆分策略优先按用户旅程步骤、可交付行为和风险先后切分；如果 blocker 出现，则先拆 blocker 后 follow-up；不要把技术层或模糊范围强行变成 issue。

## Key Claims

- explicit: `to-prd` 的输出是 PRD，`to-issues` 的输出是可执行 vertical slice issues。
- explicit: PRD 应记录问题陈述、目标、非目标、用户故事、功能需求、技术约束、测试决策、范围外和补充说明。
- explicit: 每个 issue 应包含 Summary、Current behavior、Desired behavior、Acceptance criteria、Out of scope 和 Dependencies。
- explicit: 好 issue 应独立可实现、可验证、范围小、行为化描述、耐重构，且不依赖文件行号。
- explicit: 从 PRD 到 issues 应按 vertical slice 拆分，不按技术层拆分。
- explicit: 如果验收标准不清楚，应先回到 PRD 澄清。
- inferred: 该流程把“上下文收敛”和“执行切片”分成两个阶段，以减少 agent 直接执行模糊需求的风险。

## External Links

No external links found in extracted content.

## Links

- related: PRD 到垂直切片 Issue — 可沉淀需求收敛、issue 模板和 vertical slice 拆分准则。
- related: Vibe Coding 工作流学习地图 — 可作为规划到执行交接的流程节点。

## Maintenance Notes

- Vision-based ingest; small English field labels were readable, but any exact wording should be checked against the raw image before quotation.
- No index/log updates were made because this batch worker was restricted to the five source notes only.
