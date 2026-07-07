# Images and Vision Learning Notes

## Core Use Cases

OpenAI image workflows usually fall into two categories:

- Understanding images with vision models
- Generating or editing images with image generation tools

## Vision Basics

A model can inspect one or more images and answer questions about their contents. This is useful for:

- Image captioning
- OCR-like extraction
- UI understanding
- Visual quality checks
- Product catalog enrichment

## Image Input Methods

You can send an image through:

- A public image URL
- A Base64 data URL
- A file ID uploaded through the Files API

## Detail Levels

Vision requests may support detail controls such as `low`, `high`, `original`, or `auto`. Higher detail improves fidelity but can increase cost.

## Image Generation Basics

For image creation, you describe the subject, style, scene, lighting, composition, and any constraints. Better prompts usually include:

- Subject
- Environment
- Camera framing
- Lighting
- Color palette
- Visual style

## Practical Advice

- Start with a short prompt, then add precision only where the output is drifting.
- Be explicit about what should not appear.
- Use image generation for ideation first, then refine with iterative prompts.
- Remember that image inputs count toward token or image costs.

## Azure Computer Vision Deep Dive (AI-901 aligned)

Azure Computer Vision focuses on extracting structured signals from images, while generative models focus on creating or transforming content. In exam scenarios, you are often asked to pick between these modes.

### Core Computer Vision capability groups

- Image analysis: tags, captions, and scene-level understanding.
- OCR: printed text extraction from images.
- Domain features: scenario-specific extraction and indexing workflows.

### Typical enterprise use cases

- Product catalog enrichment from image metadata.
- Receipt and signage text extraction for downstream processing.
- Content moderation and visual compliance checks.
- Accessibility support through captioning.

### Service selection guidance

| Need | Better fit |
|---|---|
| Deterministic image metadata and OCR output | Azure Computer Vision |
| Creative image synthesis from text | Image generation model |
| Complex multimodal reasoning over image plus business context | Multimodal LLM workflow |

### Design and reliability notes

- OCR quality depends on image resolution, skew, lighting, and language coverage.
- Captions are summaries, not guaranteed exhaustive object inventories.
- For production pipelines, store both raw outputs and normalized fields so you can reprocess later.
- Pair vision extraction with human-review thresholds for high-risk scenarios.

### AI-901 exam lens

- Know which tasks are perception/extraction versus generation.
- Expect scenario questions that combine OCR + NLP + search or reporting.
- Be ready to justify service choice by output type, latency, and explainability.

## Minimal Vision Pattern

```python
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-4.1-mini",
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "Describe the key objects in this image."},
                {"type": "input_image", "image_url": "https://example.com/sample.jpg"},
            ],
        }
    ],
)

print(response.output_text)
```

## Suggested Exercises

1. Build an image caption generator.
2. Extract menu text from a restaurant photo.
3. Compare the same image using different detail levels.
4. Generate marketing images with progressively more specific prompts.
