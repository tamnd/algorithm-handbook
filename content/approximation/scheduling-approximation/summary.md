## What to remember

- **Every makespan proof compares with a lower bound.** On identical machines $\text{OPT} \ge \max(P/m, p_{\max})$, where $P$ is the total time, and with precedence constraints also $\text{OPT} \ge L$, the length of the longest chain. With preemption the first bound is the optimum, which [McNaughton's rule](/mcnaughton-wrap-around/) reaches.
- **Greedy rules on identical machines.** [List scheduling](/list-scheduling/) in any order is within $2 - 1/m$. Sorting longest first improves this to $\frac43 - \frac{1}{3m}$ ([LPT](/longest-processing-time-first/)). Both bounds are tight.
- **A makespan of $T$ is a bin packing with bins of size $T$.** [MULTIFIT](/multifit-algorithm/) searches for the least $T$ at which first fit decreasing uses at most $m$ bins, within $\frac{13}{11} + 2^{-k}$ after $k$ rounds. The [Hochbaum-Shmoys scheme](/hochbaum-shmoys-ptas/) rounds the long jobs and either schedules within $(1 + 1/k)T$ or proves $\text{OPT} > T$. Since $P \mid\mid C_{\max}$ is strongly NP-hard, there is no FPTAS unless P = NP.
- **Unrelated machines need an LP.** [Lenstra-Shmoys-Tardos](/lenstra-shmoys-tardos/) forbids the pairs with $p_{ij} > T$, takes a vertex of the assignment LP, and gives each split job its own machine by a matching, for ratio 2. No ratio below $3/2$ is possible unless P = NP. On [uniform machines](/uniform-machine-scheduling/) LPT is still within $2m/(m + 1)$.
- **Precedence keeps $2 - 1/m$.** List scheduling with precedence is within $2 - 1/m$. Unit jobs are exact on in-trees by [Hu's algorithm](/hu-algorithm/) and on two machines by [Coffman-Graham](/coffman-graham-algorithm/).
- **Exchange arguments solve one machine.** [Earliest due date first](/earliest-due-date-first/) minimizes $L_{\max}$, [shortest processing time first](/shortest-processing-time-first/) $\sum C_j$, [Smith's rule](/smith-rule/) $\sum w_j C_j$, [Lawler's algorithm](/lawler-algorithm/) any $f_{\max}$ under precedence, and [Moore-Hodgson](/minimizing-tardy-jobs/) $\sum U_j$.
- **One more feature makes them hard.** Release dates make $1 \mid r_j \mid L_{\max}$ and $1 \mid r_j \mid \sum C_j$ strongly NP-hard. $\sum w_j U_j$ and [total tardiness](/total-tardiness-minimization/) are NP-hard but have FPTASs. Precedence makes $\sum w_j C_j$ strongly NP-hard, and any order of the [Sidney pieces](/sidney-decomposition/) is within 2.
- **Shops.** Johnson's rule solves the two-machine [flow shop](/flow-shop-scheduling/) and Gonzalez-Sahni the two-machine [open shop](/open-shop-scheduling/), whose optimum is $\max(\Pi_{\max}, P_{\max})$, the larger of the largest load and the longest job. Three machines make each NP-hard, and for general $m$ no ratio below $5/4$ is possible unless P = NP.

## The main algorithms side by side

| Algorithm | Problem | Ratio | Time |
|---|---|---|---|
| McNaughton | $P \mid pmtn \mid C_{\max}$ | exact | $\Theta(n + m)$ |
| List scheduling | $P \mid\mid C_{\max}$ | $2 - 1/m$ | $\Theta(m + n \log m)$ |
| LPT | $P \mid\mid C_{\max}$ | $\frac43 - \frac{1}{3m}$ | $\Theta(n \log n + m)$ |
| MULTIFIT, $k$ rounds | $P \mid\mid C_{\max}$ | $\frac{13}{11} + 2^{-k}$ | $\Theta(n \log n + k\, n \log m)$ |
| Hochbaum-Shmoys | $P \mid\mid C_{\max}$ | $1 + 1/k$ | polynomial for fixed $k$ |
| Lenstra-Shmoys-Tardos | $R \mid\mid C_{\max}$ | 2 | $O(L \log(nP) + nm)$ |
| List scheduling | $P \mid prec \mid C_{\max}$ | $2 - 1/m$ | $O(n \log n + e)$ |
| Coffman-Graham | $P \mid prec, p_j = 1 \mid C_{\max}$ | exact for $m = 2$; $2 - 2/m$ | $O(n(n + e))$ |
| Earliest due date | $1 \mid\mid L_{\max}$ | exact | $\Theta(n \log n)$ |
| Moore-Hodgson | $1 \mid\mid \sum U_j$ | exact | $O(n \log n)$ |
| Shortest processing time | $1 \mid\mid \sum C_j$ | exact | $\Theta(n \log n)$ |
| Johnson | $F2 \mid\mid C_{\max}$ | exact | $O(n \log n)$ |

: Worst-case ratios, all for minimization. There are $n$ jobs, $m$ machines and $e$ precedence arcs; $P$ is the total processing time, but the largest $p_{ij}$ for Lenstra-Shmoys-Tardos; $L$ is the time to find a vertex of one LP.

## Choosing a method

- For identical machines with all jobs known, use LPT; when jobs arrive one at a time, use list scheduling.
- When LPT is not close enough, try MULTIFIT, a few runs of first fit decreasing. The Hochbaum-Shmoys scheme is practical only for small $k$, since its time grows like $n^{k^2}$.
- For machines of different speeds, use LPT that puts each job where it would end first. For arbitrary times $p_{ij}$, or jobs allowed on some machines only, solve the LP and round it.
- With precedence constraints, use list scheduling, and for unit jobs Hu on in-trees and Coffman-Graham on two machines.
- On one machine, look first for an exact rule. Use a dynamic program or an FPTAS only when weights, release dates or tardiness sums make the problem hard.
- For larger shops the known ratios are weak; compare the schedule with $\max(\Pi_{\max}, P_{\max})$ and improve it by local search.
