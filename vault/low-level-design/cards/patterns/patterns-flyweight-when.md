---
id: patterns-flyweight-when
node: patterns.structural
type: qa
---
## Q
Flyweight: what state do you split, and what constraint makes the shared part safe?

## A
Split object state into:

- **Intrinsic** — identical across many instances (glyph shape, tree species mesh/texture, chess piece type). Stored once, **shared** via a factory/cache.
- **Extrinsic** — varies per use (position, color, owner). Passed in by the caller at each operation: `species.render(x, y)`.

The shared intrinsic part must be **immutable** — otherwise one user's mutation corrupts every other user.

Use only when instance counts are large enough that memory actually hurts (millions of particles/glyphs/cells); for ordinary object counts it's needless indirection. `Integer.valueOf` caching and string interning are the stock real-world examples.
