---
id: storage-avro-schema-resolution
node: storage.encoding
type: qa
---
## Q
Avro encodes no field names *and* no tag numbers — just values in order. How can a reader with a different schema version decode it?

## A
Decoding requires the exact **writer's schema**; the reader then performs **schema resolution** against its own **reader's schema**: fields matched **by name** (order may differ), reader-only fields filled from defaults, writer-only fields skipped.

Where the writer's schema comes from without bloating every record:
- **Files**: schema once in the file header, millions of records after it.
- **Kafka**: a **schema registry** — each message carries a small schema ID.

Payoff vs Protobuf: no tag-number bookkeeping, so schemas can be **generated dynamically** (e.g. from a DB schema per table) — which is why Avro dominates data-pipeline/CDC tooling.
