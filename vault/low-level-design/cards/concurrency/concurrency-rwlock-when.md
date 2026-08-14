---
id: concurrency-rwlock-when
node: concurrency.primitives
type: qa
---
## Q
When does replacing a mutex with a read-write lock make your code *slower*, and what failure mode does a naive reader-preferring RW lock add?

## A
- RW locks have **higher per-acquire overhead** (they track reader counts). With short critical sections or few concurrent readers, a plain mutex — or a concurrent data structure — wins.
- It only pays off when reads are **frequent and long** relative to writes.
- Reader-preference adds **writer starvation**: a continuous stream of readers keeps the write lock unavailable forever. Fair/writer-preferring modes fix this at the cost of read throughput.

Also: upgrading read → write while holding the read lock deadlocks in most implementations — release, reacquire, and re-validate instead.
