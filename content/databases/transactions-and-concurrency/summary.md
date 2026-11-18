## What to remember

- A **transaction** has the ACID properties: atomicity, consistency, isolation and durability. Concurrency control gives isolation; recovery gives atomicity and durability.
- A schedule is **serializable** when it is equivalent to some serial schedule. Conflict serializable schedules are a subset of view serializable ones, which are a subset of final-state serializable ones, and both inclusions are strict.
- Two actions **conflict** when they come from different transactions, touch the same item and at least one writes. A schedule is conflict serializable exactly when its conflict graph is acyclic, which is tested in polynomial time; testing view serializability is NP-complete.
- **Two-phase locking** guarantees conflict serializability, in the order of the lock points. **Strict 2PL**, which holds exclusive locks to the end, also gives recoverable and cascadeless schedules. Locking can deadlock: a scheduler detects cycles in a wait-for graph and aborts a victim, or prevents them with wait-die or wound-wait, where a restart keeps its timestamp.
- **Timestamp ordering** and **optimistic concurrency control** use no locks and so have no deadlocks; they abort in place of waiting. Basic timestamp ordering is not recoverable unless commits are delayed. The **Thomas write rule** skips obsolete writes and accepts some schedules that are view but not conflict serializable.
- **Multiversion concurrency control** serves reads from older versions, so readers do not block writers. Its correctness notion is one-copy serializability.
- **Snapshot isolation** reads from a snapshot and lets the first committer win among concurrent writers of an item. It prevents lost updates but allows write skew, so it is not serializable. **Serializable snapshot isolation** aborts a transaction that could be the pivot of two consecutive read-write dependencies between concurrent transactions; every history it commits is serializable, and some of its aborts are false positives.
- The SQL **isolation levels** are defined by the anomalies they forbid. Defined only by the phenomena of the standard they are ambiguous, and snapshot isolation and repeatable read are incomparable.
- Row locks do not stop **phantoms**: a new row that matches a query condition was never locked. Predicate locks cure this exactly; next-key locks on an index are the practical form.

## The schedulers side by side

| Method | On a conflict | Deadlock | Guarantee |
|---|---|---|---|
| [Two-phase locking](/two-phase-locking/) | wait | possible, detect or prevent | conflict serializable |
| [Strict 2PL](/strict-two-phase-locking/) | wait | possible, detect or prevent | also strict, so recoverable and cascadeless |
| [Wait-die, wound-wait](/wait-die-and-wound-wait/) | wait or abort by age | none | as for the 2PL beneath |
| [Timestamp ordering](/timestamp-ordering/) | abort the late transaction | none | conflict serializable in timestamp order |
| [Optimistic](/optimistic-concurrency-control/) | abort at validation | none | conflict serializable in validation order |
| [Multiversion TO](/multiversion-concurrency-control/) | read an old version, or abort a late write | none | one-copy serializable |
| [Snapshot isolation](/snapshot-isolation/) | first committer wins | readers never wait | not serializable: write skew |
| [Serializable SI](/serializable-snapshot-isolation/) | abort a possible pivot | readers never wait | serializable, with false aborts |

: The main schedulers of the chapter. A deadlock is possible only where a transaction waits for a lock; methods that abort in place of waiting have none, but may abort the same work many times.

## How to choose

Most systems use strict 2PL or a multiversion method. Strict 2PL is the safe default for short transactions with real contention: it is serializable, needs no extra validation, and its deadlocks are rare and cheap to detect. Multiversion methods help when long reads run beside short writes, because a reader never blocks a writer. If you use snapshot isolation, know which of your transactions can form write skew, and either add a conflict by hand or use serializable snapshot isolation. Optimistic validation pays off when conflicts are rare and aborts are cheap. Never trust an isolation level by its name alone; check which anomalies it allows in your system.
