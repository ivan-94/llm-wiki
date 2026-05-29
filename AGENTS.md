# AI Wiki Agent Guide

本目录是 AI 主题个人 LLM Wiki 的 canonical workspace。Agent 的任务不是一次性回答问题，而是持续把 raw 资料编译成可学习、可回顾、可关联、可复用的个人知识图谱。

## Rule Priority

- 本文件是执行入口和硬规则清单；写页面时还要读取 [wiki-templates.md](docs/wiki-templates.md) 中对应模板。
- 如果本文件和模板附录冲突，以本文件为准；如果 skill 说明和本文件冲突，以本文件为准。
- raw 是只读事实来源；wiki 是 LLM 维护的编译后知识层。
- 每次 ingest、query、review、lint 都要判断是否值得沉淀回 wiki。
- 页面应帮助用户学习和复习，而不只是保存摘要。

## Fixed Paths

- Raw source root: `/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI`
- Wiki root: 当前项目根目录。
- Canonical guide: 当前项目根目录下的 `AGENTS.md`。
- Template appendix: `docs/wiki-templates.md`。

处理路径时必须保留空格、中文、括号、冒号等原始字符。shell 命令中始终引用完整路径。

## Directory Contract

```text
AI/
  AGENTS.md
  index.md
  log.md
  docs/
    wiki-templates.md
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
- `questions/`: 用户显式要求沉淀的问题与答案；agent 不自动创建。
- `maps/`: MOC / 学习地图，组织学习路径和回顾入口。
- `outputs/`: 可交付的派生输出，如 slides、charts、reports、briefs。
- `assets/`: wiki 生成或复制的附件；不默认复制 raw 原件。
- `docs/`: agent 规则附录和长模板，不存放 raw 派生知识页。

不要再使用旧目录名 `topics/` 或 `syntheses/`。旧内容应迁移到 `concepts/` 和 `synthesis/`。

## Hard Rules

- Raw boundary: 禁止修改、重命名、移动、删除 raw 文件；禁止在 raw 目录或其旁边写中间产物；禁止为了工具成功而修复 raw；禁止直接解包、修改或手写解析 `.xmind`。允许读取 raw、使用 vision 理解图片、按 workflow 在 wiki 目录写派生产物。如果 raw 需要人工修复，必须记录到 source note `Maintenance Notes`、`index.md` Needs Attention 和 `log.md`。
- Source mapping: `sources/` 必须镜像 raw 目录层级和文件名。raw `.md` 直接映射为同名 `.md`；其他 raw 文件映射为 `<原文件名含扩展名>.md`。
- Raw links: source note 必须同时保留 FinderX iCloud raw 链接和 `raw:<source_relpath>`；链接必须指向 raw 文件，不指向 wiki 派生文件。
- External links: raw、导出 Markdown、图片可见文字、PDF 提取文本或 Excalidraw 元素中的 URL 必须进入 source note 的 `## External Links`，并尽量保留标题/锚文本、URL、支撑主题或用途；没有 URL 时写 `No external links found in extracted content.`。不要伪造只有标题没有 URL 的外链，将其放入 `Maintenance Notes` 或 `Open Questions`。不要联网核验外链，除非用户明确要求或当前任务需要当前事实；未核验时标注 `not verified`。
- XMind: 处理 `.xmind` 必须使用 `ai-wiki-xmind-ingest` skill 或 `xmind-cli`。正常路径是读取 sheet 清单，再逐 sheet 导出/读取；不能依赖默认 `xmind export "$RAW_XMIND" --format markdown`。`xmind:#...` 只说明存在 sheet 引用，不代表目标 sheet 已读取。
- Source digest: 导出材料只是临时输入。`Source Digest` 必须是 LLM 消化后的提炼，不得保存完整 raw 导出、机械 outline、前 N 行采样或截断导出。
- Large source detail: 大型或多 sheet source 完成前，必须确认高信号细节已有落点：可复用二级分类、关键步骤、指标维度、命名框架、异常节点、编号/结构问题。落点可以是 `Source Digest`、`Key Claims`、`Maintenance Notes` 或下游页面。
- Claims: source note 的 `Key Claims` 要区分 raw 明确表达和 agent 推断。建议用 `explicit:` 或 `inferred:` 开头；稀疏 source、案例 source 和 agent 补全较多的 source 必须这样标注。
- Links: 任何面向知识图谱的链接列表都必须说明关系；禁止只有裸 wikilink 的列表。source note 的 `Links` 必须列出本次创建或修改过的页面，并说明贡献。
- Questions: agent 不能自动创建 `questions/` 页面。只有用户明确要求沉淀、写入、保存某个问题或问答时，才创建或更新 `questions/`。
- Empty pages: 不创建没有 Evidence/Relations 的空壳页；不要为只出现一次且无复用价值的产品名创建实体页，先用 `entity-candidate`。
- Language and wikilinks: 正文默认中文，保留必要英文术语。文件名优先可读，中文名和官方英文名可混用。内部链接使用 Obsidian wikilink，不要为 slug 化牺牲可读性。

## Source Mapping

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

FinderX raw 链接格式：

```text
finderx://open?icloud=<URL encoded path under iCloud Drive>
```

本项目 raw root 对应的 iCloud 前缀是 `思维导图/AI`。URL encode 每个路径片段，保留 `/` 分隔符。

## Workflow Matrix

| Operation | Read First | Required Writes | Prohibited / Gate |
| --- | --- | --- | --- |
| Ingest | `AGENTS.md`, `docs/wiki-templates.md`, `index.md`, recent `log.md`, raw file | corresponding `sources/...`, `index.md` Source Coverage, `log.md`, then Compile判断 | do not write raw; do not paste full exports; do not skip XMind sheets; do not auto-create `questions/` |
| Compile | relevant `sources/`, existing concepts/entities/synthesis/maps, templates | changed concepts/entities/synthesis/maps, source note `Links`, `index.md`, `log.md` | no empty pages; no product-name-only entity pages; no user-unrequested question pages |
| Query | `index.md`, relevant wiki pages, raw if needed | answer with evidence; optionally update `synthesis/`/map/index/log when high value | create `questions/` only on explicit user request |
| Output | relevant source/concept/synthesis pages and output target | file under `outputs/`, related `synthesis/` or user-created `questions/`, `index.md`, `log.md` | do not leave generated output unregistered |
| Review | `index.md` Review Queue, related map, target page | updated learning fields, `My Understanding`, `review_after`, `log.md` | do not write generic summaries; focus on recall gaps |
| Lint | full wiki index and target checks | `synthesis/wiki-health-YYYY-MM-DD.md`, `index.md` Needs Attention, `log.md` | run only when user asks |

Operating loop:

```text
Collect -> Ingest -> Compile -> Query -> Output -> File Back -> Review -> Lint -> Collect
```

## Ingest Workflow

Ingest 处理的是单个 raw。目标是建立或更新对应 `sources/...`。

1. 读取 `AGENTS.md`、[wiki-templates.md](docs/wiki-templates.md)、`index.md` 和最近的 `log.md`。
2. 确认 raw 文件路径和目标 source note 路径。
3. 按类型读取 raw；`.xmind` 使用 `ai-wiki-xmind-ingest` skill 的 helper 或等价 `xmind sheets -> per-sheet export`。
4. 写 `Summary`、`Source Digest`、`Key Claims`、`External Links`、`Links`、`Maintenance Notes`。
5. 更新 `index.md` Source Coverage 和 `log.md`。
6. 进入 Compile 判断：这个 source 是否改变已有概念、实体、综合、学习地图，或用户显式创建的问题页。

XMind 细则：

- ingest 前必须读取 workbook sheet 清单，例如 `xmind sheets "$RAW_XMIND" --json`。
- 多 sheet workbook 必须逐个 `--sheet-index`、`--sheet-id` 或 `--sheet` 导出/读取。
- source note 的 `Source` 或 `Maintenance Notes` 必须记录 sheet 数量、sheet 标题，以及是否全部处理。
- `Source Digest` 要综合所有可读 sheets。
- 如果某个 sheet 导出失败，source note `status` 标为 `partial`，并记录失败 sheet、失败摘要、可行的人工下一步；继续处理其他 source。
- 诊断命令如 `inspect`、`tree`、`validate` 只在导出失败、内容为空/乱码或用户要求元数据时使用。

Image ingest 细则：

- 用 vision 形成可复查描述，但不承诺完美 OCR。
- 至少记录图像类型、可靠可见文字、结构描述、知识点、局限；不确定的可见文字标注 `uncertain`。
- 同一目录多张图片明显属于一组时，先为每张图片建 source note，再按目录创建综合 concept 或 synthesis 页面。

## Compile Workflow

Compile 是把 source 内容编译进全局知识图谱。

应该更新：

- 明显相关的 `concepts/`、`entities/` 页面。
- 已存在且被新 source 改变的 `synthesis/`、`maps/` 页面。
- 用户显式创建且被新 source 改变的 `questions/` 页面。
- `index.md` 的 Concepts、Entities、Synthesis、Maps、Review Queue。

可以创建：

- 反复出现、对长期理解有价值的 concept/entity 页面。
- 明显跨多个 source 的 synthesis 页面。
- 能组织学习路径的 map 页面。

每次 compile 后，在 source note 的 `Links` 中用关系类型列出创建或修改过的页面，并用短句说明该 source 对页面的贡献。

## Query And File Back

回答问题前：

1. 先读 `index.md`。
2. 搜索并读取相关 `sources/`、`concepts/`、`entities/`、`synthesis/`、`questions/`、`maps/` 页面。
3. 必要时回 raw 查原始证据。
4. 用 wiki 内容回答，并说明关键证据来自哪些页面。

默认不把所有问答写入 wiki。`questions/` 和 `synthesis/` 的写入边界不同：

- 只有用户显式要求沉淀、写入、保存某个问题或问答时，才创建或更新 `questions/` 页面。
- 如果答案综合了多个 source/concept/entity，产生新的比较、判断、路线图、分类法或决策依据，agent 可以创建或更新 `synthesis/`，但不能自动创建 `questions/`。
- “后续大概率会复用”不是创建 `questions/` 的充分条件；只能作为创建 `synthesis/` 或更新 map/index 的理由。

写回后必须更新 `index.md`、`log.md`，并在相关 concept/entity 的 `Relations` 或 `Evidence` 中互链。

## Output Policy

`outputs/` 存放可交付、可复用的派生文件，例如：

```text
outputs/slides/llm-wiki-intro.marp.md
outputs/charts/source-growth.png
outputs/reports/agent-workflow-comparison.md
outputs/briefs/rag-vs-long-context.md
```

生成 output 后必须：

- 在相关 `synthesis/` 页面链接它；如果存在用户显式创建的相关 `questions/` 页面，也可以同步链接。
- 在 `index.md` 的 `Outputs` 中登记。
- 在 `log.md` 追加 `output` 记录。

## Conflict Handling

当新 source 与旧页面冲突时，不要自动抹平。

1. 不删除旧说法，除非它只是明显错误的转录或解析问题。
2. 在相关页面的 `Key Claims` 或 `Evidence` 中标注来源差异。
3. 在 `Open Questions` 中记录待澄清问题。
4. 重要冲突创建或更新 `synthesis/` 下的对比页。
5. 在 `log.md` 记录本次 ingest/compile 发现的冲突。

## Review Workflow

Review 面向学习和回顾，不是资料清理。

触发条件：

- 用户要求复习、回顾、测验、检查掌握度。
- `review_after` 到期。
- 页面 `learning_status` 为 `new`、`learning` 或 `review-needed`。

流程：

1. 读取 `index.md` 的 Review Queue 和相关 `maps/`。
2. 读取目标 concept/synthesis/question 页面。
3. 生成 3-5 个主动回忆问题，优先考 Definition、Mental Model、Common Confusions 和关系。
4. 根据用户回答更新 `confidence`、`learning_status`、`review_after` 和 `My Understanding`。
5. 在 `log.md` 追加 `review` 记录。

不要把 review 写成泛泛总结。它必须帮助用户发现“哪里没掌握”。

## Lint Workflow

lint 不自动定时执行，只在用户要求时执行。输出写入：

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

## Relation Types

页面 `Relations` 推荐类型：

- `prerequisite`: 先修概念。
- `part-of`: 属于更大主题。
- `contains`: 包含子概念。
- `contrasts-with`: 易混或对比对象。
- `enables`: 支撑或使能另一个概念。
- `implemented-by`: 被某工具、框架、产品实现。
- `used-in`: 被某场景或 synthesis 使用。
- `related-source`: 相关 source note。
- `related-question`: 相关问题页；仅用于用户显式提出或要求创建的 `questions/` 页面。
- `map-entry`: 所属学习地图。
- `entity-candidate`: 候选实体，尚未值得建页。

source note 的 `Links` 推荐类型：

- `compiled-concept`: 本 source 编译出的概念页。
- `compiled-entity`: 本 source 编译出的实体页。
- `compiled-synthesis`: 本 source 参与形成的综合页。
- `user-question`: 本 source 关联到用户显式提出或要求创建的问题页。
- `map-entry`: 本 source 所属或更新的学习地图。
- `updates`: 本 source 更新了已有页面。
- `related`: 只有弱关系但仍值得保留；必须用一句话说明原因。

## Asset Policy

默认不复制 raw 图片或附件。source note 记录 `raw_path` 和 `source_relpath` 即可。

只有需要 Obsidian 内稳定预览、标注裁剪图、或生成派生图时，才复制到：

```text
assets/sources/<raw 相对目录>/<原文件名>
```

复制或生成 asset 后，必须在对应 source note 中说明 asset 路径和用途。

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

`Source Coverage` 按 raw 目录层级列出 `sources/...`，标注 `ingested`、`partial`、`blocked` 或 `needs-review`。`Review Queue` 汇总到期或需要复习的页面。`Needs Attention` 汇总解析失败、图片不清、冲突未解决、缺少来源的页面。

## Log Contract

`log.md` 是 append-only 单行时间线。从 2026-05-29 起，每次操作只追加一行；不要再写 `Sources`、`Produced`、`Summary`、`Issues` 多行块。历史压缩只能在用户明确要求时进行；普通修正用新记录追加。

单行格式必须可 grep：

```markdown
## [2026-05-29] ingest | LLM/Transformer/Transformer.xmind — ingested source note; issues: none
```

操作类型固定为：

```text
ingest | compile | query | output | review | lint | maintenance | schema
```

- summary 和 issues 都压缩在同一行；详细来源、产物和问题写入 source note、index、synthesis 或对应页面。
- 如果一次操作涉及很多文件，用主题或目录概括，不在 `log.md` 展开清单。
- 如果没有问题，写 `issues: none`。

常用检查命令：

```bash
grep "^## \\[" log.md | tail -5
grep "ingest |" log.md
grep "review |" log.md
```
