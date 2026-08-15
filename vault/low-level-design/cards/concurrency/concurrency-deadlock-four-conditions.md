---
id: concurrency-deadlock-four-conditions
node: concurrency.hazards
type: cloze
---
Deadlock requires **all four** Coffman conditions: {{c1::mutual exclusion}} (resources aren't shareable), {{c2::hold and wait}} (a thread holds one lock while waiting for another), {{c3::no preemption}} (locks can't be forcibly taken away), and {{c4::circular wait}} (a cycle of threads each waiting on the next). Breaking any one prevents deadlock — a **global lock acquisition order** breaks {{c5::circular wait}}, which is why lock ordering is the standard interview fix; `tryLock` with timeout breaks hold-and-wait.
