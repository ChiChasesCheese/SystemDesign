---
id: async-broker-selection
node: async.queues
type: qa
---
## Q
Kafka vs RabbitMQ vs Pulsar: which workload picks which, and why?

## A
- **RabbitMQ (queue semantics)**: task distribution — per-message ack, redelivery to any consumer, routing/priority/delay features, consumer count not tied to partitions. Weak at replay and huge retention.
- **Kafka (log semantics)**: event streams shared by many consumers, replay, high-throughput ordered-per-key feeds. Parallelism is capped by partitions and per-message routing/priorities don't exist.
- **Pulsar**: both semantics on one cluster — segmented storage (BookKeeper) separates compute from storage, so topics scale without repartitioning and tiered offload is native; also strong multi-tenancy/geo-replication. Cost: more moving parts, smaller ecosystem.

Rule of thumb: *tasks* → queue semantics; *facts other systems will re-read* → log semantics ([[async-log-vs-queue]]).
