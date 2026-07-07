# Text and General OpenAI Learning Notes

## What to Learn First

Text workflows are the best entry point because they teach the common request structure used across many OpenAI APIs.

The main ideas are:

- Choose the right model for the job.
- Use the Responses API for direct model requests.
- Keep prompts in code instead of storing them in remote prompt objects.
- Add lightweight evaluation checks when prompt behavior matters.

## Key Concepts

### 1. Model selection

Use smaller and cheaper models for classification, rewriting, and extraction. Use stronger reasoning-capable models for planning, analysis, multi-step logic, or higher-quality outputs.

### 2. Responses API

The Responses API is the recommended path for many modern text and multimodal workflows. A request usually includes:

- `model`
- `instructions` for high-priority behavior guidance
- `input` for the task itself

### 3. Prompt design

Good prompts usually include:

- A clear goal
- Constraints
- Output format instructions
- Examples when the task is ambiguous

### 4. Structured outputs

When your app needs reliable JSON, define a schema and validate the output before downstream use.

## Practical Advice

- Pin model snapshots in production if consistency matters.
- Store prompts near the feature they support.
- Test prompts with representative inputs before changing production behavior.
- Treat prompt changes like code changes.

## Minimal Python Pattern

```python
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-4.1-mini",
    instructions="You are a concise assistant.",
    input="Summarize the advantages of retrieval-augmented generation in 4 bullet points."
)

print(response.output_text)
```

## Suggested Exercises

1. Build a summarizer for long notes.
2. Build a classifier that labels feedback by topic.
3. Build a JSON extractor for resumes, invoices, or support tickets.
4. Compare a smaller model and a stronger model on the same task.
