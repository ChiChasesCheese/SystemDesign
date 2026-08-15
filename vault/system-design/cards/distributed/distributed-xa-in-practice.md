---
id: distributed-xa-in-practice
node: distributed.transactions.distributed
type: qa
---
## Q
What is XA, and what specifically goes wrong when a team adopts it to keep a database and a message broker in sync?

## A
XA is the standard C API/protocol for 2PC across heterogeneous resource managers (a DB, a JMS broker, another DB), driven by a transaction manager that usually runs **in the application process** (JTA in a Java app server, `@Transactional` spanning two `XADataSource`s).

Where it goes wrong:

- **The transaction manager becomes stateful and critical.** Its log holds the commit decisions, so it must be durable and highly available — but it lives in an application server people treat as stateless and redeploy freely. Lose that log, keep in-doubt transactions forever.
- **In-doubt transactions require a DBA.** Recovery means listing prepared transactions (`XA RECOVER`, Postgres `pg_prepared_xacts`) and manually committing/rolling back. Meanwhile the locks are still held, and Postgres won't advance its snapshot horizon, so vacuum stalls and bloat grows.
- **Locks are held across network calls**, so throughput collapses (commonly cited as an order of magnitude) and one slow participant stalls the rest.
- **Coverage is thin in modern stacks**: HTTP/gRPC services, most cloud-managed datastores, and Kafka do not implement XA at all — so the pattern doesn't even apply to the microservice case people reach for it in.

Modern default: outbox + idempotent consumers for DB↔broker, sagas for cross-service workflows.
