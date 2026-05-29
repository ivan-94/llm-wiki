# AI Wiki Agent Guide

本目录是 AI 主题个人 LLM Wiki 的 canonical workspace。Agent 的任务不是一次性回答问题，而是持续把 raw 资料编译成可学习、可回顾、可关联、可复用的个人知识图谱。

核心目标：

- raw 是只读事实来源。
- wiki 是 LLM 维护的编译后知识层。
- 每次 ingest、query、review、lint 都要判断是否值得沉淀回 wiki。
- 页面应帮助用户学习和复习，而不只是保存摘要。

## Fixed Paths

- Raw source root: `/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI`
- Wiki root: `/Users/ivan/workspace/ai/ai_llm_wiki`
- Canonical guide: `/Users/ivan/workspace/ai/ai_llm_wiki/AGENTS.md`

处理路径时必须保留空格、中文、括号、冒号等原始字符。shell 命令中始终引用完整路径。

## Directory Contract

```text
AI/
  AGENTS.md
  index.md
  log.md
  sources/
  concepts/
  entities/
  synthesis/
  questions/
  maps/
  outputs/
    slides/
    charts/
    reports/
    briefs/
  assets/
```

- `sources/`: raw 文件的一一转换结果，目录层级镜像 raw，是证据入口。
- `concepts/`: 概念页，跨多个 source 的稳定学习节点。
- `entities/`: 人物、公司、项目、产品、工具、框架、模型、组织。
- `synthesis/`: 跨来源分析、对比、路线图、判断、wiki 健康报告。
- `questions/`: 值得长期复用的问题与答案。
- `maps/`: MOC / 学习地图，组织学习路径和回顾入口。
- `outputs/`: 可交付的派生输出，如 slides、charts、reports、briefs。
- `assets/`: wiki 生成或复制的附件；不默认复制 raw 原件。

不要再使用旧目录名 `topics/` 或 `syntheses/`。旧内容应迁移到 `concepts/` 和 `synthesis/`。

## Operating Loop

推荐循环：

```text
Collect -> Ingest -> Compile -> Query -> Output -> File Back -> Review -> Lint -> Collect
```

- `Collect`: 用户收集 raw，agent 不要求 raw 整洁。
- `Ingest`: 处理单个 raw，建立或更新 `sources/...`。
- `Compile`: 把 source 中的知识更新到 `concepts/`、`entities/`、`synthesis/`、`maps/`。
- `Query`: 基于 wiki 回答问题，必要时回 raw 查证。
- `Output`: 生成可复用报告、图表、幻灯片、brief。
- `File Back`: 将高价值回答或输出归档回 wiki。
- `Review`: 主动回忆、复习、更新掌握度。
- `Lint`: 体检断链、孤立页、重复页、弱证据、矛盾和缺口。

## Source Mapping

`sources/` 必须镜像 raw 目录层级和文件名。

规则：

- raw `.md` 直接映射为同名 `.md`。
- 其他 raw 文件映射为 `<原文件名含扩展名>.md`。

示例：

```text
raw:  LLM/Transformer/Transformer.xmind
wiki: sources/LLM/Transformer/Transformer.xmind.md

raw:  生图/商品画图/高级1.png
wiki: sources/生图/商品画图/高级1.png.md

raw:  Agent/build-cli-for-agent-checklist.md
wiki: sources/Agent/build-cli-for-agent-checklist.md
```

支持类型优先级：

- P0: `.xmind`、图片。
- P1: `.md`。
- P2: `.pdf`、`.excalidraw`。

P2 使用 best-effort 提取。失败时记录限制和待处理项，不要假装完整。

## Raw Resource Links

source note 引用原始资源时必须使用 FinderX iCloud 链接，方便从 Obsidian 直接打开 raw 文件。

格式：

```text
finderx://open?icloud=<URL encoded path under iCloud Drive>
```

本项目 raw root 对应的 iCloud 前缀是：

```text
思维导图/AI
```

示例：

```markdown
- Raw file: [Agent/LangChain.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Agent/LangChain.xmind>)
- Raw ref: `raw:Agent/LangChain.xmind`
```

规则：

- 链接必须指向 raw 文件，不指向 wiki 派生文件。
- URL encode 每个路径片段，保留 `/` 分隔符。
- 同时保留 `raw:<source_relpath>`，方便 agent 搜索和脚本处理。

## Raw Boundary

Raw source root 是只读事实来源。

禁止：

- 修改、重命名、移动、删除 raw 文件。
- 在 raw 目录或其旁边写中间产物。
- 为了让工具成功而修复 raw 文件。
- 直接解包、修改或手写解析 `.xmind`。

允许：

- 读取 raw 文件。
- 使用 vision 理解图片。
- 按 Ingest Workflow 转换 `.xmind`。
- 在 wiki 的 `sources/`、`concepts/`、`entities/`、`synthesis/`、`questions/`、`maps/`、`outputs/`、`assets/` 中写派生产物。

如果 raw 需要人工修复，在 source note 的 `Maintenance Notes`、`index.md` 的 `Needs Attention` 和 `log.md` 中记录。

## XMind Handling

处理 `.xmind` raw 时使用 `ai-wiki-xmind-ingest` skill 或 `xmind-cli` skill 进行转换。正常路径优先导出 Markdown；失败或用户要求元数据时再做诊断。

不要直接操作 `.xmind` zip 包或依赖临时自写解析器。

导出的 Markdown 是临时读取材料，不是 wiki 产物。不要把完整 `.xmind` 导出树原样粘贴进 `sources/`。source note 只保存 LLM 消化和提炼后的 digest；需要完整细节时，通过 Raw file 的 FinderX 链接和 `xmind-cli` 回 raw 重读。

如果转换失败：

- source note `status` 标为 `partial` 或 `blocked`。
- 记录失败摘要、可行的人工下一步。
- 继续处理其他 source。

## Image Handling

图片 ingest 必须通过 agent 的 vision 能力形成可复查描述，但不承诺完美 OCR。

每张图片的 source note 至少记录：

- 图像类型：截图、手写笔记、白板、产品图、流程图、信息图等。
- 可见文字：只写能可靠识别的文字；不确定处标注 `uncertain`。
- 结构描述：布局、箭头、层级、关系。
- 知识点：可纳入 concept/entity/synthesis 的内容。
- 局限：模糊、遮挡、低分辨率、文字不可读等。

同一目录下多张图片明显属于一组时，先为每张图片建 source note，再按目录创建一个综合 concept 或 synthesis 页面。

## Asset Policy

默认不复制 raw 图片或附件。source note 记录 `raw_path` 和 `source_relpath` 即可。

只有需要 Obsidian 内稳定预览、标注裁剪图、或生成派生图时，才复制到：

```text
assets/sources/<raw 相对目录>/<原文件名>
```

复制或生成 asset 后，必须在对应 source note 中说明 asset 路径和用途。

## Page Language And Links

- 正文默认中文，保留必要英文术语。
- 文件名优先可读，中文名和官方英文名可混用。
- 内部链接使用 Obsidian wikilink。

示例：

```markdown
[[concepts/上下文工程|上下文工程]]
[[entities/LangChain|LangChain]]
```

不要为 slug 化牺牲可读性。

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

## Typed Relations

`Relations` 不要只堆链接。尽量使用关系类型，让 Obsidian 图谱可解释。

推荐类型：

- `prerequisite`: 先修概念。
- `part-of`: 属于更大主题。
- `contains`: 包含子概念。
- `contrasts-with`: 易混或对比对象。
- `enables`: 支撑或使能另一个概念。
- `implemented-by`: 被某工具、框架、产品实现。
- `used-in`: 被某场景或 synthesis 使用。
- `related-source`: 相关 source note。
- `related-question`: 相关问题页。
- `map-entry`: 所属学习地图。
- `entity-candidate`: 候选实体，尚未值得建页。

示例：

```markdown
## Relations

- prerequisite: [[concepts/Token and Embedding|Token 和 Embedding]]
- contrasts-with: [[concepts/RAG|RAG]]
- implemented-by: [[entities/LangChain|LangChain]]
- related-source: [[sources/LLM/Transformer/Transformer.xmind|Transformer.xmind]]
- map-entry: [[maps/大模型学习地图|大模型学习地图]]
- entity-candidate: Langflow
```

## Source Note Template

每个 `sources/*.md` 必须使用此结构：

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

## Summary

## Source Digest

## Key Claims

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

- `Source`: raw 路径、类型、状态。
- `Summary`: 该 raw 的整体摘要。
- `Source Digest`: LLM 理解 source 后写出的提炼摘要，不是机械 outline、抽样文本、截断导出或完整 raw 导出。
- `Key Claims`: 可被 concept/entity/synthesis 引用的主张或事实；重要 claim 要可追溯。
- `Links`: 本 source 创建或更新过的 wiki 页面。
- `Maintenance Notes`: 解析失败、图片不清、冲突、待补充上下文。

`Source Digest` 边界：

- 先读完整可用 source，再用自己的话概括它“讲了什么、为什么重要、能贡献给哪些知识节点”。
- 对 `.xmind`，不要机械复制层级树；只提炼主题结构、关键分支含义、重要路径、异常占位和可编译知识点。
- 对大型 `.xmind`，digest 通常控制在 30-80 行以内，除非用户明确要求更详细；行数不是目标，理解密度才是目标。
- 对图片，提炼视觉结构、可靠可见文字、关系和局限，不做伪 OCR 全文。
- 对 PDF/Excalidraw，提炼可复用内容、关键结构和提取限制，不保存大段文本预览或元素清单。
- 完整 raw 细节必须回 raw 读取，不能把 `sources/` 变成 raw 的 markdown cache。
- 禁止把 source digest 写成“导出前 N 行”“采样文本”“完整目录树压缩版”。这些只是中间材料，不是 digest。

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

`questions/` 只保存有复用价值的问题，不保存每个临时问答。

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

## Output Policy

`outputs/` 存放可交付、可复用的派生文件。

示例：

```text
outputs/slides/llm-wiki-intro.marp.md
outputs/charts/source-growth.png
outputs/reports/agent-workflow-comparison.md
outputs/briefs/rag-vs-long-context.md
```

生成 output 后必须：

- 在相关 `questions/` 或 `synthesis/` 页面链接它。
- 在 `index.md` 的 `Outputs` 中登记。
- 在 `log.md` 追加 `output` 记录。

## Ingest Workflow

Ingest 处理的是单个 raw。目标是建立或更新对应 `sources/...`。

开始前：

1. 读取 `AGENTS.md`。
2. 读取 `index.md` 和最近的 `log.md` 记录。
3. 确认 raw 文件路径和目标 source note 路径。

处理 `.xmind` raw 时使用 `ai-wiki-xmind-ingest` skill；正常转换直接导出 Markdown，失败或需要诊断时再读取元数据。

导出的 Markdown 只作为临时输入，用来理解 source，并编写 `Summary`、`Source Digest`、`Key Claims` 和下游概念页。不要把完整导出结果、机械 outline 或抽样文本原样写入 source note。

每次 ingest 必须更新：

- 对应 `sources/...` 页面。
- `index.md` 的 `Source Coverage`。
- `log.md`。

Ingest 后必须进入 Compile 判断：这个 source 是否改变了已有概念、实体、综合、学习地图或问题页。

## Compile Workflow

Compile 是把 source 内容编译进全局知识图谱。

应该更新：

- 明显相关的 `concepts/`、`entities/` 页面。
- 已存在且被新 source 改变的 `synthesis/`、`questions/`、`maps/` 页面。
- `index.md` 的 Concepts、Entities、Synthesis、Maps、Review Queue。

可以创建：

- 反复出现、对长期理解有价值的 concept/entity 页面。
- 明显跨多个 source 的 synthesis 页面。
- 能组织学习路径的 map 页面。

不要创建：

- 只在单一 source 中偶然出现且无复用价值的碎片页。
- 没有 Evidence/Relations 的空壳页面。
- 只是产品名列表的实体页；先用 `entity-candidate` 记录。

每次 compile 后，在 source note 的 `Links` 中列出创建或修改过的页面。

## Conflict Handling

当新 source 与旧页面冲突时，不要自动抹平。

规则：

1. 不删除旧说法，除非它只是明显错误的转录或解析问题。
2. 在相关页面的 `Key Claims` 或 `Evidence` 中标注来源差异。
3. 在 `Open Questions` 中记录待澄清问题。
4. 重要冲突创建或更新 `synthesis/` 下的对比页。
5. 在 `log.md` 记录本次 ingest/compile 发现的冲突。

## Query Workflow

回答问题前：

1. 先读 `index.md`。
2. 搜索并读取相关 `sources/`、`concepts/`、`entities/`、`synthesis/`、`questions/`、`maps/` 页面。
3. 必要时回 raw 查原始证据。
4. 用 wiki 内容回答，并说明关键证据来自哪些页面。

默认不把所有问答写入 wiki。满足任一条件才写入 `questions/` 或 `synthesis/`：

- 用户明确说“沉淀”“写入 wiki”“保存”。
- 答案综合了多个 source/concept/entity。
- 产生新的比较、判断、路线图、分类法、决策依据。
- 后续大概率会复用。

写回后必须更新 `index.md`、`log.md`，并在相关 concept/entity 的 `Relations` 或 `Evidence` 中互链。

## Review Workflow

Review 面向学习和回顾，不是资料清理。

触发条件：

- 用户要求复习、回顾、测验、检查掌握度。
- `review_after` 到期。
- 页面 `learning_status` 为 `new`、`learning` 或 `review-needed`。

流程：

1. 读取 `index.md` 的 `Review Queue` 和相关 `maps/`。
2. 读取目标 concept/synthesis/question 页面。
3. 生成 3-5 个主动回忆问题，优先考 Definition、Mental Model、Common Confusions 和关系。
4. 根据用户回答更新 `confidence`、`learning_status`、`review_after` 和 `My Understanding`。
5. 在 `log.md` 追加 `review` 记录。

不要把 review 写成泛泛总结。它必须帮助用户发现“哪里没掌握”。

## Lint Workflow

lint 不自动定时执行，只在用户要求时执行。

输出写入：

```text
synthesis/wiki-health-YYYY-MM-DD.md
```

同时更新 `index.md` 的 `Needs Attention` 和 `log.md`。

检查项：

- source coverage: raw 是否都有对应 source note。
- broken links: Obsidian links 是否指向存在页面。
- orphan pages: 页面是否没有被 index/source/concept/entity/map 引用。
- stale claims: 旧页面是否被新 source 反驳或需要更新。
- contradictions: 冲突 claims 是否没有标注。
- missing pages: 高频概念/实体是否缺少独立页。
- weak evidence: claim 是否缺少 source 链接。
- weak relations: `Relations` 是否只有无类型链接。
- review drift: `review_after` 过期但未进入 Review Queue。
- raw mirror bloat: `sources/` 是否保存了完整 raw 导出而不是 digest。
- mechanical digest: `Source Digest` 是否只是机械 outline、文本采样或截断导出，而不是 LLM 消化后的提炼。

## Search And Tool Use

优先使用快速、本地、可复现的工具：

- `rg` 搜索 wiki 内容。
- `find` 列 raw/wiki 文件。
- `xmind-cli` / `ai-wiki-xmind-ingest` 处理 `.xmind`。
- vision 查看图片。
- 必要时写一次性脚本做统计、链接检查、表格或图表生成。

不要引入复杂搜索基础设施，除非 index 和 `rg` 已经明显不够用。

## Index Contract

`index.md` 是全库目录和状态总览，保持人工可读，不承担学习路径职责。学习路径放在 `maps/`。

固定结构：

```markdown
# AI Wiki Index

## Recently Updated

## Source Coverage

## Concepts

## Entities

## Synthesis

## Maps

## Questions

## Outputs

## Review Queue

## Needs Attention
```

`Source Coverage` 按 raw 目录层级列出 `sources/...`，标注 `ingested`、`partial`、`blocked` 或 `needs-review`。

`Review Queue` 汇总到期或需要复习的页面。

`Needs Attention` 汇总解析失败、图片不清、冲突未解决、缺少来源的页面。

## Log Contract

`log.md` 是 append-only 时间线。不要改写历史记录；修正用新记录追加。

标题格式必须可 grep：

```markdown
## [2026-05-29] ingest | LLM/Transformer/Transformer.xmind
```

操作类型固定为：

```text
ingest | compile | query | output | review | lint | maintenance | schema
```

条目模板：

```markdown
## [2026-05-29] ingest | LLM/Transformer/Transformer.xmind

- Sources:
  - `raw:LLM/Transformer/Transformer.xmind`
- Produced:
  - `sources/LLM/Transformer/Transformer.xmind.md`
- Summary:
  - ...
- Issues:
  - ...
```

常用检查命令：

```bash
grep "^## \\[" log.md | tail -5
grep "ingest |" log.md
grep "review |" log.md
```
