---
id: networking-tls-resumption
node: networking.protocols
type: qa
---
## Q
TLS 1.3 session resumption: how do session tickets cut handshake cost, and why must 0-RTT early data be idempotent?

## A
After a full handshake the server issues an encrypted **session ticket**; on reconnect the client presents it as a pre-shared key — resuming without certificate exchange, and optionally sending application data **in the very first flight** (0-RTT).

0-RTT data is **replayable**: an attacker can capture that flight and re-send it, and the server can't tell — so only requests that are safe to execute twice (idempotent GETs) may ride 0-RTT; never mutations. Servers also rotate ticket keys, since a stolen ticket key retro-decrypts early data.
