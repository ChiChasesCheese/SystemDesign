---
id: foundations-tail-latency-amplification
node: foundations.numbers
type: cloze
---
Tail latency amplification: a page fans out to 100 backend calls, each avoiding its slow path 99% of the time — the whole page avoids all slow paths with probability 0.99¹⁰⁰ ≈ {{c1::37%}}, so {{c2::~63%}} of user requests hit at least one p99-slow call. Fan-out turns a backend's {{c3::p99 into roughly the user-facing median}} — which is why high-fan-out services obsess over tails, not medians.
