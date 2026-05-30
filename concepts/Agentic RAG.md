---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 2
learning_status: new
confidence: 2
difficulty: 4
review_after: 2026-06-13
---

# Agentic RAG

## Definition

Agentic RAG 是把 RAG 从固定检索流程提升为可自主决策的检索环路：Agent 会判断是否需要检索、检索结果是否相关、是否要重写查询或切换搜索策略，而不是对每个查询机械执行同样的检索步骤。

## Why It Matters

静态 RAG 对所有问题执行相同的 top-k 检索，无法适应复杂查询、多跳推理、相关文档稀少或初始检索失败等情形。Agentic RAG 把检索决策权交给模型，让 RAG 成为可控的多步推理环路。

## Mental Model

Agentic RAG 像一个有反馈机制的检索员：先决定"要不要查"，查了之后判断"找到的够不够用"，不够用再决定"要重写问题还是换搜索源"，最终才回答。每一步都是模型驱动的判断，而不是固定步骤。

## Key Claims

- explicit（来自 Lang Graph 案例学习.xmind）：RAG 案例把检索必要性、文档相关性、问题重写、Web search 和答案评估作为图中的决策点。
- explicit（来自 Lang Graph 案例学习.xmind）：LangGraph 的 Agentic RAG 覆盖 Adaptive RAG、Corrective RAG 和 Self RAG 等模式。
- inferred：Adaptive RAG 先判断问题是否需要检索；Corrective RAG 在检索后评估结果质量，失败时回退或改写；Self RAG 在生成后自我评估引用证据的使用质量。
- explicit（来自 RAG vs 长文本.xmind）：RAG 和长上下文的结合方案包括推理/反省 RAG，属于 Agentic RAG 思路。

## Examples

- Adaptive RAG：对于简单事实类问题不触发检索，直接用模型知识；对于复杂或不确定问题才触发检索。
- Corrective RAG（CRAG）：检索后用评估节点检查相关性，文档不相关时自动切换到 Web search。
- Self RAG：生成答案后用自我反思标记判断是否应该用检索来支撑，如果不需要则跳过检索步骤。
- LangGraph 实现：`retrieve` → `grade_documents` → （相关则 `generate`，不相关则 `rewrite_query` → `web_search` → `generate`）→ `grade_generation` → 终止或循环。

## Common Confusions

- Agentic RAG 不等于"检索更多文档"；它的核心是在每个决策点引入模型判断，而不是增大检索量。
- Self RAG 的"反思标记"不是提示语技巧，而是把反思决策建模为输出序列的一部分（需要专门训练或 prompt 设计）。
- Agentic RAG 增加了延迟，适合准确率优先场景，不适合追求最低延迟的实时场景。

## Evidence

- explicit: [[sources/Langchain(Legacy)/Lang Graph 案例学习.xmind|Lang Graph 案例学习.xmind]] — 直接记录 Agentic RAG、Adaptive RAG、Corrective RAG、Self RAG 的 LangGraph 实现框架。
- related: [[sources/RAG/RAG vs 长文本.xmind|RAG vs 长文本.xmind]] — 提到推理/反省 RAG 作为 RAG 与长上下文结合方案。

## Relations

- part-of: [[concepts/RAG|RAG]]
- enables: [[concepts/查询分析|查询分析]]
- implemented-by: [[entities/LangGraph|LangGraph]] （legacy · not verified，API 行为以官方文档为准）
- contrasts-with: [[concepts/RAG|RAG]] （静态 RAG 流程）
- map-entry: [[maps/LLM 应用与数据处理学习地图|LLM 应用与数据处理学习地图]]

## My Understanding

Agentic RAG 的本质是把检索变成受控的决策环路，而不是固定管道。它要求在"何时检索、检索什么、检索后如何评估"这三个点上都能做出可适应的判断。

## Review Questions

- Agentic RAG 和静态 RAG 的核心区别是什么？
- Adaptive RAG、Corrective RAG、Self RAG 分别在哪个决策点引入 Agent 判断？
- 为什么 Agentic RAG 增加了延迟？它适合什么场景？

## Open Questions

- LangGraph Agentic RAG 的生产部署和稳定性（legacy · not verified，API 行为以官方文档为准）。
- 如何设计 Agentic RAG 的评估数据集：需要能区分"检索决策是否合理"和"最终答案是否正确"。
