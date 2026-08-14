---
id: storage-multipart-ranged-io
node: storage.object
type: qa
---
## Q
Objects are written and read "whole" — so how do you move a 500GB object through S3 efficiently in both directions?

## A
- **Write: multipart upload** — split into parts (5MB–5GB each, up to 10,000), upload parts **in parallel with per-part retries**, then one CompleteMultipartUpload atomically assembles the object (it never exists half-visible). Required above 5GB; used well below that for parallelism. Failed uploads leave invisible parts that still bill — set a lifecycle rule to abort stale ones.
- **Read: ranged GETs** (`Range: bytes=...`) — fetch arbitrary byte ranges in parallel, or *only* the ranges you need. This is what makes Parquet-on-S3 work: read the footer, then just the needed column chunks — see [[storage-compute-separation]].

Per-request throughput is modest; **parallelism is the whole game** for object-store bandwidth.
