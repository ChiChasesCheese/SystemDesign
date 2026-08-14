---
id: concurrency-cas-aba
node: concurrency.primitives
type: qa
---
## Q
A lock-free stack pops by `compareAndSet(top, A, A.next)`. The CAS succeeds — yet the stack is corrupted. What happened, and what's the fix?

## A
**ABA problem**: between reading `top == A` and the CAS, another thread popped A, popped B, and pushed A back (or a *recycled* node at A's address). The CAS sees "still A" and succeeds, but `A.next` now points at a node that's no longer in the stack.

- Fix: pair the pointer with a **version stamp** bumped on every update (`AtomicStampedReference`, tagged pointers) — the stale version fails the CAS.
- In GC languages the classic node-reuse variant is rarer (a reachable A can't be reallocated), but logical ABA on values still bites.
