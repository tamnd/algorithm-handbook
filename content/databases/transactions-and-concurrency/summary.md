## What to remember

- A **transaction** has the ACID properties: atomicity, consistency, isolation and durability. Concurrency control gives isolation; recovery gives atomicity and durability.
- A schedule is **serializable** when it is equivalent to some serial schedule. Conflict serializable schedules are a strict subset of view serializable ones, which are a strict subset of final-state serializable ones.
- Aborts need classes of their own. **Strict** schedules are inside **cascadeless** ones, which are inside **recoverable** ones, all strictly, and recoverability is independent of serializability. Strict schedules let undo restore before images.
- Two actions **conflict** when they come from different transactions, touch the same item and at least one writes. By the **serializability theorem**, a schedule is conflict serializable exactly when its conflict graph is acyclic, and its serial orders are the topological orders; testing view serializability is NP-complete.
- **Two-phase locking** guarantees conflict serializability, in the order of the lock points. **Strict 2PL** also gives strict schedules. **Conservative 2PL** takes all locks at once and never deadlocks; otherwise a scheduler detects cycles in a wait-for graph, or prevents them with wait-die or wound-wait, where a restart keeps its timestamp. **Multiple granularity locking** adds intention modes so that a table lock and row locks can coexist, and the **tree protocol** is serializable and deadlock-free without being two-phase.
- Row locks do not stop **phantoms**. Predicate locks cure them exactly; **key-range locking** on an index, which locks the next key, is the practical form.
- **Timestamp ordering** and **optimistic concurrency control** abort in place of waiting, so they have no deadlocks. The **Thomas write rule** skips obsolete writes. **Silo** validates with per-record version words and epochs, with no global counter. **Multiversion** schedulers serve reads from older versions, and their correctness notion is one-copy serializability, tested with a version order.
- The SQL **isolation levels** are defined by the anomalies they forbid, which are ambiguous as the standard states them. **Adya's levels** define them by cycles in the dependency graph instead, and **write skew** is the cycle of two read-write edges.
- **Snapshot isolation** prevents lost updates but allows write skew. By the **dangerous structure theorem**, every cycle it allows has two consecutive read-write edges between concurrent transactions; **serializable SI** aborts a possible pivot, with some false positives, and a workload is **robust** when no such cycle can arise.
- Weaker contracts buy concurrency. **Commitment ordering** makes serializability compose across sites; **transaction chopping** commits pieces of known programs when no SC-cycle exists; a **saga** undoes completed steps with compensations and has no isolation between steps; **escrow** lets concurrent updates of a counter commit while every outcome keeps its bounds.

## The schedulers side by side

| Method | On a conflict | Deadlock | Guarantee |
|---|---|---|---|
| [Two-phase locking](/two-phase-locking/) | wait | possible, detect or prevent | conflict serializable |
| [Strict 2PL](/strict-two-phase-locking/) | wait | possible, detect or prevent | also strict, so recoverable and cascadeless |
| [Conservative 2PL](/conservative-two-phase-locking/) | wait before the start | none | serializable in admission order |
| [Tree protocol](/tree-locking-protocol/) | wait | none | serializable, not always recoverable |
| [Timestamp ordering](/timestamp-ordering/) | abort the late transaction | none | conflict serializable in timestamp order |
| [Optimistic](/optimistic-concurrency-control/), [Silo](/silo-concurrency-control/) | abort at validation | none | conflict serializable in validation order |
| [Multiversion TO](/multiversion-concurrency-control/) | read an old version, or abort a late write | none | one-copy serializable |
| [Snapshot isolation](/snapshot-isolation/) | first committer wins | readers never wait | not serializable: write skew |
| [Serializable SI](/serializable-snapshot-isolation/) | abort a possible pivot | readers never wait | serializable, with false aborts |

: The main schedulers of the chapter. A deadlock needs a cycle of transactions that wait for each other's locks. Conservative 2PL and the tree protocol wait but rule such cycles out; methods that abort in place of waiting have none, but may abort the same work many times.

## How to choose

Most systems use strict 2PL, with intention locks and key-range locks, or a multiversion method. Strict 2PL is the safe default for short transactions with real contention. Multiversion methods help when long reads run beside short writes. If you use snapshot isolation, check whether your workload is robust, and otherwise add a conflict by hand or use serializable snapshot isolation. Optimistic validation pays off when conflicts are rare and aborts are cheap. For long business processes use sagas, and for hot counters escrow. Never trust an isolation level by its name alone.
