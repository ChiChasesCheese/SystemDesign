---
id: patterns-misuse-traps
node: patterns.selection
type: qa
---
## Q
Name the signature misuse of each: singleton, observer, mediator, visitor.

## A
- **Singleton** → global mutable state in disguise: hidden dependencies, shared state across tests, hard-coded concretes.
- **Observer** → invisible control flow: cascading notifications where nobody can trace why a change happened; update storms and ordering bugs (and leaks from forgotten unsubscribes).
- **Mediator** → the god object: all interaction logic drains into one class until the mediator *is* the coupling you tried to remove.
- **Visitor** → rigidity: applied to a hierarchy that still grows, so every new element type breaks every visitor.

Common thread: each pattern trades one kind of coupling for another — the misuse is ignoring what you paid.
