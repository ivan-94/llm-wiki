---
page_type: concept
updated_at: 2026-06-11
status: active
source_count: 3
learning_status: new
confidence: 2
difficulty: 4
review_after: 2026-06-24
---

# Loop Engineering

## Definition

Loop Engineering 是把 Agent 从“人逐轮提示的工具”升级为“由系统循环驱动的执行单元”：人定义目标和边界，系统负责发现任务、分配任务、验证结果、记录状态并决定下一步。

## Why It Matters

大规模 AI Coding 的瓶颈不只是模型会不会写代码，而是长时间任务如何持续推进、并行执行如何隔离、失败如何回写、下一步如何被可靠选择。Loop Engineering 把这些问题合成一个可设计的循环系统。

## Mental Model

Loop Engineering = 自动调度 + 隔离执行 + 项目知识 + 工具连接 + 子代理验证 + 会话外记忆。

## Key Claims

- Loop Engineering 的核心转变是从 human-driven prompting 变成 system-driven iteration。
- 六个基础组件是 Automations、Worktrees、Skills、Plugins/connectors、Sub-agents 和 Memory。
- Claude Code 动态工作流是 Loop Engineering 的一个具体实现形态：用 JavaScript 脚本持有循环、分支、中间结果和子代理编排。
- Loop Engineering 只有在目标、权限、停止条件和验证证据清楚时才是工程闭环；否则只是把多轮猜测自动化。
- Anthropic AI 研发自动化 source 补充：当 AI 执行和实验吞吐上升后，系统瓶颈会迁移到目标选择、审查、验证和协调；loop 设计必须同时治理这些人类瓶颈。

## Examples

- 定时 automation 扫描 issue/backlog，分类后分配给不同 worktree 中的 agent。
- 子代理先生成多个方案，再由验证代理按评分标准筛选。
- 动态工作流循环运行修复和验证，直到日志中不再出现目标错误或达到人工停止条件。

## Common Confusions

- Loop Engineering 不是“让 Agent 一直跑”；它需要明确停止条件、外部记忆和验证门。
- Sub-agent 不是 loop 的全部；没有 worktree、memory、skills 和 connectors，循环容易退化成同一上下文里的多轮幻觉。
- 自动化循环不替代人类目标函数；人仍要定义价值、边界和风险。

## Evidence

- [[sources/Vibe/Vibe Coding 随手记/大规模 AI Coding/Loop Engineering.xmind|Loop Engineering.xmind]] — 提供定义、从人驱动到自我驱动的对比和六组件模型。
- [[sources/Vibe/工具/Claude Code/动态工作流.xmind|动态工作流.xmind]] — 提供 Claude Code 动态工作流的具体模式和适用场景。
- [[human/sources/inbox/cook-blog/2026-06-05_当 AI 开始构建自己_Anthropic|当 AI 开始构建自己]] — human source，补充 AI 研发自动化后的人类瓶颈迁移和验证治理问题。

## Relations

- part-of: [[concepts/Agentic Engineering|Agentic Engineering]] — Loop Engineering 是 Agentic Engineering 的执行循环形态。
- requires: [[concepts/Agent 并发执行环境|Agent 并发执行环境]] — worktrees/隔离运行时让多个循环分支互不污染。
- requires: [[concepts/Agent Skills|Agent Skills]] — skills 把项目知识和操作规程注入循环。
- related: [[entities/Claude Code|Claude Code]] — 动态工作流是 Claude Code 侧的 loop 编排原语。
- related: [[concepts/Agent 工作流技能编排|Agent 工作流技能编排]] — 工作流技能提供循环中的任务拆分、验证和交接协议。
- map-entry: [[maps/Vibe Coding 学习地图|Vibe Coding 学习地图]]

## My Understanding

Loop Engineering 的要点是把“下一步该做什么”从人的临场判断，部分迁移到可审查、可中断、可恢复、可验证的系统循环中。

## Review Questions

- Loop Engineering 和普通多轮 prompt 的区别是什么？
- 六个基础组件各自解决什么风险？
- 动态工作流为什么能降低目标漂移？

## Open Questions

- 还缺少真实项目中 Loop Engineering 的运行指标，例如吞吐、返工率、验证成本和人工介入频率。
