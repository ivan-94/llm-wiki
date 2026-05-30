---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 4
learning_status: new
confidence: 2
difficulty: 3
review_after: 2026-06-10
---

# Skill 触发契约

## Definition

Skill 触发契约是 skill 在何时、由谁、基于什么条件被激活的规则集：包括触发词/触发条件（`description` 字段）、持续时间（一次性 vs 持续激活）、注入方式（强注入 vs 弱注入）和前提依赖（dependency check）。它决定了 Agent 能否在正确时机使用正确 skill。

## Why It Matters

一个功能完整的 skill 如果触发契约写错，等于不存在：过宽的 `description` 让 Agent 到处触发，浪费上下文；过窄则让 Agent 在该用时想不到它。触发契约是 skill 可用性的核心控制面，独立于 skill 内容的质量。

## Mental Model

把触发契约想象成会议邀请函：
- `description`：什么情况下你应该参加（触发条件）
- 持续/一次性：这是单次会议还是固定周会
- 强注入/弱注入：是强制出席还是按需到场
- 依赖检查：参会前提条件（环境/权限是否满足）

## Key Claims

- `description` 是 Agent 决定是否读取完整 `SKILL.md` 的唯一判断依据：应写成触发条件（"Use when X"），而不是内容摘要（"This skill explains Y"）。
- `always: true` 的 skill 会在每次会话强注入 system prompt；其余 skill 以 XML 摘要弱注入，由 Agent 按需读取。
- On Demand Hooks 可以在特定事件（如会话开始、文件读取）时动态激活 skill，实现条件性强注入。
- 前提依赖检查（dependency check）让 skill 在环境不满足时给出清晰的失败信号，而不是静默执行失败。
- 轻量 workflow skill 的停止条件也是触发契约的一部分：不定义停止条件的持续 skill 会无限占用上下文。

## Examples

- `/triage` 的 `description`："Use when you need to sort issues into swimlanes, add context, and push status"——清晰的触发条件，不是摘要。
- Superpowers 的 `using-superpowers` 通过 session-start hook 强注入，确保每次会话开始时工作流框架先被激活。
- 轻量 workflow skill 示例：触发词="当用户说/ship"、持续=一次性、强注入=是（会话内）、停止条件=PR 创建完成。

## Common Confusions

- 触发契约 ≠ skill 内容：内容写得再好，触发条件模糊仍会导致 skill 失效。
- 强注入 ≠ 更好：强注入保证激活但消耗上下文；大量强注入 skill 会让上下文窗口过早饱和。
- `description` 字段 ≠ README：description 是给 Agent 读的触发判断依据，不是给人类读的说明文档。

## Evidence

- [[sources/Agent/Skills.xmind|Skills.xmind]] — 明确把 `description` 定义为触发条件，不是摘要；详述 Agent 处理 skill 的发现/激活/执行三段。
- [[sources/Agent/claude skill.pdf|claude skill.pdf]] — 描述强注入/弱注入机制和 On Demand Hooks 的条件激活原理。
- [[sources/Agent/变体/Nano Bot .xmind|Nano Bot .xmind]] — 通过强/弱注入区分说明 skill 注入方式对上下文管理的影响。
- [[sources/Vibe/工具/superpower.xmind|superpower]] — Superpowers 通过 session-start hook 的强注入展示触发契约的实际应用。

## Relations

- part-of: [[concepts/Agent Skills|Agent Skills]] — 触发契约是 skill 设计的核心控制面，决定 skill 能否有效工作。
- related: [[concepts/上下文工程|上下文工程]] — 强/弱注入是上下文工程在 skill 层的体现。
- enables: [[concepts/AI 软件工厂|AI 软件工厂]] — 精确的触发契约让软件工厂的 skill 流水线在正确节点自动激活。
- map-entry: [[maps/Vibe Coding 工具地图|Vibe Coding 工具地图]]

## My Understanding

Skill 触发契约是"skill 能不能被用到"和"skill 好不好用"的分水岭——写 skill 内容的时间，应该分出至少一半给触发条件的设计。

## Review Questions

- 为什么 `description` 应写成触发条件而不是摘要？
- 强注入和弱注入各适合什么场景？
- 停止条件为什么是触发契约的一部分？
- On Demand Hooks 解决什么问题？

## Open Questions

- skill 触发冲突（多个 skill 同时满足条件）时的优先级机制还没有统一方案。
