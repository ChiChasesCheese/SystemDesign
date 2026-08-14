---
id: networking-long-polling-costs
node: networking.realtime
type: qa
---
## Q
What does a hanging long-poll request cost the server, and why do thread-per-request servers cap out first?

## A
Every waiting client holds an open connection and a parked request for up to the poll timeout (kept at ~30 s, under proxy idle limits). With thread-per-request servers that is a thread + stack per *idle* client — concurrency caps in the low thousands; event-loop/async servers hold a cheap file descriptor instead and reach 100k+.

Second cost: a broadcast event completes every parked request at once, and all those clients **immediately re-poll** — a synchronized request wave after each event, which SSE/WebSockets avoid by keeping the channel open.
