1. ◦ Ten talks ask for a room, as half-open intervals: $a = [0, 3)$, $b = [1, 4)$, $c = [2, 6)$, $d = [3, 5)$, $e = [4, 8)$, $f = [5, 7)$, $g = [6, 9)$, $h = [7, 10)$, $i = [8, 11)$, $j = [9, 12)$. Run [earliest finish time first](/earliest-finish-time-first/) and list the talks it keeps. How many sets of pairwise disjoint talks have the largest size?

2. ◦ For the ten talks of Exercise 1, find the depth, the largest number of talks that share a point of time, and say over which times it is reached. Run greedy by start time with a min-heap, as in [interval partitioning](/interval-partitioning/), and give the talks in each room.

3. ◦ A knapsack holds weight 20. The items, as (value, weight), are $A = (36, 6)$, $B = (40, 8)$, $C = (54, 12)$ and $D = (10, 5)$. Solve the [fractional knapsack](/fractional-knapsack/). Then, for whole items only, give the value that the same ratio rule reaches and the true optimum.

4. ◦ Six sorted files have sizes 2, 3, 5, 7, 11 and 13. Find the least total cost of merging them into one by two-way merges, as in the [optimal merge pattern](/optimal-merge-pattern/). Then find the least cost with three-way merges, where merging three files costs the sum of their sizes, and say how many empty files you must add.

5. ◦ Use the test for three coins in [canonical coin system](/canonical-coin-system/), with $b = qa + r$ and $0 \le r < a$, to decide which of the systems $\{1, 3, 7\}$, $\{1, 4, 9\}$, $\{1, 7, 10\}$ and $\{1, 5, 12\}$ are canonical. For each one that is not, give the smallest amount where paying largest coin first is not optimal, with the greedy and the optimal coins.

6. ◦ Five jobs, as (processing time, weight), are $a = (4, 1)$, $b = (2, 3)$, $c = (3, 3)$, $d = (1, 2)$ and $e = (5, 4)$. Order them by [Smith's rule](/smith-rule/) and compute $\sum w_j C_j$. What does shortest processing time first give?

7. ◦ Six jobs, as (processing time, due date), are $a = (4, 10)$, $b = (3, 15)$, $c = (5, 9)$, $d = (2, 8)$, $e = (2, 4)$ and $f = (4, 5)$. Run earliest due date first and give $L_{\max}$ and the number of late jobs. Then run the Moore-Hodgson algorithm of [minimizing the number of late jobs](/minimizing-number-of-late-jobs/): which jobs does it drop, in which order, and how many jobs end late?

8. ◦ Seven unit jobs, as (deadline, profit), are $a = (2, 40)$, $b = (1, 35)$, $c = (3, 30)$, $d = (1, 25)$, $e = (3, 20)$, $f = (2, 15)$ and $g = (4, 10)$. Run the greedy algorithm of [job sequencing with deadlines](/job-sequencing-with-deadlines/), placing each kept job in the latest free slot before its deadline. Give the slot of each kept job and the profit.

9. ◦ Six vectors over $\mathbb{F}_2$ are $a = 1100$, $b = 0110$, $c = 1010$, $d = 0011$, $e = 1001$ and $f = 1111$, with weights 5, 3, 6, 4, 2 and 7. What is the rank of this [linear matroid](/linear-matroid/)? Run the [matroid greedy algorithm](/matroid-greedy-algorithm/) and say which vectors it rejects and why.

10. • Show by two small instances that for the fractional knapsack neither "largest value first" nor "lightest item first" is optimal.

11. • A variant of interval partitioning sorts the intervals by finish time and puts each one in the first room, in order of opening, whose last interval ends by its start. Find four half-open intervals of depth 2 on which this variant opens three rooms.

12. • Each talk now has a value: $a = [0, 3)$ worth 3, $b = [2, 5)$ worth 6, $c = [4, 7)$ worth 3, $d = [6, 9)$ worth 6 and $e = [1, 8)$ worth 10. What total value do earliest finish time first and "largest value first" give? Find the best value with the recurrence of [activity selection](/activity-selection/), with the value $v_j$ in place of 1: $M[j] = \max(M[j-1], v_j + M[p(j)])$ over the talks sorted by finish time. This is [weighted interval scheduling](/weighted-interval-scheduling/).

13. • The closed intervals $[0, 3]$, $[1, 5]$, $[2, 4]$, $[4, 7]$, $[3, 8]$, $[6, 9]$, $[7, 10]$ and $[8, 10]$ are to cover the segment $[0, 10]$ with as few of them as possible. The greedy rule takes, among the intervals that start at or before the point covered so far, the one that reaches farthest. Run it, and prove it optimal in general by [greedy stays ahead](/greedy-stays-ahead/) with the point covered after $k$ intervals as the measure.

14. • Files of sizes 1, 1, 2, 3, 5, 8 and 13, the first Fibonacci numbers, are merged two smallest at a time. Show that every merge after the first includes the file made by the previous merge, so that the merge tree is a path with leaves hanging off it. Compute the total cost.

15. • In the order-preserving version of the merge problem, only files next to each other in a fixed row may be merged. Show that the rule "merge the adjacent pair with the smallest sum" is not optimal, with the row of sizes 3, 2, 2, 3.

16. • For which $a \ge 2$ is the system $\{1, a, 2a + 1\}$ canonical? For which is $\{1, a, 2a - 1\}$? For each system that is not canonical, give the smallest counterexample as a function of $a$.

17. • The lateness of job $j$ is $L_j = C_j - d_j$, which may be negative. Show that the order that minimizes the total lateness $\sum L_j$ is shortest processing time first, whatever the due dates. Give two jobs on which earliest due date first does not minimize $\sum L_j$.

18. • For the four jobs $(4, 4)$, $(1, 5)$, $(1, 5)$, $(1, 5)$, as (processing time, due date), show that no order minimizes both $L_{\max}$ and the number of late jobs.

19. • Jobs now take one or two units of time on one machine. Show that the sets of jobs that can all meet their deadlines no longer form a matroid, and give an instance on which taking jobs by decreasing profit, and keeping each one that still fits, is not optimal.

20. • Let $(E, \mathcal{I})$ be a [matroid](/matroid/) and $k \ge 0$. Show that the sets of $\mathcal{I}$ with at most $k$ elements also form a matroid. Which matroid of the chapter is the case where $\mathcal{I}$ holds every subset of $E$?

21. • Prove directly from the matroid axioms, without the element-wise domination of Gale, that the basis returned by the greedy algorithm has the largest smallest weight among all bases.

22. ★ Prove the three-coin test: with $1 < a < b$ and $b = qa + r$, $0 \le r < a$, the system $\{1, a, b\}$ is not canonical exactly when $0 < r < a - q$. For one direction, look at the amount $(q + 1)a$; for the other, use the bound on the smallest counterexample.

23. ★ $n$ files with lengths $L_1 \ge L_2 \ge \cdots \ge L_n$ and equal frequencies go on $m$ tapes, each read from its start. Prove that dealing the files in this order round robin, and storing each tape's files shortest first, minimizes the sum of retrieval times, the problem $P \| \sum C_j$. Check the value 76 of the two-tape example in [optimal tape storage](/optimal-tape-storage/).

24. ★ Jobs now have release dates. Job $a$ is released at time 0 and needs 10 units, job $b$ is released at time 1 and needs 1 unit. Give $\sum C_j$ for the rule "whenever the machine is free, start the shortest released job", for the best order without preemption, and for shortest remaining processing time first with preemption. Then prove that shortest remaining processing time first minimizes $\sum C_j$ when preemption is allowed.

25. ★ With precedence constraints, the rule "at each step run the available job with the earliest due date", where a job is available when all its predecessors are done, can fail for $L_{\max}$. Show this with $a = (1, 10)$, $b = (5, 6)$ and $c = (1, 2)$, as (processing time, due date), where $a$ must precede $c$. Then prove the backward rule: among the jobs with no unscheduled successor, put last the one with the latest due date, and repeat on the rest.

26. ★ The greedy algorithm for a maximum-weight [matching](/maximum-matching/) takes the edges by decreasing weight and keeps each one that shares no end with a kept edge. Matchings are not a matroid, so this can fail. Prove that it always reaches at least half the optimum weight, and show by a path of three edges that the factor $1/2$ cannot be improved.
