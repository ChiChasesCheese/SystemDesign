---
id: distributed-failover-mechanics
node: distributed.replication
type: qa
---
## Q
Walk through automatic leader failover in leader-follower replication, and name the three classic hazards.

## A
Steps: **detect** leader death (heartbeat timeout), **elect** the most up-to-date follower as new leader, **reconfigure** so clients and followers point at it.

- **Lost writes**: with async replication the new leader may lack the old leader's last acknowledged writes; discarding them breaks anything that already consumed them (GitHub incident: reused auto-increment IDs made a Redis cache serve wrong users' data).
- **Split brain**: the old leader comes back still thinking it leads; without fencing/STONITH both accept writes and diverge.
- **Bad timeout choice**: too short → needless failovers exactly when the system is slow under load, making the outage worse; too long → longer downtime.

That's why teams often keep failover **manual** for the system of record.
