---
id: foundations-interview-opening-moves
node: foundations.method
type: qa
---
## Q
First five minutes of a system design interview: what two categories of requirements do you pin down, and what form should each take?

## A
- **Functional**: the 3–5 core use cases you will actually design for — explicitly scope out the rest ("I'll focus on posting and the feed; skip search").
- **Non-functional**: expressed as **numbers**, not adjectives — target scale (DAU, QPS), latency budget (e.g. p99 < 200 ms), availability target, read/write ratio, consistency needs.

Numbers matter because they are what later justify each design choice.
