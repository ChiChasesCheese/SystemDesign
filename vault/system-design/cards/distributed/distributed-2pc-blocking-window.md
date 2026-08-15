---
id: distributed-2pc-blocking-window
node: distributed.transactions.distributed
type: cloze
---
2PC's cost model, in numbers you can quote: a commit needs {{c1::two round trips to the slowest participant, plus a durable log flush (fsync) at every participant and at the coordinator}}. Availability of the transaction is {{c2::the product of all participants' availabilities — five 99.9% services give 99.5%, so the composite is worse than any member}}. The blocking window when the coordinator dies is {{c3::not a timeout but the coordinator's full recovery time — in-doubt participants hold their locks for as long as it takes a human or a failover to restore the coordinator's log}}, and if that log is lost the only resolution is {{c4::a heuristic decision by an operator, which may commit one participant and abort another — silently breaking atomicity, with reconciliation left to the business}}. The structural fix used by Spanner/CockroachDB is {{c5::making the coordinator itself a replicated state machine (its decision log lives in a Raft/Paxos group), so coordinator failure costs an election, not an outage}}.
