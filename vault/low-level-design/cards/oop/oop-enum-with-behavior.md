---
id: oop-enum-with-behavior
node: oop.values
type: qa
---
## Q
When does an enum with behavior (per-constant fields/methods) beat a class hierarchy for variants — and what signals you've outgrown the enum?

## A
- **Enum wins** for a small, closed variant set whose behavior is a pure function of the variant: `VehicleType.SUV.spotSize()` — constants and logic co-located, switches exhaustiveness-checked.
- **Outgrown** when variants need their own mutable state, substantially distinct logic, or open extension (new variants without editing the enum) → promote to interface + one class per variant (strategy).
