---
id: method-sequence-before-classes
node: method.modeling
type: qa
---
## Q
Why walk one concrete scenario ("car arrives → gets spot → ticket issued → ...") end-to-end *before* drawing the class diagram?

## A
The walkthrough forces every step onto some object, which exposes:

- **missing objects** — who computes the fee? who allocates the spot?
- **misplaced responsibilities** and the method signatures you actually need.

Class-diagram-first tends to produce data holders with no verbs; the gaps then surface mid-coding, when fixing them is most expensive.
