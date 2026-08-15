---
id: distributed-mvcc-visibility
node: distributed.transactions.concurrency-control
type: cloze
---
MVCC visibility rules — when transaction T (with its snapshot) may see a row version: the version's creator must have {{c1::committed before T's snapshot was taken}}, and the creator must not be in {{c2::the list of transactions that were still in progress at snapshot time (recorded when the snapshot is taken)}}, nor aborted, nor have a txid later than the snapshot. A deleted row stays visible to T until {{c3::the deleting transaction is itself visible under the same rules — deletes just mark the version with the deleter's txid; physical removal is garbage collection's job}}.
