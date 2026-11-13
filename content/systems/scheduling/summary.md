## What to remember

- On one server, every [work-conserving](/work-conserving-scheduling/) scheduler leaves the same unfinished work $V(t)$ at every time $t$, and every nonpreemptive one gives the same $\sum_j b_j W_j$. The order decides who waits, not how much work is left.
- Shortest job first minimizes the mean wait only when all jobs are present at time 0 with known bursts. With release times, $1 \mid r_j \mid \sum C_j$ is strongly NP-hard ([scheduling problem](/scheduling-problem/)), preemptive [SRPT](/srpt/) is optimal for total flow time, and a deterministic scheduler blind to the sizes has a worst-case ratio of $\Omega(n^{1/3})$ for flow time ([CPU scheduling](/cpu-scheduling/)).
- Lottery scheduling gives each client its share in expectation, with a standard deviation of $\sqrt{np(1-p)}$ wins in $n$ draws. Stride scheduling is deterministic: two clients never drift a full quantum from their ratio. The [Completely Fair Scheduler](/completely-fair-scheduler/) keeps each task within one slice of its weighted share, proved only for a fixed set of tasks that never block.
- For a static batch of disk requests with linear seek cost, the least head movement is $(hi - lo) + \min(|r - lo|, |r - hi|)$, reached by LOOK toward the nearer end. With service time 0 and one cylinder per tick, SCAN and LOOK wait at most $2(C-1)-1$ ticks and C-LOOK fewer than $3(C-1)$; SSTF and FCFS have no bound.
- With implicit deadlines on one preemptive processor, a task set is feasible if and only if $U = \sum_i C_i/T_i \le 1$, and EDF then meets every deadline. Rate-monotonic priorities are optimal among fixed priorities and succeed when $U \le n(2^{1/n}-1)$, a bound that tends to $\ln 2 \approx 0.693$, or when $\prod_i (U_i+1) \le 2$. Both tests are sufficient only.
- Response-time analysis, $R_i = C_i + B_i + \sum_{j<i} \lceil R_i/T_j \rceil C_j$, is exact for $D_i \le T_i$ with no jitter and no blocking. [Priority inheritance](/priority-inheritance-protocol/) limits blocking to $\min(n, m)$ critical sections but allows deadlock; the [ceiling protocol](/priority-ceiling-protocol/) limits it to one and prevents deadlock.
- Smith's ratio $p_j/w_j$, Moore-Hodgson and Johnson's rule solve $1 \mid\mid \sum w_j C_j$, $1 \mid\mid \sum U_j$ and $F2 \mid\mid C_{\max}$ exactly in $O(n \log n)$ time. Weights in the late-jobs problem or precedence in Smith's problem make them NP-hard; a third machine, or resource limits on a project, make them strongly NP-hard.

| Method | Model | Guarantee | Time | Source |
|---|---|---|---|---|
| SJF | one CPU, all jobs at 0, exact bursts | least mean wait | $O(n \log n)$ | [SJF optimality](/sjf-optimality/) |
| Round robin | $n$ jobs, quantum $q$, switch $s$ | wait between turns $\le (n-1)(q+s)+s$ | $O(1)$ per dispatch | [round robin](/round-robin/) |
| Lottery | tickets | share in expectation | $O(\log c)$ per draw | [lottery scheduling](/lottery-scheduling/) |
| Stride | tickets | error under 1 quantum per pair | $O(\log c)$ per quantum | [stride scheduling](/stride-scheduling/) |
| LOOK | static batch, linear seek | optimal toward the nearer end | $O(n \log n)$ | [disk scheduling](/disk-scheduling/) |
| EDF | one preemptive CPU | optimal; $U \le 1$ exact for $D = T$ | $O(\log k)$ per event | [EDF optimality](/edf-optimality/) |
| RTA | fixed priorities, $D \le T$ | exact test | pseudo-polynomial | [response-time analysis](/response-time-analysis/) |
| Smith's rule | $1 \mid\mid \sum w_j C_j$ | optimal | $\Theta(n \log n)$ | [Smith's rule](/smiths-rule/) |
| Moore-Hodgson | $1 \mid\mid \sum U_j$ | optimal | $O(n \log n)$ | [Moore-Hodgson](/moore-hodgson-algorithm/) |
| Johnson's rule | $F2 \mid\mid C_{\max}$ | optimal | $\Theta(n \log n)$ | [Johnson's rule](/johnsons-rule/) |
| CPM | precedence, no resources | least project time | $\Theta(n + m)$ | [critical path method](/critical-path-method/) |
| YDS | deadlines, power $s^\alpha$ | least energy, offline | $O(n^3)$ | [YDS algorithm](/yds-algorithm/) |
| DRF | divisible tasks, $m$ resources | sharing incentive, envy-free, Pareto efficient | $O(n^2 m)$ | [DRF](/dominant-resource-fairness/) |

: Methods with a stated guarantee, the model it holds in, and the cost. Here $c$ is the number of clients, $k$ the number of jobs and $m$ the number of arcs (CPM) or resource types (DRF). The multilevel feedback queue, HEFT and backfilling have no such guarantee and are judged by measurement.

## Choosing a method

For a general-purpose kernel, use a multilevel feedback queue or a weighted fair scheduler such as CFS, with a quantum long enough that the switch cost is a small part of it. For exact shares, use stride scheduling; lottery scheduling is simpler when shares change often.

For a real-time system, choose fixed priorities or EDF first. Deadline-monotonic priorities with response-time analysis give an exact test for constrained deadlines. EDF uses the whole processor, and the [constant bandwidth server](/constant-bandwidth-server/) isolates tasks under it. Use the utilization bounds as quick checks only, and guard shared locks with the ceiling protocol.

For a disk queue, use LOOK or C-LOOK; SSTF can starve. For machine and project problems, check for one of the exact cases, and otherwise go to [list scheduling](/list-scheduling/) and its relatives. For a batch cluster, run FCFS with backfilling, and divide several resources by DRF.
