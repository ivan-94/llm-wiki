---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 3
learning_status: new
confidence: 3
difficulty: 3
review_after: 2026-06-06
---

# AGENTS.md 设计模式

## Definition

AGENTS.md 设计模式是把项目事实、验证命令、工程约定、权限边界、工作流和局部规则组织成 Agent 可读入口的做法。

## Why It Matters

Agent 会先猜测项目结构、测试命令、风格和边界；AGENTS.md 的价值是把高频、易错、影响验证的知识显式化，减少无效探索和错误改动。

## Mental Model

AGENTS.md 是项目给 Agent 的目录和操作契约，不是百科全书。

## Progressive Disclosure Architecture

不同工具生态采用类似但命名不同的渐进披露机制：

| 工具 | 全局入口 | 局部规则 | Skill/专项 |
| --- | --- | --- | --- |
| OpenAI Codex | `AGENTS.md` (根) | 目录级 `AGENTS.md` | — |
| Claude Code | `CLAUDE.md` (根) | `CLAUDE.md` (子目录) | `.claude/` rules |
| Cursor | `AGENTS.md` / `.cursorrules` | `.cursor/rules/` | skills |

核心共识：
- 根文件是 Agent 启动时无条件读取的全局入口。
- 目录级或局部文件按任务范围动态读入，减少无关上下文噪声。
- Skill 文件把专项任务（重构/测试/惯例）从全局规则中分离，按需激活。

渐进披露原则：
- 全局规则约束"不能做什么"和"必须做什么"（宪法层）。
- 目录级规则约束"这个模块的特殊约定"。
- Skill/rules 约束"这类任务的专项流程"。

## Key Claims

- AGENTS.md 应记录环境准备、目录结构、技术栈、验证命令和局部规则。
- 好的规则像 prompt：聚焦、无歧义、结构清晰、带示例和反例。
- 规则过长时应拆分到 docs 或目录级 AGENTS.md，使用渐进披露。
- AGENTS.md 与 harness 的关系是入口和索引，具体约束应尽量落到测试、lint、hook、脚本或文档。
- inferred: Claude CLAUDE.md 与 AGENTS.md 在结构和意图上等价，主要差异在 skills/rules 的激活机制。

## Evidence

- [[sources/Vibe/Spec/AGENTS.md 全局记忆.xmind|AGENTS.md 全局记忆]]
- [[sources/Vibe/Harness Engineering.xmind|Harness Engineering.xmind]]
- [[sources/Vibe/工具/codex/cli.png|codex cli]]

## Relations

- part-of: [[concepts/Agent Harness|Agent Harness]]
- enables: [[concepts/Agent 全局记忆|Agent 全局记忆]]
- supports: [[concepts/上下文工程|上下文工程]]
- map-entry: [[maps/Vibe Coding 学习地图|Vibe Coding 学习地图]]

## My Understanding

当前理解：AGENTS.md 应该让 Agent 快速进入正确轨道，而不是把全部项目知识塞进上下文。

## Review Questions

- AGENTS.md 里哪些内容必须全局，哪些应该拆到局部文档？
- 为什么 AGENTS.md 不应变成百科全书？

## Open Questions

- 不同规模仓库的 AGENTS.md 最佳长度和拆分粒度仍需案例沉淀。
