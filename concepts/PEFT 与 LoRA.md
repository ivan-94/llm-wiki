---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 4
learning_status: new
confidence: 2
difficulty: 4
review_after: 2026-06-06
---

# PEFT 与 LoRA

## Definition

PEFT（参数高效微调，Parameter-Efficient Fine-Tuning）是一类只训练少量参数、冻结大部分基础模型权重的微调策略；LoRA（低秩适配）是其代表，通过在权重上叠加低秩适配矩阵来更新一小部分参数，QLoRA 则在 LoRA 基础上结合量化进一步降低显存。

## Why It Matters

全参数微调成本高、显存吃紧。PEFT/LoRA 让“在一两张消费级或单卡 GPU 上微调大模型”成为可能，是微调实战中最常用的工程路径，也是参数轴上和“训练阶段轴”正交的关键维度。

## Mental Model

加补丁而非重做：基础模型权重锁住不动，只在旁边挂一组小的可训练“低秩补丁”；推理时把补丁叠加上去。换任务只需换补丁，省显存、切换成本低。

## Key Claims

- 全参数微调可能更新所有参数，成本高、时间长、需大量存储（explicit，`微调生成模型.xmind`）。
- PEFT 重点是提高微调计算效率，在减少资源消耗的同时保持或提升性能（explicit，`微调生成模型.xmind`）。
- LoRA 只更新模型一小部分参数，通过只训练低秩适配减少计算和内存开销（explicit，`微调生成模型.xmind` / `Llama 微调.xmind`）。
- QLoRA 在 LoRA 上结合块状量化降低显存需求，同时尽量保持权重表示能力（explicit，`微调生成模型.xmind`）。
- LoRA 任务切换成本低，但推理阶段可能带来额外开销，需要权衡（explicit，`Llama 微调.xmind`）。
- Adapters 通过在 Transformer 模块插入小型结构只训练少量参数，可接近全面微调效果（explicit，`微调生成模型.xmind`）。
- LoRA 示例：768×768 权重对比 rank 4 适配器的参数量，直观体现参数节省（explicit，`python 深度学习入门.xmind`）。

## Examples

- `Llama 微调.xmind` 的 alpaca-lora 用 `LlamaForCausalLM` + `LoraConfig` + Trainer 组织 LoRA 训练，全参训练则需 4×A100 80G。
- `python 深度学习入门.xmind` 用 LoRA 对 GPT-2 做参数高效微调（唐诗生成）。
- `微调生成模型.xmind` 把全参微调、Adapters、LoRA、QLoRA 排成“微调成本阶梯”。

## Common Confusions

- 术语警告：`Llama 微调.xmind` 把 PEFT 误展开为 "Profiled End-to-end Flow Tuning"（更像硬件执行流调优）；本 wiki 采用通用含义 Parameter-Efficient Fine-Tuning，编译前已标注存疑。
- PEFT/LoRA 是“怎么省着训”的参数策略，SFT/对齐是“训练阶段”，两者正交、可叠加（如 LoRA 做 SFT）。
- QLoRA 的核心是量化省显存，不等于无损微调。

## Evidence

- [[sources/LLM/微调生成模型.xmind|微调生成模型]]
- [[sources/LLM/Transformer/Llama 微调.xmind|Llama 微调]]
- [[sources/LLM/大模型.xmind|大模型]]
- [[sources/机器学习/python 深度学习入门.xmind|python 深度学习入门]]

## Relations

- part-of: [[concepts/LLM 微调|LLM 微调]] — 参数轴上的核心策略。
- prerequisite: [[concepts/模型量化|模型量化]] — QLoRA 依赖量化降低显存。
- used-in: [[concepts/指令微调（SFT）|指令微调（SFT）]] — LoRA 常用于以更低成本做 SFT。
- implemented-by: [[entities/Hugging Face|Hugging Face]] — PEFT/Transformers/Trainer 生态提供 LoRA 实现。
- related-source: [[sources/LLM/微调生成模型.xmind|微调生成模型]] — 提供 PEFT/LoRA/QLoRA 成本阶梯证据。
- map-entry: [[maps/LLM 基础学习地图|LLM 基础学习地图]]
- entity-candidate: unsloth、LLaMA-Factory、AutoTrain — `Llama 微调.xmind` 中的高效微调工具，暂未单独建页。

## My Understanding

当前理解：PEFT 思路是“冻住大模型、只训小补丁”。LoRA 训低秩矩阵省算力，QLoRA 再加量化省显存；它和训练阶段无关，可叠在 SFT/对齐上用。

## Review Questions

- LoRA 为什么能大幅减少可训练参数？
- QLoRA 相比 LoRA 多做了什么？
- PEFT 与 SFT 是同一层概念吗？

## Open Questions

- `Llama 微调.xmind` 中 PEFT 术语展开存疑，需回 raw 或外部资料澄清。
