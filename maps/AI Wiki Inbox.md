---
page_type: map
updated_at: 2026-06-03
status: active
scope: human-inbox
---

```dataview
TABLE inbox_created_at AS "Created", type AS "Type", source_kind AS "Kind", inbox_status AS "Status"
FROM "human/inbox"
SORT inbox_created_at DESC
LIMIT 30
```