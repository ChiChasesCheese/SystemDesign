---
nodes: [distributed.replication.leaderless, distributed.consistency, distributed.cap, distributed.partitioning.rebalancing, storage.object]
tags: [flagship, distributed]
---
# Drill: Design a replicated key-value store

Build the storage layer itself: a Dynamo-style key-value store across
three availability zones, tunable per request. This is the drill that
forces you to say what your consistency words actually mean.

**Constraints to state and honor**
- Values up to 1 MB; single-key operations only, no cross-key transactions.
- Writes must succeed while one zone is unreachable.
- Callers choose durability and staleness per request (N, W, R), and need to be told what each choice buys.
- Nodes join and leave weekly; capacity must rebalance without a maintenance window.

**Grading points**
- The CAP claim made precisely — a choice that only bites during a partition, and per operation rather than per system ([[distributed-cap-real-claim]], [[distributed-cap-per-operation]], [[distributed-pacelc]]).
- Quorum arithmetic derived, and the crucial follow-up: W + R > N still is not linearizable ([[distributed-quorum-math]], [[distributed-quorum-not-linearizable]]).
- Read repair and anti-entropy as separate mechanisms with different costs and latencies ([[distributed-read-repair-anti-entropy]], [[distributed-anti-entropy-cost]]).
- Sloppy quorums and hinted handoff explained together with what they give up ([[distributed-sloppy-quorum-handoff]], [[distributed-leaderless-monotonic-reads]]).
- Conflicts resolved by version vectors and siblings, with last-write-wins named as data loss rather than a policy ([[distributed-conflict-detection-siblings]], [[distributed-lww-danger]]).
- The consistency the API advertises stated in model terms — what read-your-writes requires from the client ([[distributed-read-your-writes]], [[distributed-causal-vs-eventual]], [[distributed-linearizability-when-needed]]).
- Consistent hashing with virtual nodes, and the count chosen for a reason ([[distributed-consistent-hashing]], [[distributed-vnode-count]]).
- Rebalancing that moves a fraction of the keyspace, throttled against foreground traffic ([[distributed-rebalancing]], [[distributed-rebalance-throttling]], [[distributed-fixed-partition-count]]).
- Large values pushed to an object layer with metadata in the store, and the reason ([[storage-object-vs-filesystem]], [[storage-compute-separation]]).

**Attempt log**
- [ ] Attempt 1 (date, 45 min, self-graded notes):
