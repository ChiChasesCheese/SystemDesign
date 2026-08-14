---
id: storage-btree-wal-recovery
node: storage.internals
type: qa
---
## Q
B-trees write pages in place. Why does that force a write-ahead log, and what is the torn-page problem?

## A
In-place page writes aren't atomic: crash mid-write and the tree is inconsistent — worse, a page split touches **multiple pages**, so a crash between them can orphan data. So every modification is first appended to the **WAL** (sequential, fsynced); on recovery the engine replays the log to restore consistency. Every committed write is therefore written **twice** (WAL + page).

**Torn page**: a 8KB page over 4KB disk sectors can be half-old/half-new after a crash — corrupt in a way replay alone can't fix. Postgres counters with **full-page writes** (first touch after each checkpoint logs the entire page image); MySQL uses a doublewrite buffer.
