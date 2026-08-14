---
id: storage-json-contract-pitfalls
node: storage.encoding
type: qa
---
## Q
JSON is the default inter-service format anyway. Name its concrete weaknesses as a *data contract*, and what teams add to compensate.

## A
- **Numbers**: no int/float distinction, and integers beyond 2^53 silently lose precision in JS-lineage parsers — why Twitter-scale IDs ship as *strings*.
- **No binary type**: blobs go Base64 (+33% size).
- **No enforced schema**: compatibility lives in convention; nothing stops a producer renaming a field, and consumers find out at runtime.
- Verbose: field names repeated in every record (compression helps but parsing cost stays).

Compensations: **JSON Schema / OpenAPI** validation in CI, contract tests between producer and consumer, and switching to Protobuf/Avro with a registry where evolution guarantees must be machine-checked.
