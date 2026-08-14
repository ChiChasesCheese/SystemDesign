---
id: networking-connection-setup-cost
node: networking.protocols
type: cloze
---
A cold HTTPS request pays {{c1::1 RTT for the TCP handshake + 1 RTT for TLS 1.3}} before any application byte moves — on a 100 ms cross-region path that's ~200 ms of pure setup. This is why services use {{c2::keep-alive / connection pooling}} between fixed peers, and why QUIC offers {{c3::0-RTT resumption}} for repeat visitors.
