---
id: concurrency-deadlock-detect-vs-prevent
node: concurrency.hazards
type: qa
---
## Q
Asked to "make sure this can't deadlock" in a coding round: what do you build, and what belongs to detection instead?

## A
**Prevent by construction** — that's what's gradable in an hour:

- One global lock order, or better, **one lock** for a small design (say out loud that you chose coarse-grained for correctness first).
- `tryLock(timeout)` + release-all + jittered retry where ordering is impossible — breaks hold-and-wait, but you must handle the failure path.
- **Never call an alien/callback method while holding a lock** (listeners, comparators, user strategies) — you can't know what it locks, so ordering is unprovable.

**Detection** is a production/runtime tool, not a design: a wait-for-graph cycle check, `jstack`/`ThreadMXBean.findDeadlockedThreads`, watchdog timeouts. Mention it as diagnosis and recovery (kill/restart a victim), then go back to prevention.
