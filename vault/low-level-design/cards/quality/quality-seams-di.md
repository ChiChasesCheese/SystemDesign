---
id: quality-seams-di
node: quality.testability
type: qa
---
## Q
What is a "seam" in the testability sense, and why does `new` inside a method destroy one?

## A
A **seam** (Feathers): a place where you can **change the program's behavior without editing the code under test** — i.e. where a collaborator can be swapped.

```java
class OrderService {
    void place(Order o) {
        var gw = new StripeGateway();   // no seam: test MUST hit Stripe
        ...
```

`new` (like a static call) hard-wires the concrete class at the use site — there is no point of substitution. Fix: accept the dependency through the **constructor** as an interface; the test passes a fake, production wiring happens at the composition root.

Rule of thumb: a class may `new` its own **value objects and data structures**, but anything with I/O, time, randomness, or its own behavior worth faking arrives injected.
