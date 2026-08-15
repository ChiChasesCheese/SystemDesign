---
id: oop-program-to-interface-scope
node: oop.interfaces
type: qa
---
## Q
"Program to an interface" — where does it pay off in a machine coding round, and where does it become interface bloat?

## A
- **Pays** at variation points and boundaries: pricing/allocation strategies, notification channels, storage — so extension probes are additive and tests can inject fakes.
- **Bloat**: an interface per class with one implementation and no seam need — pure ceremony (speculative generality).

Extract the interface when the second implementation or the test seam actually arrives; requirements hinting at variants ("support multiple pricing schemes") count as arrival.
