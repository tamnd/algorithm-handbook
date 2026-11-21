## What to remember

- A **TU game** gives a worth $v(S)$ to every coalition. The **core** is the set of $x$ with $x(N) = v(N)$ and $x(S) \ge v(S)$ for every $S$. It can be empty. By the [Bondareva-Shapley theorem](/bondareva-shapley-theorem/) it is nonempty exactly when $\sum_S \lambda_S v(S) \le v(N)$ for every balanced family of weights, which is [LP duality](/lp-duality/) applied to the problem of minimizing $x(N)$ over the core constraints.
- The **least core** minimizes the largest excess $v(S) - x(S)$ by one LP with $n + 1$ variables and $2^n - 2$ constraints. The **nucleolus** minimizes the sorted vector of excesses lexicographically; it is unique, lies in the core when the core is nonempty, and takes at most $n - 1$ rounds of LPs.
- The **Shapley value** is $\varphi_i = \sum_{S \subseteq N \setminus \{i\}} \frac{|S|!\,(n - |S| - 1)!}{n!} \big(v(S \cup \{i\}) - v(S)\big)$, the average marginal contribution over the $n!$ orders. It is the only value that is efficient, symmetric, additive and gives null players 0. It need not be in the core.
- In a **convex game**, $v(S) + v(T) \le v(S \cup T) + v(S \cap T)$, every marginal vector is a corner of the core, the core is the convex hull of the marginal vectors, and the Shapley value is in the core (Shapley 1971).
- **Voting power is not weight.** The Shapley-Shubik and Banzhaf indices count pivots and swings. A dynamic program over the weights computes them in time polynomial in $n$ and the quota $q$; with weights in binary, computing either index is #P-complete and deciding whether it is positive is NP-complete.
- **Sampling** estimates every Shapley value within an additive $\varepsilon$ with probability at least $1 - \delta$ from $m = \lceil r^2 \ln(2n/\delta) / (2\varepsilon^2) \rceil$ random orders, where $r$ bounds the range of a marginal contribution. For weighted voting games no polynomial algorithm approximates an index within any multiplicative factor unless P = NP (NP = RP for randomized algorithms).
- For **claims problems**, the Talmud rule is the nucleolus of the bankruptcy game and the random arrival rule is its Shapley value. Both give award vectors, which are exactly the core of that game.
- A **cross-monotonic**, budget balanced cost-sharing method gives a [Moulin mechanism](/moulin-mechanism/) that is group strategyproof and budget balanced, but it need not be efficient. By the [Green-Laffont theorem](/green-laffont-theorem/), no strategyproof mechanism is both efficient and budget balanced in general.

## Solution concepts and algorithms side by side

| Object | Exists | Computed from | Time |
|---|---|---|---|
| Core point | not always | table of $v$ | one LP, polynomial in $2^n$ |
| Least core | always | table of $v$ | one LP |
| Nucleolus | if imputations exist | table of $v$ | at most $(n-1)(2^n-1)$ LPs |
| Shapley value | always | table of $v$ | $O(n\,2^n)$ terms |
| Shapley value, estimate | always | oracle for $v$ | $O(mn)$ oracle calls for $m$ orders |
| Shapley value of an MC-net | always | $z$ literals | $O(z + n)$ |
| Power indices | always | weights, quota $q$ | $O(n^3 q)$ all Shapley-Shubik, $O(n^2 q)$ all Banzhaf |
| Bird's rule | always, in the core | spanning tree costs | $O(n^2)$ |
| Talmud rule | always | claims, estate | $O(n \log n)$ |
| Optimal coalition structure | always | table of $v$ | $O(3^n)$ |

: Solution concepts of the chapter. "Table of $v$" means all $2^n$ values are given; the times for LPs assume a polynomial LP method. The index times are pseudo-polynomial, since $q$ can be exponential in the input length.

## Choosing a method

If the game is given as a full table and $n$ is small, solve the LPs directly: one LP tests the core and finds the least core, and the [sequential LP](/nucleolus-sequential-lp/) gives the nucleolus. If the game is convex, no LP is needed: any marginal vector is a core point, found greedily. If the game comes from an optimization problem, use its structure: the dual of the [assignment problem](/assignment-problem/) for the assignment game, [Bird's rule](/bird-rule/) for spanning tree games, the closed form for the [airport game](/airport-game/) and the [Talmud rule](/talmud-rule/) for bankruptcy games.

For the Shapley value, use the formula on small tables, the [dynamic program](/power-index-dynamic-programming/) for weighted voting games with moderate weights, [marginal contribution nets](/marginal-contribution-nets/) when the worth comes from small interactions, and [sampling](/shapley-value-sampling/) when $v$ is only an oracle and an additive error is enough.

When the players hold private values, choose a [cross-monotonic](/cross-monotonicity/) method and run the Moulin mechanism. If no such method covers the cost exactly, as for Steiner trees, accept approximate budget balance, as [Jain-Vazirani cost sharing](/jain-vazirani-steiner-cost-sharing/) does with a factor of 2.
