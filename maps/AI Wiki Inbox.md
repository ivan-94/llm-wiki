---
page_type: map
updated_at: 2026-06-05
status: active
scope: human-inbox
---

```dataview
TABLE inbox_created_at AS "Created", type AS "Type", source_kind AS "Kind", inbox_status AS "Status"
FROM "human/inbox"
WHERE inbox_status = "unread"
SORT inbox_created_at DESC
LIMIT 30
```

## Human Raw Promotion

- [[human/sources/inbox/cook-my-mind/2026-06-02_Codex作为个人系统超级入口|Codex 作为个人系统超级入口]] — 记录 cook -> digest -> ingest -> query 的个人知识闭环，并说明 inbox 不是 canonical 终点。
