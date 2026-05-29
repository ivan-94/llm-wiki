---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/案例/Cursor.xmind"
source_relpath: "案例/Cursor.xmind"
raw_created_at: 2024-09-12T00:39:30.020355+00:00
raw_modified_at: 2024-09-12T03:16:07.080863+00:00
raw_size: 3427492
raw_fingerprint: "size=3427492;birth=2024-09-12T00:39:30.020355+00:00;mtime=2024-09-12T03:16:07.080863+00:00"
raw_snapshot_at: 2026-05-29T22:18:10.987536+00:00
ingested_at: 2026-05-30
status: ingested
---

# Cursor.xmind

## Source

- Raw file: [案例/Cursor.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/%E6%A1%88%E4%BE%8B/Cursor.xmind>)
- Raw ref: `raw:案例/Cursor.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2024-09-12T00:39:30.020355+00:00`; modified `2024-09-12T03:16:07.080863+00:00`; size `3427492`; snapshot `2026-05-29T22:18:10.987536+00:00`
- Coverage: sheet-aware export completed for 1 sheet: `画布 1`; all exported branches were read and digested.

## Summary

这份脑图梳理 Cursor 作为 AI 编程 IDE 的主要能力：Cursor Tab 的上下文补全、聊天入口与上下文注入、代码 Review、AI 规则、Shadow Workspace 和 Composer。重点不是泛泛列工具，而是说明 Cursor 如何把代码库索引、局部编辑、规则提示和多文件变更组织成一套面向开发者的 AI Coding 工作流。

## Source Digest

Cursor Tab 被描述为区别于传统光标补全的能力：它不仅补全当前位置，还能推断当前文件前后、多行、多处变更，并自动补全导入。source 推测它可能使用自研小模型来平衡成本和性能，这反映出 IDE 内 AI 功能需要在延迟、准确率和成本之间做工程折中。

聊天部分是全图最大分支，强调 Cursor 的上下文管理哲学。普通聊天、Cmd+K、超长上下文、`@` 引用和自动添加当前文件构成多种入口；`@Codebase` 依赖代码库向量索引、查询和 rerank，默认用 `.gitignore` 排除文件，并可通过 `.cursorignore` 继续控制索引范围。上下文来源包括文件、目录、代码实体、文档、Git 提交信息、Web 搜索、聊天消息、周围定义和自定义链接。对于超大文件，source 提到 Cursor 会分块并走向量筛选，分块策略被概括为全文、框架、分块。

脑图还把 Cursor 的工程化能力扩展到 Review、AI 规则、Shadow Workspace 和 Composer：Review 用于发现潜在风险；`.cursorrules` 和 prompt 库用于项目级 AI 行为约束；Shadow Workspace 让 AI 先在影子工程中验证生成结果；Composer 则作为支持多文件增删改查的强力 Bot，适合更大范围的代码变更。

## Key Claims

- explicit: Cursor Tab 的价值在于从单点补全扩展到多行、多处、导入和上下文相关变更推断。
- explicit: Cursor 的 `@Codebase` 工作流包含代码库向量索引、查询和 rerank，用于从仓库中找出相关代码。
- explicit: Cursor 的上下文入口包括 File、Folders、Code、Docs、Git、Web、Chat、Definitions 和 Link。
- explicit: `.cursorrules` 是项目特定 AI 规则，会影响 Cursor AI 的响应结果。
- explicit: Shadow Workspace 的目标是在影子工程中先检验 AI 生成代码，从而提高生成质量。
- inferred: 这份 source 把 Cursor 定位为“上下文工程 + 编辑器入口 + 多文件执行”的 AI Coding 工具，而不仅是聊天插件。

## External Links

- prompt-library: [Prompt 库](https://cursor.directory/) — source 中作为 Cursor 规则/提示词参考；not verified.

## Links

- compiled-entity: [[entities/Cursor|Cursor]] — source 提供 Cursor Tab、Composer、@Codebase、上下文入口、`.cursorrules` 和 Shadow Workspace 的产品能力证据。
- related: [[concepts/Vibe Coding|Vibe Coding]] — Cursor 是 AI Coding 工具案例，可为后续补充工具链实践证据。
- related: [[concepts/Agentic Engineering|Agentic Engineering]] — Composer、Shadow Workspace 和代码库上下文体现 agent 化开发环境的早期形态。
- related: [[maps/Vibe Coding 工具地图|Vibe Coding 工具地图]] — 可作为后续工具地图中的 Cursor 条目候选。

## Maintenance Notes

- 未联网核验 Cursor 当前产品能力、快捷键、token 限制或 prompt 库状态。
- `Composer` 分支末尾存在空节点，已按占位处理。
- Compile candidate: Cursor 可作为 entity-candidate；Cursor Tab、Shadow Workspace、Composer 可作为工具能力候选概念。
