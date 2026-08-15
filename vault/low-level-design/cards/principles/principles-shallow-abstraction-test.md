---
id: principles-shallow-abstraction-test
node: principles.simplicity
type: qa
---
## Q
You just added a layer/wrapper. How do you tell whether it simplified the design or merely moved the complexity?

## A
Test the **interface-to-implementation ratio** (Ousterhout): a good abstraction hides much behind little. Concrete checks:

- Did any **caller get shorter or say less**? If callers pass the same arguments through to the same call, it's a *pass-through method* — pure indirection, negative value.
- Can you describe what the layer hides in one sentence? "It hides that pricing needs a calendar" is a deep module; "it forwards to the repository" is not.
- Count the files a reader must open to follow one flow. If that went up and nothing was hidden, complexity moved.

**Indirection is not encapsulation** — classes that only relay are the shallow-module smell YAGNI and KISS are really warning about.
