---
id: distributed-data-skew-vs-access-skew
node: distributed.partitioning.skew
type: qa
---
## Q
Distinguish data skew from access skew. Which remedies apply to each, and which remedy is useless for one of them?

## A
- **Data skew**: one partition holds disproportionate *bytes/rows* (a range partition on `country` where one country is 60% of users; a tenant with 100x the data). Symptoms: disk pressure, slow compactions/repairs on one node, uneven backup times.
- **Access skew (hot key/hot partition)**: bytes are fine, *traffic* is concentrated — a celebrity row, a "current day" bucket.

| Remedy | Data skew | Access skew |
|---|---|---|
| Split the range further | works | works only if the heat spans many keys |
| Salt the key | overkill | works (writes) |
| Cache in front | useless | works (reads) |
| Move the partition to a bigger node | works | useless — it's one key, and one node still serves it |

The useless-for-access-skew one to name out loud: **rebalancing/adding nodes**. It redistributes keys, and access skew concentrated on a *single* key is indivisible by any partitioning scheme. Managed systems blur this: DynamoDB's adaptive capacity will isolate a hot partition automatically, but still cannot exceed the per-partition-key ceiling (~3000 RCU / 1000 WCU).
