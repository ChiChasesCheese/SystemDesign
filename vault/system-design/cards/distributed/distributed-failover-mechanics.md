---
id: distributed-failover-mechanics
node: distributed.replication.leader
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

## Q zh
故障转移的机制是什么？哪些问题可能发生？

## A zh
**流程**：
1. 检测主库故障（心跳超时）。
2. 选举新主库（从从库中选，可能丢失未复制的数据）。
3. 将从库提升为主库。
4. 更新客户端和从库的连接配置。

**问题**：
- **数据丢失**：未复制的写操作会丢失（async replication）。
- **脑裂（split-brain）**：旧主库网络隔离但仍在运行，新主库也在运行→两个主库同时接收写，冲突。
- **客户端不一致**：某些客户端先知道新主库，某些仍连着旧主库，导致暂时的写不一致。

缓解：使用 quorum 确认、fencing token、以及快速故障检测。
