---
id: concurrency-lock-ordering-transfer
node: concurrency.hazards
type: qa
---
## Q
```java
void transfer(Account from, Account to, long amt) {
    synchronized (from) { synchronized (to) { ... } }
}
```
Concurrent `transfer(a, b, …)` and `transfer(b, a, …)` hang forever. Fix it without changing the method's signature.

## A
Classic circular wait. Impose a **global lock order** — always lock by a canonical key, regardless of argument order:

```java
Account first = from.id < to.id ? from : to;
Account second = from.id < to.id ? to : from;
synchronized (first) { synchronized (second) { ... } }
```

If keys can be equal (no unique id — e.g. ordering by `identityHashCode`), add a **tie-breaker lock** acquired before both. Same discipline generalizes: document a lock hierarchy and never acquire "upward."
