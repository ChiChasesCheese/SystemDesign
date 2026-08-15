---
id: method-self-verification
node: method.evaluation
type: qa
---
## Q
Why should you run and verify your own code before the interviewer asks — and how, when no test framework is set up?

## A
Rubrics explicitly score self-verification: a bug you catch is a plus signal; the same bug caught by the interviewer is a minus. Cheap method without a framework:

- a `main()` driver that exercises the happy path plus one edge case (full lot, invalid unpark)
- state the expected output **before** running, then run

Predict-then-run demonstrates you reason about the code rather than poke at it.
