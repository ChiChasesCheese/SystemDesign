---
id: foundations-scale-up-vs-out
node: foundations.tradeoffs
type: qa
---
## Q
When do you keep scaling *up* (bigger machine) instead of *out* (more machines), and what eventually forces the switch?

## A
Scale up while you can: no partitioning, no rebalancing, no distributed failure modes — and a single 2026 box goes further than people assume (TBs of RAM, millions of IOPS). Costs: price grows superlinearly with size, and there's a hard ceiling.

Forced out by: load beyond the biggest box, **availability** (one machine is one failure domain), or geographic latency requiring presence in multiple regions.

DDIA's point: distribution adds irreducible complexity — go distributed when a number forces you, never by default.
