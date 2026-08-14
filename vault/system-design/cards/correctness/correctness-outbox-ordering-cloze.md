---
id: correctness-outbox-ordering-cloze
node: correctness.outbox
type: cloze
---
To preserve event order through an outbox: the relay publishes rows in {{c1::commit/insert order (monotonic outbox sequence)}}, uses {{c2::the aggregate id (e.g. account id) as the broker partition key}} so one entity's events stay in one partition, and a polling relay must run {{c3::single-writer per partition/shard}} — parallel unordered pollers silently reorder events.
