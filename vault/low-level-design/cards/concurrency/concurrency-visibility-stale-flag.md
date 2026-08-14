---
id: concurrency-visibility-stale-flag
node: concurrency.model
type: qa
---
## Q
Thread A sets `running = false`, but the worker looping on `while (running) {}` never stops — no crash, no exception. Why can this happen, and what are two fixes?

## A
There is **no happens-before edge** between the write and the reads: the write can sit in a store buffer, and the JIT may hoist the read out of the loop entirely (it "proves" `running` never changes on this thread).

- Fix 1: declare the flag `volatile` / atomic — every read sees the latest write.
- Fix 2: read and write it under the **same lock** (lock release → lock acquire creates the ordering).

Key point: this is a **visibility** bug, not an atomicity bug — the write happened, it just isn't guaranteed to be seen.
