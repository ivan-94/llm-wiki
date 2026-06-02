---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/工具/mattpocock:skills  ⭐/Ext HAT - Hand Acceptance Test Run验收测试执行hat-run.xmind"
source_relpath: "Vibe/工具/mattpocock:skills  ⭐/Ext HAT - Hand Acceptance Test Run验收测试执行hat-run.xmind"
raw_created_at: 2026-06-01T11:04:57.168804+00:00
raw_modified_at: 2026-06-01T11:04:57.245551+00:00
raw_size: 3402882
raw_fingerprint: "size=3402882;birth=2026-06-01T11:04:57.168804+00:00;mtime=2026-06-01T11:04:57.245551+00:00"
raw_snapshot_at: 2026-06-01T13:47:45.024325+00:00
ingested_at: 2026-06-01
status: ingested
---

# Ext HAT - Hand Acceptance Test Run验收测试执行hat-run.xmind

## Source

- Raw file: [Vibe/工具/mattpocock:skills  ⭐/Ext HAT - Hand Acceptance Test Run验收测试执行hat-run.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/%E5%B7%A5%E5%85%B7/mattpocock%3Askills%20%20%E2%AD%90/Ext%20HAT%20-%20Hand%20Acceptance%20Test%20Run%E9%AA%8C%E6%94%B6%E6%B5%8B%E8%AF%95%E6%89%A7%E8%A1%8Chat-run.xmind>)
- Raw ref: `raw:Vibe/工具/mattpocock:skills  ⭐/Ext HAT - Hand Acceptance Test Run验收测试执行hat-run.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2026-06-01T11:04:57.168804+00:00`; modified `2026-06-01T11:04:57.245551+00:00`; size `3402882`; snapshot `2026-06-01T13:47:45.024325+00:00`
- Coverage: XMind helper exported all sheets; `sheet_count=1`; `0` titled `/hat-run` with 61 topics.

## Source Cluster

- Directory cluster: Vibe/工具/mattpocock:skills  ⭐
- Cluster role: tool
- Neighbor sources:
  - same-cluster: [[sources/Vibe/工具/mattpocock:skills  ⭐/Matt Pocock Skills.xmind|Vibe/工具/mattpocock:skills  ⭐/Matt Pocock Skills.xmind]] — 同属 Matt Pocock Skills cluster，提供工作流技能总体方法论。
  - same-cluster: [[sources/Vibe/工具/mattpocock:skills  ⭐/我的流程.xmind|Vibe/工具/mattpocock:skills  ⭐/我的流程.xmind]] — 同属个人 Agent 工作流 cluster，提供端到端流程位置。

## Summary

这份 XMind 定义 `/hat-run`：只基于 `/hat-prepare` 的产物执行 Agent 自动化验收，并把结果写成报告、日志和截图。

## Source Digest

source 明确区分 `/hat-prepare` 和 `/hat-run`：前者准备环境、数据和清单，后者只认这些产物并按优先级执行验收。执行可使用 browser、agent-browser、browser-use、Playwright、Chrome DevTools MCP、Codex 浏览器或插件等多种工具。

source 还列出现实阻碍：认证和验证码、现代前端组件自动化可达性、服务依赖生命周期、权限与验收数据不足。解决方向是提供验收账号/token、优先 API 验证并用 UI 确认用户路径、显式 dry-run 计划与恢复检查、准备不同角色账号，并用项目级 HAT.md 沉淀通用策略。

## Key Claims

- explicit: `/hat-run` 的输入只认 `/hat-prepare` 产物。
- explicit: HAT 执行应支持 browser、Playwright、Chrome DevTools MCP、Codex 浏览器等多种验证手段。
- explicit: P0 失败应优先终止，随后才考虑 P1/P2。
- explicit: 验收报告应包含 summary、需要人工介入的内容、截图和 logs。
- inferred: HAT 运行的难点不在单个工具，而在认证、数据、服务生命周期和可恢复性。

## External Links

- tool: [agent-browser](https://skills.sh/vercel-labs/agent-browser/agent-browser) — source 中列为浏览器验收工具；not verified.
- tool: [Playwright](https://skills.sh/microsoft/playwright-cli/playwright-cli) — source 中列为浏览器验收工具；not verified.

## Links

- compiled-concept: [[concepts/HAT（Hand Acceptance Test）|HAT（Hand Acceptance Test）]] — 定义 HAT 执行阶段的输入边界、工具选择、P0 停止规则和证据输出。
- updates: [[concepts/Agent Harness|Agent Harness]] — 补充 harness feedback layer 的执行和证据输出协议。
- updates: [[concepts/Agent 工作流技能编排|Agent 工作流技能编排]] — 补充 Matt Pocock 扩展 skill 在工作流链路中的位置。
- updates: [[concepts/Agent Skills|Agent Skills]] — 补充 workflow/helper/lightweight skills 的具体节点。
- compiled-entity: [[entities/Matt Pocock|Matt Pocock]] — 提供 Matt Pocock Skills 扩展集证据。
- map-entry: [[maps/Vibe Coding 工具地图|Vibe Coding 工具地图]] — 纳入 Matt Pocock Skills 工具 cluster。

## Maintenance Notes

- XMind helper 成功导出全部 1 个 sheet；每个 sheet 已在本次批量 ingest 中读取并消化。
- 本 source note 是批量 ingest 生成的消化层，不保存完整 raw 导出；需要细节时应回 raw XMind。
