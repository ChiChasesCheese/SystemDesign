---
id: distributed-conflict-detection-siblings
node: distributed.replication.multi-leader
type: qa
---
## Q
Mechanically, how does a replica decide that two writes to the same key *conflict* rather than one superseding the other — and what does it do with the pair?

## A
Each key carries a **version vector** (one counter per leader/replica). A client reads, gets the value plus its version (an opaque "causal context"), and echoes that version on the next write. On arrival the replica compares:

- Incoming version **dominates** the stored one (≥ in every slot) → the writer saw the stored value; **overwrite**.
- Versions are **incomparable** → genuinely concurrent; keep **both as siblings**.

Siblings are then resolved by application semantics — merge (union a shopping cart, take the max), let the user pick, or apply a type whose merge is defined (CRDT). Riak/Dynamo expose siblings explicitly; the *failure* is a store that silently collapses incomparable versions with a timestamp, because that discards a write the system knew was concurrent.
