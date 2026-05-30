---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/Vibe Coding 随手记/Vibe Coding 随手记.xmind"
source_relpath: "Vibe/Vibe Coding 随手记/Vibe Coding 随手记.xmind"
raw_created_at: 2026-04-10T01:43:30.788047+00:00
raw_modified_at: 2026-05-29T05:29:25.207027+00:00
raw_size: 4520918
raw_fingerprint: "size=4520918;birth=2026-04-10T01:43:30.788047+00:00;mtime=2026-05-29T05:29:25.207027+00:00"
raw_snapshot_at: 2026-05-29T15:54:30.976435+00:00
ingested_at: 2026-05-29
status: ingested
---

# Vibe Coding 随手记.xmind

## Source

- Raw file: [Vibe/Vibe Coding 随手记/Vibe Coding 随手记.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/Vibe%20Coding%20%E9%9A%8F%E6%89%8B%E8%AE%B0/Vibe%20Coding%20%E9%9A%8F%E6%89%8B%E8%AE%B0.xmind>)
- Raw ref: `raw:Vibe/Vibe Coding 随手记/Vibe Coding 随手记.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2026-04-10T01:43:30.788047+00:00`; modified `2026-05-29T05:29:25.207027+00:00`; size `4520918`; snapshot `2026-05-29T15:54:30.976435+00:00`
- Coverage: exported all sheets with `.codex/skills/ai-wiki-xmind-ingest/scripts/export_xmind_source.py`; 1 sheet read and digested.
- Sheets: `0 散记` (43 topics).

## Summary

这是一份 Vibe Coding 实践散记，围绕“先澄清再编码”、让 agent 在声明式成功标准下循环、用高能力模型做设计/计划、隔离会话与工作流、以及前端/PRD/验收类工作流展开。它不是线性方法论，而是一组关于 AI 编码项目如何降低漂移、放大杠杆、避免上下文污染的经验判断。

## Source Digest

这份 mind map 把 Vibe Coding 的核心问题放在“复杂项目容易偏移”上：代码本身越来越不值钱，真正需要管理的是需求澄清、上下文边界、成功标准和反馈循环。作者强调，除非需求已经非常明确，否则不应直接 few-shot 编码，而应先和 agent 像与人类协作者一样反复对齐问题、动机与约束。

它还提出一个重要操作范式：不要过度命令式地告诉模型每一步怎么做，而是给出可验证的成功标准，让模型通过写测试、跑测试、浏览器 MCP、朴素算法到优化算法等循环逼近目标。这与后续“Vibe Coding Sweet Spot”和 agent 并发执行环境 source 中的验证循环、状态外置、会话隔离形成同一主题链。

散记也记录了 Vibe Coding 的副作用：Vibe 生成的项目会压缩手写代码空间，若全局结构混乱，人类局部修补会越来越困难；记忆机制也可能成为 agent 的信息茧房，使回答被既有记忆框住。前端部分则把 AI 生成原型图、Figma Dev 模式、截图 diff 还原作为可循环的 UI 工作流。

## Key Claims

- explicit: 从 0 到 1 的稍复杂项目很容易出现方向偏移，因此需要接受重做和代码低沉没成本的心态。
- explicit: 开工前应先与 agent 探索并澄清需求、动机和问题边界，避免在模糊需求下直接编码。
- explicit: LLM 的杠杆来自“循环直到达标”：给成功标准、测试和反馈，而不是只给命令式步骤。
- explicit: 高能力模型适合承担设计和计划任务，虽然成本更高，但在理解用户意图方面更值得投入。
- explicit: agent 记忆可能限制发散，把回答框在历史记忆中，形成类似信息茧房的偏差。
- explicit: 前端开发可以用 AI 生成界面草图或渲染图，再通过 Figma/截图 diff 循环还原。
- inferred: 这份散记将 Vibe Coding 的工程重点从“写代码”转移到“定义规格、管理上下文、设计反馈循环和隔离工作流”。
- inferred: 会话管理的规划、执行、验收分离可以作为后续 agent workflow 和 HAT 工作流的学习地图入口。

## External Links

- learning-source: [Structured-Prompt-Driven Development (SPDD)](https://martinfowler.com/articles/structured-prompt-driven/) — source 中作为 spec driven development 参考；not verified.
- learning-source: [agent-skills](https://github.com/addyosmani/agent-skills) — source 中作为面向 AI 编码代理的生产级工程技能参考；not verified.
- social-reference: [调用栈形式的计划](https://x.com/dillon_mulroy/status/2059985696148849025) — source 中作为计划表达形式参考；not verified.

## Links

- compiled-concept: [[concepts/Vibe Coding|Vibe Coding]] — 可提炼 Vibe Coding 的实践边界、漂移风险、会话隔离和声明式成功标准。
- related: [[concepts/Agent 工作流技能编排|Agent 工作流技能编排]] — 可沉淀 PRD 生成、模糊点排除、规划/执行/验收会话分离。
- map-entry: [[maps/Vibe Coding 学习地图|Vibe Coding 学习地图]] — 可作为 Vibe Coding 方法论、前端生成、规格驱动开发和 agent skills 的入口 source。

## Maintenance Notes

- 本批 worker 被限制不修改 `index.md`、`log.md`、`concepts/`、`maps/` 等编译层页面；上面的 Links 仅记录 compile 候选。
- Sheet 中 `AI 时代的能力重塑` 下存在空白子节点，可能是未完成记录。
