---
id: reliability-async-rpo-math
node: reliability.multi-region
type: cloze
---
With async cross-region replication, your effective **RPO equals the replication lag at the moment of disaster**, and writes lost ≈ {{c1::lag × write throughput}} — e.g. 5s of lag at 2,000 writes/s ≈ 10,000 lost writes. Lag is worst exactly when you need it least: {{c2::during traffic spikes and incidents, when the replication channel falls behind}} — so monitor lag as an SLI and alert when it exceeds the RPO objective. True RPO = 0 requires synchronous quorum replication and its cross-region write latency ([[reliability-three-region-quorum]]).
