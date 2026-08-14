---
id: distributed-raft-linearizable-reads
node: distributed.consensus
type: qa
---
## Q
Why can't a Raft leader serve linearizable reads from its local state without extra work, and what are the two standard fixes?

## A
The leader may be **deposed and not know it** (partitioned away, long GC pause): a new leader is already committing writes elsewhere, so the old one's local read returns stale data as authoritative — a phantom-leader read.

- **Read index**: leader records its current commit index, **confirms leadership with a heartbeat round to a majority**, waits until its state machine has applied up to that index, then serves the read. Linearizable, costs one quorum round-trip per read batch.
- **Lease reads**: after a successful heartbeat, the leader assumes leadership for ~an election timeout and serves reads locally within that window. Nearly free, but safety now depends on **bounded clock drift** across nodes — a fast clock lets a deposed leader serve stale reads.

etcd exposes exactly this choice (linearizable vs serializable reads).
