---
id: infra-canary-automation
node: infra.delivery
type: qa
---
## Q
What components turn a canary from "deploy 5% and stare at dashboards" into automated progressive delivery?

## A
- **Baseline pairing**: compare the canary against a **freshly deployed baseline running the old version** at the same size and traffic share — not against the aged full fleet — so warmup, cache state, and node placement don't pollute the comparison.
- **Automated judgement**: predefined metric queries (error rate, latency percentiles, saturation, key business metrics) scored statistically against the baseline at each step (Kayenta/Argo Rollouts style).
- **Stepped weights**: traffic shifts 1→5→25→100%, with a judgement gate before each increase.
- **Automatic rollback**: a failed gate shifts traffic back with no human in the loop — turning rollback MTTR from "someone notices" into seconds.
