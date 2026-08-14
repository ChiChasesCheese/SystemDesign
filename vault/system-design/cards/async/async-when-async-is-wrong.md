---
id: async-when-async-is-wrong
node: async.queues
type: qa
---
## Q
Name three signals that making an operation asynchronous (via a queue) is the wrong call.

## A
- The caller **needs the result to proceed** (auth check, price quote, inventory reservation shown to the user) — you'd just rebuild synchronous RPC with extra latency and a callback.
- The operation must **fail visibly to the user** so they can correct input; a queued failure surfaces minutes later with no one watching.
- The workload is **low-volume and latency-sensitive** — the queue adds hops, ops burden, and delivery-semantics complexity with no smoothing benefit.

Async pays off for: bursty load, slow side effects, retryable work, fan-out.
