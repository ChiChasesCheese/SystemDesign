---
id: distributed-system-models
node: distributed.time
type: qa
---
## Q
Crash-stop vs crash-recovery vs Byzantine fault models — what does each assume, and which (plus which timing model) do mainstream datacenter systems design for?

## A
- **Crash-stop**: a faulty node halts and never returns — clean but unrealistic.
- **Crash-recovery**: nodes may crash and come back, keeping **stable storage** across the outage but losing memory — what Raft, Kafka, and databases actually assume.
- **Byzantine**: nodes may lie or act arbitrarily (bugs, compromise). Tolerating f liars needs **3f+1** nodes plus signed messages — the cost is why datacenter systems skip it and instead handle *weak* corruption with checksums, TLS, and input validation. BFT lives where participants distrust each other (blockchains, some aerospace).

Timing: **partial synchrony** — the network usually behaves, but delays are occasionally unbounded — which is why timeouts can trigger recovery but must never be the sole proof of death ([[distributed-failure-detection]]).
