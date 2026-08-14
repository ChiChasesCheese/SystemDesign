---
id: reliability-failover-modes-tradeoff
node: reliability.availability
type: qa
---
## Q
Rank hot, warm, and cold standby failover by recovery speed, and name the hidden risk hot standby adds.

## A
- **Hot (active-active or synced active-passive)**: seconds — standby already serves or has current state. Costs ~2x and risks **split-brain**: both nodes believe they are primary, so you need fencing/quorum before promoting.
- **Warm**: minutes — replica running but lagging; failover loses the replication-lag window of writes.
- **Cold**: hours — restore from backup; data loss up to last backup.
