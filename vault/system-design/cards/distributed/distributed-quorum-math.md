---
id: distributed-quorum-math
node: distributed.replication
type: cloze
---
Leaderless replication with N replicas: reads see the latest acknowledged write when {{c1::W + R > N}} (write and read sets must intersect). With N=3, W=2, R=2 you tolerate {{c2::one}} replica down for both reads and writes. Setting W=1, R=1 maximizes availability/latency but reads can miss recent writes. Caveat: {{c3::sloppy quorums (writes landing on non-home nodes during faults)}} break the intersection guarantee even when W + R > N — Dynamo-style stores need hinted handoff plus read repair/anti-entropy to converge.
