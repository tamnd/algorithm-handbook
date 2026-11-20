2. The edges are $T_1 \to T_2$ and $T_1 \to T_3$ on $x$, $T_3 \to T_2$ from $r_3(x)$ before $w_2(x)$, and $T_2 \to T_3$ from $r_2(y)$ before $w_3(y)$. The cycle between $T_2$ and $T_3$ means it is not conflict serializable. It is not view serializable either: $r_3(x)$ reads from $T_1$ and $T_2$ writes $x$ last, so $T_3$ must come before $T_2$, while $r_2(y)$ reads the initial $y$, which $T_3$ overwrites. Without $r_2(y)$ the only serial order is $T_1\, T_3\, T_2$. A script that builds the graph checked the edges.

4. (a) is not recoverable, since $T_2$ commits before the transaction it read from. (b) is recoverable but not cascadeless. (c) is cascadeless, since nothing is read, but not strict, since $T_2$ overwrites an uncommitted value. (d) is strict. A script that applies the three definitions checked all four.

5. (a) is read skew, A5A. (b) is the phantom anomaly A3. (c) is the dirty read A1. (d) is the lost update P4. Snapshot isolation forbids the first three because $T_1$ reads only from its snapshot, and the fourth by first-committer-wins, since $T_2$ and $T_1$ both write $x$.

6. Under wait-die, $T_1$ is older than the holder $T_2$, so it waits; $T_3$ is younger, so it dies and later restarts with timestamp 15. Under wound-wait, $T_1$ wounds $T_2$, which aborts, and $T_1$ gets the lock; $T_3$ is younger than the holder $T_1$, so it waits.

7. In (a), both write $x$, so first-committer-wins aborts $T_2$ at $c_2$, and the outcome is that of $T_1$ alone, which is serializable. In (b) the write sets are disjoint and both commit; this is write skew, with a cycle of two read-write edges. Serializable snapshot isolation sees a transaction with both an incoming and an outgoing read-write edge and aborts one of the two.

9. Only the two serial interleavings are conflict serializable. In each of the other four, both reads come before both writes, so each transaction reads $x$ before the other writes it, which gives edges both ways.

10. (a) IS on the database, IS on $A$, S on the row. (b) IX, IX and X. (c) IX on the database, SIX on $A$ and X on each updated row. SIX is compatible only with IS, so the IS request goes on, and IX and S wait.

11. (a) $T_1\, T_2\, C_2\, C_1$, after $T_3$ has been rolled back as an ordinary transaction. (b) $C_2\, C_1$. (c) $T_3\, T_4$. After $T_4$ the saga is complete and nothing is undone. Another transaction can read the effects of $T_1$ before $C_1$ removes them, since a saga has no isolation between its steps.

12. The infimum is $20 - 8 - 7 = 5$ and the supremum is $20 + 10 = 30$. A request of $-6$ would make the infimum $-1$, so it is not granted; $-5$ makes it 0 and is granted. The test $20 - 6 \ge 0$ grants $-6$, and if the three decrements commit and the increment aborts, the value is $-1$.

13. The only conflicts give $T_1 \to T_2$ and $T_3 \to T_1$, so $T_3\, T_1\, T_2$ is equivalent. Under 2PL, $T_1$ must release $x$ before $w_2(x)$, and it cannot lock $y$ until $r_3(y)$ has run, so it would lock after it unlocks. Basic TO with timestamps 1, 2, 3 aborts $T_1$ at $w_1(y)$, since $y$ was read with timestamp 3. With $\mathrm{ts}(T_3) = 1$ it accepts the schedule. A script ran both cases.

15. $T_1$ validates first and commits. $T_2$ read $\{y, z\}$, which misses the write set $\{x\}$ of $T_1$, so it commits. $T_3$ read $x$, which $T_1$ wrote after $T_3$ started, so $T_3$ aborts.

17. $r_2(x)$ reads from $T_1$, and the final writes are $w_1(x)$ and $w_3(y)$. The serial order $T_1\, T_2\, T_3$ has the same reads-from and final writes, and it is the only one, since $T_1$ must precede $T_2$ and $T_3$ must be last. The conflict graph has $T_1 \to T_2$ on $x$ and $T_2 \to T_1$ on $y$. The blind write $w_3(y)$ hides the order of $w_2(y)$ and $w_1(y)$.

18. After the two reads each holds a shared lock on $x$, and each upgrade waits for the other's shared lock, so the wait-for graph has the cycle $T_1 \to T_2 \to T_1$. With update locks, $T_2$ waits already at $r_2(x)$, so $T_1$ upgrades, finishes and lets $T_2$ go on.

21. $T_2$ reads $y$ and $T_1$ writes a newer $y$, so $T_2 \xrightarrow{rw} T_1$. $T_3$ reads $y$ from $T_1$, so $T_1 \xrightarrow{wr} T_3$. $T_3$ reads the old $x$ and $T_2$ writes $x$, so $T_3 \xrightarrow{rw} T_2$. The cycle has two consecutive read-write edges, and $T_2$, with one in and one out, is the pivot. Without $T_3$ the history is equivalent to $T_2\, T_1$.

22. $T_1$ aborts at $w_1(a)$: the version of $a$ it would follow is the initial one, and $T_2$, younger than $T_1$, has already read it. Every multiversion timestamp ordering history is one-copy serializable in timestamp order, so write skew, which has no serial order, cannot commit.

23. The conflicts give $T_1 \to T_2$ and $T_2 \to T_3$, so it is conflict serializable as $T_1\, T_2\, T_3$. It is not recoverable: $T_3$ commits before $T_2$, from which it read. Commitment ordering needs the commits in the order of the conflicts, so only $c_1\, c_2\, c_3$ works; the result is recoverable, but not cascadeless, since $T_2$ and $T_3$ read uncommitted values.

24. The C edges join the first piece to $T_2$ on $x$, $T_2$ to $T_3$ on $z$, and $T_3$ to the second piece on $y$; with the S edge between the two pieces they close an SC-cycle. Run the first piece, then $T_2$, then $T_3$, then the second piece: $T_3$ sees the change to $x$ through $T_2$ but the old $y$, and the conflict graph has the cycle $T_1 \to T_2 \to T_3 \to T_1$. Without $T_3$ the graph has no cycle and the chopping is correct.

25. A read-write edge between two concurrent transactions that both commit needs a reader that does not write the item, since two concurrent writers of one item cannot both commit. A deposit writes what it reads, so (a) is robust. A withdrawal on $x$ reads $y$, and two withdrawals on $x$ and $y$ give the write skew, so (b) and (c) are not. When Withdraw also writes $y$, every transaction writes all it reads, no such edge exists, and every workload is robust.

26. If $T_i$ acts on an item before a conflicting action of $T_j$, then $T_i$ held a conflicting lock on it, and under rigorous 2PL it kept that lock until it ended. For strict 2PL, take $r_1(x)\, w_2(x)\, c_2\, c_1$, where $T_1$ releases its shared lock after its last read.

28. The schedule gives $T_1 \to T_2$ and then, after $c_2$, $T_2 \to T_1$. New edges into a node come only from later actions of that node, and a committed transaction has none, so a node with no incoming edges never gets one.

30. The final value is the committed value plus the sum of a subset of the pending changes. That sum is at least the sum of the negative changes and at most the sum of the positive ones. For the second part, let one transaction's change be applied in place, let another add to the value and commit, and then restore the before image of the first.
