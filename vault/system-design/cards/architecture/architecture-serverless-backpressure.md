---
id: architecture-serverless-backpressure
node: architecture.serverless
type: qa
---
## Q
A traffic spike makes your FaaS platform spawn 3,000 concurrent function instances, which flatten the database behind them. What is the structural mismatch, and the two standard fixes?

## A
FaaS **scales concurrency near-instantly and unboundedly**, while downstream stateful systems (relational DBs, third-party APIs) have hard concurrency/connection ceilings — serverless removed *your* bottleneck and turned it into a weapon against dependencies. Each instance also opens its own DB connections, multiplying the damage.

- **Cap and queue**: set reserved/max concurrency on the function, and put a **queue between trigger and function** (queue-based load leveling) so bursts buffer instead of amplify.
- **Connection proxying**: a pooler (e.g. RDS Proxy, pgbouncer) multiplexes thousands of function instances onto a bounded connection pool.
