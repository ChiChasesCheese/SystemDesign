---
id: method-splitting-one-entity
node: method.modeling
type: qa
---
## Q
What signals that one class in your model is really two entities — and what's the concrete refactor?

## A
Signals, strongest first:

- **Fields with different lifetimes**: `shippedAt`, `carrier`, `trackingId` are null for most of an `Order`'s life. Nullable-until-phase-X fields are a hidden second object.
- **Different cardinality later**: "an order can ship in multiple parcels" turns those fields into a list — the split was already implied.
- Disjoint field/method clusters, and different actors changing each half.

Refactor: extract `Shipment` as its own entity with its own id and lifecycle; `Order` holds zero-or-more of them. The null checks disappear because the state is now "no shipment yet."
