---
id: principles-temporal-coupling
node: principles.coupling
type: qa
---
## Q
```java
var svc = new ReportService();
svc.setStore(store);
svc.init();
svc.run();          // NPE / IllegalStateException if you skip a step
```
Name this coupling, list its two detection signals, and give the fix.

## A
**Temporal coupling** — correctness depends on an ordering the type doesn't express. Signals:

- Methods that begin with `if (!initialized) throw new IllegalStateException(...)`.
- Setters for things the object cannot function without (`setStore`), i.e. a constructor that leaves the object invalid.

Fix: **make the invalid state unconstructable** — take every required collaborator in the constructor (or a builder that validates and returns a ready object), and drop `init()` into it. When phases are genuinely distinct, encode them in *types*: `Connection.open()` returns an `OpenConnection` that is the only thing with `query()`.

Same smell, larger scale: two calls that must happen in order across classes — merge them into one method that owns the sequence.
