---
nodes: [distributed.crdt, distributed.consistency, storage.encoding, networking.realtime]
tags: [flagship, distributed]
---
# Drill: Design a collaborative document editor

Several people typing in the same document, on flaky connections, some
offline for an hour on a plane. Everyone must end up with the same
document, and nobody's paragraph may vanish.

**Constraints to state and honor**
- Edits appear to collaborators within 200 ms while online.
- An offline client can edit for hours and must merge on reconnect without a conflict dialog.
- The document is permanent and must be loadable years later, by a client version that does not exist yet.
- Presence (cursors, selections) is live but disposable.

**Grading points**
- Convergence stated as the actual requirement, and the two families that deliver it — OT with a server authority, or CRDTs — compared rather than name-dropped ([[distributed-crdt-convergence]], [[distributed-crdt-state-vs-op]]).
- A sequence CRDT's identity scheme explained well enough to say why concurrent inserts at one position do not collide ([[distributed-or-set]], [[distributed-crdt-counters]]).
- The limits admitted: CRDTs give convergence, not intent preservation, and metadata grows ([[distributed-local-first-limits]], [[distributed-crdt-convergence]]).
- Causal consistency identified as the model that matters here, and why linearizability is neither needed nor affordable ([[distributed-causal-vs-eventual]], [[distributed-linearizability-when-needed]], [[distributed-linearizability-composability]]).
- Offline editing framed as the multi-leader case it is, with wall-clock last-write-wins rejected explicitly ([[distributed-offline-client-writes]], [[distributed-lww-danger]], [[distributed-lamport-vs-vector]]).
- The wire and storage format versioned for forward and backward compatibility, since old clients will read new documents ([[storage-encoding-compat-directions]], [[storage-rolling-upgrade-compat]], [[storage-protobuf-tag-rules]]).
- Snapshot plus operation log for load time, with compaction of the op history and what compaction may not discard ([[async-log-compaction]], [[storage-avro-schema-resolution]]).
- Presence carried on a separate, lossy channel with its own backpressure — cursors are not document state ([[networking-realtime-backpressure]], [[networking-realtime-transport-choice]]).

**Attempt log**
- [ ] Attempt 1 (date, 45 min, self-graded notes):
