---
id: ai-tokens-as-units
node: ai.foundations
type: qa
---
## Q
LLM pricing, rate limits, and context limits are all denominated in "tokens", not characters or words. What is a token, and what should a backend engineer assume when sizing requests?

## A
A **token** is a chunk of text (~3–4 English characters, ~0.75 words) from a fixed vocabulary the model was trained on; a tokenizer deterministically splits any string into them.

Sizing rules of thumb:
- English prose ≈ **4 chars/token**; code, JSON, other languages, and rare strings (UUIDs, base64) tokenize **much worse** — sometimes 1 token per character.
- Character counts are a bad proxy — count tokens with the model's own tokenizer for quotas and truncation logic.
- Every quota that matters — cost, rate limit, context limit — is input tokens + output tokens.
