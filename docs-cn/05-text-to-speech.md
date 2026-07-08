# 文本转语音学习笔记

## 概览

文本转语音（TTS）把文字转换成语音音频，常见场景：

- 语音助手
- 音频摘要
- 无障碍功能
- 语言学习应用
- 内容平台配音

## 常见模型

文本转语音模型示例：

- `gpt-4o-mini-tts`
- `tts-1`
- `tts-1-hd`

## 核心输入

一次语音请求通常需要：

- `model`
- `voice`
- `input`

部分模型还支持额外指令，用于控制说话风格。

## 声线设计思路

你可以通过指令控制表达方式，例如：

- 语速慢一些，发音清晰。
- 语气温暖且专业。
- 风格积极、有活力。
- 强调产品名称。

## 实战建议

- 低延迟播放优先 `wav` 或 `pcm`。
- 文件输出与跨平台分发优先 `mp3`。
- 向终端用户明确提示音频由 AI 生成。
- 生产选型前，对同一脚本测试多个 voice。

## 语音翻译到语音输出（对齐 AI-901）

TTS 往往是更大语音流水线的最后一环。

### 端到端模式

1. 采集源语音。
2. 转写并/或翻译到目标语言。
3. 做文本格式与术语标准化。
4. 结合 voice 与风格控制合成目标语音。
5. 以流式或文件方式输出并附带元数据。

### Azure Speech Translation 的位置

- 在实时多语言体验中，语音翻译可近实时输出翻译文本或语音。
- 在高保真品牌语音输出场景，团队通常先后处理翻译文本，再用严格风格控制做 TTS 合成。

### 多语言语音质量控制

- 合成前先校验翻译后的命名实体。
- 为产品名与法务术语维护术语表规则。
- 按语言评估韵律，因为不同语种节奏与重音差异明显。
- 面向公众的关键播报建议加入人工审核。

### 成本与延迟权衡

- 目标语言越多，翻译与合成成本越高。
- 实时语音优先延迟；离线配音可优先质量。
- 会话型体验适合短流式分块，长内容旁白适合更大分块。

### AI-901 备考视角

- 能把语音转文本、语音翻译、文本转语音区分为独立但可组合服务。
- 理解最终语音质量同时受翻译质量与 TTS 参数影响。
- 能在“直接语音翻译流”与“分阶段流水线”之间做选择。

## 最小 Python 模式

```python
from pathlib import Path
from openai import OpenAI

client = OpenAI()
out_path = Path("speech.mp3")

with client.audio.speech.with_streaming_response.create(
    model="gpt-4o-mini-tts",
    voice="coral",
    input="Welcome to the demo.",
    instructions="Speak in a calm and confident tone.",
) as response:
    response.stream_to_file(out_path)
```

## 建议练习

1. 用三种不同 voice 朗读同一脚本。
2. 用两种语气生成一个简短产品介绍。
3. 在你的播放环境中比较 `mp3` 与 `wav`。
4. 做一个 markdown 笔记的小型朗读器。
