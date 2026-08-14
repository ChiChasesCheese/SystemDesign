---
id: storage-protobuf-tag-rules
node: storage.encoding
type: qa
---
## Q
In Protobuf, what identifies a field on the wire, and what are the evolution rules that follow from it?

## A
The **field tag number** — the wire format carries `(tag, wire-type, value)`, never field names. Hence:

- **Renaming a field is free** (names are code-only); **changing its tag breaks everything** — old data decodes into the wrong field.
- **Never reuse a removed field's tag** (`reserved` it): old records with that tag would silently decode as the new field. Silent corruption, not an error.
- **New fields must be optional / have defaults** so old data (which lacks them) still parses — backward compat.
- Old code skips **unknown tags** using the wire type to know how many bytes to skip — forward compat.
