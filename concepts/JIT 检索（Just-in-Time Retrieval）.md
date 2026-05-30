---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 1
learning_status: new
confidence: 2
difficulty: 3
review_after: 2026-06-13
---

# JIT 检索（Just-in-Time Retrieval）

## Definition

JIT 检索（即时检索）是一种上下文管理策略：在上下文中只保留轻量标识符（文件路径、数据库查询、网页链接），当任务执行到真正需要具体内容时再通过工具动态加载，而不是把完整资料常驻上下文。

## Why It Matters

把所有可能用到的资料都预先放进上下文，会带来投毒、干扰和成本问题。JIT 检索让上下文保持"稀疏但精确"：只有当前步骤真正需要的内容才进入窗口，其余保留指针。

## Mental Model

JIT 检索像懒加载（lazy loading）：不提前加载所有资源，而是在需要时才从存储层拉取。上下文里的"文件路径"就是资源的引用，而不是资源本身。

## Key Claims

- explicit（来自上下文工程.xmind）：JIT 检索通过在上下文中保留轻量标识符（文件路径、数据库查询、网页链接），在需要时通过工具动态加载内容，降低把完整资料常驻上下文的成本。
- explicit（来自上下文工程.xmind）：Code Agent 不把整个代码库放进 prompt，而是通过文件搜索、grep、AST、知识图谱和重排选择相关上下文——这是 JIT 检索的典型应用。
- explicit（来自上下文工程.xmind）：Agent 把临时草稿写入文件或状态，需要时再检索，而不是长期塞在消息历史里。
- inferred：JIT 检索的核心代价是每次检索需要额外工具调用，但换来了更清洁的上下文和更低的常驻 token 成本。

## Examples

- Code Agent：上下文只存放文件名和函数签名，需要查看具体函数时调用 `read_file` 工具拉取内容。
- Web Agent：把搜索结果的 URL 保留在状态中，需要阅读某篇文章时再调用浏览器工具获取正文。
- RAG 系统：对话历史中保留检索到的文档 ID 和标题，而不是完整内容；下一轮需要引用时再检索具体段落。
- Agentic 工作流：任务分解后，子任务标识符和输出路径放在计划节点，子 Agent 执行时才加载对应上下文。

## Common Confusions

- JIT 检索不等于"不放任何资料进上下文"；关键信息（系统指令、当前任务状态）仍然需要常驻。
- 它和 RAG 有重叠，但 JIT 检索更强调时机（when to load）而不只是来源（where from）。
- JIT 检索需要工具支撑：如果 Agent 没有文件读取、数据库查询等工具，轻量标识符就无法被"兑现"为内容。

## Evidence

- explicit: [[sources/提示语工程:上下文工程/上下文工程.xmind|上下文工程.xmind]] — 定义 JIT 检索并给出 Code Agent、草稿外置等具体例子。

## Relations

- part-of: [[concepts/上下文工程|上下文工程]]
- enables: [[concepts/RAG|RAG]] （RAG 的检索步骤是 JIT 检索的一种形式）
- contrasts-with: [[concepts/上下文失效模式|上下文失效模式]] （JIT 检索是防止干扰和投毒的手段）
- related-source: [[sources/提示语工程:上下文工程/上下文工程.xmind|上下文工程.xmind]]
- map-entry: [[maps/提示语与上下文工程学习地图|提示语与上下文工程学习地图]]

## My Understanding

JIT 检索是"上下文纪律"的实践：只在需要时才加载，让 Agent 保持轻量但功能完整的工作记忆。这和软件里的懒加载思想完全一致。

## Review Questions

- JIT 检索和把资料直接放进上下文的区别是什么？
- 为什么说 Code Agent 是 JIT 检索的典型应用？
- JIT 检索需要什么工具配套？

## Open Questions

- 在网络延迟较高的环境下，JIT 检索的每次工具调用延迟对 Agent 总执行时间的影响需要量化。
- 如何设计轻量标识符的格式和存储，使 Agent 能可靠地"兑现"它，尚无标准方案。
