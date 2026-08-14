---
id: patterns-chain-of-responsibility
node: patterns.behavioral
type: qa
---
## Q
What request shape calls for chain of responsibility, and how does it differ from a decorator stack (same "linked wrappers" look)?

## A
Use it when a request should pass along a pipeline of handlers where **each may handle, transform, or reject, and the set/order must be configurable**: HTTP middleware (auth → rate-limit → validate), approval escalation (manager → director → VP), logging levels, support-ticket routing.

```java
abstract class Handler {
    Handler next;
    void handle(Request r) { if (!process(r) && next != null) next.handle(r); }
}
```

Vs decorator: a decorator **always delegates** — every layer runs, the point is *accumulating behavior*. A CoR handler **may stop the chain** — the point is *finding who deals with it* (or filtering). Also be explicit about the fall-through policy: what happens when no handler accepts (default handler vs error).
