---
id: concurrency-data-race-definition
node: concurrency.model
type: cloze
---
A **data race** is two threads accessing the same memory location where {{c1::at least one access is a write}} and {{c2::no synchronization (happens-before edge) orders the accesses}}. Racy programs aren't just "sometimes wrong" — the compiler and CPU are free to {{c3::reorder and cache accesses}}, so behavior is undefined/arbitrary, not merely stale.
