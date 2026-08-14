---
id: correctness-ledger-cutoff-settlement
node: correctness.ledger
type: qa
---
## Q
Why does a ledger need a business date and cutoff time distinct from event timestamps, and what happens to entries that arrive after cutoff?

## A
Reports, reconciliation, and settlement all run against a **closed accounting day**: "balance as of end of business date D" must be **frozen** — re-runnable forever with the same result — or every downstream report and payout is unstable.

- Each entry gets a **business/posting date** assigned at write time; at cutoff (e.g. 23:59 in a declared timezone) the day closes and its totals freeze.
- A late-arriving event (processor webhook at 00:30 for yesterday's charge) **posts to the current open day**, carrying its original event time as an attribute — never inserted into the closed day.
- Settlement runs on closed windows: payout for day D = sum of D's closed entries; late items ride the next window.

Same immutability logic as [[correctness-ledger-immutability]], applied to time: closed periods are append-never.
