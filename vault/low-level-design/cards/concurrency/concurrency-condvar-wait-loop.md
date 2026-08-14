---
id: concurrency-condvar-wait-loop
node: concurrency.primitives
type: qa
---
## Q
Why must a condition-variable wait always be
```java
while (queue.isEmpty()) { notEmpty.await(); }
```
and never `if (queue.isEmpty()) notEmpty.await();`? Two reasons.

## A
- **Spurious wakeups**: the platform may wake a waiter with no signal at all — permitted by POSIX and the JVM.
- **The predicate can be false again by the time you run**: between the signal and reacquiring the lock, another woken (or barging) thread may have consumed the item. `signalAll` deliberately wakes many threads that must re-check.

The loop re-tests the predicate *while holding the lock*, so you only proceed when the condition truly holds. Rule: wait is always inside a loop guarding the predicate.
