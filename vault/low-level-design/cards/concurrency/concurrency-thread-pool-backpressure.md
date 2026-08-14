---
id: concurrency-thread-pool-backpressure
node: concurrency.patterns
type: qa
---
## Q
A fixed thread pool fed by an **unbounded** task queue never rejects work. What actually fails under sustained overload, and what's the disciplined setup?

## A
Nothing rejects, so nothing pushes back: the queue grows without limit — latency climbs (tasks wait behind thousands of others) and the process eventually **OOMs**. The failure is *hidden* until it's catastrophic.

- Disciplined: **bounded queue + explicit rejection policy**. `CallerRuns` is the classic backpressure choice — the submitter executes the task itself, naturally slowing producers.
- Size CPU-bound pools ≈ number of cores; IO-bound pools larger (≈ cores × (1 + wait/compute)).

Rule: overload must surface at the boundary, not accumulate in memory.
