---
id: principles-cohesion-signal
node: principles.coupling
type: qa
---
## Q
What does low cohesion look like *inside* a single class, and what's the standard refactor?

## A
Signals:
- fields cluster into disjoint groups, each used by a different subset of methods
- the name needs "Manager", "Util", or "Helper" to cover everything
- methods neither call each other nor share state

Refactor: **Extract Class** along the field-usage clusters, so each class's methods use most of its fields. High cohesion inside classes is what makes low coupling between them possible.
