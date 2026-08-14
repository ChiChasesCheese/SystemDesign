---
id: patterns-selection-cues
node: patterns.selection
type: cloze
---
Requirement phrase → pattern reflex: "support multiple/pluggable algorithms for X" → {{c1::strategy}}; "notify interested parties when X changes" → {{c2::observer}}; "add optional features in any combination" (coffee add-ons, stream wrappers) → {{c3::decorator}}; "undo/redo or queue operations" → {{c4::command}}; "object behaves differently through its lifecycle, some actions illegal in some phases" → {{c5::state}}; "treat single items and groups uniformly" → {{c6::composite}}; "request tries a configurable sequence of handlers" → {{c7::chain of responsibility}}.
