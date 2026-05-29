---
source_type: image
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/工具/codex/cli.png"
source_relpath: "Vibe/工具/codex/cli.png"
raw_created_at: 2026-05-10T02:31:00.292231+00:00
raw_modified_at: 2026-05-10T02:31:00.292789+00:00
raw_size: 1576040
raw_fingerprint: "size=1576040;birth=2026-05-10T02:31:00.292231+00:00;mtime=2026-05-10T02:31:00.292789+00:00"
raw_snapshot_at: 2026-05-29T16:07:00+00:00
ingested_at: 2026-05-30
status: ingested
---

# cli.png

## Source

- Raw file: [Vibe/工具/codex/cli.png](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/%E5%B7%A5%E5%85%B7/codex/cli.png>)
- Raw ref: `raw:Vibe/工具/codex/cli.png`
- Type: image
- Status: ingested
- Raw metadata: created `2026-05-10T02:31:00.292231+00:00`; modified `2026-05-10T02:31:00.292789+00:00`; size `1576040`; snapshot `2026-05-29T16:07:00+00:00`
- Coverage: opened with Agent vision; full infographic inspected; dimensions `2658x3918`; visible text is clear enough for source note, but exact command syntax should be rechecked against raw image or current docs before operational use.

## Summary

这张 Codex CLI stable cheatsheet 面向本地终端工作流，目标是用一页速查覆盖 99% 日常场景：安装/登录、启动交互会话、常用 flags、权限与沙箱、TUI slash commands、脚本/CI 中的 `codex exec`、配置、AGENTS.md、MCP 外部上下文、prompt 模板、入口选择和排错。

## Source Digest

图片把 Codex CLI 的稳定使用面分成三个层次。第一层是启动和认证：通过 npm 安装、运行 `codex`、登录、查看登录状态，并强调首次运行会提示 ChatGPT 或 API key 登录。第二层是交互和控制面：用 `-C/--cd` 指定工作目录，`-m/--model` 覆盖模型，`-s/--sandbox` 控制沙箱，`-a` 控制审批策略，`--profile` 加载 config profile，`--add-dir` 增加可访问目录；TUI 中可用 `/model`、`/plan`、`/permissions`、`/status`、`/review`、`/mention`、`/clear`、`/init`、`/mcp`、`/resume`、`/fork`、`/quit` 等 slash commands。

第三层是可复用工程约定：默认收紧权限，需要编辑时提升到 workspace-write，需要联网或越界时明确请求；把常用模型、reasoning、approval、sandbox、web_search、personality、features 写入 config，让每次启动像同一个队友；用 AGENTS.md 保存 repo layout、启动/测试命令、工程约定和 done means；用 MCP 接入第三方文档、浏览器、Figma 和内部工具；在脚本/CI 中用 `codex exec`、`--output-schema`、`-o` 和 resume 支持自动化。图的整体判断是先使用稳定能力作为主路径，把实验能力作为扩展入口。

## Key Claims

- explicit: Codex CLI 的日常主路径包括安装登录、启动会话、改代码、读图、权限与沙箱、脚本化执行、配置、AGENTS.md、MCP 和排错。
- explicit: 权限经验法则是默认收紧权限；需要编辑时提升到 workspace-write；需要联网或越界时让 Codex 明确请求。
- explicit: TUI slash commands 覆盖模型、速度、计划、权限、状态、diff、review、mention、compact、clear、init、mcp、后台终端、resume、fork 和 quit 等操作。
- explicit: `codex exec` 适合脚本化运行，图片建议默认适合无 TUI 的脚本任务，并可结合 `--output-schema` 返回严格 JSON。
- explicit: AGENTS.md 应写入 repo layout、启动方式、测试/构建/lint 命令、工程约定、PR 要求和 done means。
- explicit: MCP 可让 Codex 接入第三方文档、浏览器、Figma 和内部工具，并支持 stdio server、streamable HTTP、Bearer token 和 OAuth。
- inferred: 这张图可作为 Codex CLI 操作地图，但具体命令和参数可能随产品更新，需要在执行前用当前 CLI/help 或官方文档确认。

## External Links

- documentation-source: [OpenAI Codex CLI docs](https://developers.openai.com/codex/cli) — image footer lists this as a source; not verified.
- documentation-source: [Codex CLI reference](https://developers.openai.com/codex/cli/reference) — image footer lists this as a source; not verified.
- documentation-source: [Codex CLI slash commands](https://developers.openai.com/codex/cli/slash-commands) — image footer lists this as a source; not verified.
- documentation-source: [Codex CLI config basics](https://developers.openai.com/codex/config-basic) — image footer lists this as a source; not verified.
- documentation-source: [Codex auth](https://developers.openai.com/codex/auth) — image footer lists this as a source; not verified.
- documentation-source: [Agent approvals and security](https://developers.openai.com/codex/agent-approvals-security) — image footer lists this as a source; not verified.
- documentation-source: [Codex non-interactive usage](https://developers.openai.com/codex/noninteractive) — image footer lists this as a source; not verified.
- documentation-source: [Codex learn best practices](https://developers.openai.com/codex/learn/best-practices) — image footer lists this as a source; not verified.

## Links

- related: Codex CLI — 可提炼安装登录、交互会话、flags、配置、脚本化和排错的操作模型。
- related: Agent 权限与沙箱 — 可补充 sandbox、approval、workspace-write、danger-full-access 和 yolo 风险边界。
- related: AGENTS.md — 可补充 repo 级长期记忆、工程约定和 done means 的角色。
- map-entry: [[maps/Vibe Coding 工具地图|Vibe Coding 工具地图]] — 可作为 Codex CLI 日常操作入口。

## Maintenance Notes

- 图片为 2026-05-10 的稳定速查图；CLI 产品和官方 docs 可能变化，外链未联网核验。
- 命令文本整体清晰，但 source note 没有保存完整命令清单；需要执行时应回 raw 图或当前 `codex --help`/官方 docs。
