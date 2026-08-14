---
id: architecture-serverless-constraints
node: architecture.serverless
type: qa
---
## Q
Name the FaaS execution-model constraints that break naive designs — and the classic database mistake.

## A
- **Ephemeral, stateless instances**: no local state between invocations (disk/memory may or may not survive); anything durable goes to external stores.
- **Execution time caps** (e.g. Lambda 15 min) and no long-lived connections — websockets/streaming need a managed gateway pattern, not a function holding a socket.
- **Scale-out is the failure mode for downstreams**: 1000 concurrent invocations = 1000 clients hammering whatever's behind them.

Classic mistake: each instance opening its own **RDBMS connection** — a traffic spike exhausts the database's connection limit. Fix: a connection proxy/pooler (RDS Proxy, PgBouncer) or an HTTP-native serverless database.
