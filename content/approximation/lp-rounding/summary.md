## What to remember

- **The LP bounds OPT, and the gap bounds the method.** For minimization $\text{LP}^* \le \text{OPT}$, so rounding at cost $\rho \cdot \text{LP}^*$ gives ratio $\rho$, and no rounding of the same LP proves a ratio below its [integrality gap](/integrality-gap/). A vertex with $r$ tight constraints besides $0 \le x \le 1$ has at most $r$ [fractional](/fractional-solution/) values.
- **Threshold rounding at $t$ costs at most $\text{LP}^*/t$.** With $t = 1/2$ it gives ratio 2 for [weighted vertex cover](/lp-rounding-vertex-cover/), and with $t = 1/f$ ratio $f$ for [set cover](/frequency-rounding-set-cover/). The vertex cover LP is [half-integral](/half-integrality/).
- **Randomized rounding: expectation for cost, Chernoff plus union for feasibility.** It gives congestion $O(\log m / \log \log m) \cdot \max(C^*, 1)$ for [routing](/randomized-rounding/) and expected cost at most $(\ln n + 2)\,\text{OPT}$ for [set cover](/lp-rounding-set-cover/). For MAX-SAT, LP rounding gives $1 - 1/e$, a [random assignment](/random-assignment-max-3-sat/) $7/8$ on 3-literal clauses, and the better of the two $3/4$, the LP gap.
- **Primal-dual: $\text{cost} \le \alpha\beta \sum_i b_i y_i$.** Relaxed complementary slackness with factors $\alpha$ and $\beta$ gives 2 for [weighted vertex cover](/bar-yehuda-even-vertex-cover/) in linear time, $2 - 2/k$ for [Steiner forest](/goemans-williamson-steiner-forest/), and 3 for metric [facility location](/jain-vazirani-facility-location/). [Dual fitting](/dual-fitting/) proves $H_d$ for greedy set cover.
- **Iterative rounding needs one large variable at every vertex.** Every vertex of the cut LP has an edge with $x_e \ge 1/2$, which gives ratio 2 for [survivable network design](/jain-iterative-rounding-network-design/) with any requirements. [Iterative relaxation](/iterative-relaxation/) gives a spanning tree of cost at most OPT with every degree at most $B_v + 1$.
- **Sparse vertices give bicriteria bounds.** A vertex of the [generalized assignment](/shmoys-tardos-gap/) LP has a pseudo-forest support, so rounding costs at most the LP with loads at most $T + \max p_{ij} \le 2T$. The same argument gives ratio 2 for [makespan on unrelated machines](/unrelated-machine-scheduling-makespan/), where $3/2 - \varepsilon$ is NP-hard.
- **A stronger LP can be worth exponentially many variables.** The [configuration LP](/configuration-lp/) is solved by a knapsack separation of its dual; the [Karmarkar-Karp algorithm](/karmarkar-karp-bin-packing/) rounds it to $\text{OPT} + O(\log^2 \text{OPT})$ bins.
- **Filtering keeps each client near its LP cost.** With it [Shmoys-Tardos-Aardal](/shmoys-tardos-aardal-facility-location/) reaches $3/(1 - e^{-3}) \approx 3.16$. For metric facility location the best ratio known is 1.488, and below 1.463 is hard unless NP has slightly superpolynomial algorithms.
- **Dependent rounding keeps sums exact.** [Dependent](/dependent-rounding/), [pipage](/pipage-rounding/) and [swap rounding](/swap-rounding/) keep each marginal $\Pr[X_i = 1] = x_i$ and the chosen sums; dependent and swap rounding give negative correlation, so Chernoff bounds hold. Pipage rounding gives $1 - 1/e$ for maximum coverage under a partition constraint.

## The main algorithms side by side

| Algorithm | Problem | Ratio | Compared with | Time |
|---|---|---|---|---|
| Threshold at $1/2$ | weighted vertex cover | 2 | LP | one LP |
| Threshold at $1/f$ | set cover | $f$ | LP | one LP |
| Bar-Yehuda-Even | weighted vertex cover | 2 | local ratio, feasible dual | $\Theta(n + m)$ |
| Rounds plus repair | set cover | $\ln n + 2$, expected | LP | one LP |
| Random assignment | MAX-3SAT | $7/8$ | number of clauses | $\Theta(n + m)$ |
| Better of LP rounding and random | MAX-SAT | $3/4$ | LP | one LP |
| Goemans-Williamson | Steiner forest | $2 - 2/k$ | dual moats | $O(n(m + np))$ |
| Jain | survivable network design | 2 | LP, each round | $O(mL)$ |
| Shmoys-Tardos | generalized assignment | cost OPT, load $2T$ | LP | $O(L + n^2(n + m)m)$ |
| Karmarkar-Karp | bin packing | $\text{OPT} + O(\log^2 \text{OPT})$ | configuration LP | $O(L \log n + n \log n)$ |
| Shmoys-Tardos-Aardal | metric facility location | $\approx 3.16$ | LP | $O(L + m^2 n^3)$ |
| Jain-Vazirani | metric facility location | 3 | feasible dual | $O(mn \log(mn))$ |

: Worst-case ratios, with $n$ and $m$ as in each entry; $k$ terminals in $p$ pairs for Steiner forest, and $L$ the time to solve one LP.

## Choosing a method

- Solve the LP on your inputs first. A small gap to your best answers says rounding will do well; a large one says to add constraints.
- When each constraint has few variables, round at a threshold. When the right sides are large, round at random.
- When the LP is too large to solve, use primal-dual, which also returns a lower bound.
- For connectivity requirements above 1, use iterative rounding; for one path per pair, primal-dual is faster.
- When cost and a budget such as load conflict, accept a bicriteria bound.
- For equality constraints, such as exactly $k$ sets, use dependent or swap rounding.
