---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/Vibe Coding 随手记/Harness/Agent Harness Engineering.xmind"
source_relpath: "Vibe/Vibe Coding 随手记/Harness/Agent Harness Engineering.xmind"
raw_created_at: 2026-05-10T10:39:59.284437+00:00
raw_modified_at: 2026-05-10T10:39:59.285304+00:00
raw_size: 3108301
raw_fingerprint: "size=3108301;birth=2026-05-10T10:39:59.284437+00:00;mtime=2026-05-10T10:39:59.285304+00:00"
raw_snapshot_at: 2026-05-29T15:53:54.926742+00:00
ingested_at: 2026-05-29
status: ingested
---

# Agent Harness Engineering.xmind

## Source

- Raw file: [Vibe/Vibe Coding 随手记/Harness/Agent Harness Engineering.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/Vibe%20Coding%20%E9%9A%8F%E6%89%8B%E8%AE%B0/Harness/Agent%20Harness%20Engineering.xmind>)
- Raw ref: `raw:Vibe/Vibe Coding 随手记/Harness/Agent Harness Engineering.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2026-05-10T10:39:59.284437+00:00`; modified `2026-05-10T10:39:59.285304+00:00`; size `3108301`; snapshot `2026-05-29T15:53:54.926742+00:00`
- Coverage: exported all sheets with `export_xmind_source.py --json`; sheet count `1`; sheets: `画布 1` with 238 topics.

## Summary

这份 mind map 把 Agent Harness 定义为模型之外的运行时工程系统：提示词、规则文件、工具、MCP、文件系统、沙箱、浏览器、子智能体、hooks、日志和监控共同决定 Agent 的实际能力。核心观点是未来 AI Agent 的竞争不是单纯模型竞争，而是围绕工具、上下文、反馈、约束和执行环境的系统工程竞争。

## Source Digest

source 以 `Agent = Model + Harness` 为主轴，强调模型只是智能体系统中的一个组件，同一模型在不同 harness 下会表现出巨大差异。好的 harness 能让普通模型稳定、低错、可扩展；差的 harness 即使配强模型，也会带来上下文混乱、任务中断和行为失控。

它把 harness 拆成若干工程组件：文件系统与 Git 提供持久化状态、协同空间、版本回滚和 diff 追踪；Bash 与代码执行支撑 ReAct loop、动态工具生成和自主调试；沙箱提供安全隔离、默认运行环境和自验证能力；记忆与搜索提供长期项目规则、经验沉淀、实时知识和跨 session 学习；上下文管理通过 compaction、tool offloading 和 progressive disclosure 对抗 context rot；长任务执行通过 loop execution、planning 和 multi-agent split 防止过早停止；hooks 系统在工具调用前、文件修改后、提交前插入自动化约束和失败反馈。

source 的方法论不是“把 prompt 写得更长”，而是把每次失败转化为永久系统改进：忽略规范时沉淀 AGENTS.md、checklist 或代码模板；危险命令通过 hook、权限确认和 shell 限制拦截；长任务迷路时引入 planner、阶段目标和中间状态；代码质量差时用测试、类型检查、lint 和 review agent 阻塞。这个循环让 harness 持续棘轮化，提高系统下限。

未来方向包括多智能体协作、trace 驱动的自我分析、自动新增规则或 hook、动态生成工具、以及把 harness 从静态配置演化为 runtime + compiler。source 还特别提醒安全边界：外部 MCP 和工具描述本身可能成为 prompt 注入入口，第三方能力必须被限制。

## Key Claims

- explicit: `Agent = Model + Harness`，智能体能力由模型和围绕模型的工程系统共同决定。
- explicit: 好的 harness 可以比更强模型更重要，因为它降低错误率、提高稳定性和可扩展性。
- explicit: harness 包含提示词、AGENTS.md/CLAUDE.md、skill 文件、工具、MCP、文件系统、沙箱、浏览器、子智能体、hooks、日志、追踪、成本和延迟监控。
- explicit: 失败应该被转化为新规则、新 hook、新验证机制或新流程，让系统持续“棘轮化”。
- explicit: context rot、context compaction、tool offloading 和 progressive disclosure 是上下文管理中的关键问题与手段。
- explicit: 外部 MCP 和工具描述可能带来 prompt 注入风险，harness 设计必须包含安全边界。
- inferred: 这份 source 可作为“Agent Harness”概念页的基础材料，特别适合定义组件 taxonomy、失败闭环和未来演化方向。
- inferred: source 把 harness 理解为 Agent 的操作系统或运行时，而不是单个配置文件，因此后续 compile 应避免把它缩减成 prompt engineering 的子类。

## External Links

- reference: [Agent Harness Engineering](https://x.com/addyosmani/status/2053231239721885918) — root topic link; not verified.

## Links

- compiled-concept: [[concepts/Agent Harness|Agent Harness]] — 可提炼 harness 的定义、组件、失败闭环和运行时心智模型。
- related: Agent Runtime — source 将 harness 类比为 runtime + compiler，可支撑 runtime 边界定义。
- compiled-synthesis: [[synthesis/Vibe Coding 工程化深度模型|Vibe Coding 工程化深度模型]] — 支撑 Agent = Model + Harness、组件分层、失败棘轮和安全边界。
- map-entry: [[maps/Vibe Coding 学习地图|Vibe Coding 学习地图]] — 可作为 AI coding 工作系统设计主题的核心入口。
- related: Agent Harness 工程化框架 — 可与同目录 Harness 循环、Skills 图形成跨 source 综合。

## Maintenance Notes

- XMind helper returned `ok: true`; `sheets_error` empty; all 1 sheet exported and digested.
- source 结构较大，当前 note 保留了组件分类、失败转规则路径、安全边界、未来方向和模型关系；完整节点细节仍需回 raw/XMind 导出复查。
