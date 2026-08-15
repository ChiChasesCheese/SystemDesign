---
id: concurrency-lock-free-trap
node: concurrency.hazards
type: qa
---
## Q
A candidate says "I'll make it lock-free, so no deadlock." Why is this usually the wrong move in an LLD round?

## A
Lock-free removes deadlock but not the hazards that actually bite:

- **CAS covers one word.** Any invariant spanning two fields (`balance` *and* `ledger`) can't be maintained by a CAS loop — you get torn, individually-atomic updates.
- **Livelock/starvation remain**: under contention, CAS retry loops burn CPU and a slow thread can retry forever (lock-*free* guarantees system progress, not per-thread progress; that's wait-free).
- Plus ABA and memory reclamation, and code no reviewer can verify in an hour.

Right answer: use lock-free **components** others wrote — `AtomicLong` counters, `ConcurrentHashMap`, `LongAdder` — and a plain lock for your own multi-field invariants. If contention is the concern, shrink the critical section or shard the lock before going lock-free.
