# AI-901 Study Alignment Guide (Based on the Microsoft Learn Study Guide)

This document keeps this repository aligned with the AI-901 (Azure AI Fundamentals) exam and defines a repeatable improvement loop.

Primary reference:
- https://learn.microsoft.com/credentials/certifications/resources/study-guides/ai-901

Related module references used in this plan:
- Anomaly Detector: https://learn.microsoft.com/azure/cognitive-services/anomaly-detector/
- Language Understanding (LUIS): https://learn.microsoft.com/azure/cognitive-services/luis/
- Azure Machine Learning: https://learn.microsoft.com/azure/machine-learning/
- Computer Vision: https://learn.microsoft.com/azure/cognitive-services/computer-vision/
- NLP technology choices: https://learn.microsoft.com/azure/architecture/data-guide/technology-choices/natural-language-processing
- Azure Bot Service: https://learn.microsoft.com/azure/bot-service/
- Speech to Text: https://learn.microsoft.com/azure/cognitive-services/speech-service/index-speech-to-text
- Speech Translation: https://learn.microsoft.com/azure/cognitive-services/speech-service/index-speech-translation

## 1. AI-901 Scope Snapshot (Objectives as of 2026-04-15)

- Identify AI concepts and capabilities (40-45%)
- Implement AI solutions by using Microsoft Foundry (55-60%)

Core exam themes:
- Responsible AI principles
- Model components and deployment/configuration basics
- AI workloads: generative AI, agentic AI, text analytics, speech, vision, information extraction
- Practical implementation patterns with Foundry portal and SDK

## 2. Mapping: AI-901 objectives -> current repository

### A. Identify AI concepts and capabilities (40-45%)

Currently covered:
- Model, prompting, and evaluation basics in `docs/01-text-and-general.md`
- Vision and image generation fundamentals in `docs/02-images-and-vision.md`
- Speech basics in `docs/04-speech-to-text.md` and `docs/05-text-to-speech.md`
- Runnable Python examples in `examples/*.py`

Current gaps:
- More explicit Responsible AI exam notes and checkpoints
- Clearer workload-to-model decision tables
- More exam-style quick checks and short Q and A sections

### B. Implement AI solutions with Foundry (55-60%)

Currently covered:
- Lightweight Python patterns for text, vision, and speech
- Basic prompt and model selection notes

Current gaps:
- End-to-end Foundry portal walkthrough (deploy, test, compare)
- Agent implementation and lightweight client patterns
- A dedicated information extraction chapter across document/image/audio/video

## 3. Module-by-Module Coverage Plan (Requested)

This section adds content by module so you can improve docs in a modular way.

### 3.1 Anomaly Detector

What to know:
- Detect unusual patterns in time-series data.
- Distinguish point anomalies vs. trend/seasonality shifts.

Why it matters for AI-901:
- Tests your understanding of AI workload selection and business fit.

Repo action:
- Add a short concept section in `docs/01-text-and-general.md` under "AI workloads".
- Add an example later: `examples/anomaly_detection_basics.py` (simple synthetic time series).

### 3.2 Language Understanding (LUIS)

What to know:
- Intent classification and entity extraction concepts.
- How conversational language understanding fits into bot scenarios.

Why it matters for AI-901:
- Classic NLP workload recognition is a common objective.

Repo action:
- Add an NLP subsection in `docs/01-text-and-general.md` contrasting intent/entity extraction vs. generative prompting.
- Add bot/NLU notes in this file under "Bot Service" integration.

### 3.3 Azure Machine Learning

What to know:
- Training vs. inference lifecycle, experiments, endpoints, and MLOps basics.
- Difference between model development platforms and prebuilt AI services.

Why it matters for AI-901:
- Helps answer "when to use custom ML vs. managed AI services" questions.

Repo action:
- Add a decision matrix subsection in `docs/01-text-and-general.md`.
- Add one exam note table in this file: "Custom model vs. prebuilt service".

### 3.4 Computer Vision

What to know:
- Image analysis tasks (classification, detection, OCR-style extraction, captioning).
- Vision input handling in multimodal applications.

Why it matters for AI-901:
- Core workload area with practical scenario questions.

Repo action:
- Expand `docs/02-images-and-vision.md` with a "task taxonomy" table.
- Keep using `examples/vision_analysis.py` and map each output to a task type.

### 3.5 NLP Technology Choices

What to know:
- Choosing between keyword extraction, sentiment, summarization, NER, translation, and generative chat.
- Trade-offs: cost, latency, explainability, and customization needs.

Why it matters for AI-901:
- Scenario-based questions often test the right technique selection.

Repo action:
- Add an "NLP workload chooser" section in `docs/01-text-and-general.md`.
- Add 10 exam-style multiple-choice questions later in a dedicated review doc.

### 3.6 Azure Bot Service

What to know:
- Bot architecture basics: channels, orchestration, dialog flow, and backend integration.
- Role of language understanding and tool invocation in bot workflows.

Why it matters for AI-901:
- Bridges concepts across NLP, agentic behavior, and app integration.

Repo action:
- Add a "bot and agent patterns" section in this file.
- Add a future lightweight client example that simulates bot-style turn handling.

### 3.7 Speech to Text

What to know:
- Speech recognition pipeline and transcription use cases.
- Accuracy factors: audio quality, language, domain vocabulary.

Why it matters for AI-901:
- Included explicitly in exam workload recognition and implementation topics.

Repo action:
- Keep `docs/04-speech-to-text.md` and `examples/speech_to_text.py` as baseline.
- Add a short "error sources and mitigation" checklist.

### 3.8 Speech Translation

What to know:
- Real-time or batch translation from spoken input.
- Difference between speech translation and text-only translation pipelines.

Why it matters for AI-901:
- Frequently appears in service-selection questions.

Repo action:
- Add a dedicated subsection in `docs/04-speech-to-text.md` (speech translation patterns).
- Add a future demo script: `examples/speech_translation_basics.py`.

## 4. Priority Roadmap (Exam-Weighted)

P0 (do first):
- [ ] Add Foundry + agent fundamentals chapter (highest exam weight)
- [ ] Add information extraction chapter across document/image/audio/video
- [ ] Add module comparison table for the 8 modules listed above

P1 (second wave):
- [ ] Add Responsible AI quick-check section and mini quiz
- [ ] Add deployment/config basics: temperature, max output, reasoning effort, latency/cost trade-offs
- [ ] Add workload-to-service quick lookup table

P2 (exam sprint):
- [ ] Add 30+ AI-901 style practice questions
- [ ] Add one-page final revision sheet
- [ ] Add prompt iteration and evaluation scoring mini lab

## 5. Weekly Upgrade Loop (Repeatable)

1. Review updates in AI-901 and Azure AI/Foundry docs.
2. Pick one module from Section 3.
3. Update one doc and one runnable example.
4. Add 5-10 quiz questions for that module.
5. Update progress in this file.

## 6. Suggested Study Sequence in This Repository

1. Start with `docs/01-text-and-general.md` for model, prompt, and evaluation fundamentals.
2. Continue with `docs/02-images-and-vision.md` and run `examples/vision_analysis.py`.
3. Run `examples/image_generation.py` for generation workflows.
4. Run `examples/speech_to_text.py` and `examples/text_to_speech.py` for speech workflows.
5. Use this file as your module-by-module progress tracker.

## 7. Exam Notes

- AI-901 is concept-oriented, but implementation familiarity improves answer quality.
- For each concept, keep at least one runnable mini-example.
- Compare quality, latency, and cost across at least two model/service options.
- Build scenario thinking: "requirement -> suitable service -> expected trade-offs".

## 8. Change Log

- Rewritten in English.
- Added module-based expansion plan for: Anomaly Detector, LUIS, Azure ML, Computer Vision, NLP choices, Bot Service, Speech to Text, and Speech Translation.
