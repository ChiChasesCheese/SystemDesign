---
id: architecture-cold-starts
node: architecture.serverless
type: qa
---
## Q
What actually happens during a FaaS cold start, roughly how expensive is it, and what are the mitigations?

## A
On a request with no warm instance, the platform must **provision a sandbox (microVM/container), load the runtime, load your code, and run init** before handling the request — typically ~100ms–1s+, worst with heavy runtimes (JVM) and large bundles; VPC networking and big dependency trees make it worse.

Mitigations:
- **Provisioned concurrency / min instances**: pay to keep N instances warm — the real fix for latency-sensitive paths.
- **Shrink init**: smaller bundles, lazy-load dependencies, lighter runtimes; snapshot-based starts (e.g. JVM snapshotting à la SnapStart) cut runtime init.
- Note cold starts hit a small fraction of requests but dominate **tail latency** — and every concurrency spike is a burst of them.
