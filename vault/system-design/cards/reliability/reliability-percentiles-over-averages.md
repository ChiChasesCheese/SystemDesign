---
id: reliability-percentiles-over-averages
node: reliability.slo
type: qa
---
## Q
Why is p99 latency the SLI to watch instead of the mean — and why does fan-out make tail latency worse than it looks?

## A
Latency is heavily right-skewed: a healthy mean can hide a p99 of seconds, and the slowest requests often belong to your **heaviest users** (biggest carts, most data).

Fan-out amplifies the tail: a page calling 100 backends in parallel is as slow as the slowest one — with p99 = 1s per backend, ~63% of pages (1 − 0.99¹⁰⁰) hit at least one 1-second call. The tail becomes the common case.
