1. $R = 24$. At most $nR = 96$ retired nodes are unfreed, and each scan frees at least $R - nK = 12$. With $R = nK = 12$, all the nodes in a list may be named by slots, so a scan may free nothing and every retire pays for a full scan.

3. $G$ does not advance, because thread 3 announced 6. With $g = 7$, the nodes with $7 \ge r + 2$, tags 4 and 5, are freed. At the next attempt all announcements are $\bot$ or 7, so $G$ moves to 8 and the nodes with tag 6 are freed; tag 7 waits for $G = 9$.

5. The count goes $2 \to 4 \to 6$ after the two reads. Thread $r$'s FAA returns 6 and leaves 4; $p$'s returns 4 and leaves 2; $q$'s returns 2 and leaves 0. Then $q$ wins CAS($rc$, 0, 1), so $rc = 1$, and $q$ frees $X$ and releases $X.next$.

6. At least $n + 1 = 9$: one counter node that holds $NRef$, and one list node for each of the 8 slots, which links the batch into that slot's list. RETIRE costs $O(n)$ steps per batch of $n + 1$ nodes, so $O(1)$ per node.

9. (a) $4(16 + 15 + 36) = 268$. (b) $G = 8$, so $4(16 + 8) + 8 = 104$. (c) $3(10 + 3 \cdot 2 \cdot 4) = 102$.

11. A scan keeps a node whose lifetime contains one of the eras 3, 7 and 8. It keeps $b$ (3), $d$ (7 and 8) and $e$ (8), and frees $a$, $c$ and $f$.

14. Thread 3's counter 7 blocks the advance, so $g = 8$ and only the nodes with tag 6 are freed. If thread 3 is offline, it is skipped, $G$ moves to 9, and the nodes with tags 6 and 7 are freed. On waking, thread 3 must come back online with a fresh counter, $C[3] \leftarrow G$, before it touches any shared node.

15. Let $p$ read $top = A$ in the middle of a pop. Then $q$ pops $A$ and retires it with tag 0; since $C = (0, 0)$, its check moves $G$ to 1, and the rule $1 \ge 0 + 1$ frees $A$. Now $p$ reads $A.next$. With the rule $r + 2$, $A$ waits until $p$ reports 1, which it does only after it drops $A$.

17. From $C = 3$: the reader writes 3 into its slot; another thread retires some node (the clock moves to 4), allocates $N$ with birth era 4 and pushes it; the reader reads $top = N$; then $N$ is popped and retired with era 4, and a scan sees only era 3, which is not in $[4, 4]$, and frees $N$. The correct code reads the clock again after reading $N$, sees $4 \ne 3$, writes 4 and loops, so the scan keeps $N$.

21. (a) Each gap of one reader, such as $(3, 4)$, lies inside a section of the other. (b) At time 1 only reader 1 is inside, in $[0, 3]$, so the grace period ends at 3. At 7.5 only reader 2 is inside, in $[6, 9]$, so it ends at 9. (c) Every section active at $s$ began at or before $s$ and lasts at most $d$.

22. Let another thread change the source between L1 and L3 every time: for example, it pushes a node or pops one. Each failure at L3 means the source changed, which only a successful CAS of another operation does, and that operation then finishes in a bounded number of its own steps.

23. Let thread 2 protect $A$ and stop. Thread 1 pops $A$ and retires it (list $\{A\}$), then pops $B$ while its slot names $B$; now the list $\{A, B\}$ reaches $R$, and both nodes are protected. A scan keeps only protected nodes, at most $nK$, and the list grows by one before the next scan, so it never passes $nK + 1$. But each retire may now scan $O(nK + R)$ words and free nothing or one node.

24. (a) Yes: $4 \le 7$ and $5 \ge 2$. (b) No: neither 2 nor 7 lies in $[4, 5]$. (c) The thread begins at epoch 2, reads $x$ at epoch 4 and raises its reservation to $[2, 4]$, keeps the pointer, and reads another node at epoch 7, which raises it to $[2, 7]$; meanwhile $x$ is retired at epoch 5. IBR does not record the epoch of each pointer, so only the whole interval covers $x$.

25. The nodes reachable from $A$ through $next$ cannot be freed while $p$ holds $A$, because each holds a counted link to the next. In the stack, $next$ fields never change after a push, so this chain is fixed at $1 + d$ nodes. In the queue, every enqueue links the new node from the last node, which is always on the chain from $A$, so the chain grows with every enqueue.
