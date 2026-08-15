---
id: oop-getter-collection-leak
node: oop.pillars
type: qa
---
## Q
```java
class Floor {
  private final List<Spot> spots;
  public List<Spot> getSpots() { return spots; }
}
```
The field is `private final`. Explain how encapsulation is still broken, and give the three fixes in order of preference.

## A
`final` protects the *reference*, not the contents — the caller holds the live list and can `add`/`clear` it, bypassing every rule `Floor` enforces. Same leak on the way **in**: a constructor storing a caller-supplied list lets the caller keep mutating it.

1. **Don't expose it** — add the operation instead: `floor.findFreeSpot(size)`.
2. Return an **unmodifiable view** (`List.copyOf` / `Collections.unmodifiableList`) and defensively copy in the constructor.
3. Expose a stream/iterator only if callers genuinely need arbitrary traversal.

Getters returning mutable internals (collections, `Date`, arrays) are the most common encapsulation leak in review.
