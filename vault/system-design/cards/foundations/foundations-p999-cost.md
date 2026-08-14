---
id: foundations-p999-cost
node: foundations.numbers
type: qa
---
## Q
Why does each further latency nine (p99 → p999) cost disproportionately more to fix — and when is p999 still worth paying for?

## A
The extreme tail is dominated by effectively **random events** — GC pauses, page faults, TCP retransmits, context switches, background compactions — not your code path, so code optimization stops helping; you're buying overprovisioning, hedging, and isolation instead. Queueing compounds it: one slow request delays everything behind it on that worker.

Worth it when the tail hits the most valuable traffic (Amazon tracks p999 because the slowest requests correlate with the heaviest-data, highest-spend customers) or when fan-out amplifies the tail into the median — [[foundations-tail-latency-amplification]].
