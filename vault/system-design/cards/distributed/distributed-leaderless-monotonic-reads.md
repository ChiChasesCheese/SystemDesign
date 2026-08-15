---
id: distributed-leaderless-monotonic-reads
node: distributed.replication.leaderless
type: qa
---
## Q
In a Dynamo-style store with W=2, R=2, N=3, a client reads a value and then reads it again and gets an *older* value. Explain how, and why the leader-based fix doesn't apply.

## A
A write reaches replicas one at a time. Read 1's coordinator happened to contact `{A, B}` where A had the new value; read 2's coordinator contacted `{B, C}` — neither of which was updated yet — so it legally returns the old one. Both quorums were valid; quorum overlap guarantees you *can* see the latest acknowledged write, not that you **stop** seeing it. That's a **monotonic reads** violation.

The leader-based fix — pin the session to one replica — doesn't work here because there is no fixed replica per key: **a different coordinator picks a different subset each request**, and any node can coordinate. Leaderless fixes instead:

- Have the client carry the **highest version it has seen** and reject/retry a quorum result older than it.
- Turn on **synchronous read repair** so a read that observes the new value pushes it to a write quorum before returning.
