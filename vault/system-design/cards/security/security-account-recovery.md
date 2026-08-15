---
id: security-account-recovery
node: security.authn.credentials
type: qa
---
## Q
You ship passkey-only login. Why is your account's real security level probably still "SMS", and how do you design recovery?

## A
An account is only as strong as its **weakest path to a session**. Attackers don't break the passkey — they run the "lost my device" flow. If recovery is an emailed magic link, an SMS code (SIM swap), or a helpdesk call, that becomes the actual authentication mechanism, and the strong factor is decoration.

Design:
- **Prefer re-enrollment over reset**: register **≥2 passkeys** at signup (phone + laptop/security key) and issue single-use **recovery codes** shown once, hashed at rest. Recovery is then "authenticate with your other credential", not "prove you own an inbox".
- Make the fallback path **slow and loud**: a delay (hours to days) with notification to every registered channel and a cancel link, so the legitimate owner can veto. Attackers need silence and speed.
- **On successful recovery, revoke everything**: all sessions, refresh tokens, and API keys — and hold high-risk actions (payouts, changing recovery contacts) behind a cool-down.
- **Helpdesk is an attack surface** (the vector behind several 2023–2025 breaches): require verified, out-of-band identity proof; never let an agent enroll a factor on a caller's say-so.
- No knowledge-based questions — mother's maiden name is public data, not a secret.
