---
nodes: [concurrency.model, concurrency.primitives, concurrency.patterns, structure.state-machines, method.evaluation]
tags: [classic, hard]
---
# Drill: In-process job scheduler

Code a scheduler an application embeds: submit a job to run after a delay
or on a fixed interval, run jobs on a bounded worker pool, cancel a
pending or running job, and shut down without losing work in flight. This
is the concurrency round in the shape it is actually asked.

**Constraints to state and honor**
- Bounded worker pool; submissions past capacity block or are rejected — say which, and why.
- Cancellation is observable: a cancelled job never starts, and a running one is asked to stop cooperatively.
- `shutdown()` drains; `shutdownNow()` interrupts. Both must terminate.
- Jobs are user code: one that throws, or blocks forever, must not take the pool down.
- Tests must not depend on real sleeping — the clock is a dependency.

**Grading points**
- The job lifecycle drawn as explicit states (pending → running → done/failed/cancelled) with the legal transitions, not flags — [[structure.state-machines|State Machines]].
- A delay queue guarded by one lock and a condition variable, waiting in a loop, signalled when an earlier job is inserted — [[concurrency.primitives|Synchronization Primitives]].
- Producer–consumer with a bounded queue, and a stated policy when it is full — [[concurrency.patterns|Concurrency Patterns]].
- Every field shared across threads justified: what makes the cancellation flag visible to the worker — [[concurrency.model|Threads & Memory Model]].
- Check-then-act on cancel-versus-start closed inside the state transition, not left as two statements — [[concurrency.model|Threads & Memory Model]].
- User exceptions caught at the worker boundary and recorded on the job, so the thread survives — [[concurrency.patterns|Concurrency Patterns]].
- Injected clock; you demonstrate a scheduling test that runs in milliseconds — [[method.evaluation|Evaluation Rubric]].
- You trace one interleaving out loud (cancel arriving exactly as the worker dequeues) before being asked — [[method.evaluation|Evaluation Rubric]].

**Attempt log**
- [ ] Attempt 1 (date, 60 min, self-graded notes):
