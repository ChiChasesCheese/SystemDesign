---
id: storage-connection-pooling
node: storage.relational
type: qa
---
## Q
Why does a fleet of 200 app instances talking straight to Postgres fall over even at modest QPS, and what is the standard fix?

## A
Each Postgres connection is a **forked OS process** with its own memory (~5–10MB) and scheduling cost; a few thousand connections exhausts memory and burns CPU on context switching even if most connections are idle. 200 instances × 20-connection app pools = 4,000 connections.

Fix: an external pooler (**PgBouncer**, RDS Proxy) in transaction mode, multiplexing thousands of client connections onto tens–hundreds of server connections. Caveat: transaction pooling breaks session state (prepared statements, `SET`, advisory locks held across transactions).
