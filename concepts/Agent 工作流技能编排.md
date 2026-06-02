---
page_type: concept
updated_at: 2026-06-01
status: active
source_count: 15
learning_status: new
confidence: 2
difficulty: 4
review_after: 2026-06-06
---

# Agent 工作流技能编排

## Definition

Agent 工作流技能编排是把 PRD、issue、triage、TDD、review、HAT、PR、merge 等工程阶段封装为可触发、可组合、可交接的 Agent skills。

## Why It Matters

单个 skill 只能解决局部问题；工作流编排决定多个 skill 如何传递产物、状态和验证证据，避免下一位 Agent 只继承摘要。

## Mental Model

Workflow skills 是 Agent 的工程流水线，每个节点有输入、输出、触发条件和停止条件。

## Key Claims

- 轻量 workflow skill 应明确触发词、持续性、输出形态和停止条件。
- setup/triage/to-prd/to-issue/tdd/review/hat/pr 等 skill 形成从想法到交付的链路。
- Source Manifest 是跨 Agent 交接中的关键产物，防止下游只依赖摘要。
- GitHub issue/PR 可以作为 Agent 工作流状态机和证据流转层。
- HAT 是工作流的验收协议层，`hat-prepare` 负责可复现验收条件，`hat-run` 负责按 prepare 产物执行并保存证据。
- `agent-context-audit` 属于治理阶段，用隔离 sub-agent 暴露入口文档、skill 描述和 handoff 里的认知偏差。

### 硬依赖图（来自 `地图2.png`）

主流 workflow skills 的前提依赖关系：

```
setup → grill/grill-with-docs → prototype（可选）→ to-prd → to-issues → triage
triage → [Ready For Agent] → tdd / deliver-issue
tdd → cross-review → create-pr
triage → [HAT Ready] → hat-dispatch → hat-run → hat-copilot（可选）
create-pr → merge-pr
```

关键规则：
- `to-issues` 必须在 `to-prd` 之后（prerequisite）
- `tdd` 必须在切片就绪并通过 triage 后才能启动（enables）
- `hat-prepare` 是 `hat-run`/`hat-dispatch` 的严格前提（prerequisite）

### Agent Brief 产物链

工作流产物的传递路径：

```
grill → 需求共识 → CONTEXT.md 更新
to-prd → PRD（含 Source Manifest）
to-issues → Vertical Slice Issues（含边界、验收条件）
triage → Agent Brief（Ready For Agent issue）
worktree → 隔离执行 → TDD 实现
cross-review → diff evidence + review 报告
hat-prepare → 验收环境 + prepare.sh + 验收清单
hat-run → summary.md + results.json + artifacts
create-pr → PR body（含测试证据和 open risks）
```

### 父/子 Agent + Worktree 职责分工

- **父 Agent**：探索代码库、规划切片顺序、分析并发依赖、编排子 Agent、合并结果、cross-review、准备 HAT。
- **子 Agent**：在隔离 worktree 中接受 Agent Brief，执行 TDD，产出 commit + 测试报告，只向父 Agent 汇报。
- **看板管理**（见 `看板管理.xmind`）：可作为编排 UI 候选，把 triage/delivery/HAT 的 Agent 工作流产品化为可视状态机 + 命令启动器。

### HAT 与上下文治理

- [[concepts/HAT（Hand Acceptance Test）|HAT（Hand Acceptance Test）]] 把用户路径验收拆成 prepare/run/human handoff 三段，避免实现完成后只剩人工临场判断。
- HAT-friendly 前后端改造属于工作流的项目侧前置条件：稳定选择器、URL 状态、日志、Request Id 和可观测性决定验收能否被 Agent 稳定执行。
- [[concepts/Agent 上下文审计|Agent 上下文审计]] 用 sub-agent 答题和主 Agent 评分来检查新 Agent 是否能从当前入口材料形成正确行动模型。

## Evidence

### 2026-06-01 扩展工作流刷新

- [[sources/Vibe/工具/mattpocock:skills  ⭐/Ext HAT - Hand Acceptance Test Prepare验收测试准备hat-prepare.xmind|Vibe/工具/mattpocock:skills  ⭐/Ext HAT - Hand Acceptance Test Prepare验收测试准备hat-prepare.xmind]] — 2026-06-01 raw diff refresh补充的 Matt Pocock 扩展工作流证据。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/Ext HAT - Hand Acceptance Test Run验收测试执行hat-run.xmind|Vibe/工具/mattpocock:skills  ⭐/Ext HAT - Hand Acceptance Test Run验收测试执行hat-run.xmind]] — 2026-06-01 raw diff refresh补充的 Matt Pocock 扩展工作流证据。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/Ext 上下文检查agent-context-audit.xmind|Vibe/工具/mattpocock:skills  ⭐/Ext 上下文检查agent-context-audit.xmind]] — 2026-06-01 raw diff refresh补充的 Matt Pocock 扩展工作流证据。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/Ext 流程控制setup-agent-workflow.xmind|Vibe/工具/mattpocock:skills  ⭐/Ext 流程控制setup-agent-workflow.xmind]] — 2026-06-01 raw diff refresh补充的 Matt Pocock 扩展工作流证据。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/我的流程.xmind|Vibe/工具/mattpocock:skills  ⭐/我的流程.xmind]] — 2026-06-01 raw diff refresh补充的 Matt Pocock 扩展工作流证据。

- [[sources/Vibe/工具/mattpocock:skills  ⭐/地图.png|地图.png]] — skill 全景图（推荐学习入口）
- [[sources/Vibe/工具/mattpocock:skills  ⭐/地图2.png|地图2.png]] — 硬依赖图，展示 skills 之间的前提/使能关系
- [[sources/Vibe/工具/mattpocock:skills  ⭐/to_prd__to_issue.png|to_prd__to_issue]]
- [[sources/Vibe/工具/mattpocock:skills  ⭐/triage 分诊.png|triage 分诊]]
- [[sources/Vibe/工具/mattpocock:skills  ⭐/tdd.png|tdd]]
- [[sources/Vibe/工具/mattpocock:skills  ⭐/定制化.xmind|定制化]]
- [[sources/Vibe/工具/mattpocock:skills  ⭐/我的流程.xmind|我的流程]]
- [[sources/Vibe/工具/mattpocock:skills  ⭐/基于 github 的工作流.png|基于 github 的工作流]]
- [[sources/Vibe/工具/mattpocock:skills  ⭐/看板管理.xmind|看板管理]] — 编排 UI 候选，Agent 工作流的可视状态机设计草案

## Relations

- contains: [[concepts/Agent Skills|Agent Skills]]
- contains: [[concepts/Agent Brief|Agent Brief]] — Brief 是工作流编排的任务分发核心产物
- contains: [[concepts/Vertical Slice Issue|Vertical Slice Issue]] — Slice 是编排的任务分发单元
- contains: [[concepts/HAT（Hand Acceptance Test）|HAT（Hand Acceptance Test）]] — HAT 是工作流中的验收协议层
- contains: [[concepts/Agent 上下文审计|Agent 上下文审计]] — 上下文审计是工作流治理阶段的反馈机制
- used-in: [[synthesis/GitHub 驱动的 Agent 开发闭环|GitHub 驱动的 Agent 开发闭环]]
- enables: [[concepts/反馈工程（Feedback Engineering）|反馈工程（Feedback Engineering）]] — 工作流产物链为反馈工程提供信号结构
- map-entry: [[maps/Vibe Coding 工具地图|Vibe Coding 工具地图]]

## My Understanding

当前理解：Agent 工作流技能编排的目标是把“怎么协作交付”从口头流程变成可被 Agent 反复执行的状态机。

## Review Questions

- workflow skill 和 helper skill 的边界是什么？
- Source Manifest 为什么是交接产物而不是装饰模板？

## Open Questions

- 还需要区分个人 workflow 和团队 workflow 的最小技能集。
