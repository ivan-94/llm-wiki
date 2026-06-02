---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/工具/mattpocock:skills  ⭐/Ext HAT - Hand Acceptance Test Prepare验收测试准备hat-prepare.xmind"
source_relpath: "Vibe/工具/mattpocock:skills  ⭐/Ext HAT - Hand Acceptance Test Prepare验收测试准备hat-prepare.xmind"
raw_created_at: 2026-06-01T11:04:57.095245+00:00
raw_modified_at: 2026-06-01T11:04:57.154743+00:00
raw_size: 2319106
raw_fingerprint: "size=2319106;birth=2026-06-01T11:04:57.095245+00:00;mtime=2026-06-01T11:04:57.154743+00:00"
raw_snapshot_at: 2026-06-01T13:47:44.951736+00:00
ingested_at: 2026-06-01
status: ingested
---

# Ext HAT - Hand Acceptance Test Prepare验收测试准备hat-prepare.xmind

## Source

- Raw file: [Vibe/工具/mattpocock:skills  ⭐/Ext HAT - Hand Acceptance Test Prepare验收测试准备hat-prepare.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/%E5%B7%A5%E5%85%B7/mattpocock%3Askills%20%20%E2%AD%90/Ext%20HAT%20-%20Hand%20Acceptance%20Test%20Prepare%E9%AA%8C%E6%94%B6%E6%B5%8B%E8%AF%95%E5%87%86%E5%A4%87hat-prepare.xmind>)
- Raw ref: `raw:Vibe/工具/mattpocock:skills  ⭐/Ext HAT - Hand Acceptance Test Prepare验收测试准备hat-prepare.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2026-06-01T11:04:57.095245+00:00`; modified `2026-06-01T11:04:57.154743+00:00`; size `2319106`; snapshot `2026-06-01T13:47:44.951736+00:00`
- Coverage: XMind helper exported all sheets; `sheet_count=1`; `0` titled `/hat-prepare` with 45 topics.

## Source Cluster

- Directory cluster: Vibe/工具/mattpocock:skills  ⭐
- Cluster role: tool
- Neighbor sources:
  - same-cluster: [[sources/Vibe/工具/mattpocock:skills  ⭐/Matt Pocock Skills.xmind|Vibe/工具/mattpocock:skills  ⭐/Matt Pocock Skills.xmind]] — 同属 Matt Pocock Skills cluster，提供工作流技能总体方法论。
  - same-cluster: [[sources/Vibe/工具/mattpocock:skills  ⭐/我的流程.xmind|Vibe/工具/mattpocock:skills  ⭐/我的流程.xmind]] — 同属个人 Agent 工作流 cluster，提供端到端流程位置。

## Summary

这份 XMind 定义 `/hat-prepare`：在 TDD 覆盖不到的用户完整路径上，准备验收环境、数据、清单和幂等脚本。

## Source Digest

source 把 HAT Prepare 的目标定义为补齐用户视角完整路径验证，而不是替代单元测试。准备阶段需要根据场景选择 blank、fork 或 attach 三种环境模式，并在涉及迁移或验收数据时生成临时脚本做验证。

输出形态是 `/hats` 下的验收指南和准备脚本：指南记录环境、schema/version、账号、数据需求、P0/P1/P2 分级清单和执行方式；`prepare.sh` 必须幂等、失败停止、打印 schema/version/seed 信息并支持 cleanup。

## Key Claims

- explicit: `/hat-prepare` 用于验证用户视角完整路径，补充 TDD 测不到的边界。
- explicit: 验收环境可分为 blank、fork 和 attach 三种构造模式。
- explicit: 验收清单按 P0 主路径、P1 重要边界、P2 探索性检查分级。
- explicit: `prepare.sh` 应该幂等、失败时停止、打印 schema/version/data seed 信息并支持 cleanup。
- inferred: `/hat-prepare` 是 HAT 执行链的前置协议层，重点在可复现环境与验收说明。

## External Links

No external links found in extracted content.

## Links

- compiled-concept: [[concepts/HAT（Hand Acceptance Test）|HAT（Hand Acceptance Test）]] — 定义 HAT 准备阶段的环境、数据、清单和幂等脚本协议。
- updates: [[concepts/Agent Harness|Agent Harness]] — 补充 harness acceptance baseline 的准备协议证据。
- updates: [[concepts/Agent 工作流技能编排|Agent 工作流技能编排]] — 补充 Matt Pocock 扩展 skill 在工作流链路中的位置。
- updates: [[concepts/Agent Skills|Agent Skills]] — 补充 workflow/helper/lightweight skills 的具体节点。
- compiled-entity: [[entities/Matt Pocock|Matt Pocock]] — 提供 Matt Pocock Skills 扩展集证据。
- map-entry: [[maps/Vibe Coding 工具地图|Vibe Coding 工具地图]] — 纳入 Matt Pocock Skills 工具 cluster。

## Maintenance Notes

- XMind helper 成功导出全部 1 个 sheet；每个 sheet 已在本次批量 ingest 中读取并消化。
- 本 source note 是批量 ingest 生成的消化层，不保存完整 raw 导出；需要细节时应回 raw XMind。
