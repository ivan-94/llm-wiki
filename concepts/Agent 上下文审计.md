---
page_type: concept
updated_at: 2026-06-01
status: active
source_count: 3
learning_status: new
confidence: 2
difficulty: 4
review_after: 2026-06-08
---

# Agent 上下文审计

## Definition

Agent 上下文审计是一种用隔离 sub-agent 模拟新会话认知的审计方法：主 Agent 设计场景题并建立 ground truth，sub-agent 只按当前入口材料回答问题和说明依据，最后由主 Agent 评估答案正确性、推理路径、探索成本和上下文污染。

## Why It Matters

AGENTS.md、README、HAT 文档、skill 描述和工作流入口可能同时存在，越复杂越容易让新 Agent 误解边界、重复探索或继承污染上下文。上下文审计能用真实“新 Agent 会怎么做”的证据，反推哪些入口、规则或 handoff 需要改。

## Mental Model

把它当成 Agent 入职考试：

```text
主 Agent 出题 -> sub-agent 独立答题 -> sub-agent 报探索账单 -> 主 Agent 查证 ground truth -> 输出修复建议
```

- sub-agent 是答题者，只回答问题、列依据、区分事实与推断。
- 主 Agent 是考官，负责读取项目文件、建立标准答案和评价失败模式。
- 审计对象不是代码质量本身，而是上下文入口是否能让新 Agent 形成正确行动模型。

## Key Claims

- explicit: `agent-context-audit` 的目标是检查新 Agent 在当前上下文引导下会怎么理解和行动。
- explicit: 每道场景题可以 fork 独立 sub-agent，避免答案之间相互污染。
- explicit: sub-agent 需要在自然回答后报告探索账单，包括读取文件、关键路径、来源和证据/推断边界。
- explicit: 主 Agent 评价维度包括答案正确性、思路正确性、探索成本、上下文污染和改进建议。
- inferred: 该方法适合审计 AGENTS.md、CLAUDE.md、README、HAT、workflow docs 和 skill 触发描述是否足够清晰。
- inferred: skill 审查和上下文审计互补：前者看单个 skill 的触发/契约/输出，后者看新 Agent 在项目入口里的整体认知。

## Audit Dimensions

- 答案正确性：是否得出项目真实规则和当前状态。
- 推理路径：是否优先读取权威入口，而不是被噪音或旧文档带偏。
- 探索成本：为了回答一个问题读了多少文件、走了多少岔路。
- 上下文污染：是否把旧摘要、相邻项目规则或无关 skill 当成当前事实。
- 修复建议：是否能定位到应改的入口文档、skill 描述、handoff 或 Source Manifest。

## Evidence

- [[sources/Vibe/工具/mattpocock:skills  ⭐/Ext 上下文检查agent-context-audit.xmind|agent-context-audit]] — 定义答题者/考官模型、探索账单和审计维度。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/Ext Skills 审查.png|Ext Skills 审查]] — 提供 skill 失败模式和审查输出要求，可与上下文审计互补。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/我的流程.xmind|我的流程]] — 把 context audit 放在工作流治理阶段。

## Relations

- used-in: [[concepts/Agent 工作流技能编排|Agent 工作流技能编排]] — 上下文审计是工作流治理阶段的质量反馈。
- related: [[concepts/Skill 触发契约|Skill 触发契约]] — skill 描述和触发条件是上下文审计的常见修复点。
- related: [[concepts/探索-执行上下文隔离|探索-执行上下文隔离]] — 两者都关注防止探索噪声污染执行。
- enables: [[concepts/AGENTS.md 设计模式|AGENTS.md 设计模式]] — 审计结果可反向改进项目入口规则。
- part-of: [[concepts/Agent Harness|Agent Harness]] — 审计是 harness learning layer 的一种反馈采样方式。
- map-entry: [[maps/Vibe Coding 工具地图|Vibe Coding 工具地图]]

## My Understanding

当前理解：上下文审计不是问“文档写得好不好”，而是让一个新 Agent 真实答题，观察它会在哪里误解、绕路或被旧上下文污染。

## Review Questions

- 为什么 sub-agent 不能给自己评分？
- 探索账单要记录哪些信息？
- 上下文审计和 skill 审查的边界是什么？

## Open Questions

- 上下文审计的最低题量和评分格式还需要按项目复杂度校准。
