---
id: concurrency-double-checked-locking
node: concurrency.patterns
type: qa
---
## Q
```java
if (instance == null) {
    synchronized (Lock.class) {
        if (instance == null) instance = new Expensive();
    }
}
return instance;
```
What's still wrong with this double-checked locking, and what are two correct alternatives?

## A
Without `volatile`, the write `instance = new Expensive()` can be **reordered**: the reference is published before the constructor finishes. The *first* (unlocked) check can then see non-null and return a **partially constructed object**.

- Fix: declare `instance` **`volatile`** (volatile write→read forbids that reordering).
- Better in Java: the **holder-class idiom** (`static class H { static final Expensive I = new Expensive(); }`) — the classloader gives lazy init + safety with no locking code. An `enum` singleton works too.
