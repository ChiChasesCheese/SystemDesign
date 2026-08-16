---
nodes: [infra.delivery, storage.relational.operations, storage.encoding, architecture.discovery, reliability.resilience.containment]
tags: [operations, migration]
---
# Drill: Split a table and a service without downtime

The least glamorous and most frequently lived-through design question:
move `orders` out of the monolith's database into its own service, change
its schema on the way, and never take the site down. Sequencing is the
whole answer.

**Constraints to state and honor**
- 2 TB table, 40 writes/second, read by nine other modules — three of which you do not own.
- No maintenance window. Any step must be reversible within minutes.
- The new schema renames a column and splits one field into two.
- Old and new code will run simultaneously for weeks, in both directions.

**Grading points**
- Expand/contract as the spine of the plan, with the migration split into additive steps and the destructive step last ([[architecture-expand-contract]], [[infra-schema-migration-deploys]]).
- Rolling upgrades acknowledged as the reason both directions of compatibility are needed, not just backward ([[storage-rolling-upgrade-compat]], [[storage-encoding-compat-directions]]).
- Schema evolution rules applied to the event and API payloads too, with field-tag and default discipline ([[storage-protobuf-tag-rules]], [[storage-avro-schema-resolution]], [[storage-json-contract-pitfalls]]).
- Contract compatibility enforced mechanically by a registry, so a breaking change fails a build rather than a customer ([[architecture-registry-compat-modes]], [[architecture-schema-compat-rules]], [[architecture-api-versioning-strategies]]).
- Backfill of 2 TB done in throttled batches, made resumable and safe to re-run ([[analytics-idempotent-reruns]], [[storage-mvcc-vacuum]]).
- Dual writes recognised as the trap they are, with change data capture or an outbox chosen instead ([[correctness-dual-write-problem]], [[correctness-outbox-mechanism]], [[async-cdc-mechanism]], [[async-cdc-initial-snapshot]]).
- Read migration staged behind a flag with shadow reads and comparison before the cutover ([[infra-flags-deploy-release]], [[infra-canary-automation]]).
- Deploy and release separated, so the rollback is a flag flip rather than a redeploy ([[infra-flags-deploy-release]], [[reliability-deploy-strategies]], [[infra-pipeline-quality-gates]]).
- Blast radius contained during cutover — one consumer at a time, with a circuit back to the old path ([[reliability-circuit-breaker-states]], [[reliability-bulkhead-vs-shedding]], [[reliability-config-deploy-risk]]).
- The operational realities named: connection pool limits, long transactions blocking DDL, and index builds on a live table ([[storage-connection-pooling]], [[storage-scaling-ladder]], [[storage-index-write-cost]]).
- Service discovery and routing updated so the nine callers find the new owner without a synchronized deploy ([[architecture-discovery-mechanisms]], [[architecture-boundaries-data-ownership]]).

**Attempt log**
- [ ] Attempt 1 (date, 45 min, self-graded notes):
