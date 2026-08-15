---
id: patterns-template-method-vs-strategy
node: patterns.behavioral
type: qa
---
## Q
Template method and strategy both vary steps of an algorithm. When is each right, and why has the default shifted to strategy?

## A
- **Template method**: the *skeleton* is fixed in a base class; subclasses override selected hook steps (**inheritance**, variation chosen at class-definition time). Right when the invariant sequence is the point and variants are few and stable — e.g. a test framework's setup/run/teardown.
- **Strategy**: the varying step is an injected object (**composition**, swappable at runtime, independently testable, combinable — one class can hold several strategies).

Default is strategy because template method inherits inheritance's problems: one variation axis only, fragile base class, subclass locked to one variant forever. Rule of thumb: template method for framework skeletons you own; strategy everywhere the variation is a *domain* concept (pricing, parsing, matching).
