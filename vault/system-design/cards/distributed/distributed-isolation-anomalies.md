---
id: distributed-isolation-anomalies
node: distributed.transactions.isolation
type: qa
---
## Q
Map the standard isolation levels to the anomaly each one newly prevents, and name the anomaly snapshot isolation still allows.

## A
| Level | Newly prevents |
|---|---|
| Read committed | Dirty reads/writes |
| Repeatable read / **Snapshot isolation** | Non-repeatable (fuzzy) reads; SI gives a consistent point-in-time snapshot |
| Serializable | Everything, incl. **write skew** and phantoms |

**Snapshot isolation still allows write skew**: two transactions read the same snapshot, make disjoint writes based on it, and jointly violate an invariant. Practical notes: Postgres defaults to read committed; Postgres "repeatable read" *is* SI; its serializable is SSI (optimistic, aborts instead of locking).

## Q zh
分布式数据库的隔离级别异常有哪些？

## A zh
**脏读（dirty read）**：事务 A 读到事务 B 还未提交的数据。（READ UNCOMMITTED）

**不可重复读（non-repeatable read）**：事务 A 两次读同一行，中间被其他事务修改，两次读值不同。（READ COMMITTED）

**幻读（phantom read）**：事务 A 两次查询范围，中间被其他事务插入新行，第二次查询看到新行。（REPEATABLE READ）

**写倾斜（write skew）**：两个事务基于同一一致性约束做决策，各自通过检查但合并后违反约束。需要 SERIALIZABLE。

**丢失更新（lost update）**：两个事务并发修改同一行，一个的修改被另一个覆盖。
