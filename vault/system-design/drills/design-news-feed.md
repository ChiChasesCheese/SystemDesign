---
nodes: [foundations.tradeoffs, caching.invalidation, caching.strategies, distributed.partitioning.skew, async.queues, storage.nosql]
tags: [classic, flagship]
---
# Drill: Design a social news feed

The fanout question. Every candidate knows "push vs pull"; the ones who
pass can say what each costs at the numbers they just estimated, and what
they do about the account with 90 million followers.

**Constraints to state and honor**
- 300M daily actives, average 200 follows, feed opened ~10× a day.
- Feed load p99 under 200 ms; a new post should appear within seconds for most followers.
- Follower counts span six orders of magnitude — the mean is a lie here.
- Edits and deletes must propagate; a deleted post lingering in feeds is a headline.

**Grading points**
- Fanout-on-write vs fanout-on-read stated as a write-amplification-versus-read-latency trade, with the arithmetic for both ([[foundations-fanout-estimation]], [[foundations-latency-vs-throughput]]).
- The hybrid: precompute for ordinary accounts, merge-on-read for the heavy tail — and the threshold justified by data, not taste ([[distributed-hot-key]], [[distributed-hot-key-detection]]).
- Celebrity fanout treated as access skew, with the cost of salting or replicating the hot timeline named ([[distributed-data-skew-vs-access-skew]], [[distributed-salting-read-cost]]).
- Fanout done asynchronously through a queue, with backpressure and what happens when the consumer falls an hour behind ([[async-queue-backpressure]], [[async-queue-vs-pubsub]], [[async-competing-consumers-ordering]]).
- Timeline storage modelled by access pattern — one partition per user, time-ordered, bounded length ([[storage-wide-column-modeling]], [[storage-secondary-index-partitioning]]).
- Invalidation on edit and delete: delete the key rather than update it, and version the feed key so a partial fanout cannot resurrect a post ([[caching-delete-not-update]], [[caching-key-version-invalidation]]).
- Warming and TTL jitter for the cache, so a redeploy does not stampede the timeline service ([[caching-cache-warming]], [[caching-ttl-jitter]]).
- The consistency you are choosing: a feed is allowed to be stale, a block list is not ([[foundations-availability-vs-consistency-axis]]).

**Attempt log**
- [ ] Attempt 1 (date, 40 min, self-graded notes):
