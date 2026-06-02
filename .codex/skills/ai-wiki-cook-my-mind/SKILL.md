---
name: ai-wiki-cook-my-mind
description: 将用户输入、当前 Agent 聊天上下文，或二者混合，烹饪成保留原始想法、区分 Agent 延伸、带中文信息图的 AI wiki human inbox 思维快照。用户说 cook my mind、总结我的想法、整理我的思路、把这段对话/想法沉淀成笔记，且目标是记录自己的思考而不是 ingest 外部 raw 时使用。
---

# AI Wiki Cook My Mind

## 目标

把用户自己的输入或当前聊天里的用户表达 cook 成一篇可回看、复盘和继续推理的 inbox 笔记。它不是 canonical ingest：默认只写入 `human/inbox/cook-my-mind/`，frontmatter 使用 `ingest_policy: on-request`。除非用户明确要求后续 ingest 或 compile，否则不要更新 `index.md`、`log.md`、`sources/`、`human/sources/`、concepts、entities、synthesis、maps 或 questions。

## 输出边界

```text
human/inbox/cook-my-mind/YYYY-MM-DD_<中文思考主题>.md
human/inbox/cook-my-mind/assets/YYYY-MM-DD_<中文思考主题>/infographic.webp
.codex/cache/cook-my-mind/<date-time-or-topic-hash>/source-capture.md
.codex/cache/cook-my-mind/<date-time-or-topic-hash>/imagegen-original.*
```

`.codex/cache/` 必须保持 git ignored。写最终笔记前，读取 `AGENTS.md` 中与 human boundary、`human/inbox/`、`human/raw/` 有关的规则。不要把 cooked note 当作 source note。

## 输入模式

- `input-only`：只 cook 用户本次粘贴、输入或指定的一段内容。
- `current-chat`：只 cook 当前 Agent 聊天上下文中的用户表达。
- `mixed`：把用户新输入和当前聊天上下文一起 cook。默认使用此模式，除非用户明确限定来源。

来源范围不明确时，优先使用最近一段连续、与当前主题直接相关的用户表达，并在 `Source Manifest` 记录范围限制。不要为了完整而回收整条长线程里的无关内容。

## 硬规则

- `我的原始想法` 是必选章节。它是证据层，不是 Agent 摘要层。
- 用户本次明确输入的原始想法如果篇幅可控，应尽量完整保留；如果很长，可以按段落保留高信号原文，但必须说明省略规则和覆盖限制。
- 从聊天上下文提取原始想法时，只摘取用户表达；不要把 Agent 回复、建议或措辞混入 `我的原始想法`。
- Agent 的总结、推断、延伸和行动建议必须与用户原文分开，不要伪装成用户原话。
- 不做心理诊断、人格判断或动机归因；只整理文本可支持的问题、取舍、假设、张力和下一步。
- 信息图是必选输出，是视觉总结方式，不是装饰封面。如果 imagegen 不可用、生成失败、无法复制原图到 cache、或无法产出最终 `infographic.webp`，本次 cook 视为 blocked：保留 `source-capture.md` 和诊断材料，向用户说明 blocker，不写最终 cooked note。
- 默认不联网扩写，也不把用户想法外推成外部事实；除非用户明确要求查证，外部事实只能标注为待核验。

## 工作流

1. 判定输入模式和来源范围。
2. 建立 cache 目录，写 `source-capture.md`：`captured_at`、mode、用户原始想法、聊天范围、消息边界、选择规则、省略规则，以及用户原文与 Agent 整理的边界。
3. Cook 内容：压缩核心问题，抽出明确判断、隐含假设、还在摇摆的地方，延伸洞察，并产出下一步行动和可复用原则。
4. 生成信息图：使用 `imagegen` skill/tool 的内置模式；prompt 来自原始问题、核心判断、关键张力、延伸洞察、下一步行动和可复用原则；默认中文；适合做成思维地图、取舍图、因果图、行动路径图或原则卡。
5. 保存信息图：把选定原图复制到 `.codex/cache/cook-my-mind/<id>/imagegen-original.<ext>`，再把最终图移动、复制或转换为 `human/inbox/cook-my-mind/assets/<note-stem>/infographic.webp`。
6. 最终 Markdown note 由 Agent 直接写作。不要使用 note builder 脚本拼模板。

## 最终笔记要求

Frontmatter：

```yaml
---
type: cook-my-mind
ingest_policy: on-request
inbox_status: unread
inbox_created_at: YYYY-MM-DD
inbox_read_at:
raw_path:
ingested_at:
archive_reason:
source_kind: user-thought
source_mode: input-only | current-chat | mixed
captured_at: YYYY-MM-DDTHH:MM:SS+TZ
---
```

推荐正文结构：

```markdown
# <中文思考主题>
## 我的原始想法
## 速读
## 我真正关心的问题
## 想法地图
## 已经明确的判断
## 隐含假设
## 还在摇摆的地方
## 可以延伸出的洞察
## 可复用原则
## 下一步行动
## 信息图
![[human/inbox/cook-my-mind/assets/<note-stem>/infographic.webp]]
## Source Manifest
```

质量规则：正文默认中文，保留必要英文术语；文件名优先中文可读，不机械照搬用户长句；`已经明确的判断` 只放用户文本支持较强的结论；`隐含假设`、`还在摇摆的地方`、`可以延伸出的洞察` 必须标注为 Agent 归纳或 Agent 延伸；内容很短时仍保留完整章节，但每节可以很短。

`Source Manifest` 必须列出 source mode、capture source、capture scope、original thought preservation、agent contribution、cache path、infographic path、limitations。没有问题写 `issues: none`。
