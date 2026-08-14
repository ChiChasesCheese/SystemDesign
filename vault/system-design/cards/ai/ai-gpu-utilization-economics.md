---
id: ai-gpu-utilization-economics
node: ai.inference
type: qa
---
## Q
`nvidia-smi` shows 100% GPU utilization but your cost per million tokens is 5x the competition. Why is that metric a lie, and what do you measure instead?

## A
`nvidia-smi` utilization = "a kernel was running" — a GPU stalled on memory reads counts as busy. Decode-heavy serving at small batch can show 100% while using **<10% of peak FLOPs** (it's bandwidth-bound, [[ai-prefill-vs-decode]]).

Measure economics directly:

- **Throughput per GPU**: tokens/sec/GPU → **$ per million tokens** (the number to benchmark against API pricing).
- **MFU** (model FLOPs utilization): useful-FLOPs ÷ peak — reveals headroom.
- **Goodput**: throughput *while meeting the latency SLO* — the real capacity-planning metric, since batch size trades inter-token latency for cheaper tokens ([[ai-continuous-batching]]).

Lever hierarchy: fill batches (utilization is a traffic problem before a kernel problem), then quantize, then optimize kernels.
