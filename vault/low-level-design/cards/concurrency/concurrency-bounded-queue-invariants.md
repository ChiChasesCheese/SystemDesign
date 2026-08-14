---
id: concurrency-bounded-queue-invariants
node: concurrency.patterns
type: qa
---
## Q
You're asked to write a bounded blocking queue from scratch. State the two blocking invariants and sketch `put`/`take` with one lock and two conditions.

## A
Invariants: `put` **waits while full**, `take` **waits while empty**; after mutating, each signals the *opposite* waiters.

```java
final ReentrantLock lock = new ReentrantLock();
final Condition notFull = lock.newCondition(), notEmpty = lock.newCondition();

void put(T x) { lock.lock(); try {
    while (count == capacity) notFull.await();
    enqueue(x); notEmpty.signal();
} finally { lock.unlock(); } }

T take() { lock.lock(); try {
    while (count == 0) notEmpty.await();
    T x = dequeue(); notFull.signal(); return x;
} finally { lock.unlock(); } }
```

Every wait is a `while` loop; unlock in `finally`.
