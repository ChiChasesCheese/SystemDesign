---
id: foundations-when-estimates-change-design
node: foundations.estimation
type: qa
---
## Q
Give three estimate outcomes that each flip a design decision (the whole point of doing the math).

## A
- **Working set fits in RAM** (≲ a few hundred GB) → cache or serve it all from memory; no need to optimize disk paths.
- **Write QPS exceeds a single node** (~tens of thousands for a tuned DB) → partitioning is mandatory, choose a shard key now.
- **Read/write ratio is 100:1+** → invest in caching and read replicas, not write throughput.

If an estimate doesn't change any decision, say so and move on.
