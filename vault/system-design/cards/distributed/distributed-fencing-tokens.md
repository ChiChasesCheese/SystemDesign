---
id: distributed-fencing-tokens
node: distributed.consensus
type: qa
---
## Q
A client holds a distributed-lock lease, pauses for a 20s GC, then resumes and writes — but its lease expired and another client took the lock. How do fencing tokens prevent the corruption, and why can't the client fix this itself?

## A
The lock service issues a **monotonically increasing token** with every lock grant. The *protected resource* (storage) records the highest token it has seen and **rejects writes carrying a lower token** — so the paused client's stale-token write bounces.

The client can't fix it alone: it cannot atomically "check lease still valid, then write" — arbitrary pauses (GC, page fault, network delay) can strike **between** the check and the write. Safety must be enforced at the resource. Corollary: a lock/lease without downstream fencing checks is only advisory, never a safety mechanism.
