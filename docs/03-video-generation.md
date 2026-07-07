# Video Generation Learning Notes

## Overview

OpenAI video generation workflows are asynchronous. Instead of getting a finished result immediately, you usually:

1. Start a render job.
2. Poll the job status or wait for a webhook.
3. Download the final video asset when the job is complete.

## Main Concepts

### 1. Prompting for motion

A strong video prompt often includes:

- Shot type
- Subject
- Action
- Setting
- Lighting
- Camera movement
- Style or mood

Example:

- `Wide shot of a paper boat floating across a rain puddle at sunset, soft golden reflections, camera slowly tracks left.`

### 2. Async workflow

A typical workflow looks like this:

- Create a video job
- Receive a `video_id`
- Check for statuses such as `queued`, `in_progress`, `completed`, or `failed`
- Download the MP4 after completion

### 3. Guidance inputs

Depending on the API and model availability, you may be able to:

- Use an image reference for the first frame
- Reuse a non-human character asset for consistency
- Extend an existing clip
- Edit an existing video with a focused prompt

## Practical Advice

- Use shorter clips while iterating.
- Start at lower resolution when testing prompts.
- Make edits narrow and specific.
- Use webhooks for production systems instead of aggressive polling.

## Restrictions and Availability

Video generation can have stricter guardrails and model availability constraints than text or image APIs. Before building around it, confirm:

- Your account has access to the needed model.
- The model is not deprecated.
- The allowed content and input types match your use case.

## Suggested Exercises

1. Write three prompts for the same scene using different cinematic styles.
2. Design a polling workflow for a video generation backend.
3. Compare when to use image reference versus video extension.
4. Draft a webhook event handler for completed renders.
