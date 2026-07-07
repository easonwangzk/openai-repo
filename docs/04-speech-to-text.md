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
