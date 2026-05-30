---
page_type: synthesis
updated_at: 2026-05-30
status: active
source_count: 13
learning_status: learning
confidence: 3
difficulty: 4
review_after: 2026-06-10
---

# GitHub 驱动的 Agent 开发闭环

## Thesis

GitHub 可以从代码托管平台升级为 Agent 协作的状态机：PRD、issue、branch/worktree、review、CI、HAT、PR 和 merge 共同构成可追踪闭环。GitHub 原住民六层机制（Issue/Sub-Issues/Projects/PR/Milestones/Discussions）为 Agent 工作流提供可靠的任务入口、状态管理和证据流转基础。

## Comparison

| 环节 | 人类目标 | Agent 资产 |
| --- | --- | --- |
| PRD | 对齐目标、非目标、验收标准 | Source Manifest、决策记录、风险 |
| Issue | 拆成可独立抓取的垂直切片 | 明确输入、边界、验收、状态 |
| Worktree | 隔离实现和并发执行 | 独立分支、运行时、日志 |
| Review | 检查 bug、风险、缺测试 | cross-review、self-review、diff evidence |
| HAT | 从用户路径验收 | guide、prepare.sh、artifacts、human report |
| PR | 对外交付和合并 | PR body、测试证据、open risks |

## GitHub 原住民六层基础（来自 `Github 原住民.xmind`）

完整 GitHub 治理分为六层，每层在 Agent 工作流中有特定职责：

| 层 | GitHub 机制 | Agent 工作流职责 |
| --- | --- | --- |
| 1 | **Issue + Labels** | 唯一任务源；Label 承担路由和分诊角色 |
| 2 | **Sub-Issues + Dependencies** | 任务拆解和依赖建模；子 issue 关闭触发主 issue 进度更新 |
| 3 | **Projects（看板）** | 跨阶段可视化；Backlog → In Progress → Review → Done 状态机 |
| 4 | **PR（质量闸门）** | 带 checklist、issue 关联（`Closes #xxx`）、分级 review 和 CI 的证据层 |
| 5 | **Milestones / Releases** | 版本节奏控制和交付里程碑追踪 |
| 6 | **Discussions** | 分离社区噪音（问法/咨询），保持 issue 池纯净 |

**最小可用版本（一人/小团队）：**
- bug/feature issue 模板 + type/priority/status 标签
- Backlog → In Progress → Review → Done 看板
- 强制 `Closes #xxx` 的 PR 模板
- CI 测试 + PR 自动打标签 + stale 提醒 Actions

## Matt Pocock Triage Labels 模式

Matt Pocock 把 GitHub Labels 升格为 Agent 工作流的状态路由机制：

**Issue 泳道 Labels（推荐）：**
- `needs-info` — 缺少足够信息，需要人工补充
- `ready-for-agent` — 有足够 Brief，可交给 Agent 执行
- `in-progress` — Agent 正在执行
- `needs-human-review` — Agent 完成，需要人工审查

**PR 泳道 Labels：**
- `hat-ready` — 已通过 CI 和 review，等待 HAT 验收
- `hat-passed` — HAT 验收通过，可合并
- `hat-needs-human` — 自动化 HAT 无法覆盖，需要人工验收步骤

**重要说明：** Skills ≠ 自动 Runner。`/triage`、`/deliver-issue`、`/hat-dispatch` 等 skills 是 Agent 执行的命令，不是 GitHub Actions 自动触发器；需要人工或看板工具（agent-board）选择 issue 并手动启动。

## Agent Brief 在闭环中的角色

Agent Brief 是闭环中连接 triage 和执行的关键产物：

```
PRD → to-issues → triage → [Agent Brief] → worktree + TDD → cross-review → HAT → PR → merge
```

Brief 包含：任务目标 + 输入/边界 + 非目标 + 决策约束 + 验收标准。没有 Brief 的 issue 不应进入 `ready-for-agent` 泳道。

## Evidence

- [[sources/Vibe/工具/Github 原住民.xmind|Github 原住民]] — 六层 GitHub 治理体系，最小可用版本，Discussion/Issue 分离模式。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/基于 github 的工作流.png|基于 github 的工作流]] — GitHub 驱动的 skill 流程全景图。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/Matt Pocock Skills.xmind|Matt Pocock Skills]] — GitHub Issue 升格为 AI 协作协议层的完整阐述（Label/Comment/Webhook/Reference 角色）。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/to_prd__to_issue.png|to_prd__to_issue]] — PRD 到垂直切片 issue 的产物结构。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/triage 分诊.png|triage 分诊]] — issue 分诊状态机和 Agent Brief 产出时机。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/tdd.png|tdd]] — 实现切片和 TDD 闭环。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/我的流程.xmind|我的流程]] — 用户侧端到端工作流链路。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/定制化.xmind|定制化]] — deliver、review、HAT 和 context audit 节点。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/看板管理.xmind|看板管理]] — 把工作流产品化为 agent-board 看板的设计草案（含 triage labels 查询模型）。

## Implications

- Agent 交付需要稳定的工作单元；issue 和 PRD 是比聊天上下文更耐用的入口。
- HAT 不是测试替代品，而是把用户路径、环境准备和验收证据落成可交接产物。
- GitHub 原生状态机需要和项目本地 AGENTS/CONTEXT/HAT 文档配合，否则 Agent 仍会重新探索。

## Related Concepts

- related: [[concepts/Agent Skills|Agent Skills]]
- related: [[concepts/Agent Harness|Agent Harness]]
- related: [[concepts/Agentic Engineering|Agentic Engineering]]
- related: [[concepts/Agent Brief|Agent Brief]] — Brief 是 triage 产出、进入 ready-for-agent 泳道的必要条件
- related: [[concepts/Vertical Slice Issue|Vertical Slice Issue]] — Slice 是 issue 的结构要求
- related: [[concepts/反馈工程（Feedback Engineering）|反馈工程（Feedback Engineering）]] — HAT + CI 是闭环中反馈信号的核心载体

## My Take

最稳的闭环是：PRD 定义方向，issue 定义切片，worktree 隔离执行，review 查风险，HAT 验用户路径，PR 汇总证据。

## Open Questions

- GitHub 当前 Sub-Issues、Dependencies、Projects 行为未联网核验。
- 不同仓库是否值得引入完整 HAT 链路，需要按风险和交付频率判断。
