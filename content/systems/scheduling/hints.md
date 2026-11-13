1. FCFS: waits 0, 5, 7 and 16, mean 7. SJF runs P2, P4, P1, P3, with waits 0, 2, 6 and 11, mean 4.75. Round robin runs P1 0–3, P2 3–5, P3 5–8, P4 8–11, P1 11–13, P3 13–16, P4 16–17 and P3 17–20. The completions are 13, 5, 20 and 17, the waits 8, 3, 11 and 13, mean 8.75. The jobs first run at 0, 3, 5 and 8, so the mean response time is 4.

2. FCFS: the long job waits 0 and the short ones 100, 101, …, 109, so the total is 1045 and the mean 95. SJF: the short jobs wait 0, 1, …, 9 and the long job 10, so the mean is $55/11 = 5$. The ratio is 19.

3. From $19(q + 0.1) + 0.1 \le 100$, $q \le 99.9/19 - 0.1 \approx 5.16$ ms. From $0.1/(q + 0.1) \le 0.02$, $q \ge 4.9$ ms. With 21 processes, $q \le 99.9/20 - 0.1 = 4.895$ ms, below 4.9.

6. FCFS moves 358 cylinders. SSTF serves 43, 28, 17, 3, 61, 82, 95 and moves 139. LOOK toward 0 moves $47 + 92 = 139$, and LOOK toward 99 moves $45 + 92 = 137$. C-LOOK moves $45 + 92 + 40 = 177$. The optimum is $(95 - 3) + \min(47, 45) = 137$, reached by LOOK toward 95, the nearer end. FCFS takes 2.6 times the optimum and SSTF 2 cylinders more.

8. $U = 5/6 \approx 0.833$, above $3(2^{1/3} - 1) \approx 0.780$. The product is $\tfrac43 \cdot \tfrac54 \cdot \tfrac54 = 25/12 > 2$. Response-time analysis gives $R_1 = 2$, $R_2 = 4$, and for the third task the iterates 3, 7, 9, 11, 11, so $R_3 = 11 \le 12$. Only the exact test accepts the set, and the set is schedulable.

10. The jobs with $a_j \le b_j$ come first by increasing $a_j$: (1, 2), (3, 6), (6, 6). Then the others by decreasing $b_j$: (7, 5), (5, 2). Machine 1 finishes at 1, 4, 10, 17 and 22, and machine 2 at 3, 10, 16, 22 and 24. The makespan is $24 = 22 + 2$. The job (6, 6) can go into either set without changing the order.

11. In the sum of the completion times, $b_{(i)}$ appears once in each $C_{(k)}$ with $k > i$ and $n - i + 1$ times in $C_{(i)}$, so its coefficient is $2(n - i) + 1$. Under SJF its coefficient is $n - i + 1$. The ratio is $2 - \sum_j b_j / \sum_j C_j^{\mathrm{SJF}}$, and with equal bursts $\sum_j C_j^{\mathrm{SJF}} = b\,n(n+1)/2$.

12. The period is $\max(48, 18) = 48$ ms and $W = 4096$, so the slices are 12, 12 and 24 ms, and each adds 12 ms of virtual runtime, since $24 \cdot 1024/2048 = 12$. For the two tasks the period is 48 ms, and the slices are $48 \cdot 1024/1039 \approx 47.3$ ms and $48 \cdot 15/1039 \approx 0.69$ ms. The rule only stretches the period; it does not bound each slice. The period grows when $6n > 48$, so from 9 tasks on.

14. The density is $\tfrac12 + \tfrac14 + \tfrac47 \approx 1.32$. Under deadline-monotonic priorities the iterates for the third task are 4, 6, 8, and $8 > 7$. With $U = 0.85$, $L_a = (2 \cdot \tfrac14 + 1 \cdot \tfrac15 + 3 \cdot \tfrac{4}{10})/0.15 \approx 12.67$. At the deadlines 2, 4, 6, 7, 9 and 10 the demand is 1, 2, 3, 7, 8 and 9, never more than $t$, so EDF meets every deadline. The demand meets the time at $t = 7$.

16. The interval $[0, 2]$ has intensity $4/2 = 2$, the largest; $[0, 6]$ has $10/6$. Run the first job at speed 2 and cut $[0, 2]$ out. The other two jobs then fill $[2, 6]$ at speed $6/4 = 1.5$, since the third job alone in $[3, 5]$ has intensity 1. The energy is $2 \cdot 2^2 + 4 \cdot 1.5^2 = 17$ for $\alpha = 2$ and $2 \cdot 2^3 + 4 \cdot 1.5^3 = 29.5$ for $\alpha = 3$.

17. With no protocol, L locks S at 1, H preempts it at 2 and blocks at 3, M runs 3–7, L leaves S at 9, H runs 9–10 and L ends at 11. H finishes at 10, M at 7, L at 11, and H is blocked for 6 units. Under inheritance, L runs at H's priority from 3 to 5, H runs 5–6, M 6–10 and L 10–11, so H is blocked for 2 units. The ceiling of S is H's priority; L gets S at 1 since no other lock is held, H blocks at 3, and the schedule is the same as under inheritance.

20. The earliest starts are A 0, B 0, C 3, D 3, E 7, F 2, and the project time is 10. The latest starts are A 0, B 3, C 3, D 5, E 7, F 9, so the floats are 0, 3, 0, 2, 0 and 7, and the critical path is A, C, E. With the resource, the serial scheme starts C at 3 and D at 7, so E starts at 9 and the makespan is 12. C and D both start at 3 or later and cannot overlap, so E cannot start before $3 + 4 + 2 = 9$.

23. By the critical instant theorem, task $i$ meets its deadlines if and only if $W_i(t) \le t$ for some $t \le T_i$. Take $t = T_i$: every higher-priority period divides $T_i$, so $\lceil T_i/T_j \rceil = T_i/T_j$ and $W_i(T_i) = T_i \sum_{j \le i} U_j \le T_i U$. The converse holds for every scheduler.

24. In $[0, r)$ the first task releases jobs at 0 and 1. If $C_1 \le r - 1$, the second task gets $(1 - C_1) + (r - 1 - C_1)$, so $C_2 = r - 2C_1$ and $U$ falls as $C_1$ grows. If $C_1 \ge r - 1$, it gets only $1 - C_1$, and $U = C_1 + (1 - C_1)/r$ grows with $C_1$. The least value is at $C_1 = r - 1$, and $r + 2/r - 2$ is least at $r = \sqrt 2$.

25. Place the tasks in order of increasing $a_i$. After all tasks with $a_i \le 2^k$ are placed, the used slots form whole residue classes modulo $2^k$, and $2^k \sum 1/a_i$ of them are taken. A class modulo $2^k$ is the union of two classes modulo $2^{k+1}$, so a free class remains while the density is below 1. Rounding each $a_i$ down to a power of 2 at most doubles the density.

26. Number the jobs by their SRPT completion times $C^P_1 \le \cdots \le C^P_n$. By induction, the nonpreemptive completion time is $C_j \le \max_{k \le j} r_k + \sum_{k \le j} p_k$. Jobs $1, \ldots, j$ are released before $C^P_j$, and they all finish by $C^P_j$ in the SRPT schedule, so both terms are at most $C^P_j$. The SRPT total is a lower bound on the nonpreemptive optimum.

27. List the activities by their start times $S_j$ in the given schedule, with predecessors first among ties. Use induction: an activity $i$ placed before $j$ has $S'_i \le S_i \le S_j$. So at any time $t \ge S_j$, $i$ runs in the new schedule only if it ran at $t$ in the given one. Hence $j$ fits at $S_j$ after its predecessors end, and the scheme starts it no later.
