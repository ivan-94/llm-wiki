---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/机器学习/python 深度学习入门.xmind"
source_relpath: "机器学习/python 深度学习入门.xmind"
raw_created_at: 2024-07-30T03:26:41+00:00
raw_modified_at: 2025-01-20T11:45:53.418223+00:00
raw_size: 27914366
raw_fingerprint: "size=27914366;birth=2024-07-30T03:26:41+00:00;mtime=2025-01-20T11:45:53.418223+00:00"
raw_snapshot_at: 2026-05-29T22:13:34.628712+00:00
ingested_at: 2026-05-30
status: ingested
---

# python 深度学习入门.xmind

## Source

- Raw file: [机器学习/python 深度学习入门.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/python%20%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E5%85%A5%E9%97%A8.xmind>)
- Raw ref: `raw:机器学习/python 深度学习入门.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2024-07-30T03:26:41+00:00`; modified `2025-01-20T11:45:53.418223+00:00`; size `27914366`; snapshot `2026-05-29T22:13:34.628712+00:00`
- Coverage: exported and read 14 sheets: `① __init__`, `② 二分类问题实战`, `③ 多分类问题实战`, `④ 标量回归问题实战`, `⑤ 机器学习基础`, `⑥ 工作流程`, `7️⃣ 计算机视觉`, `7️⃣ 计算机视觉 2`, `8️⃣ 时间序列和 RNN`, `9️⃣自然语言`, `9️⃣ 自然语言 Transformer`, `9️⃣自然语言-语言模型`, `最佳实践`, `更多`.

## Summary

这是一份大型深度学习学习笔记，围绕 Keras/Python 从基础概念一路覆盖分类、回归、泛化、工作流、计算机视觉、时间序列/RNN、自然语言、Transformer、语言模型、GPT-2 推理/微调、LoRA、Mini GPT、超参数优化、模型集成和混合精度训练。

## Source Digest

这份 workbook 的主线是从“机器学习如何通过数据、标签、损失函数和反馈信号学习表示”进入深度学习工程实践。开头把人工智能、机器学习、深度学习区分为规则系统、从数据中学习规则、以及用连续表示层学习特征；随后用 MNIST 手写数字识别建立 Keras 训练闭环：准备数据、构建 Dense 网络、编译损失/优化器/指标、归一化输入、训练、评估、保存模型和推理。

实践部分按任务类型展开。二分类以 IMDB 影评为例，讲单词索引、multi-hot 编码、Dense 层堆叠、验证集、过拟合调试和最终模型。多分类以路透社新闻为例，强调 one-hot 标签、categorical crossentropy 和输出维度。标量回归以波士顿房价为例，强调标准化、小样本下的 K 折交叉验证、MAE 等评估方式。机器学习基础 sheet 则系统总结泛化、训练/验证/测试集、过拟合原因、特征工程、正则化、dropout、模型容量、迭代改进拟合等工程判断。

中段把深度学习问题扩展到不同数据形态。计算机视觉部分从 CNN 的局部特征提取、卷积/池化、MNIST 卷积网络，到预训练模型特征提取、微调、小样本猫狗识别、数据增强、图像分割、现代 CNN 层块、残差连接、批量归一化和 SeparableConv2D。时间序列部分引入 RNN、LSTM/GRU 等序列建模思想，并以 Jena climate 温度预测为实战，同时比较基线、一维卷积和循环网络。自然语言部分从规则方法到深度学习，覆盖文本向量化、分词、词表、嵌入、IMDB 情绪分类、GloVe 等预训练词向量。

后段聚焦 Transformer 和语言模型。Transformer sheet 解释注意力机制、多头注意力、编码器、解码器、位置编码、前馈网络、层归一化、残差连接、因果掩码和 Seq2Seq；实战包括文本分类和英西机器翻译。语言模型 sheet 把语言模型定义为给定上下文预测下一个词元的概率模型，区分贪婪采样和温度采样，并覆盖 GPT-2 预训练模型推理、微调唐诗、LoRA 参数高效微调、Mini GPT 从数据集、分词器、Transformer Decoder 到采样推理的完整路径。

最后的最佳实践把训练性能和工程质量连接起来：超参数优化可通过 KerasTuner 搜索，模型集成可通过投票、平均、堆叠、装袋、提升或 MoE 提升稳定性和准确率，混合精度训练用 FP16/FP32 搭配和 loss scaling 提升训练速度与显存效率，但依赖硬件支持。整体看，这份 source 不是某个单点教程，而是一条从“基础概念 -> 任务实战 -> 泛化调试 -> 数据模态 -> Transformer/语言模型 -> 训练优化”的学习路径。

## Key Claims

- explicit: 机器学习系统是训练出来的，不是显式编写规则；它在带反馈信号的假设空间中寻找输入数据的有用表示。
- explicit: 深度学习通过连续层学习越来越有意义的表示，权重是层变换的参数，训练通过损失函数、优化器和反向传播不断微调权重。
- explicit: 常见任务有固定损失函数选择套路：二分类可用 binary crossentropy，多分类可用 categorical crossentropy，回归可用均方误差，序列学习可用 CTC。
- explicit: 深度学习张量通常以样本轴作为第一轴，图像可表示为 4D 张量，视频可表示为 5D 张量。
- explicit: 模型泛化需要独立训练集、验证集和测试集，过拟合时训练集表现优于新数据，改进可从数据管理、特征工程、正则化、dropout 和模型容量调整入手。
- explicit: CNN 适合图像，RNN 适合序列，Transformer 通过注意力机制增强并行处理和长距离依赖建模。
- explicit: 语言模型是给定前文词元预测下一个词元概率的模型，推理时可使用贪婪采样或温度采样控制输出。
- explicit: LoRA 通过低秩适配器更新少量参数，而不是直接更新完整大模型权重；source 给出 768 x 768 权重与 rank 4 适配器的参数量对比。
- inferred: 这份 source 最适合编译为“深度学习学习地图”和多个概念页，而不是单一概念页，因为它覆盖基础、CV、NLP、Transformer、语言模型和训练优化多个层级。

## External Links

- framework-doc: [Keras getting started](https://keras.io/getting_started/) — source 中用于 Keras 入门环境与示例；not verified.
- source-code: [Deep Learning with Python notebooks](https://github.com/fchollet/deep-learning-with-python-notebooks/blob/master/chapter08_intro-to-dl-for-computer-vision.ipynb) — source 中列为图书源码/扩展阅读；not verified.
- dataset: [IMDB sentiment data](https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz) — source 中用于文本情绪分类或示例数据；not verified.
- dataset: [Oxford Pets images](http://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz) — source 中用于图像分割/视觉数据；not verified.
- dataset: [Oxford Pets annotations](http://www.robots.ox.ac.uk/~vgg/data/pets/data/annotations.tar.gz) — source 中用于图像分割/视觉标注；not verified.
- dataset: [Jena climate dataset](https://s3.amazonaws.com/keras-datasets/jena_climate_2009_2016.csv.zip) — source 中用于时间序列温度预测；not verified.
- embedding-data: [GloVe 6B](http://nlp.stanford.edu/data/glove.6B.zip) — source 中用于预训练词向量；not verified.
- tutorial: [Transformer neural machine translation](https://keras.io/examples/nlp/neural_machine_translation_with_transformer/) — source 中用于 Transformer 解码器/Seq2Seq 实战；not verified.
- discussion: [Tokenizer vs TextVectorization](https://stackoverflow.com/questions/71002866/difference-between-tokenizer-and-textvectorization-layer-in-tensorflow) — source 中作为分词器与向量化差异参考；not verified.
- model-doc: [KerasNLP models](https://keras.io/api/keras_nlp/models/) — source 中列为预训练模型入口；not verified.
- tutorial: [GPT-2 text generation with KerasNLP](https://keras.io/examples/generative/gpt2_text_generation_with_kerasnlp/) — source 中用于 GPT-2 推理；not verified.
- model-card: [GPT-2 model card](https://github.com/openai/gpt-2/blob/master/model_card.md) — source 中用于 GPT-2 参数规模说明；not verified.
- dataset: [Chinese poetry](https://github.com/chinese-poetry/chinese-poetry.git) — source 中用于 GPT-2 唐诗微调；not verified.
- tutorial: [LoRA fine-tuning GPT-2](https://keras.io/examples/nlp/parameter_efficient_finetuning_of_gpt2_with_lora/) — source 中用于参数高效微调；not verified.
- tutorial: [Mini GPT text generation](https://keras.io/examples/generative/text_generation_gpt/#inference) — source 中用于实现 Mini GPT；not verified.
- dataset: [SimpleBooks](https://dldata-public.s3.us-east-2.amazonaws.com/simplebooks.zip) — source 中用于 Mini GPT 训练数据；not verified.
- tool-doc: [KerasTuner](https://keras.io/keras_tuner/) — source 中用于超参数搜索；not verified.

## Links

- compiled-concept: [[concepts/注意力机制|注意力机制]] — Transformer sheet 提供多头注意力、位置编码、因果掩码证据。
- compiled-concept: [[concepts/自回归语言模型|自回归语言模型]] — 语言模型 sheet 用“给定上下文预测下一个词元”定义。
- compiled-concept: [[concepts/解码与采样策略|解码与采样策略]] — source 区分贪婪采样与温度采样。
- compiled-concept: [[concepts/Encoder 与 Decoder 模型|Encoder 与 Decoder 模型]] — Transformer sheet 用编码器/解码器做英西翻译 Seq2Seq。
- compiled-concept: [[concepts/PEFT 与 LoRA|PEFT 与 LoRA]] — source 给出 768×768 vs rank 4 适配器参数量对比。
- compiled-concept: [[concepts/模型量化|模型量化]] — 最佳实践 sheet 讲混合精度训练。
- related-source: [[sources/LLM/Transformer/Transformer.xmind|Transformer.xmind]] — 作为深度学习侧的 Transformer/语言模型可选前置。
- map-entry: [[maps/LLM 基础学习地图|LLM 基础学习地图]] — 作为可选前置（神经网络/梯度下降通识底座）。
- Compile candidates: 深度学习基础, Keras 实战学习路径, 机器学习泛化, CNN, RNN, 模型训练最佳实践, map-candidate: 深度学习学习地图, entity-candidate: Keras, entity-candidate: KerasNLP, entity-candidate: GPT-2.

## Maintenance Notes

- 这是大型多 sheet source；source note 只保留 LLM digest 和高信号分类，完整代码片段、训练日志和示例输出需回 raw 或临时导出读取。
- workbook 中包含大量 `xmind:#...` 内部跳转链接，已视为 XMind 内部导航而非外部链接。
- `更多` sheet 仅包含 `./Transfomer` 和 Keras 官方文档入口，内容较薄。
