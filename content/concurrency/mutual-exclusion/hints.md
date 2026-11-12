1. There are $6!/(2!\,2!\,2!) = 90$ interleavings. The final value is 3 in 6 of them (the three passages run one after another), 2 in 36 and 1 in 48. For comparison, two processes give 6 interleavings, 4 of which lose an update.

2. Process 0 runs L1 and L2, so $flag[0] = true$ and $turn = 0$; it reads $flag[1] = false$ and enters. Process 1 runs L1 and L2, so $turn = 1$; it reads $flag[0] = true$, then $turn = 1 \ne 0$, and enters too. Seven steps suffice.

3. Filter: 9 registers, 28 steps. Tournament: 21 registers, 9 steps. Bakery: 10 registers, 15 steps. Burns-Lamport: 5 registers, 5 steps. Lamport's fast algorithm: 7 registers, 5 steps (3 writes and 2 reads). Burns-Lamport meets the lower bound of $n$ registers; at $n = 5$ it ties with the fast algorithm on steps, and for every larger $n$ the fast algorithm, with its constant 5, takes fewer.

5. Only accesses to $tail$ and to the nodes of other processes are remote. (a) The swap at L2 and the successful compare-and-swap at L8: 2 RMRs. (b) The swap at L2, the link at L5, the failed compare-and-swap at L8 and the hand-over at L10: 4 RMRs; the spins at L6 and L9 are on the process's own node.

7. (a) Mutual exclusion. (b) No preemption: the thread gives back what it holds. (c) Hold and wait. (d) Circular wait. (e) No preemption: the system takes the lock away.

11. Let both processes read $number = 0$ in their doorways and both take ticket 1. With test (a), each waits until the other's ticket is 0 or larger than its own; neither is, so both wait for ever. With test (b), each sees $number[j] \ge number[i]$ and passes, so both enter. The pair $(number, id)$ breaks exactly this tie.

13. Let $turn = 0$. Process 0 runs one passage; its exit writes $turn \leftarrow 1$ and $flag[0] \leftarrow false$ stay in its buffer, and it starts again with $flag[0] \leftarrow true$, also buffered, and waits at its fence. Process 1 raises its flag (fenced), reads the old values $flag[0] = true$ and $turn = 0$ from memory, and steps back at L4. Now the first two writes of process 0 drain, and so does the write of L4 of process 1. Process 1 sees $turn = 1$, leaves L5, buffers $flag[1] \leftarrow true$ at L6, reads $flag[0] = false$ and enters. Then $flag[0] \leftarrow true$ drains, the fence of process 0 completes, and it reads $flag[1] = false$ from memory and enters too. The run uses two passages of process 0 and one of process 1.

14. The need matrix is $(4,2,2), (1,2,1), (4,1,1), (1,1,1), (4,1,2)$ and the available vector is $(2,2,1)$. (a) Safe: $P_1, P_2, P_3, P_4, P_0$. (b) Granted: $P_3, P_1, P_2, P_4, P_0$ is still safe. (c) Not granted: the available vector would be $(2,1,0)$, and no process's need fits under it.

15. (a) $P_0 \to B \to P_1 \to A \to P_0$ is a cycle, since $P_2$ holds the other $A$. Nothing is free, but $P_2$ requests nothing, so it finishes and frees $A$ and $C$; then $P_3$, then $P_1$, then $P_0$ can finish. (b) Now no process can finish, so all four are deadlocked. $P_3$ lies on no cycle: it waits for an $A$, and both holders of $A$ are deadlocked.

20. Let $i$ finish its doorway, and then let $j$ run alone from its remainder section. Since the doorway of $i$ wrote nothing, the state of memory is the same as if $i$ were still in its remainder section, and $j$ cannot tell the two apart. In the run where $i$ is absent, deadlock freedom makes $j$ enter, and $j$ takes the same steps here, so it enters before $i$.

21. Exits run while the process holds $L$, so they are serialized. A process $k$ with $turn = k$ and $flag[k] = true$ keeps $turn$ fixed until it exits, and processes that arrive later block at the wait, since $turn$ is not their index and $flag[turn] = true$. So $k$ competes at $L$ with at most $n - 1$ others, none of which returns to $L$ before $k$ enters, and deadlock freedom of $L$ gets $k$ in; its exit then advances $turn$. Every exit advances $turn$ past a process whose flag is down, so $turn$ reaches every waiting process.

22. Let the two processes overlap their passages so that each takes a ticket one higher than the other's: tickets climb $1, 2, \ldots, M$. While process $a$ is in the critical section with ticket $M$, process $b$ reads $m = M$, takes $(M \bmod M) + 1 = 1$, and passes $a$ because $(1, b) < (M, a)$. For $M = 1$ only the tie-break by identity is left, and it lets process 0 in beside process 1. The shortest such run has $7M + 5$ steps.

23. If some process $q$ reachable from $p$ is active, induct on the length of the path from $p$ to $q$: $q$ can send a message to the process before it on the path, which unblocks it, and so on back to $p$. Conversely, if every reachable process is blocked, the set of reachable processes is closed: each of them waits only for processes in the set, all blocked, so no message can ever reach any of them. In the instance $P_1$ to $P_5$ reach only each other, and all are blocked, so they are deadlocked; $P_6$ reaches $P_7$, which runs, so it is not.

24. Let $K = 1/(C(e-1))$. If $w \ge C$, the cost is $E[T] + C$; since $E[T] = C/(e-1)$, this is $C\,e/(e-1)$. If $w < C$, the cost is $\int_0^w (t + C)\,p(t)\,dt + w \int_w^C p(t)\,dt$. Integration by parts gives $\int_0^w (t + C) e^{t/C} dt = C w e^{w/C}$, so the first term is $w e^{w/C}/(e-1)$; the second is $w (e - e^{w/C})/(e-1)$. The sum is exactly $w\,e/(e-1)$.

25. The last write of $x$ is some process's $k$-th write, and that process wrote before, so its last read came after a write of its own and saw at least 1; it writes at least 2. To get exactly 2, let $P$ read 0; let the others run all their increments except the last one of some $Q$; let $P$ write 1; let $Q$ read 1; let $P$ run its remaining increments; and let $Q$ write 2 last.
