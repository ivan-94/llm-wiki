---
source_type: image
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/工具/mattpocock:skills  ⭐/setup.png"
source_relpath: "Vibe/工具/mattpocock:skills  ⭐/setup.png"
raw_created_at: 2026-05-05T12:48:47.825804+00:00
raw_modified_at: 2026-05-05T12:48:47.826269+00:00
raw_size: 1728909
raw_fingerprint: "size=1728909;birth=2026-05-05T12:48:47.825804+00:00;mtime=2026-05-05T12:48:47.826269+00:00"
raw_snapshot_at: 2026-05-30T00:07:20+08:00
ingested_at: 2026-05-30
status: ingested
---

# setup.png

## Source

- Raw file: [Vibe/工具/mattpocock:skills  ⭐/setup.png](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/%E5%B7%A5%E5%85%B7/mattpocock%3Askills%20%20%E2%AD%90/setup.png>)
- Raw ref: `raw:Vibe/工具/mattpocock:skills  ⭐/setup.png`
- Type: image
- Status: ingested
- Raw metadata: created `2026-05-05T12:48:47.825804+00:00`; modified `2026-05-05T12:48:47.826269+00:00`; size `1728909`; snapshot `2026-05-30T00:07:20+08:00`
- Coverage: Vision read of a 928 x 1695 infographic. Process, exploration checklist, three confirmation areas, outputs, and general rules are readable; some small explanatory copy is summarized.

## Summary

这张图说明 `setup-matt-pocock-skills` 用于给工程 skills 配上最小必要上下文，适合在第一次使用 `to-issues`、`to-prd`、`triage`、`diagnose`、`tdd`、`architecture` 等 skill 前运行。它要求先探索 repo，确认 issue tracker、triage labels 和 domain docs 三件事，再把约定写入 `AGENTS.md` / `CLAUDE.md` 与 `docs/agents/` 文档。

## Source Digest

图的流程从“探索 repo 现状”开始，汇报已有和缺失，然后一次只确认一个决策，展示草稿，写入配置，后续 skills 再读取这些规则。左侧探索内容包括 `git remote`、`AGENTS.md`、`CLAUDE.md`、`CONTEXT.md`、`CONTEXT-MAP.md`、`docs/adr/`、`docs/agents/` 和 `.scratch/`。中间需要确认三件事：Issue tracker 是 GitHub、GitLab、local markdown 还是其他；Triage labels 包括 `needs-triage`、`needs-info`、`ready-for-agent`、`ready-for-human`、`wontfix` 等；Domain docs 是 single-context 还是 multi-context。右侧写入产物包括 `AGENTS.md` 或 `CLAUDE.md`、`docs/agents/issue-tracker.md`、`docs/agents/triage-labels.md`、`docs/agents/domain.md`。底部规则强调不要假设、一次只问一个、不要覆盖已有配置、缺文档时静默继续并按需创建。

## Key Claims

- explicit: `setup-matt-pocock-skills` 应在第一次使用多个工程 skill 前运行，为它们提供必要上下文。
- explicit: 该流程需要确认 issue tracker、triage labels 和 domain docs 三件事。
- explicit: 写入产物包括 `AGENTS.md` 或 `CLAUDE.md`，以及 `docs/agents/issue-tracker.md`、`triage-labels.md`、`domain.md`。
- explicit: 通用规则包括不要假设、一次只问一个、不要覆盖已有配置、静默继续。
- inferred: 该 setup skill 的重点不是安装工具，而是让后续工程 skill 共享 repo 的协作约定和领域入口。

## External Links

No external links found in extracted content.

## Links

- related: Agent Skill 项目上下文初始化 — 可沉淀 issue tracker、triage label、domain docs 三类上下文初始化规则。
- related: Vibe 工具与 Agent Skills 学习地图 — 可作为 mattpocock skills 中“setup/context bootstrap”分支。

## Maintenance Notes

- 图片清晰，结构信息可靠；小字号说明未逐字 OCR。
- 未实际检查对应 skill 的实现，只按图片内容记录。
