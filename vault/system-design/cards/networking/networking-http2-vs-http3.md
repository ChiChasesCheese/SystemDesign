---
id: networking-http2-vs-http3
node: networking.protocols
type: qa
---
## Q
HTTP/2 multiplexes many streams over one TCP connection. What problem remains, and how does HTTP/3 fix it?

## A
**TCP-level head-of-line blocking**: one lost packet stalls *every* HTTP/2 stream on that connection until retransmission, because TCP delivers bytes in order.

**HTTP/3 runs on QUIC (over UDP)**: loss recovery is per-stream, so a dropped packet stalls only its own stream. QUIC also folds the TLS handshake in (1-RTT, 0-RTT on resume) and survives client IP changes via connection IDs — big wins on lossy mobile networks.
