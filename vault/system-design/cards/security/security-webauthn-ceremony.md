---
id: security-webauthn-ceremony
node: security.authn.credentials
type: qa
---
## Q
At a systems level: what does your server store per passkey, and what must it verify on each login ceremony?

## A
**Registration** — server issues a random **challenge**; the authenticator generates a keypair scoped to your **RP ID** and returns the public key. You persist: `credential_id`, `public_key`, `user_handle` (an opaque per-user id, not the email), sign counter, and transports. Attestation is usually `none` for consumer passkeys — you're not verifying the hardware model.

**Authentication** — server issues a fresh challenge; the authenticator signs `authenticatorData || SHA-256(clientDataJSON)`. The server verifies:
- Signature against the **stored public key** for that `credential_id`.
- `challenge` matches the one it just issued and is **single-use** (this is the replay defense).
- `origin` in clientDataJSON is an expected origin, and the `rpIdHash` matches your RP ID.
- **UP** (user present) and, for passwordless/step-up, **UV** (user verified) flags are set.

Two design consequences: the **RP ID is baked into every credential** — it must be a registrable domain suffix (`example.com`, not `app.example.com`) or a later domain change invalidates every passkey; and with **synced** passkeys the sign counter stays 0, so clone detection via counter regression is effectively gone. Store multiple credentials per user — the credential, not the user, is the unit of enrollment and revocation.
