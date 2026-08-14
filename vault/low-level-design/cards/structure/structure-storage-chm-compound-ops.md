---
id: structure-storage-chm-compound-ops
node: structure.storage
type: qa
---
## Q
You made the wallet store a `ConcurrentHashMap<UserId, Long>` and declared it thread-safe. Why does `map.put(user, map.get(user) + amount)` still lose money, and what's the correct call?

## A
`ConcurrentHashMap` makes each *individual* call atomic — not the **get-then-put compound**. Two concurrent deposits both read 100, both write 100+x; one deposit vanishes (lost update).

```java
map.merge(user, amount, Long::sum);          // atomic read-modify-write
map.computeIfAbsent(user, u -> new Wallet())  // atomic check-then-insert
```

`compute`/`merge`/`putIfAbsent` run atomically per key. If an operation spans **multiple keys** (transfer between two wallets), no map method saves you — you're back to explicit locks with ordered acquisition.
