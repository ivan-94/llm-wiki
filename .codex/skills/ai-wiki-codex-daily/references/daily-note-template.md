# Codex 日报模板

用于 `human/raw/codex-daily/YYYY-MM-DD_{title}.md`。

这是写作结构，不是机械填空模板。Agent 需要基于 thread/session 事实进行判断、归纳和复盘，保留必要关键轨迹。

```markdown
---
title: "{date} {title}"
date: {date}
type: codex-daily
generated_at: {generated_at}
source_strategy: "{source_strategy}"
ingest_policy: on-request
---

# {date} {title}

## Source Manifest

- 公开 thread 工具:
  - <使用了哪些公开工具、筛选规则、日期时区；`read_thread` 只在实际使用时列出>
- Fallback 本机文件:
  - <group index 命令，例如 collect_session_facts.py --date YYYY-MM-DD>
  - <读取过的 parent workflow ids>
  - <读取过的 group ids>
  - <fallback 文件来源，例如 ~/.codex/sessions/YYYY/MM/DD/rollout-*.jsonl>
- 覆盖限制:
  - <哪些信息可能缺失、过期或不可见>

## 今日概览

- 一句话总结: <today's Codex work in one sentence>
- 主要项目: <repo / 主题>
- 完成状态: <已完成 / 进行中 / 阻塞 / 混合>
- 最值得复盘的问题: <一个摩擦点或成功模式>
- 横向对比结论: <当天 sessions 的共同问题、有效模式或工具改进点>

## Session 明细

### <parent workflow / group title / session title>

- Threads: `<thread-id>` / <thread id list>
- Parent thread: `<parent-thread-id or none>`
- CWD: `<path or unknown>`
- 读取来源:
  - <parent workflow id / group-id；如额外使用公开 thread 工具也列出>
- 用户输入:
  - <短请求可原样列出；超长 worker prompt 摘要为任务、约束、写入范围、输出要求>
- 最后状态: <已完成 / 活跃 / 中断 / 阻塞 / 未知>
- 关键轨迹:
  - <3-6 条短句，描述重要探索、决策、转向、失败、验证、收尾或可观测的上下文压缩事件>
- 产物:
  - <文件、PR、笔记、命令、日报条目或无>
- 未解决/下一步:
  - <后续动作或无>

### 异常 Session

- Thread: `<thread-id>`
- 状态: <中断 / 阻塞 / 未知>
- 原因: <status.reason 或 Agent 判断>
- 影响: <为什么需要单独展开>
- 下一步: <重试、人工确认、parent 接管或无需动作>

## 分析

- 做得好的地方:
  - <值得复用的模式>
- 做得不好的地方:
  - <漏掉的检查、弱提示、弱工具、过多手工工作>
- 可以沉淀:
  - <docs、wiki 页面、可复用命令、测试、清单>
- 可以改进:
  - <workflow、harness、提示词、sub-agent 边界、验证门禁>

## 启发与建议

- 更好的 Codex 交互:
  - <提示或 steering 建议>
- Workflow / harness 改进:
  - <自动化或验收测试想法>
- 候选 skills:
  - <skill 名称建议和原因>
- 需要补的知识:
  - <主题和重要性>
- 值得深入研究:
  - <研究线索>

## 待跟进

- [ ] <具体后续动作>
```
