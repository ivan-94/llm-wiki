---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 1
learning_status: new
confidence: 2
difficulty: 3
review_after: 2026-06-13
---

# Implementation Notes 审计

## Definition

Implementation Notes 审计是让 Agent 在开发过程中同步维护一份轻量记录，把实现时做出的判断、偏差、权衡和未决问题显式化，方便 code review 和下游 Agent 审计——而不是把所有决策推给人类实时跟踪或事后考古。

## Why It Matters

大型需求的 spec 永远无法覆盖所有边界；过度规约让启动变慢且仍无法穷举。完全放手则让隐性决策藏进 diff，等 review 时才暴露。Implementation Notes 是 spec 与 diff 之间的决策可追溯层。

## Mental Model

Implementation Notes = spec 的下游补丁 = "我在实现中做了哪些 spec 没有说的判断"。

## Four-Category Framework

| 类别 | 说明 |
| --- | --- |
| 设计决策 | 补足 spec 空白处做出的实现选择 |
| 偏差说明 | 主动偏离规范或约定的原因 |
| 权衡记录 | 未采用的替代方案和放弃理由 |
| 未决问题 | 需要人类判断或确认的点 |

## Carrier Format

HTML 或 Markdown 文件均可，关键属性：
- 轻量、可读
- 能随 PR 一起提交，纳入版本历史
- 可随代码文件一起 diff

建议路径：`implementation-notes.md` 或 `implementation-notes.html`，放在 PR 的根目录或 feature 目录。

## Key Claims

- explicit：大型需求中 spec 永远无法覆盖所有边界，人类也无法实时跟踪 Agent 的每一个判断。
- explicit：偏移控制的关键是承认歧义不可避免，并把 Agent 的"判断"变成可审计产物。
- explicit：Implementation Notes 应覆盖设计决策、偏差、权衡和未决问题四类信息。
- inferred：`implementation-notes` 的作用不是替代 spec，而是补上 spec 与 diff 之间的决策可追溯层。

## Examples

- Agent 实现鉴权逻辑时，在 notes 中记录"选择 JWT 而非 session 的原因：需要横跨多个微服务，无 session store 依赖"。
- Agent 偏离 AGENTS.md 里的命名约定时，在 notes 中说明"因为该接口面向外部合作方，保留了其原有命名"。
- notes 中标记未决问题："是否需要对 `/admin` 路径单独加速率限制，需要产品确认"。

## Common Confusions

- Implementation Notes 不是替代 spec 或 commit message，而是补充 spec 未覆盖的实现层判断。
- 不应写成 changelog 或 how-to 说明；只需记录"为什么这样做而不是那样做"。

## Evidence

- [[sources/Vibe/Vibe Coding 随手记/大规模 AI Coding/大型需求的偏移控制审计方向.xmind|大型需求的偏移控制审计方向]] — 提出 `implementation-notes` 的完整动机、四类信息和载体建议。

## Relations

- part-of: [[concepts/AI Coding 偏移控制|AI Coding 偏移控制]] — 审计方向是偏移控制工具链的可追溯层
- supports: [[concepts/反捷径证据|反捷径证据]] — notes 中的权衡和偏差记录为反捷径审查提供输入
- reduces-risk: [[concepts/软件工厂陷阱|软件工厂陷阱]] — notes 让 Agent 的判断从隐性变成显性，降低考古成本
- map-entry: [[maps/Vibe Coding 学习地图|Vibe Coding 学习地图]]

## My Understanding

当前理解：Implementation Notes 是"让 diff 可解释"的最小工程实践，不需要改变开发流程，只需要 Agent 边做边记录判断。

## Review Questions

- 为什么 implementation notes 应该随 PR 一起提交？
- 四类信息中哪类最容易被忽略？
- notes 和 commit message 的区别是什么？

## Open Questions

- 在大型 Agent 任务中，notes 更新的时机和粒度还需要实践规范。
