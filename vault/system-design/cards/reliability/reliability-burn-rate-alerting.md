---
id: reliability-burn-rate-alerting
node: reliability.slo
type: qa
---
## Q
Why alert on error-budget burn rate instead of a raw error-rate threshold, and how do multi-window burn alerts work?

## A
A fixed threshold either pages on blips (too sensitive) or sleeps through slow leaks (too dull). **Burn rate** = how many times faster than sustainable you are consuming the budget, which directly maps to "time until SLO is blown."

Standard practice: pair a **fast window** (e.g. 14.4x burn over 1h — 2% of a 30-day budget gone — page now) with a **slow window** (e.g. ~1–2x over days — ticket, not page). Both windows must fire, filtering transient spikes.
