---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/工具/AI 软件工厂 GStack.xmind"
source_relpath: "Vibe/工具/AI 软件工厂 GStack.xmind"
raw_created_at: 2026-04-20T15:03:22.124433+00:00
raw_modified_at: 2026-04-21T04:39:25.921337+00:00
raw_size: 1613949
raw_fingerprint: "size=1613949;birth=2026-04-20T15:03:22.124433+00:00;mtime=2026-04-21T04:39:25.921337+00:00"
raw_snapshot_at: 2026-05-29T16:03:40.320643+00:00
ingested_at: 2026-05-29
status: ingested
---

# AI 软件工厂 GStack.xmind

## Source

- Raw file: [Vibe/工具/AI 软件工厂 GStack.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/%E5%B7%A5%E5%85%B7/AI%20%E8%BD%AF%E4%BB%B6%E5%B7%A5%E5%8E%82%20GStack.xmind>)
- Raw ref: `raw:Vibe/工具/AI 软件工厂 GStack.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2026-04-20T15:03:22.124433+00:00`; modified `2026-04-21T04:39:25.921337+00:00`; size `1613949`; snapshot `2026-05-29T16:03:40.320643+00:00`
- Coverage: all sheets discovered and exported with `export_xmind_source.py`; sheet count `1`; sheets: `画布 1` (89 topics).

## Summary

这份 XMind 把 GStack 解释为围绕 Claude Code 构建的“AI 软件工厂”工具集：通过一组 Markdown skills、浏览器/设计/测试工具和斜杠命令，把计划审查、代码审查、QA、安全审计、发布、监控与复盘等工程流程封装成可复用的 Agent 工作流。

## Source Digest

GStack 的核心不是单个提示词库，而是把软件工程中的重复流程编码成带质量门禁的可执行剧本。source 强调 `/ship`、`/review`、`/qa`、`/autoplan`、`/codex`、`/canary` 等命令之间的组合关系：计划阶段由 CEO/设计/工程视角评审，开发后由多领域 reviewer、安全审计、QA 与异构模型交叉评审提高置信度，最后进入发布与线上监控。

工具层面，GStack 将浏览器、图像生成和测试评估纳入同一体系。`browse/` 被描述为基于 Playwright 的无头浏览器 CLI，服务于 QA、设计评审、安全审计、性能监控和部署验证；`design/` 用于 GPT Image API 驱动的视觉生成与变体探索；`test/` 采用三层测试：免费静态验证与生成质量检查、付费 E2E 技能运行、以及 LLM-as-judge 质量评估。

方法论层面，source 用“杠杆”解释 GStack：高质量 prompt 的复用、交叉验证的置信度、即时反馈的迭代速度与失败经验的累积共同压缩认知成本。它还强调 dogfooding、自举飞轮、Dev Mode Symlink、E2E 可观测性、JSONL 记录、失败学习与 slop-scan，这些都指向同一个模式：把工程经验从一次性人工判断沉淀为可复用、可审计、可迭代的 Agent 操作系统。

## Key Claims

- explicit: GStack 将重复性的发布、审查、监控、QA、安全审计等工程流程封装成 AI 可执行的标准化 skills 和 slash commands。
- explicit: GStack 的质量保障依赖多层防御，包括 `/review` 领域专家集合、`/codex` 异构模型交叉评审、QA、测试、E2E 可观测性和线上 canary。
- explicit: GStack 的测试体系分为静态验证/生成质量检查、端到端实际运行技能、LLM-as-judge 质量评估三层。
- explicit: 浏览器能力在 GStack 中是一等公民，用于让 Agent 真正检查网页状态，而不只是阅读代码。
- inferred: GStack 可以作为“Agent 工作流产品化”的案例：它把 prompt、工具、日志、测试和发布串成可复用的软件工程闭环。
- inferred: 该 source 适合支撑后续关于 AI 软件工厂、Agent 工程质量门禁、交叉模型评审和技能即代码的概念页。

## External Links

- project: [garrytan/gstack](https://github.com/garrytan/gstack) — source 根节点引用的 GStack 项目；not verified.

## Links

- compiled-entity: [[entities/GStack|GStack]] — 本 source 是 GStack 实体的主要证据来源。
- compiled-concept: [[concepts/AI 软件工厂|AI 软件工厂]] — GStack 是 AI 软件工厂概念的标准实现案例。
- map-entry: [[maps/Vibe Coding 工具地图|Vibe Coding 工具地图]] — GStack 工具簇来源。
- used-in: [[sources/Vibe/工具/Github 原住民.xmind|Github 原住民]] — GStack 的发布流程和质量门禁以 GitHub 原住民六层为基础。

## Maintenance Notes

- XMind 中部分工具分类节点只有标题、无展开内容，例如设计与视觉、部署与运维、安全与质量、文档与复盘、上下文写作、浏览器工具等，后续 compile 时应避免把这些空分支当作完整分类体系。
- 外部项目与功能细节未联网核验；需要当前事实时应重新打开官方仓库或文档。

- Link cleanup candidate: related: AI 软件工厂 — 可沉淀“用 Agent 工作流封装软件交付流程”的概念。.
- Link cleanup candidate: related: 技能即代码 — source 将 SKILL.md 视为可执行 prompt 和流程代码。.
- Link cleanup candidate: related: 交叉模型评审 — source 以 Claude 与 Codex 的二次评审说明异构模型验证。.
