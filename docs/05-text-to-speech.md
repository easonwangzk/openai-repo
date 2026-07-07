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

## Speech Translation to Voice Output (AI-901 aligned)

Text-to-speech is often the final stage of a larger speech pipeline.

### End-to-end pattern

1. Capture source speech.
2. Transcribe and/or translate to target language.
3. Apply formatting and terminology normalization.
4. Synthesize target speech with voice and style controls.
5. Stream or store output with metadata.

### Where Azure Speech Translation fits

- For live multilingual experiences, speech translation can output translated text or speech in near real time.
- For high-fidelity branded voice output, teams often post-process translated text and then run TTS synthesis with strict style controls.

### Quality controls for multilingual voice

- Validate named entities after translation before synthesis.
- Keep glossary rules for product names and legal terms.
- Evaluate prosody by language, because pacing and stress differ across locales.
- Add human review for public-facing critical announcements.

### Cost and latency trade-offs

- More target languages increase translation and synthesis cost.
- Real-time voice output prioritizes latency; offline narration can prioritize quality.
- Use short streaming chunks for conversational UX, and larger chunks for long-form narration.

### AI-901 exam lens

- Distinguish speech-to-text, speech translation, and text-to-speech as separate but composable services.
- Understand that output voice quality is influenced by both translation quality and TTS settings.
- Be able to choose between a direct speech translation flow and a staged pipeline.

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
