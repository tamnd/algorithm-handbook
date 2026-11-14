A print shop has $m$ identical printers and a list of jobs, each with a running time, and wants the last job to finish as early as possible. This is [makespan minimization](/makespan-minimization/), and it is NP-hard already for two machines. Problems of this kind arise in factories, compilers, operating systems and computing clusters. A compiler orders instructions that wait for one another; a cluster spreads tasks over servers of different speeds; a workshop meets due dates promised to customers. Scheduling was also one of the first areas studied for worst-case ratios: Ronald Graham analyzed list scheduling in 1966.

The methods are close to those of bin packing. A schedule with makespan $T$ on $m$ machines is a packing of the jobs into $m$ bins of size $T$. Every ratio proof compares the schedule with a lower bound on the optimum that is easy to compute: the average load $P/m$, the longest job, and, with precedence constraints, the longest chain. Some problems of the chapter are not hard at all. Earliest due date first, shortest processing time first and Johnson's rule solve their problems exactly, and the chapter keeps them because the hard variants are built on them.

The chapter is in nine groups, read in order.

## What the chapter covers

1. **Problems, notation and lower bounds.** The [makespan](/makespan/), the [machine environments](/machine-environments/), the [three-field notation](/scheduling-notation/) that names every problem in the chapter, and the [lower bounds on the makespan](/makespan-lower-bounds/).
2. **Preemption.** [Preemptive makespan scheduling](/preemptive-makespan-scheduling/) and [McNaughton's wrap-around rule](/mcnaughton-wrap-around/), which meets the lower bound $\max(P/m, p_{\max})$ in linear time.
3. **Greedy rules on identical machines.** [List scheduling](/list-scheduling/) with [Graham's bound](/list-scheduling-bound/) $2 - 1/m$, the [longest processing time rule](/longest-processing-time-first/) with [its bound](/lpt-bound/) $\frac43 - \frac{1}{3m}$, [Sorted-Balance](/sorted-balance/), and [machine covering](/machine-covering/), which maximizes the least load.
4. **Bin packing and approximation schemes.** [MULTIFIT](/multifit-algorithm/), which searches for the least bin size at which first fit decreasing succeeds, [its bound](/multifit-bound/) $\frac{13}{11}$, and the [Hochbaum-Shmoys scheme](/hochbaum-shmoys-ptas/), a PTAS by dual approximation. Chapter 18.5 treats the same scheme as an example of [dual approximation](/dual-approximation/).
5. **Uniform and unrelated machines.** [Uniform machines](/uniform-machine-scheduling/) with speeds, [unrelated machines](/unrelated-machine-scheduling/), the [Lenstra-Shmoys-Tardos](/lenstra-shmoys-tardos/) LP rounding with ratio 2, [restricted assignment](/restricted-assignment-scheduling/), and the [lower bound](/unrelated-makespan-inapproximability/) of $3/2$ for unrelated machines.
6. **Precedence constraints.** The [critical path bound](/critical-path-lower-bound/), [list scheduling with precedence](/precedence-constrained-scheduling/), [Graham's anomalies](/graham-anomalies/), and the exact algorithms of [Hu](/hu-algorithm/) for in-trees and of [Coffman and Graham](/coffman-graham-algorithm/) for two machines.
7. **Due dates on one machine.** [Lateness and tardiness](/lateness-and-tardiness/), [earliest due date first](/earliest-due-date-first/), [maximum lateness](/maximum-lateness-minimization/) with release dates, [Lawler's algorithm](/lawler-algorithm/) for precedence, the [Moore-Hodgson algorithm](/minimizing-tardy-jobs/) for the number of late jobs, its [weighted version](/weighted-tardy-jobs/), and [total tardiness](/total-tardiness-minimization/).
8. **Completion time, release dates and flow time.** [Shortest processing time first](/shortest-processing-time-first/), [weighted completion time](/weighted-completion-time-scheduling/) by Smith's rule, [Sidney's decomposition](/sidney-decomposition/) for precedence, [release dates](/scheduling-with-release-dates/) and [flow time](/flow-time-minimization/).
9. **Shops and other models.** The [flow shop](/flow-shop-scheduling/), [job shop](/job-shop-scheduling/) and [open shop](/open-shop-scheduling/), then [setup times](/scheduling-with-setup-times/), [moldable tasks](/moldable-task-scheduling/) and [scheduling with rejection](/scheduling-with-rejection/).

## A first reading

For a first pass, read these entries in order:

1. [Three-field notation](/scheduling-notation/)
2. [Lower bounds on the makespan](/makespan-lower-bounds/)
3. [McNaughton's wrap-around rule](/mcnaughton-wrap-around/)
4. [List scheduling](/list-scheduling/)
5. [Graham's bound for list scheduling](/list-scheduling-bound/)
6. [Longest processing time first](/longest-processing-time-first/)
7. [The LPT bound](/lpt-bound/)
8. [The Hochbaum-Shmoys scheme](/hochbaum-shmoys-ptas/)
9. [Unrelated machine scheduling](/unrelated-machine-scheduling/)
10. [Lenstra-Shmoys-Tardos rounding](/lenstra-shmoys-tardos/)
11. [Precedence-constrained scheduling](/precedence-constrained-scheduling/)
12. [Earliest due date first](/earliest-due-date-first/)
13. [Shortest processing time first](/shortest-processing-time-first/)
14. [Flow shop scheduling](/flow-shop-scheduling/)

These show the three lower bounds, the two greedy rules with their proofs, the scheme that gets as close as you like, the LP method for unrelated machines, and the two exchange arguments that solve one machine exactly. Skip at first MULTIFIT and its bound, Sorted-Balance, which repeats the longest processing time rule, Graham's anomalies, the tardiness entries after Moore-Hodgson, and the models of the last group after the shops.

## Before you start

From Chapter 18.1 you need [bin packing](/bin-packing/) and [first fit decreasing](/first-fit-decreasing/); from Chapter 18.5, the [approximation ratio](/approximation-ratio/) and the [PTAS](/ptas/). Ratios here follow the volume: $\rho \ge 1$ for minimization, and $\alpha \le 1$ for machine covering, the one maximization problem. From Volume 15 you need the [linear programming problem](/linear-programming-problem/), the [LP relaxation](/lp-relaxation/) and [basic feasible solutions](/basic-feasible-solution/), for group 5. From Volume 7 you need the [directed acyclic graph](/directed-acyclic-graph/), [topological sort](/topological-sort/) and [bipartite matching](/bipartite-matching/). From Volume 2 you need the [greedy algorithm](/greedy-algorithm/), the [exchange argument](/exchange-argument/) and dynamic programming, and from Volume 3 the [binary heap](/binary-heap/). The online versions of these problems, where jobs arrive one by one, are in Volume 19, starting with [online makespan minimization](/online-makespan-minimization/).

The entries also use NP-hardness, strong NP-hardness and pseudo-polynomial time, whose entries belong to Volume 39 and are not yet written; their definitions are in any textbook on computational complexity.
