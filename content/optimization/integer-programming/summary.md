## What to remember

- An integer program becomes a linear program when integrality is dropped. For a maximization, the [LP relaxation](/lp-relaxation/) gives $z_{IP} \le z_{LP}$, and every method of the chapter uses this bound. Two formulations of one problem can have very different relaxations.
- The [integrality gap](/integrality-gap/) is the worst ratio between the integer optimum and the relaxation. It is exactly 2 for the natural relaxation of [vertex cover](/vertex-cover/) and $\Theta(\log n)$ for [set cover](/set-cover/).
- In a [big-M constraint](/big-m-formulation/) $a^T x \le \beta + M(1 - z)$, the smallest valid constant is $M^* = \max_{x \in D} a^T x - \beta$ over the domain $D$ of $x$. A larger $M$ weakens the relaxation and hurts numerical safety.
- A matrix is [totally unimodular](/total-unimodularity/) when every square submatrix has determinant $0$ or $\pm 1$. By the [Hoffman-Kruskal theorem](/hoffman-kruskal-theorem/), $A$ is TU if and only if $\{x : Ax \le b,\ x \ge 0\}$ is integral for every integral $b$. Network matrices, interval matrices and incidence matrices of bipartite graphs are TU.
- A [Chvátal-Gomory cut](/chvatal-gomory-cut/) comes from $u \ge 0$ with $u^T A$ integral: $u^T A x \le \lfloor u^T b \rfloor$. Repeating the [closure](/chvatal-closure/) reaches the integer hull of a rational polyhedron after finitely many rounds, but the number of rounds can be large: at least $2t$ for the triangle $\operatorname{conv}\{(0,0), (0,1), (t, \tfrac12)\}$.
- [Gomory's algorithm](/gomory-cutting-plane-algorithm/) reads cuts off the simplex tableau and is finite with a lexicographic rule. The [Gomory mixed-integer cut](/gomory-mixed-integer-cut/) gives an integer variable with fractional part $f_j$ the coefficient $\min\{f_j / f_0,\ (1 - f_j)/(1 - f_0)\}$; it dominates the fractional cut and equals the MIR and split cut of the same row.
- Solvers run [branch and cut](/branch-and-cut/): LP-based branch and bound with cuts, presolve and heuristics. The relative gap $(\text{incumbent} - \text{bound}) / |\text{incumbent}|$ measures progress, and the search stops below a tolerance such as $10^{-4}$.
- Integer programming is NP-hard, but it is polynomial in fixed dimension: [Lenstra](/lenstra-algorithm/) in $2^{O(n^3)} s^{O(1)}$ time, [Kannan](/kannan-algorithm/) in $n^{O(n)} s^{O(1)}$. With a fixed number of constraints it is [pseudo-polynomial](/papadimitriou-pseudopolynomial-theorem/).

## The main methods side by side

| Method | What it gives | Time | Notes |
|---|---|---|---|
| [LP relaxation](/lp-relaxation/) | a bound; the optimum if the formulation is ideal | polynomial | exact when $A$ is TU and $b$ is integral |
| Enumeration of a [0-1 program](/binary-integer-programming/) | the optimum | $O(2^n mn)$ | a reference for tests |
| [Gomory's algorithm](/gomory-cutting-plane-algorithm/) | the optimum of a pure integer program | finite, no polynomial bound on rounds | at least $2t$ rounds on the thin triangle |
| [Branch and cut](/branch-and-cut/) | the optimum, or a gap | exponential in the worst case | the method of all general solvers |
| [Benders decomposition](/benders-decomposition/) | the optimum | $O(K(M + T))$ | $K$ iterations of a master solve and an LP solve |
| [Feasibility pump](/feasibility-pump/) | a feasible point, maybe | $O(N(L + n \log n))$ | a heuristic with an iteration limit $N$ |
| [Lenstra's algorithm](/lenstra-algorithm/) | the optimum | $2^{O(n^3)} s^{O(1)}$ | polynomial for fixed $n$ |
| [Kannan's algorithm](/kannan-algorithm/) | the optimum | $n^{O(n)} s^{O(1)}$ | space $s^{O(1)}$ |
| [Papadimitriou's dynamic program](/papadimitriou-pseudopolynomial-theorem/) | the optimum of $\max\{c^T x : Ax = b,\ x \in \mathbb{Z}^n_+\}$ | $O(n (4md + 1)^{2m} (md + 1)^2)$ | entries of $A$ and $b$ at most $d$ in absolute value |

: Methods for integer programs. Here $n$ is the number of variables, $m$ the number of constraints, $s$ the input size in bits, and $L$ the time of one LP solve. The dynamic program's bound comes from the proof in the entry; the [proximity theorem](/eisenbrand-weismantel-proximity-theorem/) gives $(m\Delta)^{O(m)} \|b\|_\infty^2$, where $\Delta$ bounds only the entries of $A$.

## Choosing a method

For a real model, use a branch-and-cut solver and spend your effort on the formulation.

- Check first whether the constraint matrix is totally unimodular, as for flows, assignment and interval scheduling. Then the LP relaxation has an integral optimal vertex and no branching is needed.
- Use the smallest valid $M$, or [indicator constraints](/indicator-constraint/) when no good bound is known.
- When a few integer variables control many continuous ones, as in network design and two-stage models, try [Benders decomposition](/benders-decomposition/). When the model has a huge number of columns, as in cutting stock or crew pairing, use [branch and price](/branch-and-price/).
- When the solver finds no feasible point, try the [feasibility pump](/feasibility-pump/). When it has a good incumbent but the gap closes slowly, [RINS](/relaxation-induced-neighborhood-search/) and [local branching](/local-branching/) look for better solutions near it.
- When there are few constraints and small coefficients, as in knapsack problems, a dynamic program is often faster than any LP-based method.
