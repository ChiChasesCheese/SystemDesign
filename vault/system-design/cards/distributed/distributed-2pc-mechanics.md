---
id: distributed-2pc-mechanics
node: distributed.transactions.distributed
type: qa
---
## Q
Walk the two phases of 2PC and point at the exact commit point. Why can a participant that voted "yes" not simply time out and abort?

## A
1. **Prepare**: coordinator sends `prepare` with a global txid. Each participant does everything but commit — writes its changes and locks durably to its log — then answers **yes** (a promise it can commit under any subsequent crash) or **no**.
2. **Commit**: once all vote yes, the coordinator **writes its commit decision to its own durable log** — *that write is the commit point, and it is irrevocable*. Then it sends `commit`, retrying forever until every participant acknowledges.

A yes-voter can't unilaterally abort because it doesn't know whether the coordinator already reached the commit point: the `commit` message may simply be lost or delayed. If it aborted and the decision was commit, **atomicity is broken** — some participants committed, this one didn't. So it stays **in doubt**, holding its locks, blocking every conflicting transaction on that data, until the coordinator (or its recovered log) tells it the answer.

Worth adding: 3PC removes the block only under a synchronous network with reliable failure detection — assumptions real networks don't provide, which is why nobody ships it.

## Q zh
两阶段提交的两个阶段分别是什么？

## A zh
**Phase 1（投票）**：协调者要求所有参与者执行本地事务的准备工作，每个参与者原子性地锁定资源、验证业务逻辑，然后投票 "可以提交" 或 "无法提交"。

**Phase 2（提交/中止）**：根据所有投票结果，协调者要么命令所有参与者提交（所有投票都是 "可以"），要么命令全部中止（有任何一票是 "否"）。参与者执行该决议并释放锁。
