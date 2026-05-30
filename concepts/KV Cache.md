---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 2
learning_status: new
confidence: 2
difficulty: 3
review_after: 2026-06-06
---

# KV Cache

## Definition

KV Cache 是自回归推理中的缓存优化：把已处理 token 的 key/value 投影结果存起来，生成后续 token 时直接复用，避免对整段前缀重复计算注意力。

## Why It Matters

自回归每生成一个 token 都要对全部前文做注意力。没有 KV Cache，第 n 步要重算前 n-1 个 token 的 key/value，开销随序列长度平方增长；有了缓存，每步只需为新 token 计算一次。这是 LLM 推理速度与显存占用的关键工程点。

## Mental Model

记笔记：前面 token 的 key/value 算过一次就记在本子上；生成新 token 时只算它自己的 q/k/v，再去本子里查历史的 k/v，不必把整段重新读一遍。

## Key Claims

- KV Cache 的动机是在生成后续 token 时复用此前序列的 key/value 计算结果（explicit，`语言模型内部原理.xmind`）。
- 缓存的对象正是注意力层的 key 和 value 投影（explicit，`语言模型内部原理.xmind`）。
- 上下文大小对应一次可并行处理的 token 数量，KV Cache 是把“串行生成”代价摊薄的手段（inferred，结合 `语言模型内部原理.xmind` 对 token stream 与并行化的描述）。
- KV Cache 增长占显存，长上下文推理的显存压力部分来自缓存（inferred）。

## Examples

- `语言模型内部原理.xmind` 在解释 Transformer 推理时显式引入 KV cache 作为复用机制。

## Common Confusions

- KV Cache 缓存的是 key/value，不是 query；query 每步都为当前 token 新算。
- KV Cache 是“同一次生成会话内”的复用，与跨请求的“提示词缓存（prompt caching）”是不同层面的缓存。

## Evidence

- [[sources/LLM/语言模型内部原理.xmind|语言模型内部原理]]

## Relations

- prerequisite: [[concepts/注意力机制|注意力机制]] — KV Cache 缓存的是注意力的 key/value。
- enables: [[concepts/自回归语言模型|自回归语言模型]] — 让自回归串行生成在工程上可负担。
- contrasts-with: [[concepts/提示词缓存|提示词缓存]] — 二者都叫“缓存”，但一个在单次生成内复用、一个在请求间复用前缀。
- related-source: [[sources/LLM/语言模型内部原理.xmind|语言模型内部原理]] — 唯一直接证据来源。
- map-entry: [[maps/LLM 基础学习地图|LLM 基础学习地图]]

## My Understanding

当前理解：KV Cache 把自回归里“重复计算前文注意力”这件浪费的事消掉，用显存换速度，是推理性能的基本盘。

## Review Questions

- 没有 KV Cache 时，自回归推理的计算为什么会随长度快速变大？
- KV Cache 缓存的是 q/k/v 中的哪几个？
- KV Cache 和提示词缓存的区别是什么？

## Open Questions

- 分页 KV Cache（如 PagedAttention）、缓存量化等实现细节超出当前 source。
