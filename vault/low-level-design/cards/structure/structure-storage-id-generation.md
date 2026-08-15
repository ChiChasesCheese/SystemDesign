---
id: structure-storage-id-generation
node: structure.storage
type: cloze
---
Id generation in an in-memory store: `nextId++` on a plain `long` is a {{c1::lost-update race (read-modify-write is not atomic)}} under concurrency — use {{c2::`AtomicLong.incrementAndGet()`}} for compact, ordered ids. Prefer {{c3::UUIDs}} when ids must be generated **without coordination** (multiple instances, client-side creation), accepting that they're unordered and bulky. Never derive the id from mutable business fields — it must stay stable while everything else changes.
