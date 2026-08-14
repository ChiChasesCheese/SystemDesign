---
id: async-rebalancing-protocols
node: async.log
type: qa
---
## Q
A consumer group of 50 members hiccups every deploy: all consumption stops for seconds. What causes the pause, and what are the modern mitigations?

## A
**Eager rebalancing** is stop-the-world: any membership change makes *every* member revoke *all* partitions, rejoin, and wait for reassignment — a full pause plus state-reload for stateful consumers.

Mitigations:
- **Incremental cooperative rebalancing**: only partitions that actually move are revoked; everyone else keeps consuming through the rebalance.
- **Static membership** (`group.instance.id`): a restarting member reclaims its old partitions within the session timeout with **no rebalance at all** — built for rolling deploys.
- KRaft-era **KIP-848 broker-coordinated protocol**: assignment computed server-side, per-member incremental updates, no global sync barrier.
