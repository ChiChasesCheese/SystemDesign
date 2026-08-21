You are triaging a codebase into a study system. For each artefact below decide
what it should become, and answer with one JSON object (no prose).

## Codebase
quant-stroller at 4dae805d2955, cached read-only at .trellis/codebases/quant-stroller

## Lenses and their leaves
### low-level-design
- `method.delivery` — Machine Coding Method: Requirement scoping, choosing core flows, time-boxing design vs code vs demo, driving the session.
- `method.evaluation` — Machine Coding Method: What interviewers grade — extensibility, readability, testability, and verifying your own code before they do.
- `method.modeling` — Machine Coding Method: Noun–verb extraction, finding entities and invariants, sequence-of-interactions before class diagrams.
- `oop.pillars` — Object Modeling: Encapsulation, abstraction, inheritance, polymorphism — each as a lever with a cost, not a virtue.
- `oop.relationships` — Object Modeling: Association vs aggregation vs composition vs dependency; lifetime ownership and the UML arrows for each.
- `oop.interfaces` — Object Modeling: Program-to-interface, interface vs abstract class discrimination, default methods and their limits.
- `oop.values` — Object Modeling: Entities vs value objects, equality semantics, enums with behavior, why immutability simplifies reasoning.
- `principles.solid` — Design Principles: The five principles as concrete refactoring triggers, with the violation each one detects.
- `principles.composition` — Design Principles: Why deep hierarchies rot, delegation as the default reuse tool, when inheritance is still right.
- `principles.coupling` — Design Principles: Afferent/efferent coupling, law of Demeter, dependency injection as the seam-maker.
- `principles.simplicity` — Design Principles: The simplicity principles and their failure mode — premature abstraction and speculative generality.
- `patterns.creational` — Design Patterns: Singleton, factory method, abstract factory, builder, prototype — who creates objects and how flexibly.
- `patterns.structural` — Design Patterns: Adapter, decorator, facade, composite, proxy, bridge, flyweight — composing objects into larger shapes.
- `patterns.behavioral` — Design Patterns: Strategy, observer, command, state, template method, iterator, chain of responsibility, mediator, memento, visitor.
- `patterns.selection` — Design Patterns: Mapping problem smells to patterns, pattern pairs that get confused, and over-engineering as the classic failure.
- `quality.smells` — Code Quality: Bloaters, OO abusers, change preventers, dispensables, couplers — and the refactoring each family calls for.
- `quality.refactoring` — Code Quality: Extract method/class, replace conditional with polymorphism, introduce parameter object, guard clauses.
- `quality.testability` — Code Quality: Seams, constructor injection, test double taxonomy, and why static/global state kills testability.
- `quality.errors` — Code Quality: Exceptions vs result types, validation at boundaries, designing failure paths as first-class flows.
- `concurrency.model` — Concurrency: Concurrency vs parallelism, thread lifecycle, visibility and reordering, why data races are undefined behavior.
- `concurrency.primitives` — Concurrency: Mutex, semaphore, condition variable, reentrant and read-write locks, CAS and lock-free basics.
- `concurrency.hazards` — Concurrency: The four deadlock conditions and their breakers, livelock, starvation, lock ordering discipline.
- `concurrency.patterns` — Concurrency: Producer-consumer, bounded blocking queue, thread pool, reader-writer, safe lazy initialization.
- `structure.api` — APIs & Program Structure: Small stable interfaces, fluent builders, method contracts, and evolving an API without breaking callers.
- `structure.state-machines` — APIs & Program Structure: Modeling lifecycles (order, elevator, game) as explicit states and transitions instead of boolean soup.
- `structure.storage` — APIs & Program Structure: Repository pattern, id generation, secondary indexes, and thread-safe in-memory stores for machine coding.
### system-design
- `foundations.method` — Foundations: Requirements clarification, scoping functional vs non-functional needs, driving the 40-minute structure yourself.
- `foundations.estimation` — Foundations: QPS, storage, and bandwidth sizing from DAU and access patterns; when an estimate changes the design.
- `foundations.numbers` — Foundations: Orders of magnitude every engineer should know — memory vs SSD vs disk vs same-DC network vs cross-region.
- `foundations.tradeoffs` — Foundations: Performance vs scalability, latency vs throughput, availability vs consistency — the axes every later choice moves along.
- `networking.protocols` — Networking & APIs: TCP vs UDP guarantees and costs; HTTP semantics, keep-alive, HTTP/2 and 3 in one breath.
- `networking.dns` — Networking & APIs: Resolution path, record types, TTL as a blunt failover and traffic-steering instrument.
- `networking.api-styles` — Networking & APIs: Choosing an API style by coupling, payload shape, streaming needs, and who owns the clients.
- `networking.realtime` — Networking & APIs: Long polling vs SSE vs WebSockets; connection state as the scaling cost.
- `networking.cdn` — Networking & APIs: Push vs pull CDNs, cache keys, and what belongs at the edge.
- `traffic.load-balancing` — Load Balancing & Traffic: L4 vs L7, balancing algorithms, health checks, and LB high availability itself.
- `traffic.gateways` — Load Balancing & Traffic: What a gateway centralizes — TLS termination, auth, routing, quotas — and the single-point risks it adds.
- `traffic.rate-limiting` — Load Balancing & Traffic: Token bucket vs sliding window, local vs distributed enforcement, and what to return when you shed.
- `caching.strategies` — Caching: Cache-aside, read-through, write-through, write-behind, refresh-ahead — who populates the cache and when.
- `caching.invalidation` — Caching: TTLs, eviction policies, stale reads, and cache stampede protection.
- `caching.placement` — Caching: Client, CDN, gateway, application, and database layers — what each layer can and cannot absorb.
- `storage.relational.indexing` — Storage › Relational Databases: B-tree indexes, composite and covering indexes, leftmost-prefix rule, when indexes hurt.
- `storage.relational.operations` — Storage › Relational Databases: Connection pooling, read replicas, federation, MVCC maintenance, and when a single Postgres is the right answer.
- `storage.internals` — Storage: The two storage engine families; read, write, and space amplification trade-offs.
- `storage.nosql` — Storage: Key-value, document, wide-column, graph — the access patterns each one exists to serve.
- `storage.object` — Storage: S3-style object stores, storage-compute separation, and the modern default of parking cold and big data there.
- `storage.search` — Storage: Inverted indexes, relevance basics, and keeping a search cluster in sync with the source of truth.
- `storage.encoding` — Storage: Data formats as contracts between code versions — JSON, Protobuf, Avro; forward and backward compatibility rules.
- `distributed.cap` — Distributed Data: What the theorem actually constrains during a partition, and the latency trade-off the rest of the time.
- `distributed.consistency` — Distributed Data: Linearizability, causal, read-your-writes, eventual — as contracts you promise the client.
- `distributed.replication.leader` — Distributed Data › Replication: Single-leader replication, log shipping formats, sync vs async, lag and its anomalies, failover mechanics.
- `distributed.replication.multi-leader` — Distributed Data › Replication: Multi-datacenter writes, conflict detection and resolution, why LWW loses data.
- `distributed.replication.leaderless` — Distributed Data › Replication: Dynamo-style quorums, sloppy quorums and hinted handoff, read repair and anti-entropy.
- `distributed.partitioning.schemes` — Distributed Data › Partitioning: Hash and range partitioning trade-offs; consistent hashing and virtual nodes.
- `distributed.partitioning.rebalancing` — Distributed Data › Partitioning: Moving partitions without downtime; who knows where a key lives — routing tiers and coordination services.
- `distributed.partitioning.skew` — Distributed Data › Partitioning: Detecting and defusing hot partitions — key salting, splitting, and request-level caches.
- `distributed.partitioning.indexes` — Distributed Data › Partitioning: Local vs global secondary indexes — scatter-gather reads vs write amplification.
- `distributed.transactions.isolation` — Distributed Data › Transactions: Read committed to serializable through the anomalies each level permits — dirty/non-repeatable reads, write skew, phantoms.
- `distributed.transactions.concurrency-control` — Distributed Data › Transactions: 2PL vs MVCC vs SSI — how databases actually enforce isolation, and their contention behavior.
- `distributed.transactions.distributed` — Distributed Data › Transactions: 2PC mechanics and blocking, why it's avoided at scale, and what replaces it.
- `distributed.consensus` — Distributed Data: Why single-leader systems need election, what Raft guarantees, fencing tokens, and the cost of quorum writes.
- `distributed.time` — Distributed Data: Why wall clocks lie, logical clocks, and detecting failure with timeouts you can defend.
- `distributed.crdt` — Distributed Data: Conflict-free replicated data types, merge semantics, and offline-capable multi-writer apps.
- `async.queues` — Async & Streaming: Queues vs pub-sub, backpressure, consumer scaling, and when async is the wrong call.
- `async.log` — Async & Streaming: The append-only log as system of record; partitions, consumer groups, offsets, retention.
- `async.delivery.guarantees` — Async & Streaming › Delivery Semantics: At-most-once vs at-least-once, ordering scope, dead-letter queues and poison pills.
- `async.delivery.exactly-once` — Async & Streaming › Delivery Semantics: Idempotent producers, transactional consume-process-produce, and why end-to-end exactly-once is a composition, not a feature.
- `async.streaming` — Async & Streaming: Change data capture, materialized views, windows, and keeping derived data fresh.
- `analytics.olap` — Analytics & Derived Data: Why analytical scans want column layout, compression, and vectorized execution instead of B-trees.
- `analytics.warehouse` — Analytics & Derived Data: Warehouse vs data lake vs lakehouse; open table formats (Iceberg/Delta) over object storage.
- `analytics.batch` — Analytics & Derived Data: MapReduce lineage to Spark; shuffles, distributed joins, idempotent reruns, and batch vs stream boundaries.
- `analytics.derived` — Analytics & Derived Data: Treating caches, indexes, and views as recomputable projections of a log — and keeping them fresh.
- `correctness.idempotency` — Correctness Patterns: Idempotency keys, dedup windows, and designing every mutation to survive a retry.
- `correctness.outbox` — Correctness Patterns: Why writing DB-then-publish loses events, and how the transactional outbox closes the gap.
- `correctness.saga` — Correctness Patterns: Long-running workflows via compensating actions when a distributed transaction is off the table.
- `correctness.ledger` — Correctness Patterns: Double-entry design, immutability, balance derivation, and reconciliation as the payments-grade safety net.
- `architecture.services` — Architecture: When to split, service boundaries by data ownership, and the operational bill microservices arrive with.
- `architecture.discovery` — Architecture: Registries, health checking, API versioning, and evolving schemas without breaking consumers.
- `architecture.serverless` — Architecture: FaaS execution model, cold starts, and where per-request pricing beats owning servers.
- `reliability.availability` — Reliability & Operations: Nines, serial vs parallel composition, redundancy patterns, failover modes and their data-loss windows.
- `reliability.resilience.retries` — Reliability & Operations › Resilience Patterns: Timeout budgets, deadline propagation, exponential backoff with jitter, retry storms and retry budgets.
- `reliability.resilience.containment` — Reliability & Operations › Resilience Patterns: Circuit breakers, bulkheads, load shedding, chaos engineering, and safe deployment strategies.
- `reliability.slo` — Reliability & Operations: SLIs worth measuring, percentiles over averages, and error budgets as a release throttle.
- `reliability.observability` — Reliability & Operations: Structured logs, metrics, distributed traces; correlation ids and cardinality costs.
- `reliability.multi-region` — Reliability & Operations: Active-passive vs active-active, data residency, RPO/RTO, and why failover you never test doesn't exist.
- `infra.containers` — Platform & Infrastructure: Containers vs VMs, Kubernetes primitives (pods, services, autoscaling) at design-conversation depth.
- `infra.mesh` — Platform & Infrastructure: Sidecars and ambient meshes — mTLS, retries, and traffic policy moved out of application code, at a latency cost.
- `infra.delivery` — Platform & Infrastructure: Pipelines, canary and blue-green automation, feature flags, and config/schema changes as deploys.
- `security.authn.tokens` — Security › Authentication: Server sessions vs JWTs, access/refresh pairs, rotation and reuse detection, sender-constrained tokens.
- `security.authn.oauth` — Security › Authentication: Authorization-code + PKCE flow, what OIDC adds on top, which flow for which client.
- `security.authn.credentials` — Security › Authentication: Credential storage, phishing resistance, and the WebAuthn/passkey model.
- `security.authz` — Security: RBAC vs ABAC, API keys vs user tokens, TLS everywhere, secrets handling.
- `ai.foundations` — AI Systems: What an LLM actually does at serving time — tokens, context windows, embeddings, prefill/decode — no ML math required.
- `ai.vector-search` — AI Systems: Embeddings as vectors, ANN indexes (HNSW/IVF), hybrid retrieval, and freshness of the indexed corpus.
- `ai.rag` — AI Systems: Chunking, retrieval, reranking, and grounding as a data pipeline — where quality is won and lost.
- `ai.inference` — AI Systems: GPU batching, KV-cache reuse, streaming responses, and cost/latency levers unique to LLM backends.
- `ai.evals` — AI Systems: Offline vs online evaluation, LLM-as-judge, regression suites for prompts, and tracing AI pipelines.

## Artefacts
- `contracts:.importlinter` (contracts) — .importlinter
- `decisions:0001-strategy-stack-not-layer` (decisions) — docs/adr/0001-strategy-stack-not-layer.md
- `decisions:0002-data-stages-raw-bars-panel-not-lake-layers` (decisions) — docs/adr/0002-data-stages-raw-bars-panel-not-lake-layers.md
- `decisions:0003-embedded-data-platform-duckdb-dbt-sealed-snapshots` (decisions) — docs/adr/0003-embedded-data-platform-duckdb-dbt-sealed-snapshots.md
- `decisions:0004-experiment-ledger-event-log-not-rdbms` (decisions) — docs/adr/0004-experiment-ledger-event-log-not-rdbms.md
- `decisions:0005-scout-idea-funnel-event-log-agent-triage` (decisions) — docs/adr/0005-scout-idea-funnel-event-log-agent-triage.md
- `decisions:0006-eodhd-raw-archive-contract` (decisions) — docs/adr/0006-eodhd-raw-archive-contract.md
- `decisions:0007-research-loop-checkpoint-hitl-wrap-cli` (decisions) — docs/adr/0007-research-loop-checkpoint-hitl-wrap-cli.md
- `decisions:0008-live-event-driven-nautilus-not-lean` (decisions) — docs/adr/0008-live-event-driven-nautilus-not-lean.md
- `decisions:0009-canonical-ledger-outside-worktree-git-mirror` (decisions) — docs/adr/0009-canonical-ledger-outside-worktree-git-mirror.md
- `decisions:0010-nautilus-as-hard-dependency-retire-parallel-abstractions` (decisions) — docs/adr/0010-nautilus-as-hard-dependency-retire-parallel-abstractions.md
- `decisions:0011-decisionmoment-unifies-time-cadence-becomes-constructor` (decisions) — docs/adr/0011-decisionmoment-unifies-time-cadence-becomes-constructor.md
- `decisions:0012-findings-carry-executable-probes` (decisions) — docs/adr/0012-findings-carry-executable-probes.md
- `decisions:0013-deletion-requires-retired-outdated-duplicate` (decisions) — docs/adr/0013-deletion-requires-retired-outdated-duplicate.md

## Verdicts
- `case` — the artefact records a DECISION that is an instance of something a
  leaf already teaches. Rewrite it in that lens's vocabulary: what problem it
  solves, what it forbids, what it costs. Never restate it as "we chose X";
  a reader who does not know this codebase must still learn something.
- `reading` — the artefact is SUBJECT MATTER for a leaf: it teaches a topic
  rather than recording a choice.
- `gap` — the artefact clearly belongs to one of these lenses but no leaf fits.
  Propose the leaf that is missing. This is a wanted outcome, not a failure.
- `skip` — housekeeping, duplication, or specific to this codebase in a way
  that teaches nothing transferable.

## Rules
- `nodes` must be leaf ids of the lens you chose, copied exactly from above.
- `slug` must be unique, lowercase-hyphenated, and start with `qs`.
- `body` is markdown, 100-250 words, written for someone who has never seen
  this repository. State the mechanism and the trade-off, not the conclusion.
- Be strict. An artefact that teaches nothing transferable is a `skip`, and
  skipping is cheaper than diluting the deck.

## Answer format
{"codebase": "quant-stroller", "ref": "4dae805d2955", "items": [
  {"artefact": "decisions:0004-...", "verdict": "case", "lens": "system-design",
   "nodes": ["async.log"], "slug": "qs-...", "title": "...",
   "body": "...", "confidence": "high"},
  {"artefact": "subject:...", "verdict": "gap", "lens": "quant-infra",
   "proposed_leaf": "data.point-in-time", "why": "..."},
  {"artefact": "subject:...", "verdict": "skip", "why": "..."}
]}
