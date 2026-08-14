---
id: networking-connection-pooling
node: networking.protocols
type: qa
---
## Q
A service calls a downstream over HTTP/1.1 through a 50-connection pool. Load rises; downstream "latency" explodes while both ends sit at low CPU. Mechanism — and what changes under HTTP/2?

## A
**Pool exhaustion.** HTTP/1.1 allows one in-flight request per connection, so the 51st concurrent request queues waiting for a free connection — that queue wait is invisibly folded into measured downstream latency while both services idle. Required pool size ≈ concurrency = QPS × response time ([[foundations-littles-law]]), so a downstream slowdown alone can exhaust the pool.

HTTP/2 multiplexes ~100 streams per connection, so a couple of connections replace the pool — but limits move to stream caps, and one connection's packet loss now stalls all its streams.
