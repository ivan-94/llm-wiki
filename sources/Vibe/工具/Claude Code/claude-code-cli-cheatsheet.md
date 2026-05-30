---
source_type: markdown
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/工具/Claude Code/claude-code-cli-cheatsheet.md"
source_relpath: "Vibe/工具/Claude Code/claude-code-cli-cheatsheet.md"
raw_created_at: 2026-05-10T02:26:27.481242+00:00
raw_modified_at: 2026-05-10T02:26:27.481669+00:00
raw_size: 8689
raw_fingerprint: "size=8689;birth=2026-05-10T02:26:27.481242+00:00;mtime=2026-05-10T02:26:27.481669+00:00"
raw_snapshot_at: 2026-05-29T16:03:40.320824+00:00
ingested_at: 2026-05-29
status: ingested
---

# claude-code-cli-cheatsheet.md

## Source

- Raw file: [Vibe/工具/Claude Code/claude-code-cli-cheatsheet.md](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/%E5%B7%A5%E5%85%B7/Claude%20Code/claude-code-cli-cheatsheet.md>)
- Raw ref: `raw:Vibe/工具/Claude Code/claude-code-cli-cheatsheet.md`
- Type: markdown
- Status: ingested
- Raw metadata: created `2026-05-10T02:26:27.481242+00:00`; modified `2026-05-10T02:26:27.481669+00:00`; size `8689`; snapshot `2026-05-29T16:03:40.320824+00:00`
- Coverage: full raw Markdown file read.

## Summary

这份 Markdown 是 Claude Code CLI 的日常速查文档，按操作意图整理启动、恢复、脚本化、权限、上下文、模型、MCP/插件/浏览器、远程与隔离、账号版本、调试维护、快速决策和高频组合范例。

## Source Digest

文档将 Claude Code CLI 视为一个可从“交互开发”扩展到“自动化 Agent 运行时”的控制面。基础入口包括直接打开交互会话、带初始问题启动、用 `-p` 非交互执行、以及从 stdin 接收日志或文件内容；会话能力覆盖继续最近会话、按名称或 ID 恢复、命名会话、指定 session UUID、分叉恢复和从 PR 关联会话恢复。

脚本化部分突出输出契约和资源控制：`--output-format`/`--input-format`、`--json-schema`、`--max-turns`、`--max-budget-usd`、`--no-session-persistence`、partial messages 和 hook events 让 CLI 能进入 CI、日志诊断和结构化数据管道。权限与安全部分则强调计划模式、自动编辑、工具白名单/黑名单、禁用工具、权限提示工具和 bypass 权限等边界设置。

项目和上下文部分覆盖 `--add-dir`、settings 选择、init/maintenance hooks、`--bare` 与禁用 slash commands；模型提示词部分覆盖模型、推理强度、fallback、追加或替换系统提示；生态部分覆盖 MCP、插件、本地/远程插件、Chrome 集成和 channel；远程隔离部分覆盖 web session、teleport、remote control、git worktree、tmux 和 teammate mode。最后的决策表把“想做什么”映射到优先命令，降低用户在众多 flags 中选择的成本。

## Key Claims

- explicit: Claude Code CLI 同时支持交互、人机协作、非交互脚本、CI、结构化输出和日志诊断等模式。
- explicit: `-p`/`--print`、output/input format、JSON Schema、max turns 和 budget flags 是脚本化调用的核心控制项。
- explicit: `--permission-mode`、`--allowedTools`、`--disallowedTools`、`--tools` 可用于收窄或改变 Agent 的工具和权限边界。
- explicit: `--bare` 可跳过 hooks、skills、plugins、MCP、auto memory 和 `CLAUDE.md` 自动发现，适合更干净的脚本环境。
- explicit: `-w`、`--tmux`、remote session、teleport 和 remote-control 将 CLI 扩展到隔离工作区和远程接管场景。
- inferred: 该文档可以作为 Claude Code CLI 能力模型的“索引层”，后续概念页应按能力域拆解，而不是逐 flag 复制。

## External Links

- documentation: [Claude Code Docs - CLI reference](https://code.claude.com/docs/en/cli-reference) — raw Markdown 明确列为来源；not verified.

## Links

- related: [[entities/Claude Code|Claude Code]] — 可沉淀启动、会话、脚本化、权限、上下文和远程能力。
- related: [[concepts/Agent 沙箱|Agent 沙箱]] — 文档提供工具白名单、黑名单、permission mode 与 bare mode 例子。
- related: [[maps/Vibe Coding 工具地图|Vibe Coding 工具地图]] — 可作为 CLI 操作层学习入口。
- related: [[sources/Vibe/工具/Claude Code/claude code cli.png|claude code cli.png]] — 同主题图片 source，两者覆盖相同 CLI 功能的不同表达形式。

## Maintenance Notes

- CLI flags 可能随 Claude Code 版本变动；本次未联网核验官方 reference 当前状态。
- Markdown 与同目录图片内容高度相似，后续 compile 可合并为一个 Claude Code CLI source cluster，避免重复创建概念。
