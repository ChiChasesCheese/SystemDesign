---
id: reliability-timeout-budget-arithmetic
node: reliability.resilience.retries
type: qa
---
## Q
Gateway → A → B → C, each hop with a 1s timeout and 3 attempts, under a 3s user-facing budget. Do the arithmetic and give the configuration rules.

## A
Retries **multiply down the stack**: C can take 3×1s = 3s; B wraps that in 3 attempts → 9s; A → 27s. The user's 3s budget is blown 9× over, and the extra attempts arrive at an already-sick C as 27× load.

Rules:
- **Retry at one layer only** — usually the one closest to the failure that can still classify the error, or the outermost that owns the budget. Never at every hop.
- Size the **per-attempt timeout from the dependency's p99 (times ~1.5–2)**, not from the mean and not from a framework default of 30–60s; a default-timeout client is how thread/connection pools get exhausted.
- **Total budget, not per-hop**: `attempts × per-attempt timeout ≤ remaining budget`, and each hop passes down its *remaining* time so inner deadlines are always strictly shorter than outer ones.
- Before starting an attempt, check the remaining budget against the dependency's **p50** — if it can't plausibly finish, fail fast instead of spending capacity on a request nobody will read.
