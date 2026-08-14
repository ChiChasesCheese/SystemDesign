---
id: reliability-error-budget-throttle
node: reliability.slo
type: qa
---
## Q
Your SLO is 99.9% monthly success rate. What is the error budget, and what concretely changes when it is exhausted?

## A
Budget = 1 − SLO = **0.1% of requests** (or ~43 minutes of full downtime) per month, deliberately spendable on releases, experiments, and planned risk.

When exhausted: **feature releases freeze**; engineering shifts to reliability work until the budget refills. This turns "how reliable is reliable enough" from an argument into a pre-agreed, self-enforcing policy between product and ops.
