1. ◦ For each failure, name the one of the [ACID properties](/acid-properties/) that is broken: (a) after a crash, an account has been debited but the other account of the transfer was never credited; (b) a customer got a confirmation of an order that is gone after a power cut; (c) a report that sums all balances runs during a transfer and counts the moved money twice; (d) a transaction commits a negative stock count although a rule forbids it.

2. ◦ Draw the [conflict graph](/conflict-graph/) of $r_1(x)\, r_2(y)\, w_1(x)\, r_3(x)\, w_2(x)\, w_3(y)$. Is the schedule conflict serializable? Is it view serializable? Remove $r_2(y)$ and give every equivalent serial order of what remains.

3. ◦ Show that $r_1(x)\, r_2(y)\, w_1(x)\, w_2(y)\, r_1(z)$ is [conflict serializable](/conflict-serializability/) by turning it into a serial schedule with swaps of adjacent actions that do not conflict. Can you reach both serial orders?

4. ◦ A schedule is *recoverable* if every transaction commits only after each transaction it read from has committed, *cascadeless* if every transaction reads only committed values, and *strict* if no transaction reads or overwrites an uncommitted value. Classify each schedule: (a) $w_1(x)\, r_2(x)\, c_2\, c_1$; (b) $w_1(x)\, r_2(x)\, c_1\, c_2$; (c) $w_1(x)\, w_2(x)\, c_1\, c_2$; (d) $w_1(x)\, c_1\, r_2(x)\, w_2(x)\, c_2$.

5. ◦ Name the anomaly of the [isolation levels](/isolation-levels/) entry that each history shows: (a) $r_1(x)\, w_2(x)\, w_2(y)\, c_2\, r_1(y)\, c_1$; (b) $r_1(P)\, w_2(y \in P)\, c_2\, r_1(P)\, c_1$; (c) $w_1(x)\, r_2(x)\, a_1\, c_2$; (d) $r_1(x)\, w_2(x)\, w_1(x)\, c_1$. Check that [snapshot isolation](/snapshot-isolation/) forbids all four.

6. ◦ Transactions $T_1$, $T_2$, $T_3$ have timestamps 5, 10 and 15, and a smaller timestamp means older. $T_2$ holds an exclusive lock on $x$. First $T_1$ and then $T_3$ ask for a lock on $x$. Say what happens to each of the three transactions under [wait-die and under wound-wait](/wait-die-and-wound-wait/).

7. ◦ Under snapshot isolation, what happens to each of these histories? (a) $r_1(x)\, r_2(x)\, w_1(x)\, w_2(x)\, c_1\, c_2$. (b) $r_1(x)\, r_1(y)\, r_2(x)\, r_2(y)\, w_1(x)\, w_2(y)\, c_1\, c_2$. Which of the two gives a serializable outcome, and what does [serializable snapshot isolation](/serializable-snapshot-isolation/) do with the other?

8. ◦ An index holds the keys 10, 20, 30 and 40. A transaction scans the range $15 \le k \le 25$ under next-key locking, as in the [phantom problem](/phantom-problem/) entry. Which keys does it lock? Another transaction then inserts 22, and a third inserts 33. Which insert waits?

9. ◦ Two transactions each run $r(x)\, w(x)$. List the six interleavings of their four actions and say which are conflict serializable.

10. • Show that $r_1(x)\, w_2(x)\, r_3(y)\, w_1(y)$ is conflict serializable, but that [two-phase locking](/two-phase-locking/) cannot produce it. Run basic [timestamp ordering](/timestamp-ordering/) on it with timestamps in order of first action, and again with $\mathrm{ts}(T_3) = 1$, $\mathrm{ts}(T_1) = 2$ and $\mathrm{ts}(T_2) = 3$.

11. • Give a schedule that two-phase locking allows in which the abort of one transaction forces another to abort. Show that [strict two-phase locking](/strict-two-phase-locking/) prevents it.

12. • Three transactions start together and run under [optimistic concurrency control](/optimistic-concurrency-control/) with serial backward validation. $T_1$ has read set $\{x, y\}$ and write set $\{x\}$; $T_2$ has $\{y, z\}$ and $\{z\}$; $T_3$ has $\{x, z\}$ and $\{y\}$. They validate in the order $T_1$, $T_2$, $T_3$. Which commit and which abort?

13. • Show that two-phase locking and basic timestamp ordering, with timestamps in start order, accept incomparable sets of schedules. Use exercise 10 for one direction, and for the other consider $r_1(y)\, r_2(x)\, w_1(x)\, c_1\, c_2$ with $T_1$ older.

14. • Show that $w_1(x)\, r_2(x)\, w_2(y)\, w_1(y)\, w_3(y)$ is [view serializable](/view-serializability/) but not conflict serializable. Find every view equivalent serial order, and say which action makes the difference.

15. • Two transactions each run $r(x)\, w(x)$ under two-phase locking, and the actions arrive as $r_1(x)\, r_2(x)\, w_1(x)\, w_2(x)$. Show that they deadlock when they try to upgrade their shared locks. An *update lock* is taken by a read that plans to write; it is compatible with shared locks but not with another update lock. Show that update locks remove this deadlock.

16. • Under wound-wait, suppose a wounded transaction restarted with a new timestamp. Describe a sequence of arrivals in which it is wounded forever. Then prove that a restart that keeps its timestamp is wounded only finitely often.

17. • Show that snapshot isolation and repeatable read are incomparable: give a history that snapshot isolation allows and repeatable read forbids, and one that repeatable read allows and snapshot isolation forbids. Use the anomalies of the isolation levels entry.

18. • Under snapshot isolation, take $r_2(x)\, r_2(y)\, r_1(y)\, w_1(y)\, c_1\, r_3(x)\, r_3(y)\, c_3\, w_2(x)\, c_2$, where $T_3$ only reads. Draw its dependency graph with wr, ww and rw edges, show that it is not serializable, and find the pivot. Is the history serializable without $T_3$?

19. • Run multiversion timestamp ordering, as in the [multiversion concurrency control](/multiversion-concurrency-control/) entry, on the write skew $r_1(a)\, r_1(b)\, r_2(a)\, r_2(b)\, w_1(a)\, w_2(b)$ with $\mathrm{ts}(T_1) < \mathrm{ts}(T_2)$. Which transaction aborts, and why does multiversion timestamp ordering not have the write skew of snapshot isolation?

20. ★ The direct serialization graph of a history has an edge for each write-write, write-read and read-write dependency. Prove that if a history allowed by snapshot isolation is not serializable, its graph has a cycle with two consecutive read-write edges, each between transactions that ran at the same time.

21. ★ Rigorous two-phase locking keeps every lock, shared or exclusive, until the transaction ends. Prove that if $T_i \to T_j$ is an edge of the conflict graph of a schedule it produces, then $T_i$ commits before $T_j$. Show by an example that strict two-phase locking, which may release shared locks early, does not have this property.

22. ★ A schema keeps doctors on call in separate rows, and each transaction takes one doctor off call if it sees at least two on call. Under snapshot isolation this allows write skew. Give two ways to change the transactions, without changing the isolation level, so that first-committer-wins forces one of two concurrent transactions to abort, and prove that each works.

23. ★ Serialization graph testing keeps the conflict graph of the active and committed transactions and rejects an action that closes a cycle. Show by the schedule $r_1(x)\, w_2(x)\, w_2(y)\, c_2\, r_1(y)$ that deleting a committed node that has incoming edges can miss a cycle. Then prove that a committed node with no incoming edges can be deleted safely.

24. ★ Each of $n$ transactions runs $r(x)\, w(x)$. Prove that among the $(2n)!/2^n$ interleavings, exactly the $n!$ serial ones are conflict serializable. Check the counts 6 of 90 for $n = 3$.
