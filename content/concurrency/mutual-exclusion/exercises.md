1. ◦ Three processes each run `r ← x; x ← r + 1` once on a shared register $x$ that starts at 0; each line is one atomic step. How many interleavings of the six steps are there, and how many of them end with $x = 1$, $x = 2$ and $x = 3$? (See [race condition](/race-condition/).)

2. ◦ Change line L2 of [Peterson's algorithm](/peterson-algorithm/) from $turn \leftarrow j$ to $turn \leftarrow i$, and keep the waiting condition $flag[j] \land turn = j$. Give a run in which both processes are in the critical section.

3. ◦ For $n = 5$ processes, give the number of shared registers and the number of shared steps of an entry section run alone, for the [filter lock](/filter-lock/), the [tournament lock](/tournament-lock/), the [bakery algorithm](/lamport-bakery-algorithm/), the [Burns-Lamport algorithm](/burns-lamport-algorithm/) and [Lamport's fast algorithm](/lamport-fast-mutex/). Which uses the fewest registers, and which the fewest steps?

4. ◦ The bypass bounds after the doorway are $2^{n-1} - 1$ for [Knuth's algorithm](/knuth-mutex-algorithm/), $n(n-1)/2$ for de Bruijn's change of it, and $n - 1$ for the [Eisenberg-McGuire algorithm](/eisenberg-mcguire-algorithm/). Give the three values for $n = 6$, and the smallest $n$ at which Knuth's bound is larger than de Bruijn's.

5. ◦ Count the remote memory references of one passage of the [MCS lock](/mcs-lock/) in the DSM model in two cases: (a) the lock is free and no other process arrives; (b) the process finds a predecessor, and a successor swaps itself into $tail$ just after the process has read $I.next = nil$ at L7 in its exit section.

6. ◦ A waiter uses the spin then block rule of the [spin lock](/spin-lock/) entry with $C = 4$: it spins for at most 4 time units, then blocks at cost 4. Give its cost and the cost of a waiter that knows the wait time $w$ in advance, for $w = 1$, $w = 3$ and $w = 10$.

7. ◦ For each of these practices, name the [Coffman condition](/coffman-conditions/) that it denies: (a) a print spooler that is the only process to use the printer; (b) a thread that takes lock $a$, calls trylock on lock $b$, and releases $a$ when trylock fails; (c) a lock manager that grants all the locks of a transaction in one step or none; (d) taking two locks in the order of their memory addresses; (e) a database that aborts a younger transaction that holds a lock an older one wants.

8. ◦ Thread $T$ calls `lock`, `lock`, `unlock`, `lock` on a [reentrant lock](/reentrant-lock/) $R$ that starts free. Give the state $(owner, count)$. Then thread $U$ calls `unlock(R)`: what happens? Then $T$ waits on a condition of $R$ in Java: what is the state while $T$ waits, and after it returns?

9. ◦ A [readers-writer lock](/readers-writer-lock/) is held by reader $R_1$. While $R_1$ still reads, requests arrive in the order $W_1, R_2, R_3, W_2, R_4$, and every critical section is long. Give the order in which the requests get the lock under reader preference, writer preference, task-fair and phase-fair policies; write readers that hold the lock together as one group.

10. • In [Peterson's algorithm](/peterson-algorithm/), take the doorway to be L1 alone instead of L1 and L2. Show that the algorithm is then not FCFS: give a run in which process $j$ starts its doorway after process $i$ has finished its doorway, and $j$ enters first.

11. • In the [bakery algorithm](/lamport-bakery-algorithm/) for two processes, replace the test $(number[j], j) > (number[i], i)$ in the waiting loop by (a) $number[j] > number[i]$, (b) $number[j] \ge number[i]$, keeping the test $number[j] = 0$. Show that one variant can deadlock and the other breaks mutual exclusion, with a run for each.

12. • In the bakery algorithm with $n$ processes, give a run in which process 0 finishes its doorway and then all $n - 1$ other processes enter the critical section before it does. This shows that the bypass bound $n - 1$ is reached.

13. • Run [Dekker's algorithm](/dekker-algorithm/) on x86-TSO, where each process has a FIFO store buffer, with a full fence after L1 but not after L6. Show that both processes can be in the critical section. How many passages of each process does your run use?

14. • A system has three resource types with $(9, 6, 6)$ units and five processes. Use the [banker's algorithm](/banker-algorithm/).

    | process | allocation | maximum claim |
    |---|---|---|
    | $P_0$ | 1 1 0 | 5 3 2 |
    | $P_1$ | 2 0 1 | 3 2 2 |
    | $P_2$ | 3 0 2 | 7 1 3 |
    | $P_3$ | 1 1 1 | 2 2 2 |
    | $P_4$ | 0 2 1 | 4 3 3 |

    (a) Is the state safe? Give a safe sequence if it is. (b) $P_3$ requests $(0, 1, 1)$; is it granted? (c) Starting again from the table, $P_4$ requests $(0, 1, 1)$; is it granted?

15. • Resource types $A$, $B$, $C$ have 2, 1 and 2 units. $P_0$ holds one $A$ and requests one $B$; $P_1$ holds the $B$ and requests one $A$ and one $C$; $P_2$ holds one $A$ and one $C$ and requests nothing; $P_3$ holds one $C$ and requests one $A$. (a) Find a cycle in the [resource allocation graph](/resource-allocation-graph/), and show by [deadlock detection](/deadlock-detection/) that no process is deadlocked. (b) Now $P_2$ also requests one $B$. Which processes are deadlocked? Which of them lie on no cycle?

16. • Five threads take locks in these orders: $T_1$ takes $A$ then $C$; $T_2$ takes $C$ then $B$; $T_3$ takes $B$ then $A$; $T_4$ takes $D$ then $A$; $T_5$ takes $D$ then $C$. Draw the lock order graph that a validator builds, find its cycles, give a deadlock that the program can reach, and find the change of one thread after which a single total [lock order](/lock-ordering/) fits all five threads.

17. • $n$ processes wait at a TTAS [spin lock](/spin-lock/) held by another process. Show that in the CC model the $n$ passages that follow cost $\Theta(n^2)$ RMRs in total in the worst case, while in the [MCS lock](/mcs-lock/) they cost $O(n)$.

18. • A [monitor](/monitor/) has a counter $c$, initially 0, an operation `increment` that adds 1 and signals one condition $ok$, and an operation `await_at_least(k)` that waits on $ok$ in a while loop until $c \ge k$. Under Mesa semantics with FIFO wakeups, $A$ calls `await_at_least(2)`, then $B$ calls `await_at_least(1)`, then $C$ calls `increment` once. Show that $B$ can wait for ever although $c \ge 1$, and fix the monitor.

19. • Show that no deterministic spin then block rule has a competitive ratio below 2: for each spin threshold $T$, find a wait time on which the rule costs at least twice as much as a waiter that knows the wait time.

20. • Prove that a mutual exclusion algorithm from read/write registers cannot be FCFS if its doorway contains no write. Use only deadlock freedom and what a process can see.

21. ★ Let $L$ be any deadlock-free lock for $n$ processes. Add registers $flag[0..n-1]$, all false, and $turn$, 0 at the start. The entry of process $i$ is: $flag[i] \leftarrow true$; wait until $turn = i$ or $flag[turn] = false$; lock $L$. The exit is: $flag[i] \leftarrow false$; if $flag[turn] = false$ then $turn \leftarrow (turn + 1) \bmod n$; unlock $L$. Prove that the result is starvation free.

22. ★ Bounded tickets: change line L3 of the bakery algorithm to $number[i] \leftarrow (m \bmod M) + 1$, so that tickets stay in $1..M$. Show that for every $M \ge 1$ two processes can both be in the critical section.

23. ★ In the OR model of [deadlock](/deadlock/), a blocked process waits for a message from any one process of its dependent set, and the [wait-for graph](/wait-for-graph/) has an edge from each blocked process to each process of its dependent set. Prove that a blocked process $p$ is deadlocked, when no message is in transit, if and only if every process reachable from $p$ is blocked. Then apply it: $P_1$ waits for $\{P_2, P_3\}$, $P_2$ for $\{P_1\}$, $P_3$ for $\{P_4\}$, $P_4$ for $\{P_3, P_5\}$, $P_5$ for $\{P_4\}$, $P_6$ for $\{P_2, P_7\}$, and $P_7$ runs.

24. ★ Show that the randomized spin then block rule that draws its threshold $T$ from $[0, C]$ with density $p(t) = e^{t/C} / (C(e - 1))$ has expected cost at most $\frac{e}{e-1} \min(w, C)$ for every wait time $w$.

25. ★ $n \ge 2$ processes each run `r ← x; x ← r + 1` $k \ge 2$ times on a register $x$ that starts at 0, each line one atomic step. Show that the final value of $x$ is at least 2, and that 2 can occur.
