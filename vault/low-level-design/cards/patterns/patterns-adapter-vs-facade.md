---
id: patterns-adapter-vs-facade
node: patterns.structural
type: qa
---
## Q
Adapter vs facade — both "wrap other code". What's the discriminating question?

## A
Ask **"does an interface already exist that the client expects?"**

- **Adapter**: yes — the client is written against a target interface, and you convert an *incompatible existing* class to fit it (`SlackNotifier implements Notifier` wrapping the Slack SDK). Usually wraps **one** class; the shape is dictated by the target interface.
- **Facade**: no — you *invent a new, simpler* interface over a whole **subsystem** of classes to shield clients from its complexity (`OrderFacade.checkout()` hiding inventory + payment + shipping calls). Clients could bypass it; it exists for convenience and decoupling, not compatibility.

One-liner: adapter changes an interface's **shape**; facade reduces a subsystem's **surface**.
