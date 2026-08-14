---
id: ai-kv-cache
node: ai.inference
type: qa
---
## Q
What does the KV cache store, why is it the scarce resource in LLM serving, and what does prefix caching exploit?

## A
Per sequence, the attention **keys and values of every previous token**, so each new token attends without recomputing the past. It grows linearly with context length and concurrent sequences, and it competes with model weights for GPU memory — KV capacity, not compute, usually caps batch size (hence paged attention, which allocates it in blocks like virtual memory).

**Prefix caching**: sequences sharing a prefix (system prompt, few-shot examples, chat history) reuse one copy of that prefix's KV, skipping its prefill — large TTFT and cost wins for agent/chat workloads, and the mechanism behind API-level prompt caching discounts.
