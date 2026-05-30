---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/LLM/Transformer/Llama 微调.xmind"
source_relpath: "LLM/Transformer/Llama 微调.xmind"
raw_created_at: 2024-05-06T11:28:08.213642+00:00
raw_modified_at: 2024-05-07T11:38:00.532189+00:00
raw_size: 2472172
raw_fingerprint: "size=2472172;birth=2024-05-06T11:28:08.213642+00:00;mtime=2024-05-07T11:38:00.532189+00:00"
raw_snapshot_at: 2026-05-29T22:09:34.976358+00:00
ingested_at: 2026-05-30
status: ingested
---

# Llama 微调.xmind

## Source

- Raw file: [LLM/Transformer/Llama 微调.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/LLM/Transformer/Llama%20%E5%BE%AE%E8%B0%83.xmind>)
- Raw ref: `raw:LLM/Transformer/Llama 微调.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2024-05-06T11:28:08.213642+00:00`; modified `2024-05-07T11:38:00.532189+00:00`; size `2472172`; snapshot `2026-05-29T22:09:34.976358+00:00`
- Coverage: Exported and read 1 sheet: `画布 1`.

## Summary

这张图系统整理了 Llama/LLM 微调的基本概念、工具入口、数据准备、自指令数据生成、高效微调、Alpaca 实战、LoRA 训练代码结构和模型导出格式。

## Source Digest

source 的第一层是微调基础概念：预训练模型已经在大规模数据上学习语言特征，微调是在任务特定数据上继续训练；学习率、批大小、epoch、loss、正则化、早停、超参数调优、精度和量化共同决定训练成本、收敛和泛化。图中还把提示语工程与模型工程对比为两种“知识注入”：提示语工程通过上下文学习注入新知识，模型工程通过参数学习更新权重。

第二层是 Llama 微调工具与运行入口：包含 Hugging Face 的 Llama 3 博客、Transformers 安装文档、Mac 上通过 Ollama 运行、unsloth、LLaMA-Factory、Hugging Face AutoTrain 等。数据准备部分区分 alpaca 与 sharegpt 格式，并给出 alpaca JSON 字段结构，包括 instruction、input、output、system、history。

第三层重点讲 Self-Instruct：它从少量人工 seed tasks 出发，随机抽取人工任务和模型生成任务作为 few-shot prompt，让现有 LM 继续生成新 instruction；再判断任务是否分类，不同任务类型采用 input-first 或 output-first 生成实例；最后过滤、处理、重格式化并回填任务池，直到形成足够规模的数据。source 特别保留了 seed task、分类判断 prompt、非分类/分类样例生成 prompt、ROUGE-L 多样性过滤和排除图像类任务等细节。

第四层讲高效微调和 Alpaca 实战：LoRA 通过只训练低秩适配矩阵减少可训练参数和显存/计算成本，任务切换成本低，但推理可能增加开销。Alpaca 实战部分记录了对 Self-Instruct 的升级：用 text-davinci-003、批量生成 20 条指令、取消分类/非分类生成差异、每个指令只生成一个实例；并记录全量训练依赖 4 个 A100 80G GPU，以及 alpaca-lora 代码中用 `LlamaForCausalLM`、`LoraConfig`、checkpoint 恢复、`transformers.Trainer` 和 data collator 组织训练。最后列出 GGUF、vLLM、GGML 等导出格式。

## Key Claims

- explicit: 微调是在特定任务数据集上继续训练预训练模型，使模型权重适应该任务的特征和需求。
- explicit: 微调通常使用比预训练阶段更小的学习率，以避免破坏已有有效模式。
- explicit: 任务特定数据应代表任务实际需求和场景，帮助模型学习适用于该任务的特定知识。
- explicit: 提示语工程通过上下文学习注入知识，模型工程通过参数学习更新模型参数。
- explicit: alpaca 数据格式包含 instruction、input、output、system、history 等字段，instruction 和 output 为必填。
- explicit: Self-Instruct 从有限人工 seed tasks 出发，通过现有 LM 迭代生成新指令和实例，并经过分类判断、实例生成、过滤、处理和重格式化。
- explicit: Self-Instruct 中非分类任务采用 input-first 生成输入和输出，分类任务采用 output-first 生成 class label 对应输入。
- explicit: 新生成指令需要与种子池指令的 ROUGE-L 小于 0.7 才加入任务池，并排除涉及图像/图片/图形等无法被语言模型处理的指令。
- explicit: LoRA 的目标是降低大型语言模型微调成本，通过只训练低秩适配部分减少计算和内存开销。
- explicit: LoRA 任务切换成本低，但推理阶段可能带来额外开销，需要权衡。
- explicit: Alpaca 使用 Self-Instruct 方式生成数据来对 LLaMA-7B 做指令微调。
- explicit: Alpaca 全量参数训练示例需要 4 个 A100 80G GPU；lora 训练示例使用 Hugging Face Transformers、PEFT LoRA 配置、checkpoint 恢复和 Trainer。
- explicit: source 列出 GGUF、vLLM、GGML 作为模型导出格式。
- inferred: 该 source 可以支撑一个“Llama 微调流程”综合节点，连接数据构造、PEFT、训练实现和导出部署。

## External Links

- model-running: [运行 Hugging face 的模型](https://huggingface.co/blog/zh/llama3) — source 中作为运行 Hugging Face 模型入口；not verified.
- local-running: [在 Mac 上通过 OLlama 运行](https://www.liaoxuefeng.com/article/1610536319975459) — source 中作为本地运行参考；not verified.
- installation: [Hugging Face Transformers installation](https://huggingface.co/docs/transformers/main/zh/installation) — source 中作为安装 codelab；not verified.
- tool: [unsloth](https://github.com/unslothai/unsloth) — source 中列为微调工具；not verified.
- data-format: [LLaMA-Factory data README](https://github.com/hiyouga/LLaMA-Factory/blob/main/data/README_zh.md) — source 中作为 alpaca 格式示例；not verified.
- paper: [Self-Instruct](https://arxiv.org/abs/2212.10560) — source 中用于说明自指令数据生成；not verified.
- dataset: [Self-Instruct seed tasks](https://github.com/yizhongw/self-instruct/blob/main/data/seed_tasks.jsonl) — source 中作为种子任务示例；not verified.
- implementation: [Self-Instruct implementation](https://github.com/yizhongw/self-instruct.git) — source 中列出生成、分类、实例生成和微调准备脚本；not verified.
- explanation: [Self-Instruct 解析](https://blog.csdn.net/dzysunshine/article/details/130390587#:~:text=%E4%B8%BA%E4%BA%86%E6%95%B0%E6%8D%AE%E7%9A%84%E5%A4%9A%E6%A0%B7%E6%80%A7%EF%BC%8C%E6%96%B0%E7%94%9F%E6%88%90%E7%9A%84%E6%8C%87%E4%BB%A4%E5%8F%AA%E6%9C%89%E4%B8%8E%E7%A7%8D%E5%AD%90%E6%B1%A0%E4%B8%AD%E7%9A%84%E6%8C%87%E4%BB%A4%E7%9A%84%20ROUGE%2DL%20%E5%B0%8F%E4%BA%8E0.7%E6%97%B6%E6%89%8D%E4%BC%9A%E6%B7%BB%E5%8A%A0%E8%BF%9B%E5%85%A5%E7%A7%8D%E5%AD%90%E6%B1%A0%EF%BC%9B%0A%E6%8E%92%E9%99%A4%E4%B8%80%E4%BA%9B%E6%97%A0%E6%B3%95%E8%A2%AB%E8%AF%AD%E8%A8%80%E6%A8%A1%E5%9E%8B%E5%A4%84%E7%90%86%E7%9A%84%E6%8C%87%E4%BB%A4%EF%BC%8C%E6%AF%94%E5%A6%82%E6%B6%89%E5%8F%8A%E5%9B%BE%E5%83%8F%E3%80%81%E5%9B%BE%E7%89%87%E3%80%81%E5%9B%BE%E5%BD%A2%E7%9A%84%E6%8C%87%E4%BB%A4%EF%BC%9B) — source 中作为 Self-Instruct 过滤规则解析；not verified.
- course: [极客时间](https://time.geekbang.org/column/article/713908?utm_campaign=geektime_search&utm_content=geektime_search&utm_medium=geektime_search&utm_source=geektime_search&utm_term=geektime_search) — source 中列为相关资料；not verified.
- alpaca-prompt: [Stanford Alpaca prompt](https://github.com/tatsu-lab/stanford_alpaca/blob/main/prompt.txt) — source 中作为 Alpaca 指令生成 prompt；not verified.
- alpaca-data: [Stanford Alpaca data](https://github.com/tatsu-lab/stanford_alpaca/blob/main/alpaca_data.json) — source 中作为数据集结果示例；not verified.
- full-finetune: [Stanford Alpaca README](https://github.com/tatsu-lab/stanford_alpaca/blob/main/README.md) — source 中作为全量参数训练参考；not verified.
- lora-training: [alpaca-lora](https://github.com/tloen/alpaca-lora) — source 中作为 LoRA 训练实现参考；not verified.

## Links

- compiled-concept: [[concepts/LLM 微调|LLM 微调]] — source 提供 Llama/Alpaca 指令微调、训练实现和导出部署证据。
- compiled-concept: [[concepts/指令微调（SFT）|指令微调（SFT）]] — source 提供 alpaca 指令数据格式与 LLaMA-7B 指令微调证据。
- compiled-concept: [[concepts/PEFT 与 LoRA|PEFT 与 LoRA]] — source 给出 LoRA 低秩适配、任务切换成本与 alpaca-lora 实现。
- compiled-concept: [[concepts/Self-Instruct 与合成数据|Self-Instruct 与合成数据]] — source 保留 Self-Instruct 流程与 Alpaca 升级细节。
- compiled-concept: [[concepts/Chat Template 与 Tokenizer|Chat Template 与 Tokenizer]] — source 区分 alpaca/sharegpt 格式与字段。
- compiled-concept: [[concepts/模型量化|模型量化]] — source 把量化/精度列为训练成本因素并给出 GGUF/GGML 导出。
- compiled-entity: [[entities/Llama|Llama]] — source 是 Llama 开源微调实战的主要来源。
- compiled-entity: [[entities/Hugging Face|Hugging Face]] — source 用 Transformers+PEFT+Trainer 组织训练。
- related-source: [[sources/LLM/微调生成模型.xmind|微调生成模型]] — 微调簇，互补阶段化与成本阶梯。
- related-source: [[sources/LLM/Transformer/模型微调.xmind|模型微调]] — 微调簇，共享数据准备与指令微调脉络。
- map-entry: [[maps/LLM 基础学习地图|LLM 基础学习地图]] — source 补充 LLM 微调实践路径。

## Maintenance Notes

- XMind export succeeded for all discovered sheets.
- `PEFT（Profiled End-to-end Flow Tuning）` 的展开内容描述更像硬件相关执行流调优，不同于常见的 Parameter-Efficient Fine-Tuning 用法；后续 compile 前应回 raw 或外部资料澄清术语。
