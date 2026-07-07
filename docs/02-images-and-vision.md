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
