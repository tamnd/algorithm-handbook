1. ◦ Three identical machines get the jobs $p = (7, 6, 5, 4, 4, 3, 2, 1)$. Compute the [lower bounds](/makespan-lower-bounds/) $\lceil P/m \rceil$, $p_1$ and the pair bound $p_m + p_{m+1}$, and find OPT.

2. ◦ Three identical machines get the list $2, 2, 2, 3, 3, 6$. Run [list scheduling](/list-scheduling/) in this order, and then the [longest processing time rule](/longest-processing-time-first/), with ties broken towards the lowest machine number. Find OPT, and check both makespans against the bounds $2 - 1/m$ and $\frac43 - \frac{1}{3m}$.

3. ◦ Two machines get $p = (5, 4, 3, 3, 3)$. Run LPT. Then run [first fit decreasing](/first-fit-decreasing/) with bins of size 9 and with bins of size 8, as the tests of [MULTIFIT](/multifit-algorithm/) would. What is OPT, and what is the ratio of LPT on this input?

4. ◦ Build [McNaughton's](/mcnaughton-wrap-around/) preemptive schedule for $p = (5, 5, 4, 4, 2)$ on three machines. Give the pieces on each machine and the jobs that are split. What is the nonpreemptive optimum?

5. ◦ Two [uniform machines](/uniform-machine-scheduling/) have speeds $s = (3, 1)$, and the jobs have work $p = (6, 4, 2)$. Compute the preemptive optimum from the bounds $P/S$ and the top-$k$ ratios. Then take the jobs longest first and put each on the machine where it would end first. Is the result optimal?

6. ◦ Write each problem in the [three-field notation](/scheduling-notation/), and say whether the chapter solves it exactly in polynomial time or only approximately, naming the method: (a) one machine, precedence constraints, largest lateness; (b) identical machines, preemption allowed, makespan; (c) two-machine flow shop, makespan; (d) unrelated machines, makespan; (e) one machine, release dates, total completion time.

7. ◦ Two machines get six jobs with times $a = 3$, $b = 2$, $c = 2$, $d = 4$, $e = 1$, $f = 5$ and the [precedence constraints](/precedence-constrained-scheduling/) $a \to c$, $a \to d$, $b \to d$, $d \to e$. Run list scheduling with the list $a, b, c, d, e, f$. Compute the [critical path bound](/critical-path-lower-bound/) and $\lceil P/m \rceil$, and find OPT.

8. ◦ One machine has four jobs with $p = (2, 4, 1, 3)$ and due dates $d = (9, 5, 3, 7)$. Compute $L_{\max}$ and $\sum C_j$ for the [earliest due date](/earliest-due-date-first/) order and for the [shortest processing time](/shortest-processing-time-first/) order. Which order is optimal for which objective?

9. ◦ Five jobs, already in due date order, have $p = (2, 5, 3, 1, 4)$ and $d = (3, 6, 7, 8, 9)$. Run [Moore-Hodgson](/minimizing-tardy-jobs/). Which jobs are late, and is the number of late jobs optimal?

10. • Prove that LPT is optimal on identical machines when $n = m + 1$.

11. • Prove that no deterministic online algorithm for makespan on two identical machines has ratio below $3/2$. Conclude that list scheduling is the best online algorithm for $m = 2$.

12. • In [machine covering](/machine-covering/), three machines get $p = (9, 7, 6, 5, 4, 3, 2)$. Run LPT, which gives each job to a least loaded machine, and compute the least load. Find OPT, and compare the ratio with $\frac{3m - 1}{4m - 2}$.

13. • Twelve unit jobs on two machines form an in-tree with root $r$. The arcs, each from a job to its successor, are $a \to r$, $b \to r$, $c \to a$, $d \to a$, $e \to a$, $f \to b$, $g \to c$, $h \to c$, $i \to f$, $j \to i$ and $k \to j$. Compute the levels and run [Hu's algorithm](/hu-algorithm/), breaking ties alphabetically. Prove that the makespan is optimal, although the longest chain and $\lceil n/m \rceil$ are both 6.

14. • One machine has five jobs, $p = (3, 2, 4, 1, 2)$, $d = (6, 9, 8, 4, 12)$, and the constraints $J_3 \to J_4$, $J_1 \to J_2$ and $J_2 \to J_5$. Run [Lawler's algorithm](/lawler-algorithm/) for $L_{\max}$. Give the order and $L_{\max}$, and explain why the earliest due date order cannot be used.

15. • Four jobs share the due date 10, with $p = (4, 5, 6, 3)$ and weights $w = (5, 6, 8, 3)$. Find the least total weight of [late jobs](/weighted-tardy-jobs/), and compare it with the late weight of the schedule that Moore-Hodgson finds when it ignores the weights. Which classic problem is this?

16. • One machine has four jobs with $p = (4, 3, 6, 2)$ and $d = (5, 6, 8, 9)$. Compute the [total tardiness](/total-tardiness-minimization/) of the earliest due date order and of the shortest processing time order, and find the optimum.

17. • On identical machines with $w_j = p_j$ for every job, prove that $\sum_j w_j C_j = \frac12 \sum_i L_i^2 + \frac12 \sum_j p_j^2$, where $L_i$ is the load of machine $i$, so that every order is a [Smith's rule](/smith-rule/) order. For $p = (1, 1, 2, 2, 4)$ on two machines, find the best and the worst list schedule over all orders and the optimum, and compare the worst ratio with the bound $(1 + \sqrt 2)/2$ for WSPT list scheduling.

18. • One machine has five jobs with $p = (2, 3, 1, 2, 4)$, $w = (1, 6, 2, 3, 4)$ and the constraints $J_1 \to J_2$ and $J_4 \to J_5$. Find the [Sidney decomposition](/sidney-decomposition/), the cost $\sum w_j C_j$ of the order it gives, and the cost of Smith's order without the constraints.

19. • Five jobs $(a_j, b_j)$ are $(4, 2)$, $(1, 3)$, $(3, 3)$, $(5, 1)$ and $(2, 4)$. Find an optimal schedule of the two-machine [flow shop](/flow-shop-scheduling/) by Johnson's rule and prove that it is optimal. Then find the optimum of the two-machine [open shop](/open-shop-scheduling/) on the same jobs.

20. • In [scheduling with rejection](/scheduling-with-rejection/), the cost is the makespan of the accepted jobs plus the penalties of the rejected ones. A simpler rule than the one in the entry accepts job $j$ exactly when $p_j \le m e_j$ and schedules the accepted jobs by LPT, with no guess of the longest accepted job. Show that its ratio can come arbitrarily close to $m$.

21. ★ Take the [Hochbaum-Shmoys scheme](/hochbaum-shmoys-ptas/) with $k = 3$. List the configurations, and show that none holds more than three long jobs. Then run the scheme on three machines with $p = (7, 7, 7, 7, 5, 2)$: give the guesses of the binary search, the rounded sizes at $T = 12$ and $T = 13$, and the final makespan. Compare it with OPT.

22. ★ Let $C^* = \max(P/m, p_{\max})$ be the [preemptive optimum](/preemptive-makespan-scheduling/) on $m$ identical machines. Prove that the nonpreemptive optimum is at most $\frac{2m}{m + 1} C^*$, and show that the bound is tight.

23. ★ In machine covering, prove that list scheduling in any order, each job to a least loaded machine, gives a least load of at least $\text{OPT}/m$. Together with the online lower bound in the entry, this makes list scheduling an optimal online algorithm. Show that the bound $1/m$ is reached.

24. ★ In online [restricted assignment](/restricted-assignment-scheduling/), each unit job comes with a set of allowed machines, and greedy puts it on an allowed machine of least load, with ties to the lowest number. For $m = 2^k$, give a sequence of unit jobs on which greedy reaches makespan $k + 1$ while OPT is 1.

25. ★ For $Q \mid\mid \sum C_j$, a job placed $k$-th from the end on a machine of speed $s_i$ adds $k\, p_j / s_i$ to the total. Prove that an optimal schedule pairs the $n$ smallest coefficients $k/s_i$ with the jobs, the longest job with the smallest coefficient. Use this to solve the instance with speeds $(2, 1)$ and $p = (1, 2, 3, 4, 5)$.
