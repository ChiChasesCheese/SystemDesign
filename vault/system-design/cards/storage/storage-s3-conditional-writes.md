---
id: storage-s3-conditional-writes
node: storage.object
type: qa
---
## Q
S3's consistency model changed twice in the 2020s. What do you get now, and what new class of system did conditional writes unlock?

## A
- Since 2020: **strong read-after-write consistency** — a GET/LIST after any PUT (including overwrites) sees the latest version. The old eventual-consistency caveats are dead folklore.
- Since 2024: **conditional writes** — `If-None-Match: *` (create only if absent) and `If-Match: <etag>` (compare-and-swap on overwrite).

CAS on an object is a primitive for **coordination without a separate database**: multiple writers can safely race to commit — exactly what table formats need for atomic metadata-pointer swaps ([[analytics-lakehouse-snapshot-isolation]]), and it enables leases/locks and even S3-only queue/log designs. Losing writer gets `412 Precondition Failed` and retries against fresh state.
