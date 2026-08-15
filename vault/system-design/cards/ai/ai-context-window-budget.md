---
id: ai-context-window-budget
node: ai.foundations
type: qa
---
## Q
Why should you treat an LLM's context window as a fixed resource budget rather than "room for everything", and who competes for it?

## A
The context window is a hard cap on **input + output tokens per request**, and four things compete for it: the system prompt, conversation history, injected documents (RAG), and the space reserved for the answer.

Treat it like a memory budget because:
- Overflow means **truncation** — something silently drops, usually oldest history.
- Cost and prefill latency scale with tokens sent, so "stuff everything in" is paying per request for data the model may ignore.
- Effective use degrades before the hard limit — models attend best to the **start and end** of long contexts ("lost in the middle"), so placement of critical facts matters.
