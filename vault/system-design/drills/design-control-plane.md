---
nodes: [distributed.consensus, architecture.discovery, infra.containers, infra.mesh, infra.delivery]
tags: [flagship, platform]
---
# Drill: Design the control plane for an internal platform

The system that runs the other systems: it stores cluster configuration
and service metadata, tells every service where its dependencies are, and
rolls changes out safely. Getting it wrong takes down everything at once.

**Constraints to state and honor**
- 5,000 services, 50,000 instances, instances churning constantly as deploys roll.
- Configuration reads must survive the control plane being down; writes may not.
- A configuration change must be rollable-out gradually and rollable-back in under a minute.
- Two operators editing the same key must not silently overwrite each other.

**Grading points**
- Consensus scoped to the metadata that needs it, and kept off the data path — a replicated log for config, not for traffic ([[distributed-consensus-in-practice]], [[distributed-total-order-broadcast]]).
- Raft's guarantees stated precisely, including why a read from a leader is not automatically linearizable ([[distributed-raft-guarantees]], [[distributed-raft-linearizable-reads]]).
- Quorum sized deliberately (3 vs 5) with the latency and failure-tolerance trade named ([[distributed-quorum-sizing]], [[distributed-epoch-numbers]], [[distributed-fencing-tokens]]).
- Discovery mechanism chosen — DNS, client-side registry, or mesh-managed — with the staleness each accepts ([[architecture-discovery-mechanisms]], [[networking-dns-negative-caching]]).
- Clients caching last-known-good configuration and running on it, so a control-plane outage degrades rather than cascades ([[reliability-correlated-failures]], [[caching-local-vs-remote]]).
- Schema compatibility enforced at the registry, with expand/contract used for any breaking change ([[architecture-registry-compat-modes]], [[architecture-schema-compat-rules]], [[architecture-expand-contract]], [[architecture-api-versioning-strategies]]).
- Orchestration primitives used for what they are — declarative desired state and a reconciliation loop — with the case for not adopting them acknowledged ([[infra-k8s-primitives]], [[infra-k8s-overkill]], [[infra-containers-vs-vms]]).
- Requests and limits set so one noisy tenant cannot starve a node ([[infra-requests-limits-noisy-neighbor]]).
- Mesh responsibilities separated from library responsibilities, with the sidecar's interception path and its tax named ([[infra-mesh-sidecar-intercept]], [[infra-mesh-vs-code]], [[infra-mesh-tax-ambient]], [[infra-mesh-when-not]]).
- Configuration rollout treated as a deploy: staged, canaried, automatically reverted ([[infra-canary-automation]], [[reliability-config-deploy-risk]], [[infra-pipeline-quality-gates]]).

**Attempt log**
- [ ] Attempt 1 (date, 45 min, self-graded notes):
