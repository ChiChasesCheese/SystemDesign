---
id: reliability-chaos-hypothesis
node: reliability.resilience
type: qa
---
## Q
What separates chaos engineering from "randomly breaking things in prod," and what are the steps of a proper experiment?

## A
Chaos engineering is **hypothesis testing** about resilience, not vandalism:

1. Define a **steady-state metric** (e.g. checkout success rate).
2. State the hypothesis: "if we kill 1 AZ / inject 300ms latency into service X, steady state holds."
3. Inject the fault with **minimal blast radius** (small % of traffic, one cell) and an automatic **abort condition** that stops the experiment on SLI regression.
4. If steady state breaks, you found a real weakness cheaply; fix, then widen the blast radius.

Run in production (staging lacks real traffic and real config), but only after the experiment survives staging.
