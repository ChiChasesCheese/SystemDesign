---
id: distributed-epoch-numbers
node: distributed.consensus
type: qa
---
## Q
Every consensus protocol carries an epoch number (term/ballot/view) and runs two quorum checks. What problem do epochs solve, and how do the two quorums interact?

## A
Epochs solve "**which of two would-be leaders is current**" without relying on clocks: within one epoch there is at most one leader, and a **higher epoch always defeats a lower one**.

- **Quorum 1 — election**: a candidate collects majority votes for its epoch.
- **Quorum 2 — commit**: the leader gets majority acknowledgment for each value it proposes.

The safety trick is that the two quorums **must intersect**: if a new leader was elected, every commit quorum of the old leader contains at least one node that has seen the higher epoch and therefore **rejects the old leader's proposals**. So a deposed leader can't commit anything behind the new leader's back — the generic mechanism behind Raft terms, Paxos ballots, and Viewstamped Replication views ([[distributed-raft-guarantees]] is the Raft instantiation).
