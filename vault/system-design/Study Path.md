%% trellis:begin %%
# System Design — study path

318 cards over 8 weeks ≈ 6 new cards/day.

## Week 1

**Foundations**
- [ ] [[foundations.method|Interview Method]] — 6 cards
- [ ] [[foundations.estimation|Back-of-Envelope Estimation]] — 5 cards
- [ ] [[foundations.numbers|Latency Numbers]] — 7 cards
- [ ] [[foundations.tradeoffs|Core Trade-offs]] — 5 cards
**Networking & APIs**
- [ ] [[networking.protocols|Transport & HTTP]] — 6 cards
- [ ] [[networking.dns|DNS]] — 6 cards
- [ ] [[networking.api-styles|REST, gRPC & GraphQL]] — 6 cards
## Week 2

**Networking & APIs**
- [ ] [[networking.realtime|Realtime Delivery]] — 6 cards
- [ ] [[networking.cdn|CDN]] — 6 cards
**Load Balancing & Traffic**
- [ ] [[traffic.load-balancing|Load Balancers]] — 6 cards
- [ ] [[traffic.gateways|Reverse Proxies & API Gateways]] — 6 cards
- [ ] [[traffic.rate-limiting|Rate Limiting]] — 6 cards
**Caching**
- [ ] [[caching.strategies|Write & Read Strategies]] — 6 cards
- [ ] [[caching.invalidation|Invalidation & Eviction]] — 6 cards
## Week 3

**Caching**
- [ ] [[caching.placement|Cache Placement]] — 6 cards
**Storage**
- [ ] [[storage.relational|Relational Databases]] — 6 cards
- [ ] [[storage.internals|B-trees vs LSM-trees]] — 6 cards
- [ ] [[storage.nosql|NoSQL Families]] — 6 cards
- [ ] [[storage.object|Object Storage & Separation]] — 6 cards
- [ ] [[storage.search|Search Indexes]] — 6 cards
- [ ] [[storage.encoding|Encoding & Evolution]] — 5 cards
## Week 4

**Distributed Data**
- [ ] [[distributed.cap|CAP & PACELC]] — 5 cards
- [ ] [[distributed.consistency|Consistency Models]] — 6 cards
- [ ] [[distributed.replication|Replication]] — 7 cards; needs: Consistency Models
- [ ] [[distributed.partitioning|Partitioning]] — 6 cards
- [ ] [[distributed.transactions|Transactions & Isolation]] — 7 cards; needs: Relational Databases
- [ ] [[distributed.consensus|Consensus]] — 7 cards; needs: Replication
## Week 5

**Distributed Data**
- [ ] [[distributed.time|Clocks & Ordering]] — 6 cards
- [ ] [[distributed.crdt|CRDTs & Local-First]] — 5 cards; needs: Replication
**Async & Streaming**
- [ ] [[async.queues|Message Queues]] — 6 cards
- [ ] [[async.log|The Log & Kafka]] — 6 cards; needs: B-trees vs LSM-trees
- [ ] [[async.delivery|Delivery Semantics]] — 6 cards
- [ ] [[async.streaming|Stream Processing & CDC]] — 6 cards
**Analytics & Derived Data**
- [ ] [[analytics.olap|OLTP vs OLAP & Columnar]] — 5 cards; needs: B-trees vs LSM-trees
## Week 6

**Analytics & Derived Data**
- [ ] [[analytics.warehouse|Warehouses & Lakehouses]] — 5 cards; needs: Object Storage & Separation
- [ ] [[analytics.batch|Batch Processing]] — 5 cards
- [ ] [[analytics.derived|Derived Data & Materialized Views]] — 5 cards; needs: The Log & Kafka
**Correctness Patterns**
- [ ] [[correctness.idempotency|Idempotency]] — 7 cards; needs: Delivery Semantics
- [ ] [[correctness.outbox|Dual Writes & Outbox]] — 6 cards; needs: Transactions & Isolation, Message Queues
- [ ] [[correctness.saga|Sagas]] — 6 cards; needs: Transactions & Isolation
- [ ] [[correctness.ledger|Ledgers & Reconciliation]] — 8 cards; needs: Idempotency
## Week 7

**Architecture**
- [ ] [[architecture.services|Monoliths & Microservices]] — 6 cards
- [ ] [[architecture.discovery|Service Discovery & Contracts]] — 5 cards; needs: Encoding & Evolution
- [ ] [[architecture.serverless|Serverless]] — 5 cards
**Reliability & Operations**
- [ ] [[reliability.availability|Availability Math]] — 6 cards
- [ ] [[reliability.resilience|Resilience Patterns]] — 7 cards
- [ ] [[reliability.slo|SLOs & Error Budgets]] — 6 cards
## Week 8

**Reliability & Operations**
- [ ] [[reliability.observability|Observability]] — 6 cards
- [ ] [[reliability.multi-region|Multi-Region]] — 6 cards; needs: Replication, Consensus
**Security**
- [ ] [[security.authn|Authentication]] — 7 cards
- [ ] [[security.authz|Authorization & API Security]] — 6 cards
**AI Systems**
- [ ] [[ai.vector-search|Vector Search & RAG]] — 7 cards; needs: Search Indexes
- [ ] [[ai.inference|Inference Serving]] — 7 cards
%% trellis:end %%

## Notes
