---
id: storage-rolling-upgrade-compat
node: storage.encoding
type: qa
---
## Q
Why does a rolling deploy force you to maintain *both* backward and forward compatibility at once — and why does data in a database raise the bar further?

## A
During the rollout old and new instances run side by side, and messages/RPCs flow both ways: new code reads what old code wrote (**backward**), and old code reads what new code wrote (**forward**). Break either and you can only deploy with downtime — and rollback breaks too.

Databases are stricter because **data outlives code**: a row written five years ago is still read by today's code (backward compat across *years* of schema versions), and after adding a column, old rows simply lack it — readers must handle the default, since rewriting the whole dataset is usually prohibitive.
