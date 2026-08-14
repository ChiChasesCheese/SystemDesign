---
id: oop-composition-vs-aggregation
node: oop.relationships
type: qa
---
## Q
`ParkingLot`–`Floor` vs `Course`–`Student`: which is composition, which aggregation — and what single question decides?

## A
Question: **does the part's lifetime end with the whole, under exclusive ownership?**

- `Floor` exists in exactly one lot and dies with it → **composition** (filled diamond).
- `Student` outlives the course and belongs to many → **aggregation** (hollow diamond).

Both are has-a; ownership + lifetime is the discriminator, and composition is the one your destructor/cascade-delete logic must respect.
