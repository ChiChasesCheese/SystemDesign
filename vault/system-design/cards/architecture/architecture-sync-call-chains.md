---
id: architecture-sync-call-chains
node: architecture.services
type: qa
---
## Q
A request fans through a synchronous chain of 5 services. What does the chain do to availability and latency, and what are the three escapes?

## A
Every synchronous hop is a **serial hard dependency**: availabilities multiply (five 99.9% hops ≈ 99.5% — from 43 min to 3.6 h of monthly downtime, [[reliability-serial-parallel-composition]]), latencies add, tail latencies compound (the chain is as slow as its worst hop per request), and each hop needs its own timeout/retry budget.

Escapes:

- **Collapse boundaries**: if two services always call each other synchronously, they're probably one service.
- **Go async** where the caller doesn't need the answer now (queue/event instead of RPC).
- **Cache / replicate the needed data locally** so the hop disappears from the request path.

Chain depth is an architecture review metric, not an accident.
