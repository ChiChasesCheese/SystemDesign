---
id: quality-bloaters-refactorings
node: quality.smells
type: qa
---
## Q
Pair each bloater with its primary refactoring: long method, long parameter list, primitive obsession, data clumps, large class.

## A
| Smell | Refactoring |
|---|---|
| Long method | **Extract method** (each fragment gets an intention-revealing name) |
| Long parameter list | **Introduce parameter object** / preserve whole object |
| Primitive obsession (`String email`, `int cents`) | **Replace primitive with value object** (`Email`, `Money`) |
| Data clumps (same 3 fields travel together) | **Extract class**, then pass the new object |
| Large class | **Extract class** per responsibility (SRP) |

Note the chain: data clumps and long parameter lists usually *reveal* a missing domain concept — the refactoring's real payoff is the new type, which then attracts the behavior that was envying it.
