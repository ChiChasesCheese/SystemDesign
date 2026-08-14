---
id: patterns-singleton-costs
node: patterns.creational
type: qa
---
## Q
Why is Singleton the most criticized GoF pattern, and what's the modern alternative when you genuinely need one instance?

## A
Singleton couples two decisions that should be separate: *one instance exists* and *everyone accesses it globally*.

- The global access point makes dependencies **invisible** (nothing in a signature says the class uses it) and makes tests share **hidden mutable state** you can't swap or reset.
- It hard-codes the concrete class — no substituting a test double.

Modern alternative: keep the class ordinary, create **one instance at the composition root** and inject it (DI container or hand-wired `main`). Reserve true singletons for stateless, cross-cutting facts (e.g. a process-wide logger), and if forced, use an `enum` singleton / static holder for safe lazy init.
