---
id: async-eos-boundary-choice
node: async.delivery.exactly-once
type: qa
---
## Q
Broker transactions or a transactional outbox? State the rule for choosing, and one place people wrongly assume broker EOS extends.

## A
The rule follows from **where the atomic boundary can physically be** — a transaction only spans one system:

- **System of record is the broker** (consume → transform → produce, offsets are just another topic write): use **broker transactions**. Input offsets and output records commit together inside Kafka.
- **System of record is your database** (an HTTP command mutates rows and must emit an event): the broker cannot enlist in your DB commit, so the atomic unit must be the **DB transaction** — write state + event row together (outbox) and publish from that row afterwards. Broker transactions are useless for this half.

Where it wrongly gets assumed to extend: **across clusters**. Replication (MirrorMaker 2, cross-region mirroring) re-produces records and is at-least-once with new offsets — transactional guarantees and offsets do not survive the hop. Same for a second broker of a different type in the chain: each boundary needs its own dedup.
