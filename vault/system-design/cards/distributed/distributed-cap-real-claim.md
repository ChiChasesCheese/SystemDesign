---
id: distributed-cap-real-claim
node: distributed.cap
type: qa
---
## Q
What does the CAP theorem actually constrain — and why is calling a system "CA" a red flag in an interview?

## A
It constrains behavior **only during a network partition**: a replicated system must then either refuse some requests (choose **C**, staying linearizable) or answer with possibly-stale/divergent data (choose **A**). It says nothing about normal operation.

"CA" is a red flag because partitions are not optional in a distributed system — you can't choose to forfeit P; you can only choose what to sacrifice *when* one happens. Also note "C" here means linearizability and "A" means every non-failed node answers — much narrower than everyday "consistency" and "high availability".
