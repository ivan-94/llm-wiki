---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/工具/mattpocock:skills  ⭐/Ext 上下文检查agent-context-audit.xmind"
source_relpath: "Vibe/工具/mattpocock:skills  ⭐/Ext 上下文检查agent-context-audit.xmind"
raw_created_at: 2026-06-01T11:04:56.808950+00:00
raw_modified_at: 2026-06-01T11:04:56.848415+00:00
raw_size: 1962106
raw_fingerprint: "size=1962106;birth=2026-06-01T11:04:56.808950+00:00;mtime=2026-06-01T11:04:56.848415+00:00"
raw_snapshot_at: 2026-06-01T13:47:45.394211+00:00
ingested_at: 2026-06-01
status: ingested
---

# Ext 上下文检查agent-context-audit.xmind

## Source

- Raw file: [Vibe/工具/mattpocock:skills  ⭐/Ext 上下文检查agent-context-audit.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/%E5%B7%A5%E5%85%B7/mattpocock%3Askills%20%20%E2%AD%90/Ext%20%E4%B8%8A%E4%B8%8B%E6%96%87%E6%A3%80%E6%9F%A5agent-context-audit.xmind>)
- Raw ref: `raw:Vibe/工具/mattpocock:skills  ⭐/Ext 上下文检查agent-context-audit.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2026-06-01T11:04:56.808950+00:00`; modified `2026-06-01T11:04:56.848415+00:00`; size `1962106`; snapshot `2026-06-01T13:47:45.394211+00:00`
- Coverage: XMind helper exported all sheets; `sheet_count=1`; `0` titled `/agent-context-audit` with 74 topics.

## Source Cluster

- Directory cluster: Vibe/工具/mattpocock:skills  ⭐
- Cluster role: tool
- Neighbor sources:
  - same-cluster: [[sources/Vibe/工具/mattpocock:skills  ⭐/Matt Pocock Skills.xmind|Vibe/工具/mattpocock:skills  ⭐/Matt Pocock Skills.xmind]] — 同属 Matt Pocock Skills cluster，提供工作流技能总体方法论。
  - same-cluster: [[sources/Vibe/工具/mattpocock:skills  ⭐/我的流程.xmind|Vibe/工具/mattpocock:skills  ⭐/我的流程.xmind]] — 同属个人 Agent 工作流 cluster，提供端到端流程位置。

## Summary

这份 XMind 定义 `agent-context-audit`：用 sub-agent 做答题者、主 Agent 做考官，检查新 Agent 在当前上下文下会如何理解和行动。

## Source Digest

source 的核心模型是考试：sub-agent 只看自己的试卷、只回答问题并陈述依据；主 Agent 负责出题、收卷、读取项目文件建立 ground truth、评估答案、思路和探索成本。它用于暴露上下文污染、指令冲突、认知偏差和入口分散导致的探索成本。

执行方式是每道场景题独立 fork 一个 sub-agent，先自然回答，再追问探索账单，包括读了多少文件、关键路径、来源和哪些结论是证据或推断。主 Agent 最后从答案正确性、思路正确性、探索成本、上下文污染和改进建议几个维度输出诊断。

## Key Claims

- explicit: `agent-context-audit` 目标是检查新 Agent 在当前上下文引导下会怎么理解和行动。
- explicit: sub-agent 是答题者，只回答问题、陈述事实依据和思路，不评分。
- explicit: 主 Agent 是考官，读取项目文件建立 ground truth 并评估答卷。
- explicit: 审计维度包括答案正确性、思路正确性、探索成本、上下文污染和改进建议。
- inferred: 该方法适合审计 AGENTS.md、CLAUDE.md、README、HAT 和工作流入口是否足够清晰。

## External Links

No external links found in extracted content.

## Links

- compiled-concept: [[concepts/Agent 上下文审计|Agent 上下文审计]] — 定义用 sub-agent 答题、主 Agent 建立 ground truth 和评分的上下文审计方法。
- updates: [[concepts/Agent 工作流技能编排|Agent 工作流技能编排]] — 补充 Matt Pocock 扩展 skill 在工作流链路中的位置。
- updates: [[concepts/Agent Skills|Agent Skills]] — 补充 workflow/helper/lightweight skills 的具体节点。
- compiled-entity: [[entities/Matt Pocock|Matt Pocock]] — 提供 Matt Pocock Skills 扩展集证据。
- map-entry: [[maps/Vibe Coding 工具地图|Vibe Coding 工具地图]] — 纳入 Matt Pocock Skills 工具 cluster。

## Maintenance Notes

- XMind helper 成功导出全部 1 个 sheet；每个 sheet 已在本次批量 ingest 中读取并消化。
- 本 source note 是批量 ingest 生成的消化层，不保存完整 raw 导出；需要细节时应回 raw XMind。
