---
id: distributed-mvcc-defaults
node: distributed.transactions
type: cloze
---
MVCC lets readers and writers avoid blocking each other: each transaction reads {{c1::a snapshot of versions committed before it started}}, while writers create new row versions instead of overwriting. The cost is {{c2::version garbage that must be cleaned up (Postgres vacuum; long-running transactions hold the snapshot horizon back and cause bloat)}}. Default isolation in Postgres and MySQL/InnoDB respectively: {{c3::read committed and repeatable read}}.
