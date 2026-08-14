---
id: foundations-littles-law
node: foundations.estimation
type: cloze
---
Little's Law: average requests in flight = {{c1::arrival rate × average time in system (L = λ·W)}}. So 2,000 QPS at 50 ms mean response time means {{c2::100}} concurrent requests — the number that sizes worker pools, DB connection pools, and per-server concurrency limits. Corollary: when latency doubles under load, required concurrency {{c3::doubles too}}, which is how slowdowns exhaust pools and cascade.
