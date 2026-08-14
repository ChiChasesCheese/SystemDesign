---
id: networking-http1-hol-workarounds
node: networking.protocols
type: qa
---
## Q
HTTP/1.1's head-of-line blocking lives at the application layer. What exactly blocks, and which browser-era hacks did it force (now anti-patterns under HTTP/2)?

## A
One connection carries **one request at a time**; responses must come back in order, and pipelining broke on middleboxes so browsers disabled it — leaving ~6 parallel TCP connections per host as the only concurrency.

Forced hacks: **domain sharding** (more hostnames → more connections), **concatenation/spriting** (fewer requests), inlining assets.

Under HTTP/2 multiplexing these hurt: sharding splits one prioritized connection into several and pays extra handshakes; concatenated blobs destroy caching granularity (one changed byte invalidates the bundle).
