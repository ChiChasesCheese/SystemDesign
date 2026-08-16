%% trellis:begin %%
# System Design — study path

391 cards over 8 weeks ≈ 7 new cards/day, plus 22 drills.

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
- [ ] [[networking.realtime|Realtime Delivery]] — 6 cards
- [ ] [[networking.cdn|CDN]] — 6 cards
## Week 2

**Load Balancing & Traffic**
- [ ] [[traffic.load-balancing|Load Balancers]] — 6 cards
- [ ] [[traffic.gateways|Reverse Proxies & API Gateways]] — 6 cards
- [ ] [[traffic.rate-limiting|Rate Limiting]] — 6 cards
**Caching**
- [ ] [[caching.strategies|Write & Read Strategies]] — 6 cards
- [ ] [[caching.invalidation|Invalidation & Eviction]] — 6 cards
- [ ] [[caching.placement|Cache Placement]] — 6 cards
**Storage**
- [ ] [[storage.relational.indexing|Indexing]] — 5 cards
- [ ] [[storage.relational.operations|Operating at Scale]] — 4 cards
## Week 3

**Storage**
- [ ] [[storage.internals|B-trees vs LSM-trees]] — 6 cards
- [ ] [[storage.nosql|NoSQL Families]] — 6 cards
- [ ] [[storage.object|Object Storage & Separation]] — 6 cards
- [ ] [[storage.search|Search Indexes]] — 6 cards
- [ ] [[storage.encoding|Encoding & Evolution]] — 5 cards
**Distributed Data**
- [ ] [[distributed.cap|CAP & PACELC]] — 5 cards
- [ ] [[distributed.consistency|Consistency Models]] — 6 cards
- [ ] [[distributed.replication.leader|Leader-Based]] — 4 cards
- [ ] [[distributed.replication.multi-leader|Multi-Leader]] — 5 cards
## Week 4

**Distributed Data**
- [ ] [[distributed.replication.leaderless|Leaderless & Quorums]] — 5 cards
- [ ] [[distributed.partitioning.schemes|Hash vs Range]] — 5 cards
    - [ ] **Drill:** [[design-url-shortener|Design a URL shortener]]
- [ ] [[distributed.partitioning.rebalancing|Rebalancing & Routing]] — 5 cards
    - [ ] **Drill:** [[design-object-store|Design a replicated key-value store]]
- [ ] [[distributed.partitioning.skew|Hot Keys & Skew]] — 5 cards
- [ ] [[distributed.partitioning.indexes|Partitioned Secondary Indexes]] — 5 cards
    - [ ] **Drill:** [[design-typeahead|Design search typeahead]]
- [ ] [[distributed.transactions.isolation|Isolation Levels & Anomalies]] — 5 cards
- [ ] [[distributed.transactions.concurrency-control|Concurrency Control]] — 5 cards
- [ ] [[distributed.transactions.distributed|Distributed Transactions]] — 5 cards
- [ ] [[distributed.consensus|Consensus]] — 7 cards; needs: Replication
- [ ] [[distributed.time|Clocks & Ordering]] — 6 cards
    - [ ] **Drill:** [[design-rate-limiter|Design a distributed rate limiter]]
## Week 5

**Distributed Data**
- [ ] [[distributed.crdt|CRDTs & Local-First]] — 5 cards; needs: Replication
    - [ ] **Drill:** [[design-collaborative-editor|Design a collaborative document editor]]
**Async & Streaming**
- [ ] [[async.queues|Message Queues]] — 6 cards
    - [ ] **Drill:** [[design-news-feed|Design a social news feed]]
- [ ] [[async.log|The Log & Kafka]] — 6 cards; needs: B-trees vs LSM-trees
- [ ] [[async.delivery.guarantees|Delivery Guarantees]] — 5 cards
    - [ ] **Drill:** [[design-chat-system|Design a chat system]]
- [ ] [[async.delivery.exactly-once|Effectively Exactly-Once]] — 5 cards
- [ ] [[async.streaming|Stream Processing & CDC]] — 6 cards
**Analytics & Derived Data**
- [ ] [[analytics.olap|OLTP vs OLAP & Columnar]] — 5 cards; needs: B-trees vs LSM-trees
- [ ] [[analytics.warehouse|Warehouses & Lakehouses]] — 5 cards; needs: Object Storage & Separation
- [ ] [[analytics.batch|Batch Processing]] — 5 cards
    - [ ] **Drill:** [[design-web-crawler|Design a web crawler]]
## Week 6

**Analytics & Derived Data**
- [ ] [[analytics.derived|Derived Data & Materialized Views]] — 5 cards; needs: The Log & Kafka
    - [ ] **Drill:** [[design-ad-click-aggregation|Design ad click aggregation]]
**Correctness Patterns**
- [ ] [[correctness.idempotency|Idempotency]] — 7 cards; needs: Delivery Semantics
- [ ] [[correctness.outbox|Dual Writes & Outbox]] — 6 cards; needs: Transactions, Message Queues
- [ ] [[correctness.saga|Sagas]] — 6 cards; needs: Transactions
    - [ ] **Drill:** [[design-ticket-booking|Design seat booking]]
- [ ] [[correctness.ledger|Ledgers & Reconciliation]] — 8 cards; needs: Idempotency
    - [ ] **Drill:** [[design-payment-ledger|Design a payment ledger service]]
**Architecture**
- [ ] [[architecture.services|Monoliths & Microservices]] — 6 cards
    - [ ] **Drill:** [[design-ride-matching|Design ride matching]]
- [ ] [[architecture.discovery|Service Discovery & Contracts]] — 5 cards; needs: Encoding & Evolution
- [ ] [[architecture.serverless|Serverless]] — 5 cards
    - [ ] **Drill:** [[design-video-platform|Design a video platform]]
## Week 7

**Reliability & Operations**
- [ ] [[reliability.availability|Availability Math]] — 6 cards
- [ ] [[reliability.resilience.retries|Timeouts & Retries]] — 5 cards
    - [ ] **Drill:** [[design-notification-fanout|Design a notification service]]
- [ ] [[reliability.resilience.containment|Failure Containment]] — 5 cards
- [ ] [[reliability.slo|SLOs & Error Budgets]] — 6 cards
- [ ] [[reliability.observability|Observability]] — 6 cards
    - [ ] **Drill:** [[design-metrics-platform|Design a metrics and alerting platform]]
- [ ] [[reliability.multi-region|Multi-Region]] — 6 cards; needs: Replication, Consensus
    - [ ] **Drill:** [[design-multi-region-failover|Take a single-region service multi-region]]
**Platform & Infrastructure**
- [ ] [[infra.containers|Containers & Orchestration]] — 4 cards
- [ ] [[infra.mesh|Service Mesh]] — 4 cards; needs: Timeouts & Retries
- [ ] [[infra.delivery|CI/CD & Progressive Delivery]] — 4 cards; needs: Failure Containment
    - [ ] **Drill:** [[design-control-plane|Design the control plane for an internal platform]]
    - [ ] **Drill:** [[design-zero-downtime-migration|Split a table and a service without downtime]]
**Security**
- [ ] [[security.authn.tokens|Sessions & Tokens]] — 4 cards
## Week 8

**Security**
- [ ] [[security.authn.oauth|OAuth2 & OIDC]] — 5 cards
- [ ] [[security.authn.credentials|Passwords & Passkeys]] — 5 cards
- [ ] [[security.authz|Authorization & API Security]] — 6 cards
    - [ ] **Drill:** [[design-api-platform|Design a public API platform]]
    - [ ] **Drill:** [[design-account-security|Design account sign-in and recovery]]
**AI Systems**
- [ ] [[ai.foundations|LLM Foundations for Engineers]] — 5 cards
- [ ] [[ai.vector-search|Vector Search]] — 7 cards; needs: Search Indexes, LLM Foundations for Engineers
- [ ] [[ai.rag|RAG Pipelines]] — 5 cards; needs: Vector Search
- [ ] [[ai.inference|Inference Serving]] — 7 cards; needs: LLM Foundations for Engineers
    - [ ] **Drill:** [[design-inference-service|Design an LLM inference service]]
- [ ] [[ai.evals|Evals & AI Observability]] — 5 cards
    - [ ] **Drill:** [[design-rag-assistant|Design a retrieval-augmented assistant]]
%% trellis:end %%

## Notes
