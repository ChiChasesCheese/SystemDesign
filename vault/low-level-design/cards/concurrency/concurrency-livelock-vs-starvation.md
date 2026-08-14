---
id: concurrency-livelock-vs-starvation
node: concurrency.hazards
type: qa
---
## Q
Deadlock, livelock, starvation: distinguish them by what the threads are doing and name the characteristic fix for livelock.

## A
- **Deadlock**: threads blocked forever, consuming no CPU; state never changes.
- **Livelock**: threads actively running and *changing state* but making no progress — e.g. both detect conflict, both back off, both retry in lockstep (the corridor dance). Fix: **randomized backoff/jitter** so retries desynchronize.
- **Starvation**: the system progresses, but *some* thread never gets the resource — unfair locks, reader floods starving writers, priority inversion. Fix: fair queuing / bounded waiting.

Discriminator: check CPU + state changes. Blocked & frozen = deadlock; busy & frozen = livelock; others progress while one lags = starvation.
