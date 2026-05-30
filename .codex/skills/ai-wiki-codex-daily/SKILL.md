---
name: ai-wiki-codex-daily
description: 为本 AI wiki 生成按日维度的 Codex 使用日报。用户要求 Codex 日报、今日 Codex 总结、session 复盘、交互复盘、workflow/harness 改进分析，或要求写入 human/raw/codex-daily 时使用。
---

# AI Wiki Codex 日报

## 概览

从 Codex thread/session 生成一篇“事实 + 轨迹 + 洞察 + 启发”的日报。用公开 thread 工具发现候选工作，用本机 group timeline 读取完整事实；公开工具不足时不要阻塞日报。

输出是一篇 human raw 笔记：`human/raw/codex-daily/YYYY-MM-DD_{title}.md`。不要自动 ingest 到 `human/sources`，不要自动更新 `index.md` 或 `log.md`。

## 工作流

1. 确定目标日期、标题和输出路径。
   - 默认日期：当前本地日期，默认标题：`Codex日报`。
   - 输出路径：`human/raw/codex-daily/YYYY-MM-DD_{title}.md`。
2. 发现候选 thread。
   - 如果 thread 工具未加载，先通过 tool discovery 搜索 `list_threads`。
   - 用 `list_threads` 获取当天相关 thread 的标题、preview、状态、cwd、创建/更新时间。
   - `read_thread` 只在有明确目的时使用：本机 timeline 缺失/滞后，或需要补读活跃、重要 thread 的当前状态。失败或未使用都记录到 `Source Manifest`。
3. 读取 group timeline。先看输出里的 `parent_workflows`，再按其中列出的 group ids 读取阶段事实。

   ```bash
   python3 .codex/skills/ai-wiki-codex-daily/scripts/collect_session_facts.py \
     --date YYYY-MM-DD
   ```

   按 group 读取事实：

   ```bash
   python3 .codex/skills/ai-wiki-codex-daily/scripts/collect_session_facts.py \
     --date YYYY-MM-DD \
     --group-id <group-id>
   ```

   只在调试或需要反查完整结构时使用 `--json` 或 `--full`。
4. 从 parent workflow 和 group 提炼事实：用户请求、最后状态、agent/subagent 编排、关键轨迹、产物、未解决问题和下一步。关键轨迹要覆盖重要探索、决策、转向、失败、验证、收尾，以及可观测的上下文压缩事件；不要把弱信号推断成压缩事件。
5. 写作前横向比较当天 parent workflows 和 groups：共同问题、验证缺口、协作摩擦、有效编排、工具/harness 改进点、可复用决策。日报正文默认按 parent workflow 归并，再按 group/stage 展开；没有父线程的独立 session 再单列。
6. 读取 `references/daily-note-template.md` 后写日报正文。正文由 Agent 基于事实取舍和复盘，不机械填模板；超长 worker prompt 只摘要任务、约束、写入范围和输出要求。目标文件已存在时，不要静默覆盖，除非用户明确要求 refresh。

## 日报质量标准

- frontmatter 必须包含 `type: codex-daily` 和 `ingest_policy: on-request`。
- `Source Manifest` 必须列出公开 thread 工具使用情况、读取过的 parent workflow ids、group ids、fallback 来源和覆盖限制。
- `Session 明细` 必须包含用户输入、最后状态、关键轨迹、产物和下一步。
- `分析` 要跨 session 提炼模式：协作摩擦、有效做法、漏掉的检查、值得复用的决策。
- `启发与建议` 要给出具体改进：如何更好地和 Codex 交互、workflow/harness 怎么优化、哪些内容适合生成 skill、该补什么知识、该深入研究什么。
- 不要粘贴完整 transcript、完整命令输出或冗长工具日志。
- 不要把日报当作 canonical source note；只有用户明确要求 ingest 时，才进入 `human/sources`。

## 辅助脚本

列出 group：

```bash
python3 .codex/skills/ai-wiki-codex-daily/scripts/collect_session_facts.py \
  --date YYYY-MM-DD
```

读取单个 group：

```bash
python3 .codex/skills/ai-wiki-codex-daily/scripts/collect_session_facts.py \
  --date YYYY-MM-DD \
  --group-id source-links-repair-workers
```

该脚本只用于提供事实时间线，不负责写日报正文。默认 YAML/Markdown；调试时可加 `--full` 或 `--json`。

## 参考

- `references/daily-note-template.md`：human raw 日报的通用结构，供 Agent 写作时参考。
