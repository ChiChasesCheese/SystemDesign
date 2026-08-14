---
id: async-log-ordering-partitions
node: async.log
type: qa
---
## Q
What ordering does Kafka actually guarantee, and how do you use that to keep per-entity ordering at scale?

## A
Ordering is guaranteed **only within a partition** — there is no total order across a topic.

- Choose the **partition key = entity id** (user id, account id, order id) so all events for one entity land in one partition, in order.
- Cross-entity order is undefined; if you need it, you have a design problem, not a config problem.
- Beware: changing partition count re-maps keys, breaking per-key ordering across the boundary — plan partitions up front or migrate deliberately.
