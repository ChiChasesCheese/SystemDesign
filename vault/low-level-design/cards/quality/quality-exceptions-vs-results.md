---
id: quality-exceptions-vs-results
node: quality.errors
type: qa
---
## Q
Exceptions vs result types (`Result`/`Either`/`Optional`) — what's the decision rule, and what failure of each style should you name?

## A
Rule: model by **expectedness at the call site**.

- **Expected domain outcomes** the caller must handle every time — insufficient funds, seat already booked, validation failure — return a **result type**: the compiler forces handling, and outcomes are values you can log, map, and test.
- **Exceptional conditions** the immediate caller can't fix — connection lost, invariant broken, bug — **throw**, and let a boundary handler translate (crashing on a programmer error beats limping on).

Failure modes to name: exceptions for expected cases become **control flow** — invisible in signatures, easy to forget, expensive; results for truly unrecoverable errors force `.map/.flatMap` plumbing through code that could do nothing anyway. Never signal failure with `null` or sentinel values — that's the worst of both.
