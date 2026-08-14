---
id: networking-realtime-backpressure
node: networking.realtime
type: qa
---
## Q
One WebSocket client on a bad network can't keep up with your push rate. What builds up where, and what are the three standard policies?

## A
The client's TCP receive window fills, the server's kernel send buffer fills, then the **per-connection application queue grows unbounded** — a handful of slow consumers can exhaust server memory.

- **Drop** oldest/newest — fine when messages are independent.
- **Coalesce** — keep only the latest value per key (tickers, presence, cursors): ideal when messages are snapshots, not deltas.
- **Disconnect** past a queue threshold — client reconnects and resyncs from source of truth.

Choose by semantics: deltas require either reliable delivery or resync-on-gap; snapshots can always coalesce.
