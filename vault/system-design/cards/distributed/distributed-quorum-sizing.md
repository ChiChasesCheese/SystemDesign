---
id: distributed-quorum-sizing
node: distributed.consensus
type: cloze
---
Consensus tolerating f crashed nodes requires {{c1::2f + 1}} nodes (majority quorums must intersect) — so 3 nodes tolerate 1 failure, 5 tolerate 2. A 4-node cluster tolerates {{c2::still only 1 failure (majority is 3), which is why even cluster sizes are pointless}}. Every committed write costs {{c3::a round-trip to the slowest node of the fastest majority}}, which is the latency argument against stretching a consensus group across distant regions.
