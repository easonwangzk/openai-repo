# OpenAI Learning Repository

A practical learning repository for exploring OpenAI models and APIs across text, images, video, speech-to-text, and text-to-speech.

## Goals

- Learn the core OpenAI API patterns.
- Understand which model families fit which tasks.
- Run small examples locally with clear English comments.
- Build a foundation for multimodal applications.

## Project Structure

```text
openai-repo/
├── README.md
├── .env.example
├── requirements.txt
├── docs/
│   ├── 01-text-and-general.md
│   ├── 02-images-and-vision.md
│   ├── 03-video-generation.md
│   ├── 04-speech-to-text.md
│   └── 05-text-to-speech.md
└── examples/
    ├── text_generation.py
    ├── vision_analysis.py
    ├── image_generation.py
    ├── speech_to_text.py
    └── text_to_speech.py
```

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Copy the environment template:

```bash
cp .env.example .env
```

4. Add your API key to `.env`:

```env
OPENAI_API_KEY=your_api_key_here
```

## Learning Path

1. Start with [docs/01-text-and-general.md](docs/01-text-and-general.md) to understand the Responses API and prompt design.
2. Continue with [docs/02-images-and-vision.md](docs/02-images-and-vision.md) for image understanding and generation.
3. Read [docs/03-video-generation.md](docs/03-video-generation.md) to learn the async workflow for video generation.
4. Practice audio input with [docs/04-speech-to-text.md](docs/04-speech-to-text.md).
5. Finish with [docs/05-text-to-speech.md](docs/05-text-to-speech.md).

## Example Commands

```bash
python examples/text_generation.py
python examples/vision_analysis.py
python examples/image_generation.py
python examples/speech_to_text.py
python examples/text_to_speech.py
```

## Notes

- API and model availability can change over time, so always cross-check with the official OpenAI developer docs.
- Video generation workflows are often asynchronous and may require account-level access or model availability checks.
- Keep production prompts in code and version them like any other application logic.

## Official References

- https://developers.openai.com/api/docs
- https://developers.openai.com/api/docs/models
- https://developers.openai.com/api/docs/pricing
- https://cookbook.openai.com/
