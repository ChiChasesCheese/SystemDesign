---
id: distributed-salting-read-cost
node: distributed.partitioning.skew
type: cloze
---
Salting a hot key writes to `key#0 … key#(S-1)`, spreading writes over up to S partitions, but the reader now must {{c1::fan out S requests and merge the results — read cost and read tail latency are multiplied by S, since latency is the max over S shards}}. Pick S from {{c2::the ratio of the hot key's traffic to a single partition's capacity, plus headroom — not a fixed constant, and applied only to keys detected as hot}}. You can avoid the fanout entirely when the salt is {{c3::derived deterministically from something the reader already knows (e.g. suffix = hash(user_id) % S), so a per-user read goes to exactly one salted key}} — the fanout is only unavoidable when the read genuinely needs the aggregate over all writers. For read-hot rather than write-hot keys, salting is the wrong tool: {{c4::replicate the value into a cache tier / add read replicas instead, since reads don't need to be partitioned to be scaled}}.
