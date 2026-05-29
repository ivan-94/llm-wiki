---
source_type: image
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/Vibe Coding 随手记/Harness/Skills 就是为了Agent 少走弯路.png"
source_relpath: "Vibe/Vibe Coding 随手记/Harness/Skills 就是为了Agent 少走弯路.png"
raw_created_at: 2026-04-27T10:00:38.356675+00:00
raw_modified_at: 2026-04-27T10:00:38.357049+00:00
raw_size: 1436408
raw_fingerprint: "size=1436408;birth=2026-04-27T10:00:38.356675+00:00;mtime=2026-04-27T10:00:38.357049+00:00"
raw_snapshot_at: 2026-05-29T15:53:55+00:00
ingested_at: 2026-05-29
status: ingested
---

# Skills 就是为了Agent 少走弯路.png

## Source

- Raw file: [Vibe/Vibe Coding 随手记/Harness/Skills 就是为了Agent 少走弯路.png](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/Vibe%20Coding%20%E9%9A%8F%E6%89%8B%E8%AE%B0/Harness/Skills%20%E5%B0%B1%E6%98%AF%E4%B8%BA%E4%BA%86Agent%20%E5%B0%91%E8%B5%B0%E5%BC%AF%E8%B7%AF.png>)
- Raw ref: `raw:Vibe/Vibe Coding 随手记/Harness/Skills 就是为了Agent 少走弯路.png`
- Type: image
- Status: ingested
- Raw metadata: created `2026-04-27T10:00:38.356675+00:00`; modified `2026-04-27T10:00:38.357049+00:00`; size `1436408`; snapshot `2026-05-29T15:53:55+00:00`
- Coverage: opened with Agent vision; full infographic inspected; dimensions `1157x1360`; visible text is clear enough for source note.

## Summary

这张图用迷宫和搜索曲线说明 Skills 的价值：Skills 不是让模型变聪明，而是对搜索空间施加结构化约束，把复杂问题拆成可控子问题，减少盲目探索和 token 消耗，让 Agent 始终停留在能力的 sweet spot 高效运行。

## Source Digest

图把 Agent 解题类比为在迷宫中搜索路径。没有 Skills 时，Agent 完全依赖模型能力兜底，盲走探索，随机尝试、碰壁回退、路径弯曲、成本高，表现为高熵搜索；基础 Skills 提供工具和简单策略，让探索变得有规则，例如“查-再-算”，减少回退，效率中等；强 Skills 则构建抽象模型和地图，让 Agent 能规划最优路径，基本不回退，直接接近目标，表现为低熵搜索。

图中的搜索过程对比用“信息增益”和“探索步数/token cost”表达三种曲线：无 Skills 信息增益不稳定、token 消耗大、容易超出 sweet spot；基础 Skills 借助工具和规则减少弯路，信息增益更稳定、效率提升；强 Skills 规划先行，几乎不走弯路，始终停留在 sweet spot 区间。下方对比强调无 Skills 时每一步都靠大模型推理，容易上下文膨胀、熵增、成本上升和效果下降；有 Skills 时每一步有结构化策略，处理降维，成本可控，结果稳定。

核心观点是 Skills 是 brute-force reasoning 上的 structured shortcuts。它们通过外化经验、规则、步骤和抽象模型，降低搜索空间的熵，而不是直接提升模型智力。这为 Agent Harness 中的 Skills 提供了清晰定位：它们是减少探索成本、稳定执行路径和提升可复用性的工程构件。

## Key Claims

- explicit: Skills 对搜索空间施加结构化约束，降低熵并提升效率。
- explicit: 无 Skills 时 Agent 盲走探索，随机尝试、碰壁回退、路径弯曲、成本高、效率低。
- explicit: 基础 Skills 使用工具和简单策略，减少无效尝试，形成有规则的中等熵搜索。
- explicit: 强 Skills 构建抽象模型并规划最优路径，基本不回退，形成低熵搜索。
- explicit: Skills 不是让模型变得更聪明，而是降低搜索空间的熵，让 Agent 更高效到达目标。
- explicit: `Skills = Structured Shortcuts over Brute-force Reasoning`。
- inferred: 这张图适合支撑“技能文件”概念页，把 skills 解释为搜索约束和经验复用机制，而不只是提示词片段。
- inferred: source 与 Agent Harness 的 empower/constraint 双轴有关：Skills 同时扩展能力并约束探索路径。

## External Links

No external links found in extracted content.

## Links

- compiled-concept candidate: [[concepts/Agent Skills|Agent Skills]] — 可提炼 Skills 作为结构化捷径、低熵搜索和经验复用机制的定义。
- compiled-concept candidate: [[concepts/Agent Harness|Agent Harness]] — 可补充 Skills 在 harness 中负责降低搜索空间熵的角色。
- compiled-synthesis candidate: [[synthesis/Agent Harness 工程化框架|Agent Harness 工程化框架]] — 可与 harness runtime 和循环图共同解释 skills/rules/tools 的组合价值。
- map-entry candidate: [[maps/Vibe Coding 学习地图|Vibe Coding 学习地图]] — 可作为 Agent skills 设计与调优主题入口。

## Maintenance Notes

- 图片视觉清晰；没有明显 URL。
- 图中“sweet spot”用于描述能力/成本/上下文窗口的有效运行区间，后续 compile 时可与上下文工程、token cost 和工具编排共同建模。
