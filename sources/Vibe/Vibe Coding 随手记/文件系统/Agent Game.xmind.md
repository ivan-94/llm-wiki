---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/Vibe Coding 随手记/文件系统/Agent Game.xmind"
source_relpath: "Vibe/Vibe Coding 随手记/文件系统/Agent Game.xmind"
raw_created_at: 2026-05-26T03:40:19.081182+00:00
raw_modified_at: 2026-05-29T03:40:38.712066+00:00
raw_size: 361593
raw_fingerprint: "size=361593;birth=2026-05-26T03:40:19.081182+00:00;mtime=2026-05-29T03:40:38.712066+00:00"
raw_snapshot_at: 2026-05-29T15:59:36.695470+00:00
ingested_at: 2026-05-29
status: ingested
---

# Agent Game.xmind

## Source

- Raw file: [Vibe/Vibe Coding 随手记/文件系统/Agent Game.xmind](finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/Vibe%20Coding%20%E9%9A%8F%E6%89%8B%E8%AE%B0/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/Agent%20Game.xmind)
- Raw ref: `raw:Vibe/Vibe Coding 随手记/文件系统/Agent Game.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2026-05-26T03:40:19.081182+00:00`; modified `2026-05-29T03:40:38.712066+00:00`; size `361593`; snapshot `2026-05-29T15:59:36.695470+00:00`
- Coverage: helper exported all sheets; 1 sheet (`画布 1`), 96 topics.

## Summary

这份脑图把 Agent Game 设计为“repo 即世界、文件即记忆、agent 即游戏引擎、commit 即时间线”的文件系统游戏。它定义了地图、人物、章节、势力、状态、技能、hooks、故事特写和规则引擎等目录/文件职责，并强调用索引、扁平结构、AGENTS.md 规则和自动化 hooks 让 agent 能稳定运行游戏世界。

## Source Digest

source 的核心是把一个可持续运行的文本游戏拆成可被 agent 读取和维护的文件系统协议。`map/`、`characters/`、`chapters/`、`factions/` 负责世界事实和叙事对象；`states/` 下的 `state.md`、`USER.md`、`MEMORY.md`、`logs.jsonl`、`GAME.md` 负责当前状态、玩家定义、偏好记忆、不可变历史和核心机制；`skills/` 把历史追加和历史查询固化成可调用流程；`hooks/` 用强制存档和随机变量介入来约束 agent 行为；`AGENTS.md` 则作为规则引擎，定义加载、存档、结算、行文和交互规则。它的启发不只适用于游戏，也适用于任何需要 agent 在长期文件状态中运行的系统：事实入口要可索引，状态要明确，历史要 append-only，自动化干预要进入规则层。

## Key Claims

- explicit: Agent Game 的 map、characters、chapters、factions 等目录分别承载地点、人物、故事章节和集团势力。
- explicit: `states/state.md` 表示当前状态，包括时间、天气、正在进行的章节、主角状态、当前位置、当前目标和世界大局。
- explicit: `logs.jsonl` 用于保存所有历史执行记录，要求线性插入、不可修改，并支持 grep 和工具查询写入。
- explicit: hooks 包含强制存档逻辑和随机变量介入，避免 agent 一味顺从玩家。
- explicit: 规则引擎由 `AGENTS.md` 承担，覆盖游戏规则、哲学、运行方式、加载、存档、结算、行文和交互。
- explicit: source 将核心哲学概括为 repo 即世界、文件即记忆、agent 即游戏引擎、commit 即时间线。
- inferred: 该文件系统模式可抽象为长期 agent 应用的状态管理范式：索引导航、当前状态、append-only 历史、规则文件和 hook 共同构成运行时约束。

## External Links

- project-source: [Agent Game](https://github.com/ivan-94/agent-game) — root topic links to the repository; not verified.

## Links

- map-entry: [[maps/Vibe Coding 学习地图|Vibe Coding 学习地图]] — source 可归入 Agent 运行时文件系统设计。

## Maintenance Notes

- XMind 内容覆盖文件结构和职责，但没有给出真实文件示例正文；如需实现级复用，应回到仓库或 raw 继续核对具体模板。
- 外链只提取了 root topic 中的 GitHub URL，未联网核验。

- Link cleanup candidate: compiled-concept: 文件系统作为 Agent 状态层 — source 提供目录职责、状态文件、历史日志和规则文件的完整示例。.
- Link cleanup candidate: compiled-concept: Agent Hooks — source 以强制存档和随机变量说明 hook 对长期运行的干预作用。.
- Link cleanup candidate: compiled-entity: Agent Game — 候选实体；source 明确指向 Agent Game 项目及其文件系统设计。.
