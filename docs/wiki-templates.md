# AI Wiki Templates

本文件保存长模板和示例。执行硬规则以 [AGENTS.md](../AGENTS.md) 为准。

## Common Frontmatter

`concepts/`、`synthesis/`、`questions/`、`maps/` 页面应支持学习状态字段：

```yaml
page_type: concept
updated_at: 2026-05-29
status: active
source_count: 3
learning_status: new
confidence: 2
difficulty: 3
review_after: 2026-06-05
```

字段约定：

- `status`: `active`、`draft`、`needs-review`、`deprecated`
- `learning_status`: `new`、`learning`、`familiar`、`mastered`、`review-needed`
- `confidence`: 1-5，用户或 agent 对当前理解的信心。
- `difficulty`: 1-5，学习难度。
- `review_after`: 建议下次复习日期；未知时写 `null`。

不要为了填字段伪造掌握度。没有依据时使用保守值，例如 `learning_status: new`、`confidence: 1`。

## Source Note Template

每个 `sources/*.md` 必须使用此结构。`.xmind` source 应记录 sheet 数量和 sheet 标题。

```markdown
---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/LLM/Transformer/Transformer.xmind"
source_relpath: "LLM/Transformer/Transformer.xmind"
ingested_at: 2026-05-29
status: ingested
---

# Transformer.xmind

## Source

- Raw file: [LLM/Transformer/Transformer.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/LLM/Transformer/Transformer.xmind>)
- Raw ref: `raw:LLM/Transformer/Transformer.xmind`
- Type: xmind
- Status: ingested
- Sheets processed: 1/1 (`Sheet 1`)

## Summary

## Source Digest

## Key Claims

## External Links

## Links

## Maintenance Notes
```

`source_type` 建议值：`xmind`、`image`、`markdown`、`pdf`、`excalidraw`、`other`。

`status` 建议值：

- `ingested`: 已完整处理。
- `partial`: 有可用内容，但存在缺失或解析限制。
- `blocked`: 当前无法提取有效内容，需要人工处理。
- `needs-review`: 已处理但需要用户审阅。

区块含义：

- `Source`: raw 路径、类型、状态、sheet 覆盖等可复查元数据。
- `Summary`: 该 raw 的整体摘要。
- `Source Digest`: LLM 理解 source 后写出的提炼摘要，不是机械 outline、抽样文本、截断导出或完整 raw 导出。
- `Key Claims`: 可被 concept/entity/synthesis 引用的主张或事实；重要 claim 要可追溯，并区分 raw 明确表达与 agent 推断。
- `External Links`: raw 中出现的 URL 或外部资料引用；无 URL 时显式写未发现，不伪造链接。
- `Links`: 本 source 创建或更新过的 wiki 页面；必须使用关系类型，禁止裸 wikilink 列表。
- `Maintenance Notes`: 解析失败、图片不清、冲突、待补充上下文、异常节点、结构错位。

`Source Digest` 边界：

- 先读完整可用 source，再用自己的话概括它“讲了什么、为什么重要、能贡献给哪些知识节点”。
- 对 `.xmind`，不要机械复制层级树；只提炼主题结构、关键分支含义、重要路径、异常占位和可编译知识点。
- 对大型 `.xmind`，digest 通常控制在 30-80 行以内，除非用户明确要求更详细；行数不是目标，理解密度才是目标。
- 对大型或多 sheet source，压缩前必须检查高信号细节是否被保留。
- 对图片，提炼视觉结构、可靠可见文字、关系和局限，不做伪 OCR 全文。
- 对 PDF/Excalidraw，提炼可复用内容、关键结构和提取限制，不保存大段文本预览或元素清单。
- 完整 raw 细节必须回 raw 读取，不能把 `sources/` 变成 raw 的 markdown cache。

`Key Claims` 证据边界：

- `explicit`: raw 或导出内容明确表达、列举或强支撑的 claim。
- `inferred`: agent 基于 source 做出的归纳、命名、分类或实践含义；必须能追溯到 source 中的明确内容，不能写成 raw 已经明说的事实。

External links 示例：

```markdown
## External Links

- learning-source: [OpenAI Prompt Engineering](https://platform.openai.com/docs/guides/prompt-engineering) — source 中列为提示语工程学习来源；not verified.
- related-reading: `How Long Contexts Fail` — source 只有标题，没有 URL；needs follow-up.
```

Source Links 示例：

```markdown
## Links

- compiled-concept: [[concepts/LLM 评估|LLM 评估]] — 提炼离线/在线评估、Dataset、Experiment、Score 等概念。
- compiled-entity: [[entities/Langfuse|Langfuse]] — source 以 Langfuse 为评估平台参照。
- map-entry: [[maps/提示语与上下文工程学习地图|提示语与上下文工程学习地图]] — 纳入提示语/上下文学习路径。
```

## Concept Template

`concepts/` 是个人知识图谱的核心节点。概念页不是单份资料摘要，而是跨 source 的可学习综合。

```markdown
---
page_type: concept
updated_at: 2026-05-29
status: active
source_count: 1
learning_status: new
confidence: 1
difficulty: 3
review_after: null
---

# 上下文工程

## Definition

## Why It Matters

## Mental Model

## Key Claims

## Examples

## Common Confusions

## Evidence

## Relations

## My Understanding

## Review Questions

## Open Questions
```

要求：

- `Definition`: 一句话或短段定义。
- `Why It Matters`: 为什么值得学。
- `Mental Model`: 方便回忆的心智模型。
- `Key Claims`: 稳定结论，一条一 claim，尽量带 confidence 或 evidence。
- `Examples`: 具体例子，帮助复习。
- `Common Confusions`: 易混点、误区、边界。
- `Evidence`: 链接到 `sources/...`，不要只写“根据资料”。
- `Relations`: 使用 Typed Relations。
- `My Understanding`: 用用户能复述的语言写当前理解。
- `Review Questions`: 主动回忆问题。
- `Open Questions`: 缺口、矛盾、待验证点。

## Entity Template

`entities/` 用于人物、公司、项目、产品、工具、框架、模型、组织。不要为只出现一次且无复用价值的名字创建空实体页。

```markdown
---
page_type: entity
updated_at: 2026-05-29
status: active
source_count: 1
---

# LangChain

## What It Is

## Role In This Wiki

## Key Facts

## Related Concepts

## Evidence

## Open Questions
```

## Synthesis Template

`synthesis/` 用于跨来源分析、对比、路线图和判断。它通常来自 query 或多次 ingest 后的 compile。

```markdown
---
page_type: synthesis
updated_at: 2026-05-29
status: active
source_count: 3
learning_status: learning
confidence: 2
difficulty: 4
review_after: null
---

# RAG vs 长上下文

## Thesis

## Comparison

## Evidence

## Implications

## Related Concepts

## My Take

## Open Questions
```

## Question Template

`questions/` 只保存用户显式提出或要求创建的问题。Agent 不能因为内容“值得复用”、跨多个 source、适合沉淀或后续可能有用，就自行创建 question 页面。

允许创建或更新 `questions/` 的条件：

- 用户直接提出一个问题，并明确要求沉淀、写入 wiki、保存为 question，或使用等价表达。
- 用户明确要求创建某个问题页、复用问题页模板，或将某次问答归档到 `questions/`。
- 已存在的问题页是用户显式创建的，且当前 source 或回答需要更新其证据、答案或 follow-up。

不允许：

- 在 ingest 或 compile 中自动创建问题页。
- 把 agent 自己归纳出的“好问题”写入 `questions/`。
- 用 `Questions` 或 `Review Questions` 区块替代 `questions/` 页面创建规则；页面内复习题和开放问题可以正常存在。

```markdown
---
page_type: question
updated_at: 2026-05-29
status: active
learning_status: learning
confidence: 2
review_after: null
---

# 什么时候该用 RAG 而不是长上下文？

## Question

## Short Answer

## Answer

## Evidence

## Filed Back To

## Follow-up Questions
```

## Map Template

`maps/` 是 MOC / 学习地图，负责组织学习路径，不替代 `index.md`。

```markdown
---
page_type: map
updated_at: 2026-05-29
status: active
scope: Agent
---

# Agent 学习地图

## Purpose

## Entry Points

## Learning Path

## Core Concepts

## Key Entities

## Synthesis To Read

## Review Queue

## Open Gaps
```

地图要回答：“我从哪里开始？下一步读什么？哪些概念互相关联？哪些还没掌握？”

## Typed Relations Example

```markdown
## Relations

- prerequisite: [[concepts/Token and Embedding|Token 和 Embedding]]
- contrasts-with: [[concepts/RAG|RAG]]
- implemented-by: [[entities/LangChain|LangChain]]
- related-source: [[sources/LLM/Transformer/Transformer.xmind|Transformer.xmind]]
- map-entry: [[maps/大模型学习地图|大模型学习地图]]
- entity-candidate: Langflow
```
