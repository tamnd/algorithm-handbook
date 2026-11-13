1. ◦ Four jobs P1, P2, P3 and P4 arrive at time 0 in this order, with CPU bursts of 5, 2, 9 and 4. Compute the mean waiting time under [FCFS](/fcfs-scheduling/), [shortest job first](/shortest-job-first/) and [round robin](/round-robin/) with quantum 3 and no switch cost. For round robin, give also the mean response time, as defined in [scheduling metrics](/scheduling-metrics/).

2. ◦ One job with a burst of 100 and ten jobs with a burst of 1 arrive at time 0, with the long job at the head of the queue. Compute the mean waiting time under FCFS and under SJF, and their ratio.

3. ◦ A round-robin scheduler has 20 ready processes and a switch time of 0.1 ms. Using the bound of the round robin entry, find the largest quantum for which every process waits at most 100 ms between two turns, and the smallest quantum for which switching wastes at most 2% of the processor. Show that with 21 processes no quantum meets both goals.

4. ◦ Three clients hold 50, 30 and 20 tickets in [lottery scheduling](/lottery-scheduling/), with one draw per quantum. Find the probability that the client with 20 tickets loses five draws in a row, and the expected number of draws up to its first win. Over 100 draws, give the mean and the standard deviation of the number of wins of the client with 50 tickets.

5. ◦ Clients A, B and C hold 3, 2 and 1 tickets in [stride scheduling](/stride-scheduling/) with $\mathit{stride1} = 6$. All passes start at 0, and ties go to the client that joined first, in the order A, B, C. Give the clients that run in the first 12 quanta and the passes after quantum 6.

6. ◦ A disk has cylinders 0 to 99, and the head is at cylinder 50. The queue holds requests for cylinders 82, 17, 43, 61, 3, 95 and 28, in that order. Find the total head movement under FCFS, [SSTF](/shortest-seek-time-first/), [LOOK](/look/) moving first toward 0, LOOK moving first toward 99, and [C-LOOK](/c-look/) moving up, with the return jump counted as movement. Compare each with the static optimum of [disk scheduling](/disk-scheduling/).

7. ◦ Four periodic tasks have periods 4, 6, 10 and 15 and execution times 1, 1, 2 and 3. Find the [hyperperiod](/hyperperiod/), the number of jobs released in one hyperperiod, the [utilization](/utilization/) and the busy time of the processor in one hyperperiod.

8. ◦ Three tasks $(C, T)$ = (2, 6), (2, 8) and (3, 12) have implicit deadlines and [rate-monotonic](/rate-monotonic-scheduling/) priorities. Apply the [Liu-Layland bound](/liu-layland-utilization-bound/), the hyperbolic bound and [response-time analysis](/response-time-analysis/). Which tests accept the set?

9. ◦ Four jobs have processing times and weights $(p_j, w_j)$ = (3, 1), (1, 2), (4, 3) and (2, 1). Find the order of [Smith's rule](/smiths-rule/) and its weighted completion time $\sum w_j C_j$. Compare it with the order by shortest processing time.

10. ◦ Five jobs have times $(a_j, b_j)$ on machines 1 and 2 of a [two-machine flow shop](/two-machine-flow-shop/): (3, 6), (5, 2), (1, 2), (6, 6) and (7, 5). Find the order of [Johnson's rule](/johnsons-rule/) and its makespan, and show that the makespan meets the lower bound $\sum_j a_j + \min_j b_j$.

11. • Jobs with bursts $b_{(1)} \le \cdots \le b_{(n)}$ arrive at time 0. Under processor sharing, the limit of round robin, the job with the $k$-th shortest burst completes at $b_{(1)} + \cdots + b_{(k-1)} + (n-k+1)\, b_{(k)}$. Show that the total completion time of processor sharing is $2\sum_j C_j^{\mathrm{SJF}} - \sum_j b_j$, so that it is less than twice the optimum, and that the ratio is $2n/(n+1)$ when all bursts are equal. Processor sharing does not use the sizes, so this is a bound for a policy of the kind studied under [non-clairvoyant flow time](/non-clairvoyant-flow-time-minimization/).

12. • In the [Completely Fair Scheduler](/completely-fair-scheduler/), take a target latency of 48 ms and a minimum granularity of 6 ms. Find the slices of three tasks of weights 1024, 1024 and 2048, and how much each slice adds to the virtual runtime of its task. Then take two tasks of weights 1024 and 15, and show that line L7 of the entry gives a slice shorter than the minimum granularity. From how many tasks of equal weight on does the period grow beyond the target latency?

13. • Two tasks $(C, T)$ = (3, 6) and (4, 9) have implicit deadlines. Show with response-time analysis that rate-monotonic priorities miss a deadline. Draw the schedule of [earliest deadline first](/earliest-deadline-first/) over the hyperperiod, breaking ties in favour of the running job, and check that every deadline is met.

14. • Three tasks $(C, T, D)$ = (1, 4, 2), (1, 5, 4) and (4, 10, 7) are released together. Show that the density test fails and that [deadline-monotonic](/deadline-monotonic-scheduling/) priorities miss a deadline. Then apply the processor demand criterion of [schedulability analysis](/schedulability-analysis/): compute the bound $L_a$ and the demand at every absolute deadline up to it, and decide whether EDF meets every deadline.

15. • Three tasks $(C, T)$ = (2, 3) run on two identical processors, with $U = 2$. Show that global EDF, which runs the two jobs of earliest deadline with ties broken by task index, misses a deadline at time 3. Give a schedule of period 3 that meets every deadline, so that EDF is not optimal on two processors.

16. • Three jobs $(r_j, d_j, w_j)$ = (0, 2, 4), (0, 6, 4) and (3, 5, 2) run on one processor whose power at speed $s$ is $s^\alpha$. Run the [YDS algorithm](/yds-algorithm/): find each critical interval, the speeds, and the least energy for $\alpha = 2$ and for $\alpha = 3$.

17. • Three jobs share a lock S under fixed priorities H > M > L. Job L is released at 0 and runs 1 unit, then 3 units inside S, then 1 unit. Job H is released at 2 and runs 1 unit, then 1 unit inside S. Job M is released at 3 and runs 4 units with no lock. Find the completion time of each job with no protocol, with the [priority inheritance protocol](/priority-inheritance-protocol/) and with the [priority ceiling protocol](/priority-ceiling-protocol/), and the length of the [priority inversion](/priority-inversion/) of H in each case.

18. • Five jobs have processing times and due dates $(p_j, d_j)$ = (4, 5), (3, 6), (2, 8), (5, 9) and (1, 10). Run the [Moore-Hodgson algorithm](/moore-hodgson-algorithm/) and give the jobs it makes late. Show by hand that no schedule has four jobs on time.

19. • With one common due date $d$, the problem $1 \mid d_j = d \mid \sum w_j U_j$ of [minimizing late jobs](/minimizing-late-jobs/) is a knapsack problem. Give a dynamic program in $O(nd)$ time, and solve it for $d = 10$ and $(p_j, w_j)$ = (4, 5), (3, 4), (5, 6), (2, 3) and (6, 7). Why is this running time not polynomial?

20. • A project has activities A (3), B (2), C (4) after A, D (2) after A and B, E (3) after C and D, and F (1) after B, with durations in parentheses. With the [critical path method](/critical-path-method/), find the project time, the float of each activity and the critical path. Then let C and D each need the only unit of a resource. Run the serial scheme of [resource-constrained project scheduling](/resource-constrained-project-scheduling/) with the list ordered by latest start time, and show that its makespan is optimal.

21. • A cluster has 4 processors. Jobs J1 to J4 are queued at time 0 in this order, and they need 2, 4, 2 and 2 processors for 4, 2, 3 and 5 time units, with exact runtime estimates. Find the start times and the mean wait under FCFS with no [backfilling](/backfilling/), and under EASY backfilling.

22. • A cluster has 10 CPUs and 20 GB of memory. The tasks of user A need $\langle 1, 4 \rangle$, those of B $\langle 2, 1 \rangle$ and those of C $\langle 1, 1 \rangle$. Run [dominant resource fairness](/dominant-resource-fairness/) by progressive filling. Give each user's dominant resource, its number of tasks and its dominant share, and the resource left idle.

23. ★ Let the periods of an implicit-deadline task set be harmonic: each period divides every longer one. Prove that rate-monotonic priorities meet every deadline if and only if $U \le 1$.

24. ★ Prove the Liu-Layland bound for two tasks without the hyperbolic bound. Fix $T_1 = 1$ and $T_2 = r$ with $1 < r < 2$, and call a task set *full* if rate-monotonic priorities meet every deadline but any increase of $C_1$ or $C_2$ makes one miss. Show that the least utilization of a full set is $r + 2/r - 2$, that its minimum over $r$ is $2(\sqrt 2 - 1)$, and use Step 1 of the entry's proof to deal with $r \ge 2$.

25. ★ In [pinwheel scheduling](/pinwheel-scheduling/), let every number $a_i$ be a power of 2 and $\sum_i 1/a_i \le 1$. Prove that a schedule exists, by giving task $i$ every $a_i$-th slot from an offset you choose. Deduce that every instance with density at most $1/2$ is schedulable.

26. ★ The problem $1 \mid r_j \mid \sum C_j$ is strongly NP-hard, while its preemptive version is solved by SRPT ([SRPT optimality](/srpt-optimality/)). Take the SRPT schedule, list the jobs in the order of their completion times in it, and run them without preemption in that order, each as early as possible. Prove that each job completes at most twice as late as in the SRPT schedule, so that this is a 2-approximation.

27. ★ Prove that for every feasible schedule of a resource-constrained project there is an activity list for which the serial scheme starts every activity no later than the schedule does. Conclude that some list gives an optimal schedule.
