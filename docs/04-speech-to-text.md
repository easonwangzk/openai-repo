# Speech to Text Learning Notes

## Overview

Speech-to-text turns audio into text. This is useful for:

- Meeting transcription
- Voice note indexing
- Subtitle generation
- Call analytics
- Search over audio archives

## Common Models

Examples of speech-to-text model families include:

- `gpt-4o-mini-transcribe`
- `gpt-4o-transcribe`
- `gpt-4o-transcribe-diarize`
- `whisper-1`

## Core Patterns

### 1. Basic transcription

You upload an audio file and receive text.

### 2. Speaker diarization

For multi-speaker recordings, diarization can separate speakers and return segment metadata.

### 3. Translation

Some workflows translate spoken content into English during transcription.

### 4. Prompting

You can improve accuracy by giving the model context, such as domain terms, acronyms, or the topic of the conversation.

## Practical Advice

- Keep files under the size limits or split them into chunks.
- Avoid splitting audio in the middle of a sentence when possible.
- Use prompts to improve recognition of uncommon words.
- Use timestamps when you need subtitles, edit points, or word-level alignment.

## Azure Speech to Text Deep Dive (AI-901 aligned)

### Core modes

- Real-time transcription for live interactions and assistive interfaces.
- Batch transcription for offline processing of recordings.
- Speaker diarization for multi-speaker sessions.
- Custom speech for domain-specific vocabulary and acoustic tuning.

### Engineering considerations

- Real-time mode optimizes latency, while batch mode usually optimizes throughput.
- Accuracy depends on noise level, microphone quality, accents, and domain terms.
- Chunking strategy should preserve sentence boundaries to reduce context loss.
- Use confidence and segment metadata to route low-confidence spans for review.

### Common failure points

- Domain terms are out of vocabulary.
- Overlapping speakers degrade diarization quality.
- Poor gain or clipping causes irreversible transcript loss.

Mitigations:

- Add domain hints/custom speech training where possible.
- Preprocess audio (denoise, normalize, channel separation).
- Add post-correction workflows for critical transcripts.

## Azure Speech Translation Deep Dive

Speech translation is not just STT + text translation glued together. It is designed for real-time speech-to-text and speech-to-speech multilingual communication.

### Key capabilities

- Speech-to-text translation
- Speech-to-speech translation
- Multi-lingual speech translation (including language switching scenarios)
- Live interpreter patterns
- Multi-target translation outputs

### Practical cost insight

- Multi-target output can increase cost significantly because each additional target language adds translation workload.
- For long sessions, budget for both transcription and translation components.

### Service choice guidance

| Scenario | Recommended baseline |
|---|---|
| Meeting notes in one language | Speech to Text |
| Live cross-language conversation | Speech Translation |
| Post-call analytics in many languages | STT + batch translation pipeline |

### AI-901 exam lens

- Recognize the difference between transcription and translation workloads.
- Understand when custom speech is needed for quality.
- Expect questions about real-time vs batch trade-offs.

## Minimal Python Pattern

```python
from openai import OpenAI

client = OpenAI()

with open("speech.mp3", "rb") as audio_file:
    transcription = client.audio.transcriptions.create(
        model="gpt-4o-transcribe",
        file=audio_file,
    )

print(transcription.text)
```

## Suggested Exercises

1. Transcribe a short lecture recording.
2. Compare `whisper-1` and `gpt-4o-transcribe` on a noisy sample.
3. Add timestamps for subtitle generation.
4. Test whether a domain prompt improves technical vocabulary recognition.
