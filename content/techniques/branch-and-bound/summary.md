## What to remember

- **Four parts make the method**: a branching rule, a bounding function, an incumbent $z$ and a node selection rule. For a maximization problem it is correct when each bound is at least every value below its node, the children cover all solutions of their parent, and a node is dropped only if it is infeasible, its bound is at most $z$, or its relaxation is solved by a feasible solution.
- **Good bounds come from relaxations.** Drop a hard constraint and solve what is left: the fractional knapsack, the reduced cost matrix, the linear program. A tighter bound expands fewer nodes but costs more per node. A value that is not a true bound, such as a greedy completion, can prune the optimum away.
- **The order of the live nodes sets the memory.** Depth-first order keeps at most $d(b-1)+1$ nodes on its stack. Every order must expand the nodes whose bound and whose ancestors' bounds exceed the optimum $z^*$; best-first order expands no node with bound below $z^*$, but its queue can hold a large part of the tree. Breadth-first order holds a whole level.
- **A good incumbent early saves work.** Starting depth-first branch and bound on the knapsack example with the greedy value 80 instead of 0 cuts the expanded nodes from 6 to 5.
- **The worst case stays exponential.** With $v_i = w_i = 2$, $n$ even and $W = n + 1$, knapsack branch and bound pops $\binom{n+1}{n/2} - 1$ nodes, 352715 for $n = 20$. LP-based branch and bound needs exponentially many linear programs to show that $2x_1 + \cdots + 2x_n = n$ has no 0-1 solution when $n$ is odd.
- **Dominance prunes without a bound.** A partial solution that another one beats for every completion can go. For the knapsack this keeps at most $W + 1$ pairs of weight and value per level, which is the $O(nW)$ dynamic program. Branch and reduce simplifies before each branch; for maximum independent set it gets $L(n) \le L(n-1) + L(n-4)$ leaves, so $O(1.3803^n)$.
- **The method works on real boxes too.** Interval arithmetic bounds a function on a box from below, so interval branch and bound returns an interval that contains the global minimum. A formula in which a variable appears more than once gives a looser bound and more boxes.

## The methods side by side

| Method | Bound | Time | Extra space |
|---|---|---|---|
| [Depth-first branch and bound](/depth-first-branch-and-bound/) | any | $O(T)$ worst, $O(db)$ best | $O(db)$ |
| [Best-first branch and bound](/best-first-branch-and-bound/) | any | $O(T \log T)$ worst | $O(T)$ |
| [Breadth-first branch and bound](/breadth-first-branch-and-bound/) | any | $O(T)$ worst | $O(w)$ |
| [Knapsack branch and bound](/knapsack-branch-and-bound/) | fractional knapsack | $O(n 2^n)$ worst, $O(n^2)$ best | $O(n^2)$ |
| [Little's algorithm](/little-algorithm/) | reduced cost matrix | $O(N(n^3 + \log N))$ | $O(N n^2)$ |
| [Land-Doig algorithm](/land-doig-algorithm/) | linear program | $O(N(L + \log N))$ | $O(N)$ |
| [Balas additive algorithm](/balas-additive-algorithm/) | partial sums | $O(2^n m n)$ worst | $O(n(n+m))$ |
| [Branch and reduce](/branch-and-reduce/), independent set | reduction rules | $O(1.3803^n n^4)$ | $O(n^3)$ |
| [Interval branch and bound](/interval-branch-and-bound/) | interval extension | $O(N(C + d + \log N))$ | $O(Nd)$ |

: $T$ is the number of nodes of the search tree, $d$ its depth, $b$ the largest number of children, $w$ the largest number of nodes at one depth, $N$ the number of nodes or boxes the search makes, $L$ the time for one linear program, $C$ the time for one interval evaluation in dimension $d$, and $m$ the number of constraints. The [Gilmore-Lawler bound](/gilmore-lawler-bound/) for the quadratic assignment problem takes $O(n^3)$ time per node.

## Choosing a method

- Start with depth-first branch and bound. It needs little memory and can be stopped at any time with the best solution so far and a gap.
- Use best-first order when the bound is strong and the live nodes fit in memory. Integer programming solvers mix the two: they dive depth-first, then jump to the best bound.
- Spend most of your effort on the bound, and test on small instances that it is a true bound.
- When the states are few, as with a small knapsack capacity, use dominance, which is dynamic programming.
- For an integer linear program, bound with the linear program and branch on a fractional variable.
- For a guaranteed global minimum on a box, use interval branch and bound, with each variable written as few times as possible.
