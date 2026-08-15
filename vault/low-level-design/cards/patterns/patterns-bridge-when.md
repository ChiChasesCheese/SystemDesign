---
id: patterns-bridge-when
node: patterns.structural
type: qa
---
## Q
You have `Shape` × `Renderer` and inheritance is producing `VectorCircle`, `RasterCircle`, `VectorSquare`, `RasterSquare`... Which pattern fixes this, and how is it different from adapter?

## A
**Bridge**: split the two independent dimensions into two hierarchies and connect them by **composition** — `Circle` holds a `Renderer`. Class count drops from *n×m* subclasses to *n+m* classes, and each dimension varies independently.

```java
abstract class Shape { protected final Renderer r; ... }
class Circle extends Shape { void draw() { r.renderCircle(radius); } }
```

Vs adapter: **bridge is designed up front** so abstraction and implementation can evolve separately; **adapter is retrofitted** to make already-incompatible things work together. Same "interface + impl" skeleton, opposite point in the lifecycle.

Tell: the phrase "every combination of A and B" in requirements.
