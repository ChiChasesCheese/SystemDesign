---
id: security-credential-stuffing
node: security.authn.credentials
type: qa
---
## Q
Credential stuffing vs brute force: why does per-account rate limiting barely help, and what actually detects it?

## A
Brute force is *many guesses against one account*; **stuffing replays leaked username+password pairs across millions of accounts** — typically **one or two attempts per account**, from a large residential proxy pool. It never trips a per-account limiter, and the passwords are correct, so hashing cost doesn't matter either.

What detects and blocks it:
- **Fleet-level signals, not per-request ones**: a sudden shift in the global login **failure ratio**, one client/ASN touching thousands of distinct usernames, or unusual success clustering. Rate-limit per IP **and** per ASN/fingerprint **and** globally per endpoint.
- **Breached-credential screening** at signup, login, and password change (HIBP k-anonymity range API — you send 5 hash chars, never the password).
- **Risk-based step-up**: new device/IP/geo → require the second factor or an email confirmation, rather than blocking outright.
- **Passkeys / WebAuthn** remove the attack class entirely — there is no reusable shared secret to replay.

Avoid: locking accounts after N failures (turns stuffing into a **DoS against your users**), and relying on CAPTCHA alone (solver farms cost cents per thousand).
