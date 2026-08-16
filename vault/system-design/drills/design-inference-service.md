---
nodes: [ai.inference, ai.foundations, reliability.slo, traffic.load-balancing, infra.containers]
tags: [flagship, ai]
---
# Drill: Design an LLM inference service

Serve a large model to product teams behind one API: streaming responses,
a latency SLO, and a GPU fleet that costs more per hour than the team
running it. The question is capacity planning with unusual hardware.

**Constraints to state and honor**
- Mixed traffic: chat (short prompts, streamed output) and document summarization (30k-token prompts).
- p95 time-to-first-token under 500 ms for chat; total throughput matters more for summarization.
- GPUs are scarce and cannot be autoscaled in seconds.
- Tenants must not be able to starve each other with one enormous request.

**Grading points**
- Prefill and decode separated as the two phases with different bottlenecks — compute-bound versus memory-bandwidth-bound ([[ai-prefill-vs-decode]], [[ai-generation-loop]], [[ai-tokens-as-units]]).
- The KV cache sized in GB per concurrent request, and named as the real limit on batch size ([[ai-kv-cache]], [[ai-context-window-budget]]).
- Continuous batching explained as what turns idle decode steps into throughput, with its latency effect on a single request ([[ai-continuous-batching]]).
- Cost levers ranked honestly — batching, quantization, speculative decoding, a smaller model — with the quality cost of each ([[ai-inference-cost-levers]], [[ai-quantization-tradeoffs]], [[ai-speculative-decoding]]).
- Utilization economics stated: an idle GPU is the dominant cost, so queueing policy is a budget decision ([[ai-gpu-utilization-economics]]).
- Two SLOs defined rather than one, because time-to-first-token and tokens-per-second fail differently ([[reliability-latency-sli-form]], [[reliability-percentiles-over-averages]], [[reliability-burn-rate-alerting]]).
- Routing that respects the batch: least-outstanding-requests rather than round-robin, with session affinity for prefix reuse ([[traffic-lb-algorithm-choice]], [[traffic-l4-vs-l7]], [[traffic-bounded-load-consistent-hashing]]).
- Hedging rejected here, with the reason — a duplicate request costs a whole GPU slot ([[traffic-request-hedging]]).
- Long prompts isolated into their own queue or pool so one 30k-token job cannot hold the chat batch hostage ([[infra-requests-limits-noisy-neighbor]], [[traffic-rate-limit-key-choice]]).
- Model deployment treated as an infrastructure problem: image size, warm-up, and node pools that cannot be scaled from zero ([[infra-k8s-primitives]], [[infra-containers-vs-vms]], [[architecture-cold-starts]]).
- Guardrails and evals kept on the serving path, with their latency budgeted ([[ai-guardrails-validation]], [[ai-temperature-sampling]]).

**Attempt log**
- [ ] Attempt 1 (date, 45 min, self-graded notes):
