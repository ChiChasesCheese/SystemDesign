---
id: patterns-when-to-refuse
node: patterns.selection
type: qa
---
## Q
In an LLD round, what signals tell you to REFUSE a pattern, and what's the disciplined way to hold the door open for it?

## A
Refuse when:

- There's **one concrete case** and the second is hypothetical — an interface with a single implementation is speculative generality (YAGNI / rule of three: abstract on the ~3rd occurrence, not the 1st).
- The pattern adds **more classes than the logic it organizes** — a strategy interface + factory + 2 one-line strategies vs a 5-line `if`.
- You'd be pattern-dropping to impress: the interviewer grades whether the design fits, not vocabulary count.

Disciplined move: write the simple version, then **say out loud where the seam is** — "if a third pricing rule appears, this `if` becomes a `PricingStrategy`." Patterns are best introduced as *refactoring targets* when duplication actually arrives, not as upfront scaffolding.
