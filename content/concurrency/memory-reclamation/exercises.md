1. ◦ Hazard pointers run with $n = 4$ threads and $K = 3$ slots per thread, and the scan threshold is $R = 2nK$. What is $R$, what is the bound on retired nodes not yet freed, and how many nodes does each scan free at least? What can go wrong if $R = nK$ instead?

2. ◦ A tagged word on a stack is updated once every 10 ns. How long does it take for the tag to wrap around if it has 16, 32 or 64 bits? A thread is preempted for 1 ms between its read and its compare-and-swap. Is a 16-bit tag safe for that pop?

3. ◦ Epoch-based reclamation runs with four threads. The global epoch is $G = 7$, and the announcements are $A = (7, \bot, 6, 7)$. Thread 1's limbo list holds nodes with tags 4, 5, 6 and 7 and has reached $R$, so it runs L6 to L10. Does $G$ advance, and which nodes are freed? Thread 3 then ends its operation and nothing else happens before thread 1's next attempt. What does that attempt do?

4. ◦ Four readers have read-side sections $R_1 = [1, 6]$, $R_2 = [3, 9]$, $R_3 = [5, 12]$ and $R_4 = [7, 10]$. A node is unlinked at time 4, and a grace period starts at that moment. Which readers must the grace period wait for, and what is the earliest time it can end?

5. ◦ In lock-free reference counting with steps of 2, node $X$ has one link to it and no holders. Thread $p$ and then thread $q$ run SAFE_READ and get $X$. Thread $r$ removes the link and calls RELEASE($X$). Then $p$ and then $q$ release $X$. Give $X.rc$ after each step, the value each FAA at L5 returns, and the thread that frees $X$.

6. ◦ Hyaline-1 runs with $n = 8$ threads. How many nodes must a batch have at least, and what is each of them used for? What is the cost of RETIRE per node?

7. ◦ A traversal visits $L = 1000$ nodes of a queue. How many anchor writes and checks does drop the anchor make with $K = 8$ and with $K = 3$, and how many protecting writes do hazard pointers with two slots make? In each of the three cases, how many nodes can a thread that stops during the traversal hold back?

8. ◦ The ERA theorem names three goals: ease of integration, robustness and applicability. Which goal does each of epoch-based reclamation, hazard pointers and neutralization-based reclamation give up?

9. ◦ Compute the garbage bound in each case. (a) DEBRA+ with $n = 4$, $K = 3$ and $T = 16$. (b) Pass the buck with $n = 4$ threads and $K = 2$ guards each, and $R = 16$. (c) Hazard eras with $n = 3$, $K = 2$, $R = 10$ and $L = 4$.

10. • Hazard pointers run with $n = 3$ and $K = 2$. The slots hold $(B, \text{nil})$ for thread 1, $(D, F)$ for thread 2 and $(\text{nil}, B)$ for thread 3. Thread 1's retire list is $A, B, C, D, E, F, G, H$, and with $R = 8$ it scans. Which nodes does it free, which stay, and does the result agree with the guarantee $R - nK$?

11. • Hazard eras run with three threads whose published eras are $\{3\}$, $\{7, 8\}$ and none. Six retired nodes have lifetimes $a = [1, 2]$, $b = [2, 5]$, $c = [4, 6]$, $d = [6, 9]$, $e = [8, 10]$ and $f = [9, 11]$, written as [birth era, retire era]. Which nodes does a scan free?

12. • Interval-based reclamation runs with three threads whose reservations are $[2, 4]$, $[7, 7]$ and nil. Five retired nodes have lifetimes $a = [1, 1]$, $b = [1, 3]$, $c = [5, 6]$, $d = [5, 8]$ and $e = [8, 9]$. Which nodes does a scan free?

13. • Under epoch-based reclamation, thread $p$ announces 5 when $G = 5$ and then stops forever inside its operation. The other threads keep running and retire 1000 more nodes. What is the largest value $G$ can reach, which tags can still be freed, and how many of the 1000 nodes are ever freed?

14. • QSBR runs with three threads, $G = 8$ and $C = (8, 8, 7)$. Thread 3 is blocked on input and has not reported since the epoch was 7. Thread 1's limbo list holds nodes with tags 6, 7 and 8 and has reached $R$. Which nodes does thread 1 free? Answer again for the case in which thread 3 went offline before it blocked. What must thread 3 do when it wakes up?

15. • Change QSBR so that a node with tag $r$ is freed when $G \ge r + 1$. Give a schedule with two threads and $R = 1$ on the stack $top \to A \to B$, starting from $G = 0$ and $C = (0, 0)$, in which a node is read after it is freed.

16. • In the user-space RCU template, $G = 5$ and four reader slots hold $(0, 3, 5, 0)$. An updater runs SYNCHRONIZE. What value $g$ does it compute at L6? Then, in order: reader 4 enters, reader 2 leaves, reader 2 enters again, and reader 3 leaves. Which readers does L7 wait for, and after which event can it finish?

17. • A wrong version of hazard eras writes the current clock into the slot first and then reads the pointer once, with no loop. Give a schedule on a stack, starting from $C = 3$, in which a scan frees a node that the reader still holds. Show what the correct loop of L1 to L4 does in the same schedule.

18. • A pop may be delayed by up to 50 ms, and the stack word changes at most $10^8$ times per second. What is the smallest tag width $w$ that rules out ABA on that pop? Does it fit into the spare bits of a 64-bit pointer on x86-64?

19. • One operation reads $L = 1000$ nodes and then makes one CAS. Count the extra shared writes, fences and reads that the reads of the nodes cost under hazard pointers, epoch-based reclamation, optimistic access and neutralization-based reclamation. Ignore restarts.

20. • A hazard pointer scan costs $nK + R$ steps and frees at least $R - nK$ nodes. With $n = 8$ and $K = 2$, find the worst-case cost per freed node and the garbage bound $nR$ for $R = 17$, 20, 32 and 64.

21. ★ Two readers alternate sections. Reader 1 uses $[0, 3]$, $[4, 7]$, $[8, 11]$, $[12, 15]$, $[16, 19]$ and reader 2 uses $[2, 5]$, $[6, 9]$, $[10, 13]$, $[14, 17]$, $[18, 21]$. (a) Show that some reader is inside a section at every time in $[0, 21]$. (b) When do the grace periods that start at times 1 and 7.5 end? (c) Prove that if every section lasts at most $d$, every grace period that starts at $s$ ends by $s + d$.

22. ★ Show that PROTECT in hazard pointers is lock-free but not wait-free. Give an infinite schedule in which one thread's PROTECT never returns, and show that the other threads complete infinitely many operations in it.

23. ★ Hazard pointers run with $n = 2$, $K = 1$ and $R = 2$, so $R \le nK$. On the stack $top \to A \to B \to C$, give a run in which a scan frees nothing. Then prove that each retire list still holds at most $nK + 1$ nodes, and explain why the cost per retire is no longer $O(1)$ amortized.

24. ★ A thread under interval-based reclamation holds the reservation $[2, 7]$, and node $x$ has the lifetime $[4, 5]$. (a) Does a scan keep $x$? (b) Under hazard eras, a thread has published the eras 2 and 7. Does a scan keep $x$ because of it? (c) Give a run in which the IBR thread still holds $x$ when its reservation is $[2, 7]$, and conclude that IBR cannot publish only the two ends of its interval as hazard eras.

25. ★ Lock-free reference counting runs on the Treiber stack and on the Michael and Scott queue, and thread $p$ stops for good right after SAFE_READ returns node $A$. Prove that on the stack, $p$ keeps at most $1 + d$ nodes from being freed, where $d$ is the number of nodes below $A$ at that moment. Prove that on the queue, every node enqueued after $p$ stopped is never freed.
