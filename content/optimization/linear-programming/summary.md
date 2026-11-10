## What to remember

- Every linear program is **infeasible**, **unbounded**, or has an **optimum**, and in the last case the optimum is attained; there is no fourth case. For $\min c^\top x$ subject to $Ax = b$, $x \ge 0$ with $A$ of rank $m$, some optimal solution is a [basic feasible solution](/basic-feasible-solution/): $x_B = A_B^{-1} b \ge 0$ for $m$ independent columns $B$, and $x_j = 0$ elsewhere. There are at most $\binom{n}{m}$ of them.
- The **dual** of $\max c^\top x$, $Ax \le b$, $x \ge 0$ is $\min b^\top y$, $A^\top y \ge c$, $y \ge 0$. [Weak duality](/weak-duality/) gives $c^\top x \le b^\top y$ for every feasible pair, in two lines. [Strong duality](/strong-duality/) says the optima are equal when either exists, so every optimum has a short certificate.
- [Farkas' lemma](/farkas-lemma/): a system $Mz \le q$ has no solution exactly when some $u \ge 0$ has $u^\top M = 0$ and $u^\top q < 0$. It is the engine of strong duality, and [Fourier-Motzkin elimination](/fourier-motzkin-elimination/) proves it.
- A feasible pair is optimal exactly when [complementary slackness](/complementary-slackness/) holds: each constraint is tight or its dual variable is zero, and each variable is zero or its dual constraint is tight. The optimal dual variables are [shadow prices](/shadow-price/).
- The **simplex method** moves between adjacent bases. The [reduced costs](/reduced-cost/) $r_j = c_j - y^\top A_j$ with $y = A_B^{-\top} c_B$ choose the entering variable; the [ratio test](/ratio-test/) chooses the leaving one. All $r_j \ge 0$ proves optimality, and an entering column with no positive entry proves unboundedness. A pivot costs $O(mn)$ on a full tableau.
- At a [degenerate](/lp-degeneracy/) vertex a pivot can have length zero, and a rule can cycle. [Bland's rule](/bland-rule/) never cycles. On the [Klee-Minty cube](/klee-minty-cube/), [Dantzig's rule](/dantzig-pivot-rule/) takes $2^n - 1$ pivots, and no pivot rule is known to be polynomial.
- Linear programming with rational data is **in P**. The [ellipsoid method](/ellipsoid-method/) needs $O(n^2 L)$ iterations and only a [separation oracle](/separation-oracle/); [Karmarkar's algorithm](/karmarkar-algorithm/) needs $O(nL)$ iterations and $O(n^{3.5} L)$ operations. No strongly polynomial algorithm is known.
- In **fixed dimension** $n$, linear programming takes $O(m)$ time: expected $O(n!\, m)$ with [Seidel's algorithm](/seidel-linear-programming/), and worst case $O(2^{2^n} m)$ with [Megiddo's algorithm](/megiddo-fixed-dimension-lp/).

## The main methods side by side

| Method | Iterations | Cost per iteration | Total, worst case | Output |
|---|---|---|---|---|
| [Simplex method](/simplex-method/), tableau | $2^n - 1$ on Klee-Minty (Dantzig's rule) | $O(mn)$ | $O(2^n mn)$ | exact vertex and dual |
| [Revised simplex](/revised-simplex-method/) | as simplex | far less than the tableau when sparse | $O(2^n mn)$ | exact vertex and dual |
| [Dual simplex](/dual-simplex-method/) | as simplex | $O(mn)$ | $O(2^n mn)$ | exact vertex and dual |
| [Ellipsoid method](/ellipsoid-method/) | $O(n^2 L)$ | $O(n^2 + mn)$ | $O(n^3 (m + n) L)$ | feasible point |
| [Karmarkar's algorithm](/karmarkar-algorithm/) | $O(nL)$ | $O(n^{2.5})$ on average | $O(n^{3.5} L)$ | interior point, then rounding |
| [Affine scaling](/affine-scaling-method/) | no polynomial bound known | $O(m^2 n)$ | — | interior point |
| [Fourier-Motzkin elimination](/fourier-motzkin-elimination/) | $n$ eliminations | up to $4(m/4)^{2^n}$ rows | $O(n (m + n) m^{2^n})$ | feasibility, certificate |
| [Seidel's algorithm](/seidel-linear-programming/), fixed $n$ | — | — | $O(n!\, m)$ expected | exact optimum |
| [Megiddo's algorithm](/megiddo-fixed-dimension-lp/), fixed $n$ | — | — | $O(2^{2^n} m)$ | exact optimum |

: Methods for linear programming with $n$ variables, $m$ constraints and input bit length $L$, counted in arithmetic operations. The simplex bound $O(2^n mn)$ counts at most $\binom{n}{m} \le 2^n$ bases. In practice the simplex method takes between $m$ and a small multiple of $m$ pivots.

## Choosing a method

- For a program you need solved, use a solver. It runs the revised or dual simplex method, or an [interior-point method](/interior-point-method/), with care for sparsity and rounding that a short program does not have.
- When you need an exact vertex, a dual solution or a warm start after a small change, use the simplex method. After a constraint is added, as in branch and bound or cutting planes, use the dual simplex method from the old basis.
- For very large sparse programs, interior-point methods are the other main choice, and they come with a polynomial bound.
- When the program has exponentially many constraints but a violated one can be found fast, the ellipsoid method proves that it is solvable in polynomial time. When it has exponentially many columns, use [column generation](/column-generation/).
- In two or three variables, as in geometry, use Seidel's algorithm.
- To learn the method, or to check a solver on tiny inputs, run the tableau simplex method with exact fractions and [Bland's rule](/bland-rule/), or enumerate all bases.
