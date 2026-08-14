---
id: distributed-linearizability-when-needed
node: distributed.consistency
type: qa
---
## Q
Which concrete features genuinely require linearizability (not just causal or session guarantees), and why?

## A
Anything where **two nodes agreeing on one current value** is the point:

- **Locks and leader election**: all nodes must agree who holds the lock — a stale view means two leaders.
- **Uniqueness constraints**: usernames, one-seat-one-buyer, balance-can't-go-negative — concurrent claims must serialize on a single answer (this is a compare-and-set).
- **Cross-channel dependencies**: service A writes storage then sends a message via a queue; the consumer's read must see the write, or it processes stale data — the side channel outruns replication.

Everything else (feeds, profiles, counters) usually needs only session/causal guarantees, which don't require coordination.
