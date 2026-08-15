---
id: security-passkeys-phishing
node: security.authn.credentials
type: qa
---
## Q
Why are passkeys (WebAuthn) phishing-resistant when passwords + TOTP codes are not?

## A
Password and TOTP are **user-typeable secrets** — a fake site can ask for them and relay them to the real site in real time (proxy phishing defeats OTP).

Passkeys sign a **challenge with a device-held private key**, and the browser scopes the credential to the **origin** it was registered on:

- On `evil-bank.com`, the browser simply has no credential for that origin — there is nothing to phish and nothing to relay.
- The private key never leaves the authenticator (or synced keychain), so there's no shared secret on the server to breach — the server stores only public keys.

Per-site keypairs also kill credential reuse/stuffing. This is why 2026 guidance treats passkeys, not SMS/TOTP, as the strong second (or only) factor.
