---
id: storage-object-vs-filesystem
node: storage.object
type: qa
---
## Q
What can't you do with S3-style object storage that you can with a filesystem or block store, and why doesn't that matter for its main use cases?

## A
No **partial update**: objects are written whole (PUT replaces; no seek-and-write into the middle), listing is a paged API call rather than a cheap directory read, and first-byte latency is tens of ms, not µs.

Doesn't matter because its targets are **write-once, read-many blobs**: images, video, logs, backups, data-lake files (Parquet), ML artifacts. In exchange you get ~unlimited capacity, 11-nines durability, per-GB pricing, and HTTP access with no capacity planning — which is why "big or cold bytes go to object storage" is the modern default.
