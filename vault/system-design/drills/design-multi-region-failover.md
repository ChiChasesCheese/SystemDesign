---
nodes: [reliability.multi-region, reliability.availability, reliability.resilience.containment, distributed.replication.leader, distributed.replication.multi-leader]
tags: [flagship, operations]
---
# Drill: Take a single-region service multi-region

The follow-up that ends most interviews: "now make it survive losing a
region." A migration question, not a greenfield one — you must say what
breaks on the way, and what you are willing to lose.

**Constraints to state and honor**
- Today: one region, a leader database with read replicas, 99.9% availability.
- Target: survive a full region loss with RPO under 60 seconds and RTO under 10 minutes.
- Some data is subject to residency rules and may not leave its region.
- The budget will not stretch to running everything twice at full size.

**Grading points**
- The availability target turned into a downtime budget and checked against the dependency chain — you cannot exceed your least available dependency ([[reliability-nines-downtime-budgets]], [[reliability-slo-dependency-ceiling]], [[reliability-serial-parallel-composition]]).
- RPO and RTO defined separately, with the asynchronous-replication lag arithmetic that decides RPO ([[reliability-rpo-vs-rto]], [[reliability-async-rpo-math]], [[distributed-sync-vs-async-replication]]).
- Active-active versus active-passive chosen on the write pattern, not on fashion, with the cost of each stated ([[reliability-active-active-vs-passive]], [[distributed-multi-leader-fit]]).
- Failover mechanics described concretely — promotion, fencing, and the split-brain the fencing prevents ([[distributed-failover-mechanics]], [[distributed-fencing-tokens]], [[distributed-epoch-numbers]]).
- Multi-leader conflicts confronted where writes are accepted in both regions, with the resolution strategy and its data loss named ([[distributed-multi-leader-conflict-timing]], [[distributed-conflict-detection-siblings]], [[distributed-multi-leader-topologies]]).
- The three-region quorum argument for anything requiring consensus, and why two regions cannot arbitrate ([[reliability-three-region-quorum]], [[distributed-quorum-sizing]]).
- Residency treated as a partitioning decision made at the data model, not a routing patch ([[reliability-data-residency-conflict]], [[distributed-shard-key-one-way-door]]).
- Correlated failure acknowledged: shared control planes, shared deploy pipelines, and a shared configuration push are all single regions in disguise ([[reliability-correlated-failures]], [[reliability-config-deploy-risk]]).
- Failover exercised on a schedule, because an untested failover is a hypothesis ([[reliability-untested-failover]], [[reliability-chaos-hypothesis]], [[reliability-gray-failure]]).

**Attempt log**
- [ ] Attempt 1 (date, 45 min, self-graded notes):
