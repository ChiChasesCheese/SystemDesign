---
id: architecture-registry-compat-modes
node: architecture.discovery
type: cloze
---
A schema registry's compatibility mode dictates **deploy order**: BACKWARD (new schema can read old data) means upgrade {{c1::consumers first}}, then producers; FORWARD (old schema can read new data) means upgrade {{c2::producers first}}; FULL allows {{c3::either order}}. Kafka-style event streams default to BACKWARD because consumers must be able to reprocess {{c4::old events retained in the log}} — the registry rejects an incompatible schema at publish/CI time, before it can strand data. See [[architecture-schema-compat-rules]].
