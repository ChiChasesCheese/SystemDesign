---
id: structure-api-leaking-internals
node: structure.api
type: qa
---
## Q
```java
public List<Item> getItems() { return this.items; }  // internal list
```
What two failure modes does returning the internal collection create, and what should the method return instead?

## A
- **Invariant bypass**: callers can `add`/`remove` directly, skipping validation the class does in its own mutators (totals drift, capacity checks skipped).
- **Concurrency hole**: callers iterate the live list while the owner mutates it — `ConcurrentModificationException` or silent corruption, outside any lock the class holds.

Return `List.copyOf(items)` (snapshot) or `Collections.unmodifiableList(items)` (live read-only view — pick copy if callers may iterate while you mutate). Encapsulation isn't the field being `private`; it's **no external reference to mutable internals**.
