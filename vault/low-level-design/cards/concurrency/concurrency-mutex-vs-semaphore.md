---
id: concurrency-mutex-vs-semaphore
node: concurrency.primitives
type: qa
---
## Q
A binary semaphore and a mutex both admit one thread at a time. What's the real difference, and when do you reach for a semaphore?

## A
**Ownership.** A mutex must be released by the thread that locked it (enabling reentrancy and priority-inheritance); a semaphore's permit can be released by *any* thread.

- Reach for a **counting semaphore** to limit access to N identical resources (connection pool of 10, rate-limit concurrent downloads).
- Reach for a **binary semaphore** for cross-thread signaling: thread A `acquire`s, thread B `release`s to wake it — impossible with a mutex.
- Protecting shared mutable state = mutex; permits/signaling = semaphore.
