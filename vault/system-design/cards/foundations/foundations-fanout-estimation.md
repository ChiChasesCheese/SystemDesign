---
id: foundations-fanout-estimation
node: foundations.estimation
type: qa
---
## Q
Twitter-style home timelines: ~5k tweets/s written, ~300k timeline reads/s, avg 75 followers. Walk the fan-out-on-write math and the estimate that breaks it.

## A
Fan-out on write: 5k tweets/s × 75 followers ≈ **375k timeline-cache inserts/s** — heavy but feasible, and it makes the dominant operation (reads) a cheap precomputed lookup.

The **tail of the distribution** breaks it: one 100M-follower account tweeting = 100M inserts for a single event — impossible within a delivery SLO. Hence the hybrid: push for normal users, pull celebrity tweets at read time and merge.

Lesson: estimate with the skew, not the mean — averages hide the case that forces the design.
