2. List scheduling puts the three 2s on the three machines, the two 3s on machines 1 and 2, and the 6 on machine 3: loads $5, 5, 8$. LPT puts 6, 3, 3 on machines 1, 2, 3, then the 2s on machines 2, 3 and 2: loads $6, 7, 5$. OPT is 6, with $\{6\}$, $\{3, 3\}$ and $\{2, 2, 2\}$. The bounds are $\frac53 \cdot 6 = 10$ and $\frac{11}{9} \cdot 6 = \frac{22}{3}$, and both makespans are below them.

4. $C^* = \max(20/3, 5) = 20/3$. Machine 1 runs job 1 in $[0, 5)$ and job 2 in $[5, \frac{20}{3})$. Machine 2 runs job 2 in $[0, \frac{10}{3})$ and job 3 in $[\frac{10}{3}, \frac{20}{3})$. Machine 3 runs job 3 in $[0, \frac23)$, job 4 in $[\frac23, \frac{14}{3})$ and job 5 in $[\frac{14}{3}, \frac{20}{3})$. Jobs 2 and 3 are split. Without preemption no two of the jobs 5, 5, 4, 4 fit in 7, so some machine holds two of them, and OPT is 8, by $\{5, 2\}$, $\{5\}$, $\{4, 4\}$.

7. At time 0, $a$ and $b$ start; at 2, $f$ starts, since $c$ and $d$ still wait for $a$; at 3, $c$ starts; at 5, $d$; at 9, $e$. The makespan is 10. The chain $a, d, e$ gives 8 and $\lceil 17/2 \rceil = 9$. OPT is 9: one machine runs $a, d, e$ in $[0, 8)$, the other $b, f, c$ in $[0, 9)$.

9. Job 2 ends at 7, after its due date 6, so the longest job so far, job 2, is removed. Jobs 3 and 4 fit. Job 5 ends at 10, after 9, and the longest of jobs 1, 3, 4, 5 is job 5, which is removed. Jobs 2 and 5 are late, and 2 is optimal by the correctness of Moore-Hodgson.

11. Give two jobs of length 1. If the algorithm puts them on one machine, stop: it has 2 and OPT is 1. Otherwise give one job of length 2: the algorithm ends at 3 and OPT is 2.

13. The levels are $r = 1$; $a, b = 2$; $c, d, e, f = 3$; $g, h, i = 4$; $j = 5$; $k = 6$. Hu runs $\{k, g\}$, $\{j, h\}$, $\{i, c\}$, $\{d, e\}$, $\{f, a\}$, $\{b\}$, $\{r\}$, so 7 steps. The 11 jobs other than $r$ must all finish before $r$ starts, and they need $\lceil 11/2 \rceil = 6$ steps.

16. The earliest due date order gives $0 + 1 + 5 + 6 = 12$ and the shortest processing time order gives 11. The order $J_1, J_2, J_4, J_3$ gives $0 + 1 + 0 + 7 = 8$, which is optimal; check the 24 orders, or use Emmons' rules to cut them down.

17. On a machine with jobs $j_1, \ldots, j_r$ in order, $\sum_s p_{j_s} C_{j_s} = \sum_{t \le s} p_{j_t} p_{j_s}$, which is half of $L^2$ plus half of $\sum_s p_{j_s}^2$. The loads $(5, 5)$ give 38, which is OPT; the order $1, 1, 2, 2, 4$ gives loads $(7, 3)$ and cost 42. The ratio $42/38 \approx 1.105$ is below $1.207$.

20. One job with $p = M$ and $e = M/m + \delta$ is accepted, at cost $M$, while rejecting it costs $M/m + \delta$.

21. With $k = 3$ the rounded sizes are $3, \ldots, 9$. The configurations are the 7 single sizes, the pairs $(3,3)$, $(3,4)$, $(3,5)$, $(3,6)$, $(4,4)$, $(4,5)$, and the triple $(3,3,3)$: 14 in all. Here $\text{LB} = 12$, and the search tests 18, 15 and 13, which succeed, and 12, which fails. At $T = 12$ the 7s round to 5 and the 5 to 3, and no two 5s fit in 9, so four machines are needed. At $T = 13$ the 7s round to 4 and the 5 to 3, and three machines suffice. The schedule has makespan 14, above the guess 13 but within $\frac43 \cdot 13$; OPT is 14, since two of the four 7s share a machine.

22. Run LPT and let $\ell$ be the job that ends last. If $\ell \le m$, it runs alone and the makespan is $p_\ell \le C^*$. Otherwise $P \ge (m + 1) p_\ell$, so $p_\ell \le \frac{m}{m+1} C^*$, and the makespan is at most $P/m + (1 - \frac1m) p_\ell$. Tightness: $m + 1$ unit jobs.

23. Let machine $i$ have the least load $x$. Every other machine $h$ had load at most $x$ before its last job, so $P \le mx + p(J')$, where $J'$ is the set of these last jobs, at most $m - 1$ of them. Any schedule has a machine with no job of $J'$, and its load is at most $P - p(J') \le mx$. For tightness, take $m$ unit jobs followed by $m - 1$ jobs of length $m$.

24. Pair the machines: jobs allowed on $\{1, 2\}, \{3, 4\}, \ldots$ put load 1 on machines $1, 3, 5, \ldots$. Then pair those: jobs on $\{1, 3\}, \{5, 7\}, \ldots$ put load 2 on machines $1, 5, \ldots$. After $k$ rounds machine 1 has load $k$, and a last job allowed only on machine 1 gives $k + 1$. Each job could have gone to a machine of its own.

25. Any schedule uses $n$ distinct coefficients, so by the rearrangement inequality its cost is at least the sum that pairs the $n$ smallest coefficients with the jobs in opposite order, and a schedule reaches that sum. Here the smallest coefficients are $\frac12, 1, 1, \frac32, 2$, and the optimum is $5 \cdot \frac12 + 4 + 3 + 2 \cdot \frac32 + 1 \cdot 2 = \frac{29}{2}$.
