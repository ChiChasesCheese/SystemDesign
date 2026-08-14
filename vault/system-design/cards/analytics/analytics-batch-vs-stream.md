---
id: analytics-batch-vs-stream
node: analytics.batch
type: qa
---
## Q
What is the real boundary between batch and stream processing, and how does each recover from failure?

## A
The input: batch reads a **bounded** dataset of known size (job can finish, sort, and take multiple passes); streaming reads an **unbounded** log and must produce results incrementally, forcing explicit handling of time — windows, watermarks, late events.

Recovery differs accordingly:
- **Batch**: throw away partial output, rerun the job — cheap because inputs are immutable and outputs atomic (see [[analytics-idempotent-reruns]]).
- **Stream**: can't replay from the beginning of time forever, so recover from periodic **checkpoints of operator state + log offsets**, replaying only since the last checkpoint.

Microbatching (Spark Structured Streaming) and unified engines blur the API, not this recovery distinction.
