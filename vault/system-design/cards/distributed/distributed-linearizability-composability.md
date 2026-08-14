---
id: distributed-linearizability-composability
node: distributed.consistency
type: cloze
---
Linearizability is a {{c1::composable ("local") property — if each object is linearizable, the system of all objects is linearizable}}, and it concerns {{c2::single operations on single objects, ordered against real time}}. Serializability is {{c3::not composable — running transactions serializably on two separate databases does not make cross-database executions serializable}}, which is one reason splitting a transactional workload across stores silently weakens its guarantees.
