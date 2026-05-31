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
  - <使用了哪些公开工具、筛选规则、日期时区；默认只用 `list_threads` 做候选发现>
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

## 工作日报（对上汇报）

<以 Codex 使用者第一人称或团队工作口吻撰写，面向上级同步今天推进了什么、结果怎样、风险和下一步。避免暴露过多 agent/thread/tool 内部细节。>

- 今日推进:
  - <完成或推进的 2-5 项工作>
- 当前结果:
  - <已完成、已验证、已产出的内容>
- 风险与问题:
  - <仍未解决的问题、阻塞、质量风险；没有则写“暂无明显阻塞”>
- 下一步:
  - <明天或后续最重要的 1-3 个动作>

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

## 分析与洞察

<不要按栏目罗列。先从今天所有 session 中选出 2-4 个最值得复盘的张力点：哪里一开始看起来合理、后来被新的事实、反馈、验证或真实使用约束推翻；哪个成功依赖某种证据路径及时暴露问题；哪个纠正暴露了 Agent 的默认倾向、误解或替代路径；如果没有这个纠正或验证，最可能留下什么隐患。>

<每个洞察写成一段，而不是一句原则。段落里要包含：事实片段 -> 暴露的问题 -> 背后的机制 -> 以后应该怎样改变工作方式。优先写“改变 Agent 下一次怎么做”的洞察，而不是正确但泛化的道理。>

## 启发与下一步

<不要把所有建议都列出来。只写最值得改变的 2-4 件事，把上面的洞察转成行动选择。每条建议说明：它来自今天哪个具体摩擦或失败信号；要改变的是输入澄清方式、执行流程、验证方式、工具选择、交接/沉淀方式还是复盘口径；下次遇到什么触发条件时启用；如果不做，最可能重复今天哪个问题。>

## 待跟进

- [ ] <具体后续动作>
```
