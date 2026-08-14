---
id: storage-wide-column-modeling
node: storage.nosql
type: qa
---
## Q
In Cassandra/DynamoDB-style wide-column stores, how does data modeling invert compared to relational, and what do partition key vs clustering (sort) key each decide?

## A
You model **query-first**: design one table per access pattern and denormalize, instead of normalizing then joining — there are no joins.

- **Partition key** → *which node/partition* the row lives on; every efficient query must supply it.
- **Clustering/sort key** → *order within the partition*, enabling range scans (e.g. `messages` partitioned by `channel_id`, clustered by `sent_at`).

What breaks: a query pattern you didn't design a table for needs a full scan or a new denormalized table backfilled.
