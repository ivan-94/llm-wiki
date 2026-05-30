---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/Vibe Coding 随手记/文件系统/Karpathy LLM Wiki.xmind"
source_relpath: "Vibe/Vibe Coding 随手记/文件系统/Karpathy LLM Wiki.xmind"
raw_created_at: 2026-05-25T14:18:24.404251+00:00
raw_modified_at: 2026-05-25T15:29:32.695475+00:00
raw_size: 1702849
raw_fingerprint: "size=1702849;birth=2026-05-25T14:18:24.404251+00:00;mtime=2026-05-25T15:29:32.695475+00:00"
raw_snapshot_at: 2026-05-29T15:59:36.711532+00:00
ingested_at: 2026-05-29
status: ingested
---

# Karpathy LLM Wiki.xmind

## Source

- Raw file: [Vibe/Vibe Coding 随手记/文件系统/Karpathy LLM Wiki.xmind](finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/Vibe%20Coding%20%E9%9A%8F%E6%89%8B%E8%AE%B0/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/Karpathy%20LLM%20Wiki.xmind)
- Raw ref: `raw:Vibe/Vibe Coding 随手记/文件系统/Karpathy LLM Wiki.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2026-05-25T14:18:24.404251+00:00`; modified `2026-05-25T15:29:32.695475+00:00`; size `1702849`; snapshot `2026-05-29T15:59:36.711532+00:00`
- Coverage: helper exported all sheets; 1 sheet (`画布 1`), 76 topics.

## Summary

这份脑图围绕 Karpathy 提到的 LLM Wiki 模式，描述如何把长期收集的大量资料转化为会积累、会更新、可查询、可复用的个人知识库。它区分 raw 证据仓库、LLM 维护的 wiki 知识层和 AGENTS.md 规则层，并给出 sources、concepts、entities、synthesis、outputs、index.md、log.md 的职责。

## Source Digest

source 把 LLM Wiki 定义为一种“先编译、后查询、持续回写”的知识系统。raw 层保存未改写的事实来源，允许文章、论文、图片、数据集、repo 文档等混杂存在，且不应由 LLM 修改；wiki 层不是原文缓存，而是 LLM 从 raw 中编译出的结构化知识，包括单 source 入口、跨 source 概念页、实体页、综合分析和派生输出；规则层用 AGENTS.md/CLAUDE.md 约束 agent 的 ingest、query、compile、lint 和 file-back 行为。index.md 是内容导向的导航入口，log.md 是 append-only 操作记录，可用 Unix 工具检索。该模式强调知识复利：每次新资料进入后，不只增加孤立摘要，而是更新已有概念、关系和综合判断。

## Key Claims

- explicit: LLM Wiki 适用于长期收集大量资料，并持续转化为会积累、会更新、可查询、可复用的个人知识库。
- explicit: raw 是 source of truth，LLM 可以读取但不应修改 raw 文件。
- explicit: wiki 层是 LLM 从原文中编译出的知识结构，不是原文副本。
- explicit: sources 保存每个原始资料对应的标准化入口；concepts 是跨多篇 source 的综合理解；entities 用于人物、公司、项目、工具等实体；synthesis 用于更高层分析。
- explicit: index.md 是整个 wiki 的目录和导航页；log.md 是 append-only 操作记录，并建议统一前缀以便检索。
- explicit: File Back 指一次 query 的结果如果有长期价值，应归档回 wiki，而不是停留在聊天记录。
- inferred: 该模式与普通 query-time RAG 的区别在于，它把整理、链接和更新提前沉淀到 Markdown artifact 中。

## External Links

- discussion-source: [Karpathy LLM Wiki](https://x.com/karpathy/status/2039805659525644595) — root topic links to the source discussion; not verified.

## Links

No downstream wiki pages were created or updated in this scoped ingest.

## Maintenance Notes

- source 内含大量示例目录和模板片段；本 note 已提炼其结构和职责，没有保存完整导出。
- 外链只提取了 X/Twitter URL，未联网核验。

- Link cleanup candidate: compiled-concept: LLM Wiki — source 系统说明 raw/wiki/rules 三层结构和持续编译流程。.
- Link cleanup candidate: compiled-concept: 知识复利 — source 强调每次新增资料都更新已有概念和综合，而不是产生孤立摘要。.
- Link cleanup candidate: compiled-concept: File Back — source 将有长期价值的 query/output 归档回 wiki。.
- Link cleanup candidate: map-entry: AI Wiki 维护学习地图 — source 可作为本 wiki 规则体系的元资料。.
