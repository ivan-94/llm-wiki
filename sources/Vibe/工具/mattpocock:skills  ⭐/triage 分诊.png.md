---
source_type: image
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/工具/mattpocock:skills  ⭐/triage 分诊.png"
source_relpath: "Vibe/工具/mattpocock:skills  ⭐/triage 分诊.png"
raw_created_at: 2026-05-05T12:35:32.978414+00:00
raw_modified_at: 2026-05-05T12:35:32.978678+00:00
raw_size: 1602929
raw_fingerprint: "size=1602929;birth=2026-05-05T12:35:32.978414+00:00;mtime=2026-05-05T12:35:32.978678+00:00"
raw_snapshot_at: 2026-05-29T16:07:40+00:00
ingested_at: 2026-05-30
status: ingested
---

# triage 分诊.png

## Source

- Raw file: [Vibe/工具/mattpocock:skills  ⭐/triage 分诊.png](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/%E5%B7%A5%E5%85%B7/mattpocock%3Askills%20%20%E2%AD%90/triage%20%E5%88%86%E8%AF%8A.png>)
- Raw ref: `raw:Vibe/工具/mattpocock:skills  ⭐/triage 分诊.png`
- Type: image
- Status: ingested
- Raw metadata: created `2026-05-05T12:35:32.978414+00:00`; modified `2026-05-05T12:35:32.978678+00:00`; size `1602929`; snapshot `2026-05-29T16:07:40+00:00`
- Coverage: Vision ingest of the full 864x1821 vertical infographic; role labels, status machine, process steps, outputs, rules, and legend were inspected.

## Summary

这张图把 issue triage 设计为一个状态机：每个 issue 只能保留一个类别角色和一个状态角色。类别角色主要是 bug 或 enhancement；状态从 unlabelled 进入 needs-triage，再分流到 needs-info、ready-for-agent、ready-for-human 或 wontfix，并产生对应交付物。

## Source Digest

图中先建立标签约束：一个 issue 只保留一个 Category Role 和一个 Status Role，避免多状态叠加导致责任不清。处理流程要求先读取正文、评论、标签、历史和 triage notes，再检查 `.out-of-scope`，探索代码与 domain docs，推荐类别与状态；如果是 bug，先复现；必要时通过 `grill-with-docs` 追问或补全上下文，最后设置标签、评论、更新文档或关闭。

状态机表达了从发现到交付的分流：`unlabelled` 表示待发现或分配，`needs-triage` 等待维护者评估，`needs-info` 等待报告者补充，`ready-for-agent` 表示规格完整可交给 AFK agent，`ready-for-human` 表示需要人类判断或外部权限，`wontfix` 表示不处理。输出也随状态变化：ready-for-agent 生成 Agent Brief，needs-info 生成 triage notes，wontfix/enhancement 写入 out-of-scope 并关闭 issue。底部规则强调 tracker 评论必须以 AI triage disclaimer 开头，异常状态迁移先问维护者，issue brief 要行为化、耐重构，不写实现细节。

## Key Claims

- explicit: 每个 issue 只保留一个类别角色和一个状态角色。
- explicit: 类别角色包括 bug 与 enhancement。
- explicit: 状态流包括 unlabelled、needs-triage、needs-info、ready-for-agent、ready-for-human 和 wontfix。
- explicit: triage 一个 issue 时应读取正文、评论、标签、历史、triage notes，检查 `.out-of-scope`，探索代码和 domain docs，再推荐类别与状态。
- explicit: bug 在进入结论前应优先尝试复现。
- explicit: ready-for-agent 应产出 Agent Brief，包含 current behavior、desired behavior、key interfaces、acceptance criteria 和 out of scope。
- inferred: 该状态机的主要价值是把“能否交给 agent”从普通优先级判断中拆出来，用状态标签表达上下文完备度和执行责任。

## External Links

No external links found in extracted content.

## Links

- related: Issue 分诊状态机 — 可沉淀类别角色、状态角色、分流规则和 Agent Brief 输出。
- related: Vibe Coding 工作流学习地图 — 可作为 issue 进入 agent 执行前的治理节点。

## Maintenance Notes

- Vision-based ingest; exact tracker label spelling was readable for main labels, but should be checked against raw image or repository conventions before automation.
- No index/log updates were made because this batch worker was restricted to the five source notes only.
