---
id: reliability-rpo-vs-rto
node: reliability.multi-region
type: qa
---
## Q
RPO vs RTO: which one is about data, which about time-to-recover, and which replication choice controls each?

## A
- **RPO (Recovery Point Objective)**: max acceptable **data loss**, measured backward from the failure. Controlled by replication mode — synchronous replication gives RPO ≈ 0; async gives RPO = replication lag; nightly backups give RPO up to 24h.
- **RTO (Recovery Time Objective)**: max acceptable **downtime** until service is restored. Controlled by failover automation and standby warmth (active-active ≈ seconds; cold restore ≈ hours).

They are independent knobs: you can have RPO 0 with a slow manual failover (RTO hours), or instant failover that drops recent writes.
