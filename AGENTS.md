# AI Wiki Agent Guide

本目录是 AI 主题个人 LLM Wiki 的 canonical workspace。Agent 的任务不是一次性回答问题，而是持续把 raw 资料编译成可学习、可回顾、可关联、可复用的个人知识图谱。

## Rule Priority

- 本文件是执行入口、全局硬规则和 ingest 路由清单；写页面时还要读取 [wiki-templates.md](docs/wiki-templates.md) 中对应模板。
- 类型专属 ingest 规则内聚到对应 skill；如果 skill 与本文件的全局硬规则冲突，以本文件为准。
- 外部 raw 和 `human/raw/` 是只读事实来源；wiki 是 LLM 维护的编译后知识层。
- 每次 ingest、query、review、lint 都要判断是否值得沉淀回 wiki。
- 页面应帮助用户学习和复习，而不只是保存摘要。

## Fixed Paths

- Raw source root: `/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI`
- Human source root: 当前项目根目录下的 `human/raw/`。
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
  human/
    inbox/
    raw/
    sources/
    archived/
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
- raw 目录本身是用户已有的主题组织；同一 raw 目录下的 source 默认属于一个 source cluster，必须在 ingest/compile 时判断互证、前后置、重复、对比或案例关系。
- `human/`: 人类在 Obsidian 中写作和积累的区域，不属于外部 raw 镜像。
- `human/inbox/`: 临时笔记和未整理想法；agent 默认不 ingest、不 compile、不纳入 coverage。
- `human/raw/`: 人类长期笔记和原创材料；agent 默认只读，只有用户明确要求或笔记声明 `ingest_policy: allowed` 时才作为 human source ingest。
- `human/sources/`: `human/raw/` 被 ingest 和 compile 后的 source note / 索引层，目录层级镜像 `human/raw/`。
- `human/archived/`: 从 `human/inbox/` 废弃或暂不处理的笔记归档；不属于 source coverage，也不自动 ingest。
- `concepts/`: 概念页，跨多个 source 的稳定学习节点。
- `entities/`: 人物、公司、项目、产品、工具、框架、模型、组织。
- `synthesis/`: 跨来源分析、对比、路线图、判断、wiki 健康报告。
- `questions/`: 用户显式要求沉淀的问题与答案；agent 不自动创建。
- `maps/`: MOC / 学习地图，组织学习路径和回顾入口。
- `outputs/`: 可交付的派生输出，如 slides、charts、reports、briefs。
- `assets/`: wiki 生成或复制的附件；不默认复制 raw 原件。
- `docs/`: agent 规则附录和长模板，不存放 raw 派生知识页。

不要再使用旧目录名 `topics/` 或 `syntheses/`。旧内容应迁移到 `concepts/` 和 `synthesis/`。

## Human Inbox Workflow

`human/inbox/` 是待消化内容池，不是 canonical source 层；不纳入 coverage，也不自动 ingest / compile。Agent 生成的 inbox note 默认写入：

```yaml
inbox_status: unread
inbox_created_at: YYYY-MM-DD
inbox_read_at:
raw_path:
ingested_at:
archive_reason:
```

状态只允许 `unread`、`read`、`raw`、`ingested`、`archived`。默认流转是 `unread -> read -> raw -> ingested`，也允许 `unread/read -> archived`。

- `read` / `unread`: 只改 frontmatter。
- `raw`: 剪切到 `human/raw/inbox/...`，成为可按 human raw 规则处理的来源。
- `archived`: 剪切到 `human/archived/inbox/...`，不进入 raw / ingest。
- `ingested`: 已从 `human/raw/` ingest 到 `human/sources/`，并完成必要 compile 判断。



## Hard Rules

- Raw boundary: 禁止修改、重命名、移动、删除 raw 文件；禁止在 raw 目录或其旁边写中间产物；禁止为了工具成功而修复 raw；禁止直接解包、修改或手写解析 `.xmind`。允许读取 raw、使用 vision 理解图片、按 workflow 在 wiki 目录写派生产物。如果 raw 需要人工修复，必须记录到 source note `Maintenance Notes`、`index.md` Needs Attention 和 `log.md`。
- Human boundary: 禁止自动改写、移动、删除 `human/inbox/` 和 `human/raw/` 下的人类原文；`human/raw/` 是内部来源域，不是 agent 草稿区。agent 的消化、摘要、claims、links 写入 `human/sources/`，再按 compile gate 写入 `concepts/`、`entities/`、`synthesis/`、`maps/` 或用户显式创建的 `questions/`。
- File scope: 当前支持 `.xmind`、图片、Markdown、PDF、Excalidraw raw。其他文件类型默认不 ingest、不转换、不创建 source note；发现时只在 `index.md` Needs Attention 或 `log.md` 记录为 unsupported，除非用户明确扩展支持范围。
- Human file scope: `human/raw/` 当前默认只 ingest Markdown 笔记；附件或非 Markdown 文件只在用户明确要求且有对应规则时处理。`human/inbox/` 永远不自动进入 source coverage。
- Source mapping: 对当前支持的外部 raw，`sources/` 必须镜像 raw 目录层级和文件名。raw `.md` 直接映射为同名 `.md`；其他支持类型映射为 `<原文件名含扩展名>.md`。对当前支持的 human raw，`human/sources/` 必须镜像 `human/raw/` 目录层级和 Markdown 文件名。不支持类型不创建 `sources/...` 或 `human/sources/...`。
- Source clusters: 新建或刷新 source note 前，必须查看来源文件所在目录和同目录已有 source note。外部 raw 查看 `sources/...`；human raw 查看 `human/sources/...`。source note 应记录目录主题、cluster role，以及与同目录或相邻目录 source 的 typed relation；如果没有可确认邻居，也要说明判断结果。
- Raw links: 外部 source note 必须同时保留 FinderX iCloud raw 链接和 `raw:<source_relpath>`；human source note 必须保留指向 `human/raw/...` 的 wikilink 和 `human-raw:<human-raw-relpath>`；链接必须指向来源文件，不指向 wiki 派生文件。
- Raw metadata: 新建或刷新 source note 时必须在 frontmatter 记录 `raw_created_at`、`raw_modified_at`、`raw_size`、`raw_fingerprint`、`raw_snapshot_at`。更新判断使用来源文件内容修改时间 `mtime`；不要使用 `ctime`，因为 iCloud 或本地元数据变化会污染它。旧 source note 缺少这些字段时，先标记为 `needs_metadata` 或重新 ingest/backfill 后再依赖更新/移动判断。
- External links: 支持类型中可可靠提取或看见的 URL 必须进入 source note 的 `## External Links`，并尽量保留标题/锚文本、URL、支撑主题或用途；没有 URL 时写 `No external links found in extracted content.`。不要伪造只有标题没有 URL 的外链，将其放入 `Maintenance Notes` 或 `Open Questions`。不要联网核验外链，除非用户明确要求或当前任务需要当前事实；未核验时标注 `not verified`。
- Skill routing: 处理 `.xmind` 必须使用 `ai-wiki-xmind-ingest`；处理图片必须使用 `ai-wiki-image-ingest`；处理 raw Markdown 必须使用 `ai-wiki-markdown-ingest`；处理 `.pdf` 必须使用 `ai-wiki-pdf-ingest`；处理 `.excalidraw` 必须使用 `ai-wiki-excalidraw-ingest`。底层命令和类型专属覆盖策略由对应 skill 定义，不在 `AGENTS.md` 分散维护。
- Source digest: 导出材料只是临时输入。`Source Digest` 必须是 LLM 消化后的提炼，不得保存完整 raw 导出、机械 outline、前 N 行采样或截断导出。
- Large source detail: 大型或多 sheet source 完成前，必须把真正可复用的细节消化进 `Source Digest`、`Key Claims`、`Links` 或下游页面，例如关键步骤、指标维度、命名框架、异常节点和结构问题。不要在 `Maintenance Notes` 保存导出标题采样、机械 outline 或前 N 行作为覆盖证明。
- Claims: source note 的 `Key Claims` 要区分 raw 明确表达和 agent 推断。建议用 `explicit:` 或 `inferred:` 开头；稀疏 source、案例 source 和 agent 补全较多的 source 必须这样标注。
- Links: 任何面向知识图谱的链接列表都必须说明关系；禁止只有裸 wikilink 的列表。source note 的 `Links` 必须同时覆盖本次创建或修改过的页面、相关 source-source 关系，并说明贡献或关系判断。
- Questions: agent 不能自动创建 `questions/` 页面。只有用户明确要求沉淀、写入、保存某个问题或问答时，才创建或更新 `questions/`。
- Entity density: 实体不只限于大公司或知名产品。人物、组织、项目、工具、框架、模型、协议、平台、方法论来源只要反复出现、连接多个 source/concept/synthesis，或在工作流中承担稳定角色，就应考虑创建或更新 `entities/`。
- Empty pages: 不创建没有 Evidence/Relations 的空壳页；不要为只出现一次且无复用价值的产品名创建实体页，先用 `entity-candidate`。
- Language and wikilinks: 正文默认中文，保留必要英文术语。文件名优先可读，中文名和官方英文名可混用。内部链接使用 Obsidian wikilink，不要为 slug 化牺牲可读性。

## Source Mapping

示例：

```text
raw:  LLM/Transformer/Transformer.xmind
wiki: sources/LLM/Transformer/Transformer.xmind.md

raw:  生图/商品画图/高级1.png
wiki: sources/生图/商品画图/高级1.png.md

raw:  生图/人物画图/初级.PNG
wiki: sources/生图/人物画图/初级.PNG.md

raw:  Agent/build-cli-for-agent-checklist.md
wiki: sources/Agent/build-cli-for-agent-checklist.md

raw:  LLM/长文材料/Survey.pdf
wiki: sources/LLM/长文材料/Survey.pdf.md

raw:  Agent/闪极智能体/闪极智能体 2.excalidraw
wiki: sources/Agent/闪极智能体/闪极智能体 2.excalidraw.md

human raw:  human/raw/Obsidian/我的 Obsidian 学习笔记.md
human wiki: human/sources/Obsidian/我的 Obsidian 学习笔记.md
```

当前支持类型：

- `.xmind`
- 图片：`.png`、`.jpg`、`.jpeg`、`.webp`、`.gif`、`.heic`、`.PNG` 等常见图片扩展名
- `.md`
- `.pdf`
- `.excalidraw`

不处理类型：

- Office 文档、音视频、压缩包和其他非支持类型。
- 不处理意味着不 ingest、不转换、不创建 `sources/...`；只在需要时记录 unsupported 状态和后续人工/规则扩展需求。

FinderX raw 链接格式：

```text
finderx://open?icloud=<URL encoded path under iCloud Drive>
```

本项目 raw root 对应的 iCloud 前缀是 `思维导图/AI`。URL encode 每个路径片段，保留 `/` 分隔符。

Human raw 链接格式：

```text
[[human/raw/<path-without-md-extension>|<title>]]
human-raw:<path-under-human-raw>
```

`human/raw/` 是 vault 内部路径，不使用 FinderX 链接。human source note 也必须记录来源文件 metadata，便于判断是否需要刷新。

## Workflow Matrix

| Operation | Read First | Required Writes | Prohibited / Gate |
| --- | --- | --- | --- |
| Ingest | `AGENTS.md`, `docs/wiki-templates.md`, `index.md`, raw file or human raw note, required type skill/template | corresponding `sources/...` or `human/sources/...`, `index.md` Source Coverage, `log.md`, then Compile判断 | do not write raw or human original; do not paste full exports; do not bypass required type skill/template; do not auto-create `questions/` |
| Compile | relevant `sources/` and `human/sources/`, existing concepts/entities/synthesis/maps, templates | changed concepts/entities/synthesis/maps, source note `Links`, `index.md`, `log.md` | no empty pages; no product-name-only entity pages; no user-unrequested question pages |
| Query | `index.md`, relevant wiki pages, source notes, human sources if needed | answer with evidence; optionally update `synthesis/`/map/index/log when high value | create `questions/` only on explicit user request; do not modify human originals |
| Output | relevant source/concept/synthesis pages and output target | file under `outputs/`, related `synthesis/` or user-created `questions/`, `index.md`, `log.md` | do not leave generated output unregistered |
| Review | `index.md` Review Queue, related map, target page | updated learning fields, `My Understanding`, `review_after`, `log.md` | do not write generic summaries; focus on recall gaps |
| Lint | full wiki index and target checks | `synthesis/wiki-health-YYYY-MM-DD.md`, `index.md` Needs Attention, `log.md` | run only when user asks |

Operating loop:

```text
Collect -> Ingest -> Compile -> Query -> Output -> File Back -> Review -> Lint -> Collect
```

## Ingest Workflow

Ingest 处理的是单个外部 raw 或 human raw。目标是建立或更新对应 `sources/...` 或 `human/sources/...`。

1. 读取 `AGENTS.md`、[wiki-templates.md](docs/wiki-templates.md) 和 `index.md`。
2. 确认来源域：外部 raw root 或 `human/raw/`。外部 raw 写入 `sources/...`；human raw 写入 `human/sources/...`。
3. 确认来源文件路径和目标 source note 路径。`human/inbox/` 不作为 ingest 输入。
4. 识别 source cluster：外部 raw 查看同目录 raw 和同目录已有 `sources/...`；human raw 查看同目录 human note 和同目录已有 `human/sources/...`。判断本 source 是目录入口、细节展开、案例、工具、对比、补充还是索引。
5. 按类型路由读取来源；外部 `.xmind`、图片、raw Markdown、`.pdf`、`.excalidraw` 分别使用对应 `ai-wiki-*-ingest` skill。human raw 当前默认只处理 Markdown，并使用 docs 中的 Human Source Note Template；以后如果新增 dedicated skill，以该 skill 为准。
6. 写 frontmatter raw metadata、`Source Cluster`、`Summary`、`Source Digest`、`Key Claims`、`External Links`、`Links`、`Maintenance Notes`。
7. 更新 `index.md` Source Coverage 和 `log.md`。
8. 进入 Compile Gate：这个 source 是否改变已有概念、实体、综合、学习地图，或用户显式创建的问题页；是否需要与 source cluster 内其他 source 建立 typed links。

## Compile Workflow

Compile 是把 source 内容编译进全局知识图谱。

Compile Gate 必须逐项判断：

1. Cluster: raw 目录提供了什么主题结构？本 source 在 cluster 中是入口、前置、展开、案例、对比、工具还是补充？
2. Concepts: 是否产生新概念、补强已有概念、暴露易混点或改变心智模型？
3. Entities: 是否出现可复用实体，或让已有实体获得新证据、新角色、新关系？
4. Synthesis: 是否改变跨来源判断、对比、路线图、风险或决策依据？
5. Maps: 是否应进入学习路径；如果同一目录或主题下已有 3 个以上 source 指向同一学习目标，必须考虑创建或更新 map/synthesis。
6. Source links: 是否应与同目录、父子目录或同工具链 source 建立 `same-cluster`、`prerequisite-source`、`extends-source`、`contrasts-source`、`duplicate-or-overlap`、`case-of` 或 `toolchain-neighbor` 关系？

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

如果判断不创建 concept/entity/synthesis/map，也要在 `Maintenance Notes` 或 `Links` 中留下原因，避免下游 agent 重新做同一轮浅判断。

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

- source coverage: 外部 raw 是否都有对应 source note；声明为可 ingest 的 `human/raw` Markdown 是否有对应 `human/sources` source note。`human/inbox` 不参与 coverage。
- broken links: Obsidian links 是否指向存在页面。
- orphan pages: 页面是否没有被 index/source/concept/entity/map 引用。
- stale claims: 旧页面是否被新 source 反驳或需要更新。
- contradictions: 冲突 claims 是否没有标注。
- missing pages: 高频概念/实体是否缺少独立页。
- weak evidence: claim 是否缺少 source 链接。
- weak relations: `Relations` 是否只有无类型链接。
- weak source clusters: source note 是否忽略同目录 source、缺少 cluster role 或缺少必要 source-source typed links。
- weak entities: 多个 source 反复出现的工具、框架、项目、人物或协议是否仍停留在零散文本里，没有实体页或 `entity-candidate` 记录。
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
- `same-cluster`: 与另一个 source 属于同一 raw 目录主题簇。
- `prerequisite-source`: 阅读或理解当前 source 的前置 source。
- `extends-source`: 对另一个 source 的细节展开、步骤补充或深挖。
- `contrasts-source`: 与另一个 source 构成方法、工具、观点或案例对比。
- `duplicate-or-overlap`: 与另一个 source 内容明显重叠，可互相校验或去重。
- `case-of`: 当前 source 是某概念、方法、工具或问题的案例。
- `toolchain-neighbor`: 与另一个 source 属于同一工具链、工作流阶段或执行闭环。
- `related`: 只有弱关系但仍值得保留；必须用一句话说明原因。

## Asset Policy

默认不复制 raw 图片或附件。source note 记录 `raw_path`、`source_relpath` 和 raw metadata 即可。

只有需要 Obsidian 内稳定预览、标注裁剪图、或生成派生图时，才复制到：

```text
assets/sources/<raw 相对目录>/<原文件名>
```

复制或生成 asset 后，必须在对应 source note 中说明 asset 路径和用途。

## Search And Tool Use

优先使用快速、本地、可复现的工具：

- `rg` 搜索 wiki 内容。
- `find` 列 raw/wiki 文件。
- `ai-wiki-raw-diff` 检查 raw 与 `sources/` 的新增、删除、更新、移动、缺失元数据、iCloud 占位和 unsupported 文件。
- `ai-wiki-xmind-ingest` 处理 `.xmind`。
- `ai-wiki-image-ingest` 处理图片。
- `ai-wiki-markdown-ingest` 处理 raw Markdown。
- `ai-wiki-pdf-ingest` 处理 `.pdf`。
- `ai-wiki-excalidraw-ingest` 处理 `.excalidraw`。
- human raw Markdown 当前按 Human Source Note Template ingest 到 `human/sources/`；如果后续存在 `ai-wiki-human-ingest`，以该 skill 为准。
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

`Source Coverage` 按来源域组织：外部 raw 按 raw 目录层级列出 `sources/...`；human sources 按 `human/raw` 目录层级列出 `human/sources/...`。状态标注 `ingested`、`partial`、`blocked` 或 `needs-review`。`Review Queue` 汇总到期或需要复习的页面。`Needs Attention` 汇总解析失败、图片不清、冲突未解决、缺少来源的页面。

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
