---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/工具/Claude Code/解构 Claude Code.xmind"
source_relpath: "Vibe/工具/Claude Code/解构 Claude Code.xmind"
raw_created_at: 2025-07-22T06:54:37+00:00
raw_modified_at: 2026-05-29T02:55:05.577237+00:00
raw_size: 4843550
raw_fingerprint: "size=4843550;birth=2025-07-22T06:54:37+00:00;mtime=2026-05-29T02:55:05.577237+00:00"
raw_snapshot_at: 2026-05-29T16:03:40.320859+00:00
ingested_at: 2026-05-29
status: ingested
---

# 解构 Claude Code.xmind

## Source

- Raw file: [Vibe/工具/Claude Code/解构 Claude Code.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/%E5%B7%A5%E5%85%B7/Claude%20Code/%E8%A7%A3%E6%9E%84%20Claude%20Code.xmind>)
- Raw ref: `raw:Vibe/工具/Claude Code/解构 Claude Code.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2025-07-22T06:54:37+00:00`; modified `2026-05-29T02:55:05.577237+00:00`; size `4843550`; snapshot `2026-05-29T16:03:40.320859+00:00`
- Coverage: all sheets discovered and exported with `export_xmind_source.py`; sheet count `5`; sheets: `解构 Claude Code` (306 topics), `最佳实践` (163 topics), `子智能体系统 SubAgent` (70 topics), `Agent 团队` (30 topics), `动态工作流` (28 topics).

## Summary

这份多 sheet XMind 从架构、交互、定制、记忆、工具、编排、最佳实践、SubAgent、Agent Teams 和动态工作流多个层面拆解 Claude Code，把它从“终端编程工具”扩展为一个可定制、可编排、可脚本化的 Agent 工程平台。

## Source Digest

主 sheet 描述 Claude Code 的基本形态：它是基于终端的自然语言交互系统，但通过命令、`@` 文件选取、`#` 记忆、`!` shell、自动补全、多模态输入、计划模式、GitHub CI、SDK、MCP、hooks、主题、状态栏、Vim 模式等能力，把传统 CLI 变成 Agent 操作界面。source 特别强调计划模式适合代码探索、复杂改动规划和安全审查；无头模式、TypeScript/Python SDK 与流式/单次模式说明 Claude Code 不只是交互工具，也可作为编程智能体框架使用。

记忆与上下文部分区分固定记忆、自动记忆、`CLAUDE.md`、`.claude/rules/`、全局/项目级配置、MCP、skills、commands、agents、output-styles 与 agent-memory。一个重要主题是“渐进披露”：根 CLAUDE.md 不应堆积所有细节，而应保存普适规则和指针，把更细的上下文放入 docs、rules、skills、commands 或专用 agents。

最佳实践 sheet 偏工程方法论：先 plan、从最小规格开始、让 Agent 采访澄清、用带门禁的分阶段计划、跨模型/多 Agent 评审、保持小 PR、频繁提交、使用浏览器调试、使用命令和 skills 固化重复工作流、利用 worktree/tmux 组织并行 Agent。它还把 CLAUDE.md 写作、skills 设计、hooks、workflow、Git PR、debug、工具选择等都视为提高 Claude Code 可控性的手段。

后三个 sheet 对编排层进行分层：SubAgent 是主 Agent 下的专门助手，拥有独立上下文、工具限制、模型与提示词，适合保留主上下文、行为专业化、约束工具和并行研究；Agent Teams 是多个 Claude Code 实例协作，成员可直接沟通、共享任务并被负责人协调；动态工作流则把计划、循环、分支和中间结果搬进 JavaScript 脚本，由后台长时间编排子代理，减少主对话上下文负担并提高可重复性。

## Key Claims

- explicit: Claude Code 的核心交互仍是自然语言对话，但它通过 slash commands、文件上下文、记忆、shell、计划模式和多模态输入扩展了终端体验。
- explicit: Claude Code 的定制层包括自定义命令、输出风格、子代理、记忆管理、hooks、MCP、SDK、主题、状态栏和 Vim 模式。
- explicit: Claude Code 可以通过无头模式、TypeScript SDK、Python SDK、流式/单次模式用于自动化和应用集成。
- explicit: SubAgent 通过独立上下文、专门提示词、工具限制和模型配置处理特定任务，并可用于保留主上下文、强制约束和行为专业化。
- explicit: Agent Teams 与 SubAgent 的区别在于粒度和协作机制：团队成员是独立 Claude Code 实例，可以直接沟通并共享任务，而子代理只向主代理汇报。
- explicit: 动态工作流把计划移入 JavaScript 脚本，由脚本持有循环、分支和中间结果，适合并行和长时间运行任务。
- inferred: Claude Code 的知识结构可拆成交互层、上下文层、定制层、执行层、编排层、治理层和工作流产品化层。
- inferred: 这份 source 是 Claude Code 学习地图的核心骨架，能连接 CLI、memory、skills、hooks、subagents、teams、dynamic workflows 与 Agent 工程实践。

## External Links

- documentation: [Claude Code auto memory](https://code.claude.com/docs/en/memory#auto-memory) — source 用于说明自动记忆机制；not verified.
- analysis: [shareAI-lab/analysis_claude_code](https://github.com/shareAI-lab/analysis_claude_code) — 扩展阅读；not verified.
- analysis: [Claude Code: An analysis](https://southbridge-research.notion.site/claude-code-an-agentic-cleanroom-analysis) — 扩展阅读；not verified.
- analysis: [Understand How Claude Code Work](https://medium.com/@guillaumesabran/understanding-how-claude-code-works-13036595a8a7) — 扩展阅读；not verified.
- learning-source: [可视化学习](https://learn.shareai.run/zh/) — 扩展阅读；not verified.
- social-thread: [你不知道的 Claude Code：架构、治理与工程实践](https://x.com/HiTw93/status/2032091246588518683) — 扩展阅读；not verified.
- best-practice: [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) — 最佳实践来源；not verified.
- guide: [Writing a good CLAUDE.md](https://www.humanlayer.dev/blog/writing-a-good-claude-md) — CLAUDE.md 写作建议来源；not verified.
- documentation: [Claude Code custom slash commands](https://docs.anthropic.com/zh-CN/docs/claude-code/common-workflows#%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89%E6%96%9C%E6%9D%A0%E5%91%BD%E4%BB%A4) — 自定义命令来源；not verified.
- documentation: [Claude Code skills](https://code.claude.com/docs/en/skills) — skills 机制来源；not verified.
- tool: [claudia](https://github.com/getAsterisk/claudia) — 可视化终端扩展；not verified.
- tool: [claude-code-router](https://github.com/musistudio/claude-code-router) — 模型代理工具；not verified.
- documentation: [Claude Code Desktop recurring tasks](https://code.claude.com/docs/zh-CN/desktop#schedule-recurring-tasks) — 会话外调度相关；not verified.
- documentation: [Claude directory](https://code.claude.com/docs/en/claude-directory) — 项目级/全局 `.claude` 目录来源；not verified.
- documentation: [Claude Code sub agents](https://docs.claude.com/zh-CN/docs/claude-code/sub-agents) — SubAgent sheet 来源；not verified.
- documentation: [Agent teams](https://code.claude.com/docs/en/agent-teams) — Agent Teams sheet 来源；not verified.
- announcement: [Introducing dynamic workflows in Claude Code](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code) — 动态工作流来源；not verified.
- social-thread: [Claude Code Dynamic Workflows：把编排逻辑搬进代码的新原语](https://x.com/riba2534/status/2060102236676792711) — 动态工作流解读；not verified.

## Links

- related: [[entities/Claude Code|Claude Code]] — 可沉淀整体架构、交互、定制和运行模型。
- related: [[maps/Vibe Coding 工具地图|Vibe Coding 工具地图]] — 该 source 可作为 Claude Code 主题学习地图的主入口。

## Maintenance Notes

- 部分节点为空标题或占位，例如架构下的空节点、内置工具下的空节点、最佳实践中的“分支主题 2/3/4”，compile 时应忽略或标记为待补充。
- source 中包含示例 API key/token 形态的配置片段；source note 已避免复制完整敏感片段，后续引用时也应避免传播。
- 外链均从 XMind 导出内容提取，本次未联网核验当前有效性或产品版本状态。

- Link cleanup candidate: related: Claude Code SubAgent — source 有专门 sheet 说明子代理用途、委派、配置、生命周期和协作模式。.
- Link cleanup candidate: related: Agent Teams — source 对比团队与 SubAgent 的粒度、人机交互和协作机制。.
- Link cleanup candidate: related: 动态工作流 — source 解释把编排逻辑搬进脚本后的执行模型。.
- Link cleanup candidate: related: CLAUDE.md 设计 — source 汇总 CLAUDE.md、rules、skills、commands 和渐进披露原则。.
