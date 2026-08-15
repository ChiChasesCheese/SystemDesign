---
id: structure-api-rich-return-contract
node: structure.api
type: qa
---
## Q
Parking-lot round: you can sign `park(Vehicle)` as returning `boolean` or returning a `Ticket`. The interviewer will add "compute the fee at exit" in 20 minutes. Which contract survives, and why?

## A
`Ticket park(Vehicle)` survives. The **rich return object** carries entry time, spot, and vehicle — `unpark(Ticket)` can compute fees, find the spot, and validate, all without changing any signature. The `boolean` version forces breaking changes for every new requirement and gives callers nothing to hand back.

General rule: return a **domain object that names the interaction** (Ticket, Booking, Receipt), not a bare success flag. New requirements then land as new *fields*, not new *signatures*.
