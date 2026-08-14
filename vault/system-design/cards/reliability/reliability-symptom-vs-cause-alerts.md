---
id: reliability-symptom-vs-cause-alerts
node: reliability.slo
type: qa
---
## Q
"Page on symptoms, ticket on causes" — what does that mean, and why does cause-based paging (CPU > 90%, disk 80% full) rot an on-call rotation?

## A
- **Symptom alerts** fire on what users experience — the SLIs behind your SLO (error rate, latency). Every page then means real or imminent user impact and maps to budget burn ([[reliability-burn-rate-alerting]]).
- **Cause alerts** fire on internal states that *might* cause impact. Most are false alarms (high CPU with healthy latency), and no finite list of causes covers every failure — so you get both noise *and* misses.

Cause signals still matter — as **dashboards and tickets** for debugging and slow-moving risks (disk filling over days), not pages. Rule: a page must be urgent, user-impacting, and actionable.
