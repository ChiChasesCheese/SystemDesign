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

## Q zh
XA（两阶段提交）在实践中为什么很少使用？

## A zh
**理论上**：XA 协调原子提交跨越多个数据库。

**实践中的问题**：
- **阻塞** — 参与者锁定资源直到协调器决定，长时间持有锁。
- **协调器故障** — 如果协调器在第一阶段后崩溃，参与者冻结。
- **性能** — 三轮（准备、承诺、确认）很慢，特别是跨地理位置。
- **事务长度** — 典型 XA 事务长于 HTTP 请求；现代应用不能等。
- **协调器成为瓶颈** — SPOF 和吞吐量限制。

现代替代：Sagas（最终一致，无阻塞）或许多数据库中单主复制（所有分片通过主协调）。
