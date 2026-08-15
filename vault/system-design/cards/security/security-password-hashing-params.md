---
id: security-password-hashing-params
node: security.authn.credentials
type: qa
---
## Q
You must store user passwords and also verify high-entropy API keys. Which algorithm and parameters for each, and why are they different?

## A
**Passwords — a slow, memory-hard KDF.** Argon2id is the default (OWASP baseline ~19 MiB memory, t=2, p=1); bcrypt cost ≥ 12 is acceptable legacy (watch its 72-byte input truncation); scrypt if Argon2 is unavailable. Tune parameters to ~**100–250 ms** per verify on your hardware, then sanity-check that against peak login QPS — password hashing is a deliberate CPU cost and a login stampede can saturate the fleet.

Why: human passwords have maybe 20–30 bits of entropy, so the only defense after a DB leak is making each guess expensive. **Memory-hardness** is the point — it denies GPUs/ASICs the parallelism that lets them do billions of SHA-256/s.

**API keys, session tokens — plain SHA-256 is correct.** A 128-bit random secret is unguessable by brute force, so a slow KDF buys nothing and would add 100 ms to *every API request*. Store the hash, show the key once.

Also: a **per-user salt** (already inside the modular hash string) defeats rainbow tables and shared-password detection; an optional **pepper** held in a KMS/HSM — not in the DB — makes a database-only leak useless.
