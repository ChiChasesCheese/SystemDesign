---
id: distributed-crdt-counters
node: distributed.crdt
type: cloze
---
A G-counter (grow-only) keeps {{c1::one slot per replica; each replica increments only its own slot}}; the value is {{c2::the sum of all slots}}, and merge is {{c3::element-wise max}} — max is idempotent, so re-merging never double-counts, which is exactly why a single shared integer can't work (summing two copies double-counts, max loses increments). A PN-counter supports decrement by {{c4::pairing two G-counters — increments and decrements — and reporting P − N}}. Limitation worth stating: it can transiently go below an intended floor (e.g. negative inventory), because no CRDT can enforce a global invariant without coordination.
