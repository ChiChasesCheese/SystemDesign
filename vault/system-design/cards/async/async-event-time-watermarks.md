---
id: async-event-time-watermarks
node: async.streaming
type: qa
---
## Q
In stream processing, why window on event time instead of processing time, and what problem do watermarks solve?

## A
**Processing time** windows depend on when data *arrived* — a delayed producer or a replay shifts events into the wrong window and results become non-reproducible. **Event time** windows use timestamps in the data, so results are stable across delays and reprocessing.

But event time forces the question "when is a window complete?" — a **watermark** is the processor's claim that no events older than time T are still coming, letting it close windows. Events arriving after the watermark are *late data*: drop them, or emit corrected/updated window results.
