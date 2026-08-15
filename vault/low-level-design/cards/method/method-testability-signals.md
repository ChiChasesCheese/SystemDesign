---
id: method-testability-signals
node: method.evaluation
type: qa
---
## Q
A grader skims your code for "testable" in about 30 seconds. What are they actually looking at?

## A
Whether they could exercise one rule **without constructing the world**:

- Does the fee/allocation logic take its inputs as parameters, or does it reach into a fully-built `ParkingLot`?
- Any `new Collaborator()`, `Singleton.getInstance()`, or `LocalDateTime.now()` **inside** logic? Each is an unsubstitutable dependency — an injected `Clock` is the standard tell that you've met this before.
- Are the interesting rules pure functions of their arguments, with I/O and mutation pushed to the edges?

"I wrote tests" is weaker evidence than a constructor that lets them.
