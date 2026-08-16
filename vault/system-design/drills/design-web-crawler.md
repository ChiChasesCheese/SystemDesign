---
nodes: [async.queues, storage.object, traffic.rate-limiting, distributed.partitioning.rebalancing, analytics.batch]
tags: [classic]
---
# Drill: Design a web crawler

Crawl a billion pages a month, politely, and hand the content to an
indexing pipeline. A queue, a fetcher, and a store — and every hard part
is in the words "politely" and "again next month".

**Constraints to state and honor**
- 1B pages/month sustained; average page 500 KB raw.
- No more than one request per second to any single host, robots.txt honored, regardless of how many workers exist.
- The crawl must survive worker loss and worker addition without re-crawling everything.
- Recrawl frequency varies by page: news hourly, an archived PDF yearly.

**Grading points**
- The frontier as a queue with per-host sub-queues, so politeness is a property of the data structure rather than a hope ([[async-queue-vs-pubsub]], [[traffic-rate-limit-key-choice]]).
- Host-level rate limiting that holds globally across workers, with the accuracy-versus-chatter trade named ([[traffic-token-bucket-vs-sliding-window]], [[traffic-distributed-rate-limiting]]).
- Hosts assigned to workers by consistent hashing so a worker joining moves a fraction of the frontier, not all of it ([[distributed-consistent-hashing]], [[distributed-rebalancing]], [[distributed-request-routing]]).
- Rebalancing throttled so a deploy does not become a self-inflicted outage ([[distributed-rebalance-throttling]], [[distributed-fixed-partition-count]]).
- Raw pages in object storage with the small-object economics acknowledged — batching or packing rather than a billion 500 KB PUTs ([[storage-object-vs-filesystem]], [[storage-small-objects-cost]], [[storage-s3-numbers]]).
- URL dedup and content dedup separated: a seen-set for links, a content hash for mirrored pages.
- Poison pages (redirect loops, 50 MB responses, tarpits) sent to a dead-letter path with a retry policy that backs off ([[async-dlq-poison-pill]], [[async-retry-delay-implementation]]).
- Recrawl scheduling as a batch job over the frontier, made safe to re-run ([[analytics-batch-vs-stream]], [[analytics-idempotent-reruns]], [[analytics-skew-stragglers]]).

**Attempt log**
- [ ] Attempt 1 (date, 40 min, self-graded notes):
