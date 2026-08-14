---
id: distributed-failure-detection
node: distributed.time
type: qa
---
## Q
Why can no timeout prove a remote node is dead, and how do real systems pick and use timeouts anyway?

## A
In an asynchronous network you can't distinguish **crashed** from **slow / partitioned / GC-paused**: no reply within T is consistent with all of them, and the node may resume and keep acting (why fencing exists).

Practice:
- Pick T from **observed latency distributions** (e.g. p999 × margin), not a folklore constant; adaptive detectors like **phi-accrual** (Cassandra/Akka) output a suspicion level from the heartbeat history instead of a binary verdict.
- Make the *reaction* safe rather than the detection perfect: quorum-agreed membership, leases that must expire before takeover, fencing on the resource.

Trade-off to state: short timeout = fast failover but false positives (flapping, duplicate leaders' work); long timeout = slow recovery.
