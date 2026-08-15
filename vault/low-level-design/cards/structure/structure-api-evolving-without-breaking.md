---
id: structure-api-evolving-without-breaking
node: structure.api
type: qa
---
## Q
Mid-round the interviewer keeps adding options to `search(String query)` — filters, sort, pagination. Name two evolution moves that don't break existing callers, and the smell if you don't.

## A
- **Parameter object**: `search(SearchQuery q)` where `SearchQuery` is a builder-built value object — new options become new optional fields, signature never changes again.
- **Overload delegation**: keep `search(String)` and have it delegate to the richer form with defaults (in interfaces, a `default` method does the same job).

The smell you're avoiding: a growing positional list `search(q, filter, sort, page, size, asc…)` where every addition breaks call sites and `null` gets passed for "don't care."
