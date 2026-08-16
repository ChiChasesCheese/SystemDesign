---
nodes: [patterns.structural, patterns.selection, oop.interfaces, principles.solid, principles.composition]
tags: [classic, medium]
---
# Drill: Notification dispatcher library

Code the library other teams call to notify a user: email, SMS, and push
today; Slack and webhooks next quarter, added by *them*, not you. Each
channel needs templating, and some need retry, rate limiting, and an audit
log — but not the same ones.

**Constraints to state and honor**
- A new channel is a new class in the caller's own package: no edit to your dispatcher, no `switch` on channel type.
- Retry, rate limiting, and audit logging are opt-in per channel and stackable in any order.
- The third-party SMS SDK has an awkward, unchangeable signature; it must not leak into your interfaces.
- A user's preferences decide which channels fire; "quiet hours" suppress all but critical.

**Grading points**
- Channel as a narrow interface named for the caller's need, not the SDK's shape — [[oop.interfaces|Interfaces & Abstract Classes]].
- Decorator for retry/rate-limit/audit, so behaviours compose instead of multiplying subclasses — [[patterns.structural|Structural Patterns]].
- Adapter around the SMS SDK; facade for the one-line `notify(user, event)` entry point — [[patterns.structural|Structural Patterns]].
- Naming why decorator and not proxy or template method here, and refusing a pattern where a plain function does — [[patterns.selection|Choosing (and Refusing) Patterns]].
- Open/closed demonstrated concretely: walk through adding Slack without opening an existing file — [[principles.solid|SOLID]].
- Composition for the channel stack; inheritance only where the base genuinely is-a channel — [[principles.composition|Composition over Inheritance]].
- Interface segregation: a push-only channel is not forced to implement `attachFile` — [[principles.solid|SOLID]].

**Attempt log**
- [ ] Attempt 1 (date, 45 min, self-graded notes):
