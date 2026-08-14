---
id: method-noun-verb-extraction
node: method.modeling
type: qa
---
## Q
In noun–verb extraction from a requirements statement, what do nouns, verbs, and constraint sentences each become — and which nouns should you reject?

## A
- **Nouns** → candidate classes; **verbs** → responsibilities (methods), assigned to the noun that owns the data the verb touches.
- **Constraint sentences** ("a spot holds one vehicle") → invariants some class must enforce.
- **Reject**: synonyms of an existing noun, and attributes in disguise — "registration number" is a field on `Vehicle`, not a class.
