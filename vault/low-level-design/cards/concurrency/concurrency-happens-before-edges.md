---
id: concurrency-happens-before-edges
node: concurrency.model
type: cloze
---
The happens-before edges you actually use in an interview: unlocking a mutex → a later {{c1::lock of the same mutex}}; a volatile write → a later {{c2::read of the same volatile variable}}; everything before `Thread.start()` → {{c3::the started thread's first action}}; a thread's last action → {{c4::`join()` returning in the waiting thread}}. If two accesses aren't connected by such a chain, the read may see a stale or torn value.
