---
id: patterns-command-when
node: patterns.behavioral
type: qa
---
## Q
Command turns a method call into an object. Name the three capabilities you buy that a plain call can't give, and the LLD problems where each shows up.

## A
Reifying `execute()` (plus receiver and args) as an object lets you:

- **Queue / schedule / log** invocations — thread-pool tasks, job queues, write-ahead logs, request replay.
- **Undo/redo** — each command carries `undo()` (or a memento); a history stack replays or reverts (text editor, drawing app).
- **Compose and parameterize** — macro commands, binding the same button to different actions, transactional batches.

Cost: one class (or lambda) per action. In languages with first-class functions, a bare lambda *is* a command — reach for the full pattern only when you need undo state or metadata alongside the action.
