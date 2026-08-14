---
id: principles-dry-limit
node: principles.simplicity
type: qa
---
## Q
Two modules contain near-identical 10-line blocks. When is extracting a shared helper the WRONG move?

## A
When the duplication is **accidental**: the blocks look alike today but encode different business knowledge that will change for different reasons. The merged helper then sprouts flags and branches per caller — the wrong abstraction.

DRY deduplicates *knowledge*, not text. Heuristics: "duplication is cheaper than the wrong abstraction" (Sandi Metz); wait for the rule of three before extracting.
