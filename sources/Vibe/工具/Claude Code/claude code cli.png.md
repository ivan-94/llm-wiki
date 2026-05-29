---
source_type: image
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/工具/Claude Code/claude code cli.png"
source_relpath: "Vibe/工具/Claude Code/claude code cli.png"
raw_created_at: 2026-05-10T02:24:48.139297+00:00
raw_modified_at: 2026-05-10T02:24:48.139647+00:00
raw_size: 1758568
raw_fingerprint: "size=1758568;birth=2026-05-10T02:24:48.139297+00:00;mtime=2026-05-10T02:24:48.139647+00:00"
raw_snapshot_at: 2026-05-29T16:03:40.320778+00:00
ingested_at: 2026-05-29
status: ingested
---

# claude code cli.png

## Source

- Raw file: [Vibe/工具/Claude Code/claude code cli.png](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/%E5%B7%A5%E5%85%B7/Claude%20Code/claude%20code%20cli.png>)
- Raw ref: `raw:Vibe/工具/Claude Code/claude code cli.png`
- Type: image
- Status: ingested
- Raw metadata: created `2026-05-10T02:24:48.139297+00:00`; modified `2026-05-10T02:24:48.139647+00:00`; size `1758568`; snapshot `2026-05-29T16:03:40.320778+00:00`
- Coverage: full image inspected with vision; dimensions `1536x1024`; image type: visual CLI cheatsheet.

## Summary

这张图片是一页 Claude Code CLI 速查表，面向日常使用场景，把启动提问、会话恢复、脚本输出、权限工具、项目上下文、模型提示词、MCP/插件/浏览器、远程隔离、账号版本、调试维护、快速决策和组合范例压缩到一张可视化索引中。

## Source Digest

图片以 12 个编号卡片组织 CLI 能力。前半部分覆盖基础操作：`claude` 启动交互，带 query 启动，`-p` 非交互输出，管道输入；`-c`/`--continue` 续接最近会话，`-r`/`--resume` 按会话恢复，`--session-id` 指定会话，`--fork-session` 恢复时分叉；`--output-format`、`--input-format`、`--json-schema`、`--max-turns`、`--max-budget-usd`、`--no-session-persistence` 用于脚本化和结构化输出。

中间部分强调 Agent 安全边界与上下文控制：`--permission-mode` 控制计划/自动/绕过等权限模式，`--allowedTools`、`--disallowedTools`、`--tools` 和 permission prompt tool 收窄工具能力；`--add-dir`、`--settings`、`--setting-sources`、`--init-only`、`--bare` 控制项目上下文与启动行为；`--model`、`--effort`、fallback model、append/replacement system prompt 控制模型与系统提示。

后半部分把 Claude Code 放入更大的工具生态：MCP 配置、插件安装、本地插件、Chrome 开关；远程 web session、teleport、remote-control、worktree 与 tmux；认证、状态、更新、安装、版本、setup token；调试分类、debug file、verbose、project purge、agents、auto-mode defaults、ultrareview。最后用“快速决策”和组合范例把常见目标映射到优先 flag，例如交互开发用 `claude`，脚本调用用 `claude -p --output-format json`，先看计划用 `--permission-mode plan`，隔离开发用 `-w`。

## Key Claims

- explicit: Claude Code CLI 支持交互模式、非交互 `-p` 模式和管道输入三类日常入口。
- explicit: 会话可以通过最近会话、名称/ID、session UUID、PR 来源或分叉方式继续和恢复。
- explicit: CLI 提供结构化输出、回合数、预算、工具权限、项目上下文、模型、MCP、插件、远程控制、worktree、调试和维护等控制面。
- explicit: 图片将 `--permission-mode plan`、工具白/黑名单、`--bare`、`--add-dir`、`--append-system-prompt-file`、`-w` 等归为高频决策入口。
- inferred: 这张图适合作为 Claude Code CLI 学习地图的索引页，而不是单独解释每个 flag 的权威来源。
- inferred: 图片与同目录 Markdown cheatsheet 内容高度重叠，可互相校验；精确命令含义应优先回到 Markdown 或官方 CLI reference。

## External Links

- documentation: [Claude Code CLI reference](https://code.claude.com/docs/en/cli-reference) — 图片底部 source 引用；not verified.

## Links

- compiled-concept candidate: [[concepts/Claude Code CLI|Claude Code CLI]] — 可沉淀 CLI 入口、权限、上下文、脚本化和远程能力。
- map-entry candidate: [[maps/Claude Code 学习地图|Claude Code 学习地图]] — 可作为命令行能力速查入口。

## Maintenance Notes

- 图片文本整体清晰，但小号 code font 仍属于 vision 识别；精确 flag 拼写应与 raw Markdown 或官方 CLI reference 二次核对。
- 该图片是速查图，不含每个 flag 的完整语义、版本边界或废弃状态。
