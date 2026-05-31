---
name: ai-wiki-codex-weekly
description: Generate a weekly work review from existing Codex daily reports in this AI wiki. Use when the user asks for a Codex weekly report, seven-day daily report synthesis, weekly workflow/work-efficiency review, or writing to human/raw/codex-weekly.
---

# AI Wiki Codex 周报

## 概览

从已经存在的 Codex 日报生成一篇周报。周报的重点不是复述执行流水，而是基于日报材料提炼一周的工作主线、工作流变化、效率损耗或收益、质量风险、组织化沉淀和下周调整。

输出是一篇 human raw 笔记：`human/raw/codex-weekly/YYYY-MM-DD_to_YYYY-MM-DD_Codex周报.md`。不要自动 ingest 到 `human/sources`，不要自动更新 `index.md` 或 `log.md`。

## 输入边界

- 输入材料限于 `human/raw/codex-daily/` 下已经存在的日报 Markdown。
- 缺失或格式不完整的日期只在 `每日摘要索引` 中表达。
- collector 仅做日期、文件、Obsidian 链接、frontmatter 和分节抽取。

## 时间范围

- 默认：目标日期所在自然周的周一到目标日期；目标日期是周日时即完整自然周。
- 用户给出明确起止日期时，按显式范围。
- 用户明确要求“最近 7 天”或滚动窗口时，按目标日期向前滚动 7 天。

## 工作流

1. 确定周报范围、标题和输出路径。
2. 读取 `references/weekly-note-template.md`。
3. 收集日报材料：

   ```bash
   python3 .codex/skills/ai-wiki-codex-weekly/scripts/collect_daily_reports.py \
     --date YYYY-MM-DD
   ```

   显式范围可使用 `--start-date YYYY-MM-DD --end-date YYYY-MM-DD`；滚动窗口可使用 `--recent-days 7 --date YYYY-MM-DD`。
4. 阅读 collector 输出中的每日链接、缺失状态、软校验 warning 和关键分节。
5. 写周报正文。不要机械拼接七篇日报；先归纳 `本周主线`，再写对上汇报、每日索引、分析洞察、下周调整和待跟进归并。
6. 如果目标文件已存在，不要静默覆盖，除非用户明确要求 refresh。

## 周报质量标准

- frontmatter 必须包含 `type: codex-weekly`、`week_start`、`week_end` 和 `ingest_policy: on-request`。
- `工作周报（对上汇报）` 面向上级同步本周推进、结果、风险和下周计划；面向业务和管理语境表达，不展开执行细节。
- `本周主线` 用 3-5 条概括这一周真正围绕的工作主题，不做冗长分类表。
- `每日摘要索引` 必须用 Obsidian wikilink 引用已存在日报；缺失日期写明 missing，不伪造链接。
- `分析与洞察` 必须提升到工作流、工作方式、效率、质量或组织化层面；日报中的执行记录只是材料来源，不是分析主体。
- `启发与下周调整` 只写少量高价值行动选择，说明触发条件和要改变的工作方式。
- `待跟进归并` 要合并同类待办，并保留来源日报链接；不要复制七天 checklist。
- 不要粘贴完整日报正文、完整命令输出或冗长工具日志。

## 验证

生成后至少检查：

```bash
rg -n "^(type: codex-weekly|week_start:|week_end:|ingest_policy: on-request|## 工作周报（对上汇报）|## 本周主线|## 每日摘要索引|## 分析与洞察|## 启发与下周调整|## 待跟进归并)" \
  human/raw/codex-weekly/YYYY-MM-DD_to_YYYY-MM-DD_Codex周报.md
git diff --check -- human/raw/codex-weekly/YYYY-MM-DD_to_YYYY-MM-DD_Codex周报.md
```
