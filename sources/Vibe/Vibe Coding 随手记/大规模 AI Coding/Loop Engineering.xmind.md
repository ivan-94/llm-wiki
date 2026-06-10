---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/Vibe Coding 随手记/大规模 AI Coding/Loop Engineering.xmind"
source_relpath: "Vibe/Vibe Coding 随手记/大规模 AI Coding/Loop Engineering.xmind"
raw_created_at: 2026-06-09T01:31:39.257199+00:00
raw_modified_at: 2026-06-09T02:50:16.542687+00:00
raw_size: 2208984
raw_fingerprint: "size=2208984;birth=2026-06-09T01:31:39.257199+00:00;mtime=2026-06-09T02:50:16.542687+00:00"
raw_snapshot_at: 2026-06-10T13:15:09.864761+00:00
ingested_at: 2026-06-10
status: ingested
---

# Loop Engineering.xmind

## Source

- Raw file: [Vibe/Vibe Coding 随手记/大规模 AI Coding/Loop Engineering.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/Vibe%20Coding%20%E9%9A%8F%E6%89%8B%E8%AE%B0/%E5%A4%A7%E8%A7%84%E6%A8%A1%20AI%20Coding/Loop%20Engineering.xmind>)
- Raw ref: `raw:Vibe/Vibe Coding 随手记/大规模 AI Coding/Loop Engineering.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2026-06-09T01:31:39.257199+00:00`; modified `2026-06-09T02:50:16.542687+00:00`; size `2208984`; snapshot `2026-06-10T13:15:09.864761+00:00`
- Coverage: XMind helper discovered and exported all sheets; sheet count `1`; sheets: `画布 1` (21 topics).

## Source Cluster

- Directory cluster: Vibe/Vibe Coding 随手记/大规模 AI Coding
- Cluster role: expansion
- Neighbor sources:
  - extends-source: [[sources/Vibe/Vibe Coding 随手记/大规模 AI Coding/长时间任务运行.xmind|长时间任务运行.xmind]] — 本 source 把长时间任务的 workflow 方向进一步命名为 loop engineering。
  - same-cluster: [[sources/Vibe/Vibe Coding 随手记/大规模 AI Coding/为 Agents 构造并发执行环境.xmind|为 Agents 构造并发执行环境.xmind]] — worktrees 是 loop engineering 的并行隔离组件之一。
  - same-cluster: [[sources/Vibe/Vibe Coding 随手记/大规模 AI Coding/多智能体协作.xmind|多智能体协作.xmind]] — sub-agents 和验证代理是 loop engineering 的执行角色。

## Summary

这份 XMind 把 Loop Engineering 定义为从“人一轮轮提示 Agent”转向“设计系统来驱动 Agent 自我迭代”的工程方式。它列出自动化、worktrees、skills、plugins/connectors、sub-agents 和 memory 六个组件。

## Source Digest

source 的核心转变是：人不再亲自持续下达下一步指令，而是定义目标，并设计一个系统去寻找任务、分配任务、检查结果、记录完成情况、决定下一步行动。传统人驱动模式依赖人写提示词、读结果、再输入下一步；loop engineering 则把“下一步是什么”外置到自动化循环中。

六个组件各承担不同控制面：Automations 用于按计划发现和分类任务；Worktrees 让多个并行 Agent 不互相干扰；Skills 记录项目知识，避免 Agent 凭空猜测；Plugins and connectors 接入已有工具；Sub-agents 用不同角色产生想法与验证；Memory 则用 Markdown、Linear 看板等会话外载体保存完成事项和下一步计划。

## Key Claims

- explicit: Loop Engineering 意味着不再亲自向智能体逐轮下达指令，而是设计一个系统来替你驱动智能体。
- explicit: 从人驱动到自我驱动的差异在于，后者让系统负责找任务、分配任务、检查结果、记录完成和决定下一步。
- explicit: Loop Engineering 的组件包括 Automations、Worktrees、Skills、Plugins/connectors、Sub-agents 和 Memory。
- inferred: Loop Engineering 是大规模 AI Coding 中 L3 Execution 与 L5 Learning 之间的连接层：它把执行、验证、记忆和再调度组织成循环。

## External Links

- social-thread: [Loop Engineering](https://x.com/addyosmani/status/2064127981161959567) — source 标题链接；not verified.

## Links

- compiled-concept: [[concepts/Loop Engineering|Loop Engineering]] — 本 source 提供定义和六组件模型。
- updates: [[synthesis/Vibe Coding 工程化深度模型|Vibe Coding 工程化深度模型]] — 补充 L3/L5 的循环执行模型。
- map-entry: [[maps/Vibe Coding 学习地图|Vibe Coding 学习地图]] — 纳入大规模 AI Coding 与 Agentic Engineering 路径。
- extends-source: [[sources/Vibe/Vibe Coding 随手记/大规模 AI Coding/长时间任务运行.xmind|长时间任务运行.xmind]] — 将长时间任务运行的工具入口扩展为系统循环模型。

## Maintenance Notes

- 外链未联网核验；当前只记录 raw 中导出的 URL。
- source 是轻量定义型 XMind，尚未提供真实项目案例或运行度量。
