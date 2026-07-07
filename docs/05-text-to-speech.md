# Text to Speech Learning Notes

## Overview

Text-to-speech converts written text into spoken audio. This is useful for:

- Voice assistants
- Audio summaries
- Accessibility features
- Language learning apps
- Narration for content platforms

## Common Models

Examples of text-to-speech models include:

- `gpt-4o-mini-tts`
- `tts-1`
- `tts-1-hd`

## Core Inputs

A speech request usually needs:

- `model`
- `voice`
- `input`

Some models also accept additional instructions that shape the speaking style.

## Voice Design Ideas

Control the delivery with directions such as:

- Speak slowly and clearly.
- Use a warm and professional tone.
- Sound energetic and optimistic.
- Emphasize the product name.

## Practical Advice

- Use `wav` or `pcm` when low-latency playback matters.
- Use `mp3` for simple file output and portability.
- Tell end users when the audio is AI-generated.
- Test multiple voices for the same script before choosing one for production.

## Minimal Python Pattern

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

## Suggested Exercises

1. Read the same script with three different voices.
2. Generate a short product intro in two tones.
3. Compare `mp3` and `wav` outputs for your playback environment.
4. Build a small narrator for markdown notes.
