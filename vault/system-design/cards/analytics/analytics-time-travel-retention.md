---
id: analytics-time-travel-retention
node: analytics.warehouse
type: cloze
---
Lakehouse time travel works because commits never delete data files — old snapshots keep referencing them. The costs are storage growth and unbounded metadata, so tables need {{c1::snapshot expiration / vacuum}} to drop snapshots past a retention window and physically delete unreferenced files. Two operational consequences: you can only roll back or audit within {{c2::the retention window}}, and GDPR-style hard deletes aren't complete until expired snapshots' files are {{c3::physically removed}}, not just dropped from the latest snapshot.
