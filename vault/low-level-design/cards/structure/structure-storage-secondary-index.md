---
id: structure-storage-secondary-index
node: structure.storage
type: qa
---
## Q
Your repo stores `Map<OrderId, Order>` but `findByUser(userId)` is called constantly. How do you avoid the O(n) scan, and what's the correctness trap the index introduces?

## A
Maintain a **secondary index** inside the repository:

```java
Map<OrderId, Order> byId;
Map<UserId, Set<OrderId>> byUser;   // index holds ids, resolve via byId
```

The trap: the index and primary map must change **together** — every `save`, `delete`, and any update that changes the indexed field (order reassigned to another user: remove from old set, add to new) must update both, under the same lock/atomic operation. Keeping index writes *inside* the repository is exactly why the repository boundary exists — callers can't forget the second write.
