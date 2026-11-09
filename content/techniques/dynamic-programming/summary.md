## What to remember

- **Two conditions.** Optimal substructure makes the optimum a recurrence over smaller instances; overlapping subproblems make storing their answers pay. The naive Fibonacci recursion makes $2F(n+1) - 1$ calls for $n + 1$ distinct subproblems; the plain rod-cutting recursion makes $2^n$.
- **Substructure can fail.** The longest simple path has no such recurrence, because the two halves of a path must not share vertices. A cost taken modulo 10 breaks it too.
- **Design is naming the subproblems.** Say in words what one entry means, then give the recurrence and the base cases. The time is the number of subproblems times the work per subproblem, which is the number of edges of the subproblem graph.
- **Top down or bottom up.** Memoization fills only the entries it reaches and needs no order; tabulation needs a safe order, and in return has no recursion and allows rolling arrays.
- **Store the choice.** Keep the minimizing or maximizing choice in a second table and follow it back to print a solution in time proportional to its size.
- **Every DP is a DAG.** Optimizing over the subproblems is a shortest or longest path in their graph, and counting the solutions is counting the paths, in $O(n + m)$ time for a DAG with $n$ vertices and $m$ edges.
- **Pick the state by the shape of the input.** A prefix for sequences, an interval when a solution splits into two contiguous parts, a vertex for trees, a subset for $n$ up to about 20, a position with a small summary for digits and grids.
- **Structure in the cost buys speed.** A cost with the quadrangle inequality makes the best split points monotone; Knuth's optimization, the divide and conquer optimization and SMAWK use this to save a factor of $n$ or $n / \log n$. A transition linear in the query point gives the convex hull trick.

## Costs side by side

| Problem or method | Subproblems | Time | Space |
|---|---|---|---|
| [Rod cutting](/rod-cutting-problem/) | $n + 1$ lengths | $\Theta(n^2)$ | $\Theta(n)$ |
| [Coin change](/coin-change-problem/), $k$ coins | $n + 1$ amounts | $O(nk)$ | $O(n)$ |
| [Unbounded knapsack](/unbounded-knapsack/) | $W + 1$ capacities | $O(nW)$ | $O(W)$ |
| [Grid paths](/grid-paths-with-obstacles/), $m \times n$ | $mn$ cells | $O(mn)$ | $O(n)$ with one row |
| [Text segmentation](/text-segmentation/) | $n + 1$ suffixes | $O(n^2)$ oracle calls | $O(n)$ |
| [Segmented least squares](/segmented-least-squares/) | $n + 1$ prefixes | $O(n^2)$ | $O(n)$ |
| [Printing neatly](/printing-neatly/) | $n + 1$ prefixes | $O(n \min(n, M))$ | $O(n)$ |
| [Matrix chain](/matrix-chain-multiplication/) | $\Theta(n^2)$ intervals | $\Theta(n^3)$ | $\Theta(n^2)$ |
| [Optimal BST](/optimal-binary-search-tree/) | $\Theta(n^2)$ intervals | $\Theta(n^3)$, $\Theta(n^2)$ by Knuth | $\Theta(n^2)$ |
| [Tree DP](/tree-dynamic-programming/) | $n$ subtrees | $O(n)$ times one merge | one table per vertex |
| [Bitmask DP](/bitmask-dp/), assignment | $2^n$ sets | $O(n 2^n)$ | $O(2^n)$ |
| [Held-Karp](/held-karp-algorithm/) | $(n-1) 2^{n-2}$ pairs | $\Theta(n^2 2^n)$ | $\Theta(n 2^n)$ |
| [Broken profile](/broken-profile-dp/), $n \times m$ | $2^m$ profiles per cell | $O(nm 2^m)$ | $O(2^m)$ |
| [Divide and conquer optimization](/divide-and-conquer-optimization/) | one layer of $n$ | $O(n \log n)$ per layer | |
| [SMAWK](/smawk-algorithm/), $n \times m$ | | $\Theta(n + m)$ | $O(n + m)$ |
| [Convex hull trick](/convex-hull-trick/), sorted case | $n$ lines | $O(n)$ | $O(n)$ |
| [Slope trick](/slope-trick/) | break points in a heap | $O(n \log n)$ | $O(n)$ |

: Here $n$ is the size of the input (items, words, points, vertices, cities, rows), $W$ the capacity and $M$ the line width. The rows from SMAWK down are the costs of one step of a larger program.

## Choosing a method

- Check the substructure with a cut-and-paste argument first. If the parts of a solution compete for a resource, add it to the state or look elsewhere.
- Use memoization when few states are reachable or the order is awkward, and tabulation when most states are needed or the recursion would be deep.
- A table indexed by a number $W$ of the input is pseudo-polynomial: fine for $W$ in the millions, useless for $W = 10^{18}$. Digit DP indexes by digits instead.
- For an interval program with a cost on the interval alone that satisfies the quadrangle inequality and is monotone, use Knuth's optimization. Matrix chain does not qualify, because its cost depends on the split.
- For a layered program with $k$ layers and a Monge cost, use the divide and conquer optimization, or SMAWK for linear time per layer; if the value is convex in $k$, the Aliens trick removes $k$ from the bound.
