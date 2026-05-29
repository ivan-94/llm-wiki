---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Agent/各种 Agent 类型.xmind"
source_relpath: "Agent/各种 Agent 类型.xmind"
raw_created_at: 2025-01-27T08:20:40.099434+00:00
raw_modified_at: 2025-01-27T08:28:23.107556+00:00
raw_size: 3292567
raw_fingerprint: "size=3292567;birth=2025-01-27T08:20:40.099434+00:00;mtime=2025-01-27T08:28:23.107556+00:00"
raw_snapshot_at: 2026-05-29T22:03:14.890006+00:00
ingested_at: 2026-05-30
status: ingested
---

# 各种 Agent 类型.xmind

## Source

- Raw file: [Agent/各种 Agent 类型.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Agent/%E5%90%84%E7%A7%8D%20Agent%20%E7%B1%BB%E5%9E%8B.xmind>)
- Raw ref: `raw:Agent/各种 Agent 类型.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2025-01-27T08:20:40.099434+00:00`; modified `2025-01-27T08:28:23.107556+00:00`; size `3292567`; snapshot `2026-05-29T22:03:14.890006+00:00`
- Coverage: XMind helper discovered and exported 1 sheet, `思维导图`. The exported sheet was fully read and digested.

## Summary

这份 XMind 把 RAG 相关智能体形态按能力升级路径组织：从原生 RAG、ReRank、多模态 RAG，到 Agentic RAG、混合 RAG 和 Graph RAG。它的重点不在通用 Agent 类型学，而是在检索增强生成系统中如何逐步加入路由、多智能体协作、图结构推理和混合检索。

## Source Digest

该 source 描述的是 RAG 系统从“单一路径检索 + 生成”向“可路由、可协作、可推理”的演进。原生 RAG、ReRank 和多模态 RAG是基础能力层，分别对应基本检索增强、结果重排和跨模态信息引入。Agentic RAG 的关键增量是让系统不再固定走同一条检索链路，而是通过 Router 根据查询意图、复杂度和领域选择检索策略、知识库或生成模型；Multi Agent RAG 则把复杂检索与生成拆成多个专业智能体，通过交互、辩论和验证提升准确性、深度和可解释性。

Graph RAG 被放在更高复杂度位置。source 认为它利用知识图谱把离散知识点转成可推理的语义网络，尤其适合深度推理和可解释性要求高的场景；但同时明确指出工程成本很高，包括图数据库与向量数据库的双系统维护、实时同步、高质量知识图谱冷启动、领域本体设计、实体对齐、关系抽取模型微调，以及图遍历带来的计算资源消耗。混合 RAG 则被描述为结合原生 RAG 与 Graph RAG 的折中路线。

这份材料的长期价值是帮助区分“RAG 增强点”到底发生在哪里：检索排序、模态覆盖、路由控制、智能体协作、图结构建模，还是多策略混合。它也提醒 Graph RAG 不应只被当成更强版本的 RAG，而应被视为一个会显著增加数据建模、同步和计算复杂度的系统工程选择。

## Key Claims

- explicit: Agentic RAG 可以引入 Router，根据输入查询的意图、复杂度和领域动态选择检索策略、知识库或生成模型。
- explicit: MultiAgent RAG 将传统单一路径 RAG 拆解为多个分工协作的智能体，通过交互、辩论和验证提升回答质量。
- explicit: 混合 RAG 可以结合原生 RAG 和 Graph RAG。
- explicit: Graph RAG 利用知识图谱增强模型输出，将离散知识点转化为可推理的语义网络。
- explicit: Graph RAG 的实现复杂度包括同时维护图数据库、向量数据库和实时同步机制。
- explicit: Graph RAG 冷启动需要领域本体设计、实体对齐和关系抽取模型微调。
- inferred: 这份 source 更像 RAG 能力分层，而不是覆盖所有 Agent 类型的通用分类。
- inferred: 选择 Graph RAG 前应先确认任务是否真的需要跨实体关系推理和可解释路径，否则工程成本可能超过收益。

## External Links

No external links found in extracted content.

## Links

- related: [[concepts/上下文工程|上下文工程]] — Router 和检索策略选择都依赖把正确上下文放进正确链路。
- related: [[concepts/Agentic Engineering|Agentic Engineering]] — MultiAgent RAG 提供了一个把 Agent 协作嵌入检索生成系统的具体场景。
- related: [[concepts/LLM 评估|LLM 评估]] — RAG 类型选择需要通过准确性、可解释性、成本和延迟等指标验证。
- entity-candidate: Neo4j — source 将其列为 Graph RAG 可能维护的图数据库之一。
- entity-candidate: TigerGraph — source 将其列为 Graph RAG 可能维护的图数据库之一。
- entity-candidate: Pinecone — source 将其列为 Graph RAG 可能维护的向量数据库之一。
- entity-candidate: Milvus — source 将其列为 Graph RAG 可能维护的向量数据库之一。

## Maintenance Notes

- XMind helper 成功发现并导出全部 sheet。
- source 标题为“各种 Agent 类型”，但实际内容集中在 RAG/Graph RAG/Agentic RAG 类型；后续 compile 时应避免把它误读为完整 Agent 类型 taxonomy。
- External Links 未发现 URL，未联网核验任何工具或产品名。
