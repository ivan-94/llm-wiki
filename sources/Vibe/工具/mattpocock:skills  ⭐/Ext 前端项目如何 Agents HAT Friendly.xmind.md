---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/工具/mattpocock:skills  ⭐/Ext 前端项目如何 Agents HAT Friendly.xmind"
source_relpath: "Vibe/工具/mattpocock:skills  ⭐/Ext 前端项目如何 Agents HAT Friendly.xmind"
raw_created_at: 2026-06-01T11:04:56.712766+00:00
raw_modified_at: 2026-06-01T11:04:56.799143+00:00
raw_size: 4410266
raw_fingerprint: "size=4410266;birth=2026-06-01T11:04:56.712766+00:00;mtime=2026-06-01T11:04:56.799143+00:00"
raw_snapshot_at: 2026-06-01T13:47:45.582948+00:00
ingested_at: 2026-06-01
status: ingested
---

# Ext 前端项目如何 Agents HAT Friendly.xmind

## Source

- Raw file: [Vibe/工具/mattpocock:skills  ⭐/Ext 前端项目如何 Agents HAT Friendly.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/%E5%B7%A5%E5%85%B7/mattpocock%3Askills%20%20%E2%AD%90/Ext%20%E5%89%8D%E7%AB%AF%E9%A1%B9%E7%9B%AE%E5%A6%82%E4%BD%95%20Agents%20HAT%20Friendly.xmind>)
- Raw ref: `raw:Vibe/工具/mattpocock:skills  ⭐/Ext 前端项目如何 Agents HAT Friendly.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2026-06-01T11:04:56.712766+00:00`; modified `2026-06-01T11:04:56.799143+00:00`; size `4410266`; snapshot `2026-06-01T13:47:45.582948+00:00`
- Coverage: XMind helper exported all sheets; `sheet_count=1`; `0` titled `/hat-frontend-friendly` with 13 topics.

## Source Cluster

- Directory cluster: Vibe/工具/mattpocock:skills  ⭐
- Cluster role: tool
- Neighbor sources:
  - same-cluster: [[sources/Vibe/工具/mattpocock:skills  ⭐/Matt Pocock Skills.xmind|Vibe/工具/mattpocock:skills  ⭐/Matt Pocock Skills.xmind]] — 同属 Matt Pocock Skills cluster，提供工作流技能总体方法论。
  - same-cluster: [[sources/Vibe/工具/mattpocock:skills  ⭐/我的流程.xmind|Vibe/工具/mattpocock:skills  ⭐/我的流程.xmind]] — 同属个人 Agent 工作流 cluster，提供端到端流程位置。

## Summary

这份 XMind 给出前端项目 HAT-friendly 改造原则：给复杂组件稳定测试入口、让状态 URL 化、记录关键日志，并为 Playwright 暴露测试专用动作。

## Source Digest

source 的主要原则是不要让 Agent 猜 DOM 结构、浮层位置、虚拟滚动或 portal。复杂组件要提供稳定 testid 和 aria 标签，避免依赖文本和层级选择器；产品路由层需要让状态可 URL 化，关键链路要有日志方便排查。

source 还提出对 Playwright 暴露测试专用动作和数据驱动页面的方向。这说明前端 HAT-friendly 不是单纯写测试，而是为 Agent 提供稳定选择器、可重入状态、可观察日志和低脆弱度操作入口。

## Key Claims

- explicit: 前端复杂组件应有稳定测试入口，不要让 Agent 猜 DOM、浮层、虚拟滚动或 portal。
- explicit: 应使用稳定 testid 和 aria 标签，避免依赖文本和层级选择器。
- explicit: 产品路由层应让状态可 URL 化。
- explicit: 关键链路需要日志，方便 Agent 排查。
- inferred: HAT-friendly 前端的核心是降低自动化验收的选择器脆弱性和状态恢复成本。

## External Links

No external links found in extracted content.

## Links

- compiled-concept: [[concepts/HAT（Hand Acceptance Test）|HAT（Hand Acceptance Test）]] — 补充 HAT-friendly 前端对稳定选择器、URL 状态和日志的要求。
- updates: [[concepts/Agent 工作流技能编排|Agent 工作流技能编排]] — 补充 Matt Pocock 扩展 skill 在工作流链路中的位置。
- updates: [[concepts/Agent Skills|Agent Skills]] — 补充 workflow/helper/lightweight skills 的具体节点。
- compiled-entity: [[entities/Matt Pocock|Matt Pocock]] — 提供 Matt Pocock Skills 扩展集证据。
- map-entry: [[maps/Vibe Coding 工具地图|Vibe Coding 工具地图]] — 纳入 Matt Pocock Skills 工具 cluster。

## Maintenance Notes

- XMind helper 成功导出全部 1 个 sheet；每个 sheet 已在本次批量 ingest 中读取并消化。
- 本 source note 是批量 ingest 生成的消化层，不保存完整 raw 导出；需要细节时应回 raw XMind。
