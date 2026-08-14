---
id: storage-lsm-read-path
node: storage.internals
type: qa
---
## Q
Walk the read path for a point lookup in an LSM-tree, and name the structure that keeps misses cheap.

## A
1. Check the **memtable** (in-memory, newest data).
2. Check immutable memtables awaiting flush.
3. Check SSTables newest-to-oldest, level by level; first hit wins (newer versions shadow older).

**Bloom filters** (one per SSTable) keep this cheap: they answer "definitely not here" with no I/O, so a lookup skips most files and misses don't touch disk ~99% of the time. Without them, every miss would read every level.
