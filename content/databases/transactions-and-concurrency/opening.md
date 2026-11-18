A database serves many users at once. Each of them runs transactions, groups of reads and writes that should act as one step: a transfer debits one account and credits another, and nobody should see the money in neither or in both. If the system ran the transactions one after another, this would be easy, but slow. It interleaves their actions instead, and the interleaving can produce results that no one-at-a-time run could give: a lost update, a read of data that is later rolled back, or two checks that each pass while their combination breaks a rule.

This chapter is about the theory that says which interleavings are correct and the schedulers that produce only those. The theory turns a schedule into a graph and asks whether the graph has a cycle. The schedulers lock items, compare timestamps, validate at commit, or keep old versions. Real systems also offer weaker isolation levels for speed, and the chapter says exactly what each of them allows.

## What the chapter covers

The chapter is in six groups, read in order.

1. **Transactions and what correct means.** The [ACID properties](/acid-properties/). [Serializability](/serializability/), with its three nested classes from final-state, view and conflict equivalence. The [isolation levels](/isolation-levels/) of SQL and their anomalies, from dirty writes to write skew.
2. **Testing a schedule by its conflicts.** The [conflict graph](/conflict-graph/) and [conflict serializability](/conflict-serializability/), which holds exactly when that graph is acyclic.
3. **Schedulers without locks.** The [concurrency control problem](/concurrency-control/) itself, then [optimistic concurrency control](/optimistic-concurrency-control/), [timestamp ordering](/timestamp-ordering/), [multiversion concurrency control](/multiversion-concurrency-control/) and [snapshot isolation](/snapshot-isolation/), which is not serializable because of write skew.
4. **Locking.** [Two-phase locking](/two-phase-locking/), which guarantees conflict serializability; [strict two-phase locking](/strict-two-phase-locking/), whose schedules are also recoverable and cascadeless; and the deadlock prevention rules [wait-die and wound-wait](/wait-die-and-wound-wait/).
5. **Beyond conflicts and rows.** [View serializability](/view-serializability/), larger than conflict serializability and NP-complete to test. The [phantom problem](/phantom-problem/) and its cure by [predicate locking](/predicate-locking/).
6. **Two refinements.** The [Thomas write rule](/thomas-write-rule/) for timestamp ordering, and [serializable snapshot isolation](/serializable-snapshot-isolation/), which aborts the possible pivots of dangerous structures.

The entries on the schedule as an object, the serializability and two-phase locking theorems, recoverable, cascadeless and strict schedules, conservative two-phase locking, the lock table, multiple granularity, tree and key-range locking, commitment ordering, multiversion serializability, the NP-completeness proof for view serializability, write skew and the dangerous structure theorem, Adya's generalized isolation levels, robustness against weak isolation, transaction chopping, sagas, the escrow method and Silo are not written yet. Several of these appear briefly inside the written entries.

## A first reading

For a first reading, take these nine entries in order: ACID properties, serializability, the conflict graph, conflict serializability, the concurrency control problem, two-phase locking, strict two-phase locking, isolation levels and snapshot isolation. They give the definition of correctness, the test for it, the scheduler that most systems use, and the weaker guarantee that many systems give by default.

Then read timestamp ordering and multiversion concurrency control for the other main family of schedulers, and serializable snapshot isolation to see how the gap left by snapshot isolation is closed. View serializability, the Thomas write rule and the phantom problem can wait until the basic picture is clear.

## Before you start

The tests on schedules are graph algorithms: a schedule is conflict serializable when its graph has no cycle, found by [cycle detection with DFS](/dfs-cycle-detection/), and an equivalent serial order is a [topological sort](/topological-sort/), both from Volume 7. The NP-completeness of view serializability uses [NP-hardness](/np-hard/) from Volume 39.

Concurrency in a single program is the subject of Volume 22, and much of it carries over. Shared and exclusive locks are the [readers-writer lock](/readers-writer-lock/); deadlocks are found with a [wait-for graph](/wait-for-graph/) and [deadlock detection](/deadlock-detection/), or avoided by [deadlock prevention](/deadlock-prevention/). [Software transactional memory](/software-transactional-memory/) applies optimistic validation and multiple versions to memory instead of disk, and [TL2](/tl2/) is a close relative of optimistic concurrency control. Recovery after a crash, which the atomicity and durability of ACID need, is the subject of Chapter 40.6.
