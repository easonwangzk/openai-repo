# AI-901 学习对齐指南（基于 Microsoft Learn 学习指南）

本文档用于让本仓库持续对齐 AI-901（Azure AI Fundamentals）考试范围，并形成可重复执行的改进闭环。

主要参考：
- https://learn.microsoft.com/credentials/certifications/resources/study-guides/ai-901

本计划关联模块参考：
- Anomaly Detector: https://learn.microsoft.com/azure/cognitive-services/anomaly-detector/
- Language Understanding (LUIS): https://learn.microsoft.com/azure/cognitive-services/luis/
- Azure Machine Learning: https://learn.microsoft.com/azure/machine-learning/
- Computer Vision: https://learn.microsoft.com/azure/cognitive-services/computer-vision/
- NLP technology choices: https://learn.microsoft.com/azure/architecture/data-guide/technology-choices/natural-language-processing
- Azure Bot Service: https://learn.microsoft.com/azure/bot-service/
- Speech to Text: https://learn.microsoft.com/azure/cognitive-services/speech-service/index-speech-to-text
- Speech Translation: https://learn.microsoft.com/azure/cognitive-services/speech-service/index-speech-translation

## 1. AI-901 范围快照（截至 2026-04-15 的目标权重）

- 识别 AI 概念与能力（40-45%）
- 使用 Microsoft Foundry 实现 AI 解决方案（55-60%）

考试核心主题：
- 负责任 AI 原则
- 模型组件与部署/配置基础
- AI 工作负载：生成式 AI、Agentic AI、文本分析、语音、视觉、信息抽取
- 基于 Foundry 门户与 SDK 的实践实现模式

## 2. 映射：AI-901 目标 -> 当前仓库

### A. 识别 AI 概念与能力（40-45%）

已覆盖：
- `docs/01-text-and-general.md` 中的模型、提示与评测基础
- `docs/02-images-and-vision.md` 中的视觉与图像生成基础
- `docs/04-speech-to-text.md` 与 `docs/05-text-to-speech.md` 中的语音基础
- `examples/*.py` 中可运行的 Python 示例

当前缺口：
- 更明确的负责任 AI 考点笔记与检查点
- 更清晰的“工作负载 -> 模型/服务”决策表
- 更多考试风格的快测与短问答

### B. 使用 Foundry 实现 AI 方案（55-60%）

已覆盖：
- 文本、视觉、语音的轻量 Python 模式
- 基础提示与模型选型说明

当前缺口：
- Foundry 门户端到端实操（部署、测试、对比）
- Agent 实现与轻量客户端模式
- 面向文档/图像/音频/视频的信息抽取专章

## 3. 按模块覆盖计划（按你的要求）

本节按模块补充内容，方便你做模块化升级。

### 3.1 Anomaly Detector

要点：
- 检测时间序列中的异常模式。
- 区分点异常与趋势/季节性偏移。

为何对 AI-901 重要：
- 会考察你对 AI 工作负载选型与业务匹配的理解。

仓库动作：
- 在 `docs/01-text-and-general.md` 的“AI workloads”下补充概念小节。
- 后续新增示例：`examples/anomaly_detection_basics.py`（简单合成时间序列）。

### 3.2 Language Understanding (LUIS)

要点：
- 意图分类与实体抽取概念。
- 对话式语言理解在 Bot 场景中的作用。

为何对 AI-901 重要：
- 经典 NLP 工作负载识别是常见目标。

仓库动作：
- 在 `docs/01-text-and-general.md` 增加 NLP 子节，对比意图/实体抽取与生成式提示。
- 在“Bot Service”集成部分补充 bot/NLU 说明。

### 3.3 Azure Machine Learning

要点：
- 训练 vs 推理生命周期，实验、端点与 MLOps 基础。
- 模型开发平台与预构建 AI 服务的差异。

为何对 AI-901 重要：
- 有助于回答“何时用自定义 ML、何时用托管 AI 服务”。

仓库动作：
- 在 `docs/01-text-and-general.md` 增加决策矩阵子节。
- 在该文件加入“自定义模型 vs 预构建服务”考试表格。

### 3.4 Computer Vision

要点：
- 图像分析任务（分类、检测、类 OCR 抽取、描述）。
- 多模态应用中的视觉输入处理。

为何对 AI-901 重要：
- 核心工作负载领域，常见场景题。

仓库动作：
- 在 `docs/02-images-and-vision.md` 扩展“任务分类法”表格。
- 继续使用 `examples/vision_analysis.py` 并将每类输出映射到任务类型。

### 3.5 NLP 技术选型

要点：
- 在关键词抽取、情感分析、摘要、命名实体、翻译、生成式对话间做选择。
- 权衡成本、延迟、可解释性与定制化需求。

为何对 AI-901 重要：
- 场景题常考“选对技术路线”。

仓库动作：
- 在 `docs/01-text-and-general.md` 增加“NLP 工作负载选择器”部分。
- 后续单独新增复习文档，补充 10 道考试风格选择题。

### 3.6 Azure Bot Service

要点：
- Bot 架构基础：渠道、编排、对话流、后端集成。
- 语言理解与工具调用在 Bot 流程中的角色。

为何对 AI-901 重要：
- 连接 NLP、Agent 行为与应用集成。

仓库动作：
- 在本文件新增“bot 与 agent 模式”部分。
- 后续新增轻量客户端示例，模拟 bot 式多轮处理。

### 3.7 Speech to Text

要点：
- 语音识别流水线与转写场景。
- 准确率影响因素：音频质量、语言、领域词汇。

为何对 AI-901 重要：
- 明确包含在工作负载识别与实现目标中。

仓库动作：
- 以 `docs/04-speech-to-text.md` 与 `examples/speech_to_text.py` 作为基线。
- 增加“错误来源与缓解”清单。

### 3.8 Speech Translation

要点：
- 实时或批量把语音输入翻译为目标语言。
- 区分语音翻译与纯文本翻译流水线。

为何对 AI-901 重要：
- 常出现在服务选型题。

仓库动作：
- 在 `docs/04-speech-to-text.md` 增加专门小节（语音翻译模式）。
- 后续新增示例脚本：`examples/speech_translation_basics.py`。

## 4. 优先级路线图（按考试权重）

P0（优先）：
- [ ] 增加 Foundry + Agent 基础章节（最高权重）
- [ ] 增加跨文档/图像/音频/视频的信息抽取章节
- [ ] 增加以上 8 个模块的对比表

P1（第二波）：
- [ ] 增加负责任 AI 快速检查与小测
- [ ] 增加部署/配置基础：temperature、max output、reasoning effort、延迟/成本权衡
- [ ] 增加工作负载到服务的速查表

P2（冲刺）：
- [ ] 增加 30+ 道 AI-901 风格练习题
- [ ] 增加一页最终冲刺速记
- [ ] 增加提示迭代与评测打分小实验

## 5. 每周升级循环（可复用）

1. 跟踪 AI-901 与 Azure AI/Foundry 文档更新。
2. 从第 3 节选择 1 个模块。
3. 更新 1 篇文档 + 1 个可运行示例。
4. 为该模块新增 5-10 道测验题。
5. 在本文件更新进度。

## 6. 本仓库建议学习顺序

1. 先看 `docs/01-text-and-general.md`（模型、提示、评测基础）。
2. 再看 `docs/02-images-and-vision.md` 并运行 `examples/vision_analysis.py`。
3. 运行 `examples/image_generation.py` 理解生成流程。
4. 运行 `examples/speech_to_text.py` 与 `examples/text_to_speech.py` 学习语音流程。
5. 把本文件作为模块进度跟踪器使用。

## 7. 备考提示

- AI-901 偏概念，但具备实现经验会显著提升答题质量。
- 每个概念至少保留一个可运行最小示例。
- 至少比较两种模型/服务的质量、延迟与成本。
- 建立场景思维：`需求 -> 合适服务 -> 预期权衡`。

## 8. 变更记录

- 已重写为英文版本（源文件）。
- 已新增基于模块的扩展计划：Anomaly Detector、LUIS、Azure ML、Computer Vision、NLP 选型、Bot Service、Speech to Text、Speech Translation。
