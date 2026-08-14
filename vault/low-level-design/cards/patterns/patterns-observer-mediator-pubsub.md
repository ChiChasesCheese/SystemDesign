---
id: patterns-observer-mediator-pubsub
node: patterns.behavioral
type: qa
---
## Q
Observer vs mediator vs pub-sub — all decouple communicating objects. Separate them by topology and by who knows whom.

## A
- **Observer**: one-to-many, **subject knows its observers** (holds the list, calls them directly, usually synchronously). Observers know the subject to subscribe. Decouples subject from observer *types*, not existence.
- **Mediator**: many-to-many collapsed into a **star** — colleagues only know the mediator, which centralizes the interaction logic (air-traffic control, dialog coordinating its widgets). Use when peer-to-peer links have become a tangle; cost: the mediator can grow into a god object.
- **Pub-sub**: publisher and subscriber **don't know each other at all** — an event channel/broker sits between, often async. Strongest decoupling, weakest traceability.

Axis: how much the sender knows about receivers — observer (list of them) → mediator (one hub) → pub-sub (nothing).
