---
id: principles-yagni-in-round
node: principles.simplicity
type: qa
---
## Q
In the machine coding round, how do you reconcile YAGNI with the interviewer's known love of extensibility probes?

## A
**Build seams, not features.** An interface at a variation point the requirements actually signal (pricing, spot allocation) costs one file and makes the probe answer additive. Don't build unrequested capability — config systems, factories over a single implementation, generics "for later."

When probed about something you skipped, pointing at the seam where it plugs in scores; dead speculative code reads as poor judgment, not foresight.
