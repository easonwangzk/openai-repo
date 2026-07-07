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

## GPT Model Evolution (Official-Info-Oriented Summary)

Note: OpenAI model capabilities and availability change over time. Always verify with the official model page, release notes, and pricing page before production decisions.

### Phase A: GPT-3.5 era (practical baseline)

Typical value:

- Fast response and low cost.
- Good enough for lightweight tasks such as rewrite, classify, and simple extraction.

Typical limits:

- Weaker multi-step reasoning.
- Less stable instruction following on complex constraints.
- More quality variance on coding and long-context tasks.

### Phase B: GPT-4 era (quality and reasoning jump)

Typical value:

- Significant improvement in reasoning reliability and instruction following.
- Better coding, analysis, and complex writing quality.
- Stronger safety behavior than earlier generation.

Typical limits:

- Higher latency and cost than smaller models.
- Throughput and real-time interaction can be less favorable for high-volume apps.

### Phase C: GPT-4 Turbo / optimized GPT-4 variants (efficiency upgrade)

Typical value:

- Better price-performance balance than earlier GPT-4 snapshots.
- Larger context windows (for long prompts and bigger documents).
- Better practical fit for production systems with cost constraints.

Typical limits:

- Still not always optimal for the hardest reasoning chains compared with newer dedicated reasoning models.

### Phase D: Newer GPT family (for example GPT-5.x line)

Typical value (according to official release positioning):

- Better coding and agent-like task completion.
- Stronger long-context understanding (for large codebases and long documents).
- Better instruction adherence and output consistency in many practical workloads.

Typical limits:

- Model choice still depends on target: quality, speed, and budget trade-offs remain.
- Not every workload benefits equally from larger/stronger models.

### GPT-5 versions: concrete differences (quick reference)

Note: numbers below are based on the official models docs at the time of writing and can change. Re-check the model and pricing pages before production rollout.

| Model | Positioning | Context window | Max output | Text price (per 1M tokens) | Reasoning effort defaults | Typical use cases |
|---|---|---|---|---|---|---|
| GPT-5.5 (`gpt-5.5`) | Strongest quality for most complex professional/coding tasks | 1,050,000 | 128,000 | Input $5.00, Output $30.00 | Supports `none/low/medium/high/xhigh`, default `medium` | Hard multi-step reasoning, difficult coding, high-stakes agent workflows |
| GPT-5.4 (`gpt-5.4`) | Frontier quality with better cost-performance than 5.5 | 1,050,000 | 128,000 | Input $2.50, Output $15.00 | Supports `none/low/medium/high/xhigh`, default `none` | Strong coding/analysis with tighter budget |
| GPT-5.4 mini (`gpt-5.4-mini`) | High-throughput mini model with strong practical capability | 400,000 | 128,000 | Input $0.75, Output $4.50 | Supports `none/low/medium/high/xhigh`, default `none` | Production chat, subagents, tooling-heavy workloads at scale |
| GPT-5.4 nano (`gpt-5.4-nano`) | Cheapest GPT-5.4-class option focused on speed/cost | 400,000 | 128,000 | Input $0.20, Output $1.25 | Supports `none/low/medium/high/xhigh`, default `none` | Classification, extraction, ranking, lightweight automation |

Extra details that often affect cost planning:

- For long-context GPT-5.5 and GPT-5.4 sessions, very large prompts (official docs mention >272K input tokens) can trigger higher session pricing multipliers.
- `mini` and `nano` are usually the first choice for high QPS workloads; escalate only failed/complex requests to `gpt-5.4` or `gpt-5.5`.
- Tool support differs by tier in some cases (for example, official docs show stronger computer-use/tool-search support on `gpt-5.4 mini` than `gpt-5.4 nano`).

### Simple routing strategy for GPT-5 family

1. Start with `gpt-5.4-nano` for deterministic short tasks (extract/classify/rank).
2. Use `gpt-5.4-mini` as default for general product traffic.
3. Escalate to `gpt-5.4` when quality thresholds fail.
4. Reserve `gpt-5.5` for hardest reasoning/coding or premium tiers.
5. For difficult samples, increase `reasoning.effort` before switching model class.

### Parallel track: reasoning-focused models

In OpenAI product positioning, some newer models focus more on reasoning depth via additional inference-time compute.

Typical value:

- Better performance on difficult math, logic, planning, and coding decomposition tasks.
- More robust performance on multi-step tool usage in difficult workflows.

Typical trade-off:

- Higher latency and cost per hard query compared with mini/fast models.

## Practical Performance Differences by Generation

Instead of only asking "which model is newer", use the matrix below to compare behavior in real systems.

| Dimension | GPT-3.5-like baseline | GPT-4 generation | Newer GPT (for example GPT-5.x) and reasoning-focused generation |
|---|---|---|---|
| Complex reasoning | Basic to moderate | Strong | Stronger on difficult multi-step tasks |
| Instruction following | Good on simple prompts | More stable | Highest stability in constrained tasks |
| Coding quality | Useful for snippets | Better architecture-level output | Better repo-scale and agentic coding patterns |
| Long context | Limited to moderate | Larger windows in later variants | Best long-context behavior in newer lines |
| Multimodal understanding | Limited/none in early text-only models | Introduced and improved | More mature multimodal execution |
| Latency and cost | Best efficiency | Higher quality but pricier | Split by model tier (mini vs full vs reasoning) |
| Tool use / function calling | Basic | Better | More reliable in complex tool chains |

## Evaluation Matrix: What to Measure in Production

OpenAI official guidance consistently emphasizes evaluation, not just intuition. Build a scorecard that combines benchmark-style and business-style metrics.

### 1. Capability benchmarks (public/common)

- Knowledge and reasoning: MMLU, GPQA-style difficult QA sets.
- Math and logic: MATH, GSM8K-style tasks.
- Coding: HumanEval, MBPP, SWE-bench style end-to-end fix tasks.
- Multimodal: MMMU and related image-text understanding benchmarks.

### 2. Task-level product metrics (your own eval set)

- Correctness: exact match, factual consistency, schema validity.
- Instruction adherence: format compliance, policy compliance.
- Tool success: function-call accuracy, retry count, final task completion rate.
- User value: acceptance rate, edit distance from desired output, human preference wins.

### 3. System metrics

- P50/P95 latency.
- Cost per successful task.
- Throughput under concurrency.
- Failure rate and fallback frequency.

### 4. Safety and reliability metrics

- Harmful output refusal quality.
- Hallucination rate on high-risk prompts.
- Prompt-injection resistance for retrieval/tool workflows.
- Stability across prompt/version updates.

## What Newer Models Commonly Add (Official High-Level View)

OpenAI does not publish every architecture detail for each model generation, but official docs and system cards generally point to these trends:

- Better post-training alignment (instruction tuning, preference optimization, safety tuning).
- Stronger tool-use training (function calling, multi-step task orchestration).
- Long-context improvements (training + inference optimizations for large-context retrieval and reasoning).
- Multimodal unification improvements (text + image + audio pipelines becoming more practical).
- Better reliability-focused training and eval loops (more adversarial and policy-focused testing).
- In reasoning-focused lines, more deliberate inference-time reasoning for difficult tasks.

## Model Selection Playbook (Simple and Effective)

1. Start from task type, not model hype.
2. Build a 100-300 sample eval set from real user inputs.
3. Compare at least one mini model and one stronger model.
4. Score quality, latency, and cost in the same table.
5. Pick the cheapest model that meets your quality threshold.
6. Keep a fallback model for high-stakes or failed cases.

## Minimal Python Pattern

```python
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-5.4-mini",
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
5. Add an evaluation script that records correctness, latency, and cost for each model.

## Official Evals Workflow Note

- OpenAI documentation emphasizes iterative evaluation as a core production practice.
- Official eval flow is: define task -> run on representative data -> analyze results -> iterate.
- In current official docs, the legacy Evals platform is being phased out; for new workflows, start with Datasets and newer evaluation guidance pages.
- Keep your own golden test set and rerun it for every prompt/model upgrade to prevent regressions.

## Responsible AI Quick Notes (AI-901 high-frequency topic)

When designing AI applications, use these six principles as a practical checklist:

1. Fairness
    Ensure outputs do not systematically disadvantage specific user groups.
2. Reliability and Safety
    Verify model behavior across normal and edge cases, and define safe fallbacks.
3. Privacy and Security
    Protect sensitive data, minimize retention, and use least-privilege access.
4. Inclusiveness
    Design for diverse users, languages, and accessibility needs.
5. Transparency
    Make it clear when AI is used and communicate capability limits.
6. Accountability
    Assign ownership for model behavior, incidents, and policy compliance.

In practice, connect these principles to your eval matrix: quality metrics, safety checks, latency/cost, and release gates.

## AI-901 Module Deep Dive (Text and Strategy)

### 1. Anomaly Detector

What it is:

- A time-series anomaly service for detecting unusual behavior in numeric sequences.
- Supports both univariate and multivariate anomaly detection patterns.

When it fits:

- Monitoring telemetry such as traffic, latency, CPU, sensor streams, and financial trend breaks.
- Early warning scenarios where precision and alert fatigue must be balanced.

Important lifecycle note:

- Microsoft Learn currently states that creating new Anomaly Detector resources is no longer available and service retirement is scheduled. Treat this module as a concept target for exam readiness and a migration-planning topic for real projects.

Practical design considerations:

- Seasonality and trend handling strongly affect false positives.
- Missing data and irregular sampling require preprocessing.
- Alerting should include confidence thresholds and suppression windows.

### 2. Language Understanding (LUIS)

What it is:

- A classic NLU service centered on intent detection and entity extraction.
- Key design objects include intents, entities, utterances, and phrase features.

Why it matters:

- AI-901 questions often test intent-vs-entity thinking in conversational workflows.
- It helps you reason about deterministic NLU pipelines before jumping to fully generative chat.

Important lifecycle note:

- The current LUIS documentation appears in previous-versions/archive context. For new production builds, treat LUIS primarily as a foundational concept and evaluate current Azure Language and Foundry options.

### 3. NLP Technology Choices (Architecture-level)

A common exam pitfall is mixing up NLP tasks and language model tasks.

Use classical NLP when you need:

- Structured outputs (labels, entities, sentiment scores, key phrases).
- Deterministic behavior and easier auditability.
- Lower cost for narrow tasks.

Use generative language models when you need:

- Open-ended generation, summarization, rewriting, or complex Q and A.
- Rich context handling across heterogeneous inputs.
- Agentic workflows with tool orchestration.

Use a hybrid approach when possible:

- Run NLP extraction first, then feed structured signals into a model for reasoning or report generation.

### 4. Azure Machine Learning (AML)

What it is:

- A platform for full ML lifecycle management: data prep, training, deployment, endpoints, and MLOps governance.

When to choose AML instead of prebuilt AI services:

- You need custom model training on domain-specific data.
- You need strict MLOps controls (experiment tracking, model registry, rollout policies).
- You need custom performance tuning beyond managed API defaults.

When prebuilt AI services are better:

- You need fast time-to-value with minimal infrastructure operations.
- The task matches available built-in capabilities.

Quick selection matrix:

| Requirement | Prefer prebuilt AI service | Prefer Azure Machine Learning |
|---|---|---|
| Fastest delivery | Yes | No |
| Custom training on proprietary data | Limited | Yes |
| Deep MLOps and lifecycle control | Limited | Yes |
| Low ops overhead | Yes | No |

## Official References (Must-Check Before Shipping)

## Official References (Must-Check Before Shipping)

- https://developers.openai.com/api/docs
- https://developers.openai.com/api/docs/models
- https://developers.openai.com/api/docs/pricing
- https://cookbook.openai.com/
- https://openai.com/research and model/system-card release pages
