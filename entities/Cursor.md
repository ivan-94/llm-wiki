---
page_type: entity
updated_at: 2026-05-30
status: active
source_count: 2
---

# Cursor

## What It Is

Cursor 是 AI 编程 IDE。raw 资料将其作为 AI Coding 工具案例，重点记录 Cursor Tab、聊天上下文、代码库索引、`.cursorrules`、Shadow Workspace 和 Composer。

## Role In This Wiki

Cursor 用于说明 Vibe Coding 工具如何把上下文工程、编辑器入口、多文件修改和规则提示结合到开发者工作流中。

## Key Facts

- Cursor Tab 被记录为上下文相关的多行、多处和导入补全（推测使用自研小模型平衡成本和性能）。
- `@Codebase` 工作流包含代码库向量索引、查询和 rerank，`.cursorignore` 控制索引范围。
- `.cursorrules` 用于项目级 AI 行为约束，等价于 Claude Code 的 CLAUDE.md 项目级规则。
- Shadow Workspace 被记录为在影子工程中验证 AI 生成代码的能力，与 Claude Code 的无头模式/SubAgent 有功能对应关系。

**Composer vs CLI Agent 对比：**

| 维度 | Cursor Composer | Claude Code CLI |
| --- | --- | --- |
| 界面 | IDE 内嵌 GUI | 终端 CLI |
| 上下文注入 | `@` 引用 + 代码库索引 | CLAUDE.md + rules + MCP |
| 多文件编辑 | 内置支持 | 无头模式 + SDK |
| 编排能力 | 当前以单 session 为主 | SubAgent / Teams / 动态工作流 |
| 主要定制方式 | `.cursorrules` / prompt 库 | CLAUDE.md / skills / hooks |

- 当前页面没有联网核验 Cursor 当前产品能力。

## Related Concepts

- used-in: [[concepts/Vibe Coding|Vibe Coding]]
- related: [[concepts/上下文工程|上下文工程]] — Cursor 的 `@Codebase`、`.cursorrules` 和上下文入口是上下文工程在 IDE 层的体现
- contrasts-with: [[entities/Claude Code|Claude Code]] — Claude Code 是终端优先+SDK定制，Cursor 是 IDE 内嵌+代码库索引
- contrasts-with: [[entities/Codex|Codex]] — Codex 主打云端托管容器，Cursor 主打 IDE 本地体验
- map-entry: [[maps/Vibe Coding 工具地图|Vibe Coding 工具地图]]

## Evidence

- [[sources/案例/Cursor.xmind|Cursor.xmind]]
- [[sources/Vibe/Vibe Coding 随手记/大规模 AI Coding/claude code 大型项目落地.PNG|claude code 大型项目落地]]

## Open Questions

- Cursor 当前快捷键、产品形态和上下文限制需要按官方资料核验。
