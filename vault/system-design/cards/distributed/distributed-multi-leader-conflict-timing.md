---
id: distributed-multi-leader-conflict-timing
node: distributed.replication.multi-leader
type: cloze
---
The reason multi-leader conflicts are painful is *when* they are detected: in single-leader (or serializable) systems the second writer is {{c1::blocked or given an error while it is still on the request path, so the user can be asked to retry}}, whereas in multi-leader replication both writes are {{c2::accepted and acknowledged locally, and the conflict only surfaces asynchronously when the two leaders exchange logs — nobody is on the line to ask}}. The practical consequence is that resolution must be {{c3::automatic and deterministic (every replica must reach the same answer independently), or deferred by storing siblings for a later on-read merge}}. It also means synchronous conflict detection ("make one write wait for the other leader") is possible but {{c4::throws away the entire point of multi-leader — independent local writes — so you should use single-leader instead}}.
