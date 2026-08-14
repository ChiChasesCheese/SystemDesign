---
id: quality-parameter-object
node: quality.refactoring
type: qa
---
## Q
Introduce parameter object: beyond shortening signatures, what two design payoffs justify it — and what's the anti-pattern version?

## A
```java
book(String from, String to, LocalDate out, LocalDate in, int guests)
→ book(Route route, StayPeriod period, int guests)
```

Payoffs beyond brevity:

- **A home for validation and behavior**: `StayPeriod` enforces `out < in` once in its constructor and grows methods like `nights()` — logic that was duplicated at every call site.
- **A stable seam**: adding a field changes the object, not every signature in the chain (kills a shotgun-surgery vector).

Anti-pattern: the grab-bag `RequestContext`/`Options` object that bundles *unrelated* params just to shorten a signature — that's a data clump faked, coupling every caller to every field. Group only what forms a real concept.
