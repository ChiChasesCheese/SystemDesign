---
id: distributed-pacelc
node: distributed.cap
type: qa
---
## Q
What does PACELC add over CAP, and how do DynamoDB and Spanner classify under it?

## A
The **ELC part**: *Else* (no partition, i.e. almost always), you still trade **Latency vs Consistency** — strong consistency requires coordination (quorum/leader round-trips) on every operation, paying latency even on a healthy network.

- **DynamoDB (default), Cassandra: PA/EL** — on partition choose availability; normally choose low latency (eventual consistency).
- **Spanner, CockroachDB, ZooKeeper: PC/EC** — on partition refuse minority-side operations; normally pay coordination latency for strong consistency.

Interview use: PACELC explains why "strongly consistent" systems are slower *every day*, not just during rare partitions.
