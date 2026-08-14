---
id: networking-tcp-vs-udp
node: networking.protocols
type: qa
---
## Q
When is UDP the right transport despite giving up TCP's guarantees? Name the guarantees you're dropping and two workloads that want that.

## A
Dropping: **ordering, retransmission, and connection state** — which means no head-of-line blocking and no handshake/teardown cost.

- **Live media / voice / games**: a late packet is worthless; retransmitting old data adds latency for nothing.
- **Protocols that reimplement reliability themselves**: DNS lookups (single tiny request/response), and **QUIC**, which builds TLS + streams + loss recovery on UDP to escape TCP's kernel-level head-of-line blocking.
