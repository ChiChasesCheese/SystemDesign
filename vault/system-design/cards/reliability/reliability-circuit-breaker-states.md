---
id: reliability-circuit-breaker-states
node: reliability.resilience
type: qa
---
## Q
What problem does a circuit breaker solve that per-request timeouts and retries do not, and how do its three states work?

## A
Timeouts protect one call; a breaker protects the **caller's capacity** — when a dependency is down, threads/connections stop being wasted on calls that are doomed, and the dependency gets room to recover.

- **Closed**: normal traffic; failures counted.
- **Open**: failure rate tripped the threshold; calls fail fast (or serve fallback) without hitting the dependency.
- **Half-open**: after a cooldown, a few probe requests pass; success closes it, failure reopens it.
