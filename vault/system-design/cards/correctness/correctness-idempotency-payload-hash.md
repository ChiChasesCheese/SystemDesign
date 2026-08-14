---
id: correctness-idempotency-payload-hash
node: correctness.idempotency
type: cloze
---
An idempotency-key record must also store a {{c1::hash of the request payload (and the endpoint/params)}}; a request reusing the key with a **different** body must be {{c2::rejected with an error (Stripe: 422), never replayed or re-executed}} — otherwise a client bug that reuses keys across distinct operations gets the *first* operation's stored response and silently believes the second one succeeded.
