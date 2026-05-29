---
source_type: image
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/工具/tmux.png"
source_relpath: "Vibe/工具/tmux.png"
raw_created_at: 2026-05-06T17:22:47+08:00
raw_modified_at: 2026-05-06T17:22:53+08:00
raw_size: 1772804
raw_fingerprint: "size=1772804;birth=2026-05-06T17:22:47+08:00;mtime=2026-05-06T17:22:53+08:00"
raw_snapshot_at: 2026-05-29T16:13:22+00:00
ingested_at: 2026-05-30
status: ingested
---

# tmux.png

## Source

- Raw file: [Vibe/工具/tmux.png](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/%E5%B7%A5%E5%85%B7/tmux.png>)
- Raw ref: `raw:Vibe/工具/tmux.png`
- Type: image
- Status: ingested
- Raw metadata: created `2026-05-06T17:22:47+08:00`; modified `2026-05-06T17:22:53+08:00`; size `1772804`; snapshot `2026-05-29T16:13:22+00:00`
- Coverage: vision inspected full 1024x1536 cheat sheet; visible commands and workflow captured, QR code not decoded.

## Summary

这张图是 tmux 核心用法速览，面向 99% 常见场景：理解 session/window/pane/buffer 层级，掌握会话管理、前缀键、窗口和窗格快捷键、复制粘贴、滚动查看，以及一个后台任务工作流。

## Source Digest

图片首先定义 tmux 是终端复用器：在一个终端中管理多个会话、窗口和窗格，让工作在后台持续运行并可随时恢复。核心概念按层级展开：session 是顶层单位，用于管理一组窗口；window 是 session 中的工作区，类似标签页；pane 是窗口内的分割区域，每个 pane 运行一个 shell 命令；buffer 是复制/粘贴存储区。

操作层面分为命令和前缀键两类。会话管理命令包括创建命名会话 `tmux new -s <session-name>`、附加 `tmux attach -t <session-name>`、列出 `tmux ls`、切换 `tmux switch -t <session-name>`、重命名、杀死会话，以及前缀键 `Ctrl+b, d` 分离会话。前缀键默认为 `Ctrl+b`，图片也给出在 `~/.tmux.conf` 中改为 `Ctrl+a` 的配置片段。

快捷键部分覆盖窗口和窗格。窗口操作包括 `c` 新建、`n/p` 切换、数字键跳转、`,` 重命名、`w` 列表、`&` 关闭。窗格操作包括 `%` 垂直分割、`"` 水平分割、方向键切换、`o/;` 遍历、`x` 关闭、`!` 拆出、空格切换布局、`q` 显示编号。复制粘贴用 `[` 进入复制模式、`v` 选择、`y` 复制到 tmux buffer、`]` 或 `p` 粘贴。典型 workflow 是创建 `work` 会话，分割窗格运行 `make` 和 `tail -f log/app.log`，分离会话后再 attach 恢复现场。

## Key Claims

- explicit: tmux 是终端复用器，可以在一个终端中管理多个会话、窗口和窗格，并让工作在后台持续运行、随时恢复。
- explicit: 掌握 session、window、pane、buffer 四个概念后，可以覆盖大多数 tmux 使用场景。
- explicit: tmux 操作通常先按前缀键，默认是 `Ctrl+b`，再按后续键。
- explicit: 常用工作流是创建会话、分割窗格、运行不同任务、分离会话、再重新连接恢复现场。
- inferred: 对远程 Agent 或长时间命令执行场景，tmux 的核心价值是降低 SSH 断线和本地终端关闭造成的任务丢失风险。

## External Links

- reference: [github.com/gpakosz/.tmux](https://github.com/gpakosz/.tmux) — 图片底部列为交互式教程资源；not verified.
- reference: [github.com/tmux-plugins/tmux-example-config](https://github.com/tmux-plugins/tmux-example-config) — 图片底部列为配置示例资源；not verified.

## Links

- compiled-concept: [[concepts/tmux 远程工作流|tmux 远程工作流]] — 候选概念；本图提供会话、窗格和恢复现场的操作基础。
- map-entry: [[maps/Vibe Coding 工具地图|Vibe Coding 工具地图]] — 候选地图入口；适合归入远程/长时间 agent 执行工具。

## Maintenance Notes

- Vision ingest; QR code 未解码，未作为外链记录。
- 图片里 “man tmux” 是本地手册入口，不是 URL；未写入 External Links。
