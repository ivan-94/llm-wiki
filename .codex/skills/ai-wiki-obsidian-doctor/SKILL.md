---
name: ai-wiki-obsidian-doctor
description: 结合 Obsidian CLI 链接检查和本仓库 wiki 契约检查，诊断这个 AI wiki 的 Obsidian vault 健康状况。用户要求 Obsidian doctor、坏链审计、损坏笔记检查、孤岛/死端页面检查或 `/Users/ivan/workspace/ai/ai_llm_wiki` vault 健康报告时使用。
---

# AI Wiki Obsidian Doctor

使用这个 skill 对 AI wiki 的 Obsidian vault 视角做只读健康检查。它只负责诊断，不负责修复；任何修复都必须作为单独任务，并得到用户明确同意。

## 快速开始

在 wiki 根目录运行：

```bash
python3 .codex/skills/ai-wiki-obsidian-doctor/scripts/doctor.py --markdown
```

输出机器可读 JSON：

```bash
python3 .codex/skills/ai-wiki-obsidian-doctor/scripts/doctor.py --json
```

当 Obsidian 未打开或 CLI 不可用时，只运行仓库本地检查：

```bash
python3 .codex/skills/ai-wiki-obsidian-doctor/scripts/doctor.py --skip-obsidian --markdown
```

## 工作流

1. 解释结果前先读 `AGENTS.md`、`docs/wiki-templates.md` 和 `index.md`。
2. 从 wiki 根目录运行 doctor 脚本。
3. 将 Obsidian CLI 结果视为 vault 语义证据：
   - `unresolved`：坏链或无法解析的 wikilink。
   - `orphans`：没有入链的笔记。
   - `deadends`：没有出链的笔记。
4. 将仓库本地结果视为 AI wiki 契约证据：
   - `index.md` 缺少必需章节。
   - append-only `log.md` 单行记录格式错误。
   - 不依赖 Obsidian 即可检查的 path-style wikilink 坏链。
5. 行动前先分级：
   - `P0`：需要 CLI 证据但 CLI/vault 不可用、缺少 `index.md`，或 canonical 区域存在 unresolved link。
   - `P1`：canonical 区域孤岛/死端模式、`log.md` 格式错误、path-style wikilink 坏链。
   - `P2`：连接性较弱或卫生建议。
6. 如需写入持久化报告，放到 `outputs/reports/`，保留简短 Source Manifest，再更新 `index.md` 的 Outputs 并向 `log.md` 追加一条 `output` 记录。

## 边界

- 不运行破坏性 Obsidian CLI 命令，例如 `delete`、`move`、`rename`、`sync:restore` 或 `publish:*`。
- doctor 工作不修改 `human/inbox/` 或 `human/raw/`。
- 不用这个 skill 检查 raw coverage；raw/source 镜像状态使用 `ai-wiki-raw-diff`。
- 不把 `human/inbox/` 的 orphan/dead-end 结果视为 canonical 损坏。

## 验证

修改 helper 后运行：

```bash
python3 .codex/skills/ai-wiki-obsidian-doctor/scripts/test_doctor.py
```
