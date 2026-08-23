%% trellis:begin %%
# quant-stroller

What this codebase contributed, by lens.
19 case(s) accepted.


## low-level-design
- [[qs-a-claim-without-a-probe-is-a-guess|A claim without a probe is a guess]] — [[quality.fitness-functions]]  `decisions:0012-findings-carry-executable-probes` @ `4dae805d2955`
- [[qs-deleting-code-needs-positive-evidence|Dead code needs positive evidence, not silence]] — [[quality.smells]]  `decisions:0013-deletion-requires-retired-outdated-duplicate` @ `4dae805d2955`
- [[qs-durable-phase-machine-that-decides-nothing|A durable phase machine that decides nothing]] — [[structure.state-machines]]  `decisions:0007-research-loop-checkpoint-hitl-wrap-cli` @ `4dae805d2955`
- [[qs-layering-as-a-checked-import-direction|Layering is a claim about import direction — check it or lose it]] — [[principles.coupling]]  `contracts:.importlinter#module-graph-tiers` @ `4dae805d2955`
- [[qs-mutual-independence-is-stronger-than-layering|Independence: neither side may know the other]] — [[principles.coupling]]  `contracts:.importlinter#alpha-broker-independent` @ `4dae805d2955`
- [[qs-one-sanctioned-route-to-the-dangerous-layer|Forbidding the edge to the dangerous layer]] — [[principles.coupling]]  `contracts:.importlinter#forbid-alpha-to-execution` @ `4dae805d2955`
- [[qs-package-cycles-and-the-shrink-only-ratchet|Package cycles, and the exception list that may only shrink]] — [[principles.coupling]]  `contracts:.importlinter#quant-acyclic-siblings` @ `4dae805d2955`
- [[qs-sealed-constructor-as-unforgeable-permission|Sealed constructors: when holding the object is the proof]] — [[patterns.creational]]  `contracts:.importlinter#protect-tradable-seal` @ `4dae805d2955`
- [[qs-sink-the-shared-type-dont-invert-the-layer|When a low layer needs a high layer's type, sink the type]] — [[principles.solid]]  `contracts:.importlinter#forbid-data-to-experiment` @ `4dae805d2955`
- [[qs-the-tax-on-an-optional-dependency|The tax on an optional dependency, and what a wrapper really is]] — [[patterns.structural]]  `decisions:0010-nautilus-as-hard-dependency-retire-parallel-abstractions` @ `4dae805d2955`
- [[qs-unify-the-declaration-fork-the-implementation|Unify the declaration, fork the implementation]] — [[principles.simplicity]]  `decisions:0011-decisionmoment-unifies-time-cadence-becomes-constructor` @ `4dae805d2955`

## system-design
- [[qs-content-addressed-intake-with-recorded-rejections|Content-addressed intake, with rejections on the record]] — [[correctness.idempotency]]  `decisions:0005-scout-idea-funnel-event-log-agent-triage` @ `4dae805d2955`
- [[qs-embedded-warehouse-and-a-hand-rolled-commit-log|An embedded warehouse and a hand-rolled commit log]] — [[analytics.warehouse]], [[analytics.batch]]  `decisions:0003-embedded-data-platform-duckdb-dbt-sealed-snapshots` @ `4dae805d2955`
- [[qs-materialize-the-archive-derive-the-rest|Materialize the archive, derive the rest]] — [[analytics.derived]]  `decisions:0002-data-stages-raw-bars-panel-not-lake-layers` @ `4dae805d2955`
- [[qs-one-honest-ledger-with-a-discriminator|One honest ledger with a discriminator, not two stores]] — [[storage.record-modeling]]  `decisions:0001-strategy-stack-not-layer` @ `4dae805d2955`
- [[qs-one-implementation-two-drivers-replay-parity|One implementation, two drivers: replay/live parity]] — [[async.streaming]]  `decisions:0008-live-event-driven-nautilus-not-lean` @ `4dae805d2955`
- [[qs-resumable-ingestion-against-a-metered-api|Resumable ingestion against a metered API]] — [[correctness.idempotency]], [[traffic.rate-limiting]]  `decisions:0006-eodhd-raw-archive-contract` @ `4dae805d2955`
- [[qs-two-writers-and-the-conflict-you-cannot-see|Two writers and the conflict you cannot see]] — [[distributed.replication.multi-leader]]  `decisions:0009-canonical-ledger-outside-worktree-git-mirror` @ `4dae805d2955`
- [[qs-write-model-is-a-log-read-model-is-a-projection|Write model as immutable log, read model as projection]] — [[async.log]], [[analytics.derived]]  `decisions:0004-experiment-ledger-event-log-not-rdbms` @ `4dae805d2955`

%% trellis:end %%

## Notes
