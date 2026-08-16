---
nodes: [quality.smells, quality.refactoring, quality.testability, principles.simplicity, principles.coupling]
tags: [refactoring, medium]
---
# Drill: Refactor a legacy pricing method

Not a blank page — a repair job, which is what the second half of most
machine-coding rounds turns into. You are handed one `OrderService`
method of ~200 lines that computes an order total: line items, tiered
discounts, coupon codes, tax by region, shipping bands, loyalty points. It
reads `Clock.now()` and a `FeatureFlags` singleton directly, takes eleven
parameters, and is covered by no tests. Make it changeable without
changing what it computes.

**Constraints to state and honor**
- Behaviour is frozen: the same inputs must produce the same total, including the two rounding oddities you will find.
- No test suite exists. You may not "refactor and then test" — decide what to pin down first.
- The next feature (a second coupon per order) must land in one small, obvious place when you are done.
- 45 minutes: you will not finish the whole method. Choose what to cut.

**Grading points**
- Characterization tests before the first edit, generated from the current behaviour rather than the spec — [[quality.testability|Designing for Tests]].
- Naming the smells out loud (long method, long parameter list, feature envy, temporal coupling on the flag read) and the refactoring each one calls for — [[quality.smells|Code Smells]].
- Guard clauses and extract-method first — the cheap, reversible moves — before any class extraction — [[quality.refactoring|Core Refactorings]].
- A parameter object for the pricing context, not eleven arguments threaded down — [[quality.refactoring|Core Refactorings]].
- Clock and flags injected, so the tests stop depending on today's date — [[principles.coupling|Coupling, Cohesion & DI]].
- Discounts as a list of small rules only if the code already shows three of them; a rule engine invented for one coupon is the failure mode — [[principles.simplicity|DRY, KISS, YAGNI]].
- The rounding oddities preserved deliberately and flagged as questions for the product owner, not silently "fixed" — [[quality.smells|Code Smells]].

**Attempt log**
- [ ] Attempt 1 (date, 45 min, self-graded notes):
