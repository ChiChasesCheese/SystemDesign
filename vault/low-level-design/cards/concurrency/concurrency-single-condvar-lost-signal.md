---
id: concurrency-single-condvar-lost-signal
node: concurrency.patterns
type: qa
---
## Q
Your bounded queue uses **one** condition variable for producers and consumers and wakes with single `signal()`. Tests pass, but under load all threads eventually park forever. Why?

## A
The signal can be **delivered to the wrong class of waiter**. A consumer taking an item signals "state changed" — but the single condition may wake *another consumer*, which re-checks "queue empty", and waits again. The wakeup intended for a producer is consumed and lost; eventually every producer and consumer is parked.

- Fix 1: **two conditions** (`notFull`, `notEmpty`) so a signal targets the right waiters.
- Fix 2: keep one condition but use **`signalAll`** — correct, at the cost of thundering-herd wakeups.
