---
id: ai-guardrails-validation
node: ai.evals
type: qa
---
## Q
"Guardrails" around an LLM are best understood as which classic backend pattern, and what runs on each side of the model call?

## A
**Validation layers at a trust boundary** — the model is an untrusted component whose input and output both need checking.

- **Input side**: prompt-injection screening (user text and *retrieved documents* are attacker-controlled input), PII redaction, topic/policy filters.
- **Output side**: **schema validation** for structured output (parse-or-retry, the single highest-value guardrail), content/policy classifiers, groundedness checks against sources.

Design rules: run **deterministic checks first** (regex, JSON schema — free) and probabilistic ones (classifier or judge-model calls) after; they add latency, so run them **in parallel with streaming** or accept buffering the response. On failure: retry with the error fed back, fall back, or refuse — never ship unvalidated output downstream.
