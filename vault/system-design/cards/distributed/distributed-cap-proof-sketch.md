---
id: distributed-cap-proof-sketch
node: distributed.cap
type: cloze
---
CAP proof sketch: partition two replicas, write `x=1` on one side, read `x` on the other. If the read side answers without hearing from the writer's side it may return {{c1::stale data — violating linearizability (sacrifices C)}}; if it waits or refuses until the partition heals it is {{c2::unavailable for that request (sacrifices A)}}. There is no third option, because the only way to know about the write is {{c3::a message across the very link that is down}}.
