---
id: method-design-pitch-before-coding
node: method.delivery
type: qa
---
## Q
You have a class sketch and 60 minutes of coding ahead. How do you present the design in ~3 minutes so the interviewer can redirect you *before* you write code?

## A
Present it as a **walk, not a catalogue**:

- Name the 5–7 core types in one breath, then trace one flow through them: "`Gate` asks `SpotAllocator` → `Lot` reserves → `Ticket` issued."
- Call out the **variation points** you're putting behind interfaces and why (`FareStrategy`, because pricing was hinted at).
- State what you're deliberately leaving as a stub, then explicitly ask: "anything you want moved before I start typing?"

The ask is the point — a redirect costs 30 seconds now and 20 minutes after the code exists.
