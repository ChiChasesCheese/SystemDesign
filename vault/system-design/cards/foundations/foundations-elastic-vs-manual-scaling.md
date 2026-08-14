---
id: foundations-elastic-vs-manual-scaling
node: foundations.tradeoffs
type: qa
---
## Q
Elastic (auto) scaling vs manually planned capacity — what does each buy, and when is manual the right answer?

## A
- **Elastic**: tracks unpredictable load and saves money at the trough — but reacts with lag (a sharp spike outruns instance boot), and feedback loops surprise you: scaling on the wrong metric, oscillation, or autoscaling silently absorbing a bug until the bill lands.
- **Manual**: fewer moving parts and forced capacity planning — right when load is predictable (daily/weekly cycles) or the unit is **stateful** (DB shards don't autoscale gracefully; rebalancing data is the cost).

Working rule: autoscale stateless compute; scale stateful tiers deliberately, ahead of need.
