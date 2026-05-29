---
page_type: synthesis
updated_at: 2026-05-29
status: active
source_count: 10
learning_status: learning
confidence: 2
difficulty: 4
review_after: 2026-06-05
---

# GitHub 驱动的 Agent 开发闭环

## Thesis

GitHub 可以从代码托管平台升级为 Agent 协作的状态机：PRD、issue、branch/worktree、review、CI、HAT、PR 和 merge 共同构成可追踪闭环。

## Comparison

| 环节 | 人类目标 | Agent 资产 |
| --- | --- | --- |
| PRD | 对齐目标、非目标、验收标准 | Source Manifest、决策记录、风险 |
| Issue | 拆成可独立抓取的垂直切片 | 明确输入、边界、验收、状态 |
| Worktree | 隔离实现和并发执行 | 独立分支、运行时、日志 |
| Review | 检查 bug、风险、缺测试 | cross-review、self-review、diff evidence |
| HAT | 从用户路径验收 | guide、prepare.sh、artifacts、human report |
| PR | 对外交付和合并 | PR body、测试证据、open risks |

## Evidence

- [[sources/Vibe/工具/Github 原住民.xmind|Github 原住民]] 将 Projects、Sub-Issues、Dependencies、Actions、Milestones 等视为 Agent 工作流基座。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/基于 github 的工作流.png|基于 github 的工作流]] 展示 GitHub 驱动的 skill 流程。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/to_prd__to_issue.png|to_prd__to_issue]] 说明 PRD 到垂直切片 issue。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/triage 分诊.png|triage 分诊]] 展示 issue 分诊状态机。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/tdd.png|tdd]] 将实现切片和测试闭环连接起来。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/我的流程.xmind|我的流程]] 汇总用户侧工作流链路。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/定制化.xmind|定制化]] 包含 deliver、review、HAT 和 context audit 等工作流节点。

## Implications

- Agent 交付需要稳定的工作单元；issue 和 PRD 是比聊天上下文更耐用的入口。
- HAT 不是测试替代品，而是把用户路径、环境准备和验收证据落成可交接产物。
- GitHub 原生状态机需要和项目本地 AGENTS/CONTEXT/HAT 文档配合，否则 Agent 仍会重新探索。

## Related Concepts

- [[concepts/Agent Skills|Agent Skills]]
- [[concepts/Agent Harness|Agent Harness]]
- [[concepts/Agentic Engineering|Agentic Engineering]]

## My Take

最稳的闭环是：PRD 定义方向，issue 定义切片，worktree 隔离执行，review 查风险，HAT 验用户路径，PR 汇总证据。

## Open Questions

- GitHub 当前 Sub-Issues、Dependencies、Projects 行为未联网核验。
- 不同仓库是否值得引入完整 HAT 链路，需要按风险和交付频率判断。
