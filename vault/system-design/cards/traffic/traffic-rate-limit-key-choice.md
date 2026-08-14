---
id: traffic-rate-limit-key-choice
node: traffic.rate-limiting
type: qa
---
## Q
What key do you rate limit on — and what goes wrong with per-IP limits?

## A
Primary: the **authenticated principal** (API key / user id) — the unit quotas and billing are written against. Per-IP is the fallback for unauthenticated endpoints (login, signup) but fails both ways: CGNAT puts thousands of legitimate users behind one IP (false positives), while botnets spread across thousands of IPs (false negatives).

Production layers several: a global limit protecting infrastructure, per-principal limits for fairness, and per-endpoint limits weighted by cost — expensive operations (search, export) may count units of work, not requests.
