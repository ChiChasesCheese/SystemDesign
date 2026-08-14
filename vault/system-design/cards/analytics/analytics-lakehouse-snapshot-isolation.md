---
id: analytics-lakehouse-snapshot-isolation
node: analytics.warehouse
type: qa
---
## Q
Object storage has no transactions. How do Iceberg/Delta provide snapshot isolation and atomic commits on top of it?

## A
Data files are **immutable**; a commit writes new data + a new metadata tree, then atomically swings a single **root pointer** to it — via a catalog compare-and-swap or a conditional PUT (`If-None-Match`/`If-Match`, which S3 now supports).

- **Readers** pin the root they started from, so they see one consistent snapshot for the whole query — snapshot isolation for free from immutability.
- **Writers** use optimistic concurrency: if the pointer moved since you read it, your CAS fails and you retry/rebase the commit.

The entire ACID story reduces to one atomic pointer swap; everything else is immutable files.
