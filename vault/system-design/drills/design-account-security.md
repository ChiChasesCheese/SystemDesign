---
nodes: [security.authn.credentials, security.authz, traffic.rate-limiting, reliability.observability]
tags: [security]
---
# Drill: Design account sign-in and recovery

The login box: 200M accounts, an attacker with a list of a billion leaked
credentials, and a support queue full of people who lost their phone. The
design question that is really a threat-modelling question.

**Constraints to state and honor**
- Credential stuffing runs constantly from a rotating residential proxy pool — IP rate limiting alone will not do.
- Passkeys are the goal, passwords must keep working for years.
- Account recovery must be usable by a non-technical person and must not become the attacker's front door.
- Sign-in must stay available during a partial outage; degraded is acceptable, open is not.

**Grading points**
- Password storage specified concretely: a memory-hard KDF with named parameters, and the peppering/upgrade path when parameters change ([[security-password-hashing-params]]).
- Credential stuffing distinguished from brute force, with defences matched to it — per-account and per-credential-pair limits, breach-list checks, adaptive challenges ([[security-credential-stuffing]], [[traffic-rate-limit-key-choice]]).
- Rate limiting versus load shedding separated, and the response to a rejected attempt designed so it leaks nothing ([[traffic-rate-limiting-vs-load-shedding]], [[traffic-shedding-response]], [[traffic-distributed-rate-limiting]]).
- Passkeys explained by the property that matters — phishing resistance from origin binding, not "no password" ([[security-passkeys-phishing]], [[security-webauthn-ceremony]]).
- Recovery designed as the weakest link it is, with the trade between account loss and account takeover stated out loud ([[security-account-recovery]]).
- Session lifetime, step-up authentication for sensitive actions, and what a privilege change does to live sessions ([[security-sessions-vs-jwt]], [[security-access-refresh-tokens]]).
- Authorization checks placed at the boundary rather than trusted from the client, including the confused-deputy case in support tooling ([[security-rbac-vs-abac]], [[security-confused-deputy]], [[security-api-keys-vs-user-tokens]]).
- Detection designed in: the signals logged, the cardinality budget they cost, and the alert that fires on a stuffing wave rather than on every failed login ([[reliability-symptom-vs-cause-alerts]], [[reliability-metric-cardinality]], [[reliability-logs-metrics-traces]]).

**Attempt log**
- [ ] Attempt 1 (date, 40 min, self-graded notes):
