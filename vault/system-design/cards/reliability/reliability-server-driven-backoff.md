---
id: reliability-server-driven-backoff
node: reliability.resilience.retries
type: qa
---
## Q
Every client is individually well-behaved (exponential backoff + jitter, 3 attempts) and the service is still being retried into the ground. Why, and what two mechanisms fix it?

## A
Client-side backoff is **local knowledge**: each client only sees its own failures, so it cannot know that 10k other clients are backing off against the same overloaded server. The aggregate retry rate is still far above what the server can absorb, and the server pays CPU to reject each one.

- **Server-driven backoff**: reply `429`/`503` with **`Retry-After`** (or a gRPC push-back / throttling hint) — the server is the only party that knows the real recovery time, and it can spread clients by returning jittered values. Rejects must be *cheap* (shed at the edge before touching the DB) or the rejection path becomes the outage.
- **Adaptive client throttling** (Google SRE): each client tracks `requests` and `accepts` over ~2 minutes and drops its own requests with probability `max(0, (requests − K·accepts) / (requests + 1))`, K≈2. As the server's accept rate falls the client self-limits, so the retry load converges to roughly what the server can serve — a client-side circuit breaker with a knob instead of a switch.

Both are the enforcement mechanism behind a **retry budget** (e.g. retries ≤ 10% of requests), which is otherwise just an unenforced intention.
