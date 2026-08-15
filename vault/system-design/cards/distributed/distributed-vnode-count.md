---
id: distributed-vnode-count
node: distributed.partitioning.schemes
type: cloze
---
Choosing the number of virtual nodes (tokens) per physical node is a variance-vs-overhead trade: with V random tokens per node, load imbalance shrinks roughly as {{c1::1/sqrt(V)}}, which is why naive random placement needs V in the hundreds (Cassandra's historic default was {{c2::256 tokens per node}}) to keep ownership within a few percent of even. The cost of a large V is {{c3::more ranges to track in the ring/metadata, and repair and streaming fragmenting into many small ranges — Merkle-tree repair and bootstrap get slower and more IO-bound}}. Modern deployments therefore drop V drastically (Cassandra 4+ recommends {{c4::16 tokens with the allocation algorithm, which places tokens deliberately to balance load instead of relying on randomness}}). Rendezvous hashing and bounded-load variants sidestep the tuning entirely.
