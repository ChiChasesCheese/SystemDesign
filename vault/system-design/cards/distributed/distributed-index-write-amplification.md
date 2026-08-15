---
id: distributed-index-write-amplification
node: distributed.partitioning.indexes
type: cloze
---
Write amplification from global secondary indexes: inserting one row with k global indexes costs {{c1::1 + k writes, and each index write lands on a different partition (usually a different node) than the base row}}. Updating a row is worse than inserting it, because for each index whose indexed column changed you must {{c2::delete the entry under the old term and insert one under the new term — 2 index writes per changed indexed column, in two different index partitions}}. This is why the standard guidance is {{c3::index only the attributes you actually query on, and project only the attributes the query needs (DynamoDB KEYS_ONLY / INCLUDE beat ALL, since every projected attribute is copied on every write)}}. It is also why the writes cannot be transactional with the base row at scale: {{c4::making them atomic would require a distributed transaction across partitions on every single write, so systems make the index eventually consistent instead}}.
