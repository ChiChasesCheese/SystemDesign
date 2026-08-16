---
nodes: [oop.pillars, oop.interfaces, patterns.behavioral, method.modeling, method.evaluation]
tags: [classic, hard]
---
# Drill: Chess

The heaviest of the classic modelling rounds: six piece types with
different movement rules, plus castling, en passant, promotion, check and
checkmate. The trap is that it looks like a textbook inheritance exercise
and punishes you for treating it as one.

**Constraints to state and honor**
- Legal-move generation per piece, plus the rules that span pieces (you may not leave your own king in check).
- Undo of the last move, including the captured piece and the castling rights it consumed.
- Board state must be printable and comparable — you will want it for your own verification.
- 60 minutes: pawns and the king's special rules are where people run out of time. Sequence deliberately.

**Grading points**
- Nouns and verbs extracted before any class is written; the move — not just the piece — named as an object — [[method.modeling|Requirements to Objects]].
- `Piece` as an interface or thin abstract class over movement *rules*, not a five-deep hierarchy; the cost of inheritance stated where you use it — [[oop.pillars|OOP Pillars in Practice]].
- Board owns the invariant "no move may leave your own king attacked"; no piece is allowed to decide that alone — [[method.modeling|Requirements to Objects]].
- Command objects for moves, which is what makes undo a data structure instead of a reverse-engineering problem — [[patterns.behavioral|Behavioral Patterns]].
- Polymorphic move generation instead of a `switch` on piece type — [[oop.pillars|OOP Pillars in Practice]].
- Interfaces kept narrow enough that a test can stand up a two-piece board — [[oop.interfaces|Interfaces & Abstract Classes]].
- You verify a scholar's mate and one en-passant line yourself before the interviewer asks — [[method.evaluation|Evaluation Rubric]].
- The extension probe answered out loud: what changes to add a variant (Chess960, three-check)? — [[method.evaluation|Evaluation Rubric]].

**Attempt log**
- [ ] Attempt 1 (date, 60 min, self-graded notes):
