---
id: traffic-request-hedging
node: traffic.load-balancing
type: qa
---
## Q
Request hedging: mechanism, the cost math that makes it cheap, and its prerequisites?

## A
If no reply arrives within roughly the **p95 latency**, send the same request to a second replica; take whichever answers first and cancel the other. The user's tail becomes the *min* of two draws — tail events (GC pause, slow disk) rarely strike both replicas.

Cost math: hedging only after p95 means ≤5% of requests are duplicated — ~5% extra load buys an order-of-magnitude better p99.

Prerequisites: idempotent (or deduplicated) operations, cross-replica cancellation, and never hedging a hedge — otherwise overload turns it into a self-amplifying storm.
