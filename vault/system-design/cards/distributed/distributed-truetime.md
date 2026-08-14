---
id: distributed-truetime
node: distributed.time
type: cloze
---
Spanner's TrueTime API returns not a timestamp but {{c1::an interval [earliest, latest] bounding the true time (uncertainty from GPS/atomic clock sync, typically a few ms)}}. To make timestamp order match real-time order, a transaction {{c2::commit-waits: holds its result until `latest` of its commit interval has passed}}, guaranteeing every later-starting transaction gets a strictly greater timestamp — this is how Spanner achieves external consistency (strict serializability) across datacenters, paying clock uncertainty as write latency.
