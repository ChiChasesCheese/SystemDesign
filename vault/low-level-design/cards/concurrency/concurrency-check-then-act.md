---
id: concurrency-check-then-act
node: concurrency.model
type: qa
---
## Q
```java
if (!map.containsKey(key)) {
    map.put(key, createExpensive(key));
}
```
`map` is a `ConcurrentHashMap`, so every call is thread-safe. What's the bug, and what fixes it?

## A
**Check-then-act race**: two threads both pass the check before either puts, so both create the value and one overwrites the other. A *composite* operation is not atomic just because each step is.

- Fix: one atomic operation — `computeIfAbsent(key, k -> createExpensive(k))` (or `putIfAbsent`).
- Or hold one lock across **both** the check and the act.

`volatile` cannot help here — it fixes visibility, not atomicity.
