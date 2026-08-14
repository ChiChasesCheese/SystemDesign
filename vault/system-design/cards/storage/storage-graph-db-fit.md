---
id: storage-graph-db-fit
node: storage.nosql
type: qa
---
## Q
What query shape justifies a graph database over a relational schema with join tables?

## A
**Variable-depth, multi-hop traversals**: "friends-of-friends-of-friends", fraud rings, dependency chains — where the number of hops isn't fixed at query time.

Relationally, each hop is another self-join whose cost grows with total edge-table size; a graph DB stores adjacency directly, so traversal cost scales with the **edges actually touched**, not the whole graph.

If your queries are fixed one/two-hop lookups ("this user's friends"), join tables with proper indexes are fine — don't pay the operational cost of a niche database for that.
