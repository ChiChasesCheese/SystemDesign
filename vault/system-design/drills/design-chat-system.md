---
nodes: [networking.realtime, networking.protocols, async.delivery.guarantees, storage.nosql, distributed.time]
tags: [classic, flagship]
---
# Drill: Design a chat system

One-to-one and group messaging with delivery receipts, presence, and
history. The interesting half is not the socket — it is what happens to a
message when the recipient's phone is in a tunnel.

**Constraints to state and honor**
- 50M concurrent connections; a message delivered to an online recipient in under 500 ms.
- Groups up to 1000 members; history is permanent and searchable by conversation.
- Offline recipients get the message when they return, exactly once as far as the user can tell.
- Messages within a conversation must appear in the same order for everyone in it.

**Grading points**
- Transport chosen with its costs: WebSocket for bidirectional, SSE where the flow is one-way, long-polling only as a fallback ([[networking-realtime-transport-choice]], [[networking-sse-mechanics]], [[networking-long-polling-costs]]).
- The memory and connection budget for 50M sockets, and what the gateway layer holds per connection ([[networking-websocket-scaling-cost]], [[networking-connection-setup-cost]]).
- Heartbeats and idle timeouts, and how a half-open connection is detected rather than assumed ([[networking-heartbeats-idle-timeouts]], [[distributed-failure-detection]]).
- At-least-once transport plus a client-side dedup key, with "exactly once" named as an end-to-end property rather than a transport feature ([[async-delivery-semantics-cloze]], [[async-exactly-once-myth]], [[async-redelivery-causes]]).
- Per-conversation ordering from a sequence assigned by one owner of that conversation — not from client wall clocks ([[distributed-lww-danger]], [[distributed-lamport-vs-vector]], [[distributed-monotonic-vs-wallclock]]).
- History stored partitioned by conversation and ordered by sequence, with pagination that does not deep-scan ([[storage-wide-column-modeling]], [[storage-search-deep-pagination]]).
- Backpressure toward a slow client: bounded per-connection buffers, and the drop-or-disconnect policy stated ([[networking-realtime-backpressure]]).
- Group fanout costed at 1000 members, and the decision to fan out at delivery rather than store 1000 copies ([[foundations-fanout-estimation]]).

**Attempt log**
- [ ] Attempt 1 (date, 40 min, self-graded notes):
