---
id: patterns-memento-vs-command-undo
node: patterns.behavioral
type: qa
---
## Q
You're asked to add undo. Memento and command both do it — how do the two approaches differ, and when do you pick each?

## A
- **Memento**: snapshot the originator's **state** before each change; undo = restore the snapshot. The memento is opaque to everyone but the originator, so encapsulation survives. Simple and bulletproof, but memory-heavy for large state (mitigate with diffs or copy-on-write).
- **Command with `undo()`**: store the **inverse operation** (`InsertText` undoes by deleting the range). Cheap per step and gives redo/replay for free, but every command must implement a correct inverse — and some operations aren't invertible (irreversible side effects, lossy edits).

Practical answer: commands for the history mechanism, carrying small mementos of just the affected fragment — the hybrid most editors use.
