---
id: reliability-gray-failure
node: reliability.availability
type: qa
---
## Q
A node passes every health check but serves 100x slower due to a dying disk. What is this failure class, why is it worse than a crash, and what detects it?

## A
**Gray (partial) failure** — the component is degraded, not dead, and the health checker's view differs from the clients' view (*differential observability*).

Worse than crash-stop because nothing evicts the node: it keeps receiving traffic, drags down tail latency, and slow responses tie up caller threads (a slow dependency is more dangerous than a down one).

Detection: health checks that exercise **real work paths** (not just "port open"), and **outlier ejection** — compare each instance's error/latency stats against its peers and evict the relative outlier.
