## What to remember

- **The cost of a transform.** Transform, solve, map back. The total is the sum of the three costs, with the solver run on the new instance, which can be larger than the input.
- **Direction.** If $A$ reduces to $B$, an algorithm for $B$ gives one for $A$, and a lower bound for $A$ gives one for $B$. Nothing passes the other way. Two problems that reduce to each other in polynomial time are equivalent.
- **Many-one and Turing.** A many-one reduction makes one call and returns its answer. A Turing reduction may make many calls, as a search-to-decision reduction does.
- **Sort first.** After a sort, equal items are neighbours and near items are adjacent, so one scan finds duplicates, the mode or the intervals to merge. Coordinate compression replaces values by their ranks, which keeps every comparison and nothing else.
- **Normal and canonical.** A normal form fixes the shape of a representation; a canonical form also gives each meaning exactly one representation. Only a canonical form turns equivalence into equality. A normal form can be exponentially larger than the input.
- **Linear programs.** Shortest paths, flows and bipartite matching have integral optima; vertex cover can have a fractional one, which is only a bound.
- **Scaling.** Solve with the top bits, then add one bit per phase. A gap lemma bounds the repair in each phase by a quantity free of $C$, so $C$ appears only in the number of phases, $\lfloor \lg C \rfloor + 1$.
- **New graphs.** Splitting a vertex moves its capacity onto an edge. Two copies with switching edges record the parity of a walk, so a distance in the double cover is a shortest odd or even walk.

## Transforms and their costs

| transform | size of the new instance | cost |
|---|---|---|
| [Presorting](/presorting/) for distinctness | the same $n$ items, sorted | $n = 10^6$: 19,951,424 comparisons against 499,999,500,000 for all pairs |
| [Coordinate compression](/coordinate-compression/) | $n$ ranks in $0, \ldots, m - 1$ | $O(n \log n)$ time, $O(n)$ space |
| Bipartite matching to max flow | $\lvert L \rvert + \lvert R \rvert + 2$ vertices, $\lvert E \rvert + \lvert L \rvert + \lvert R \rvert$ arcs | $O(VE)$ by Ford-Fulkerson; [Hopcroft-Karp](/hopcroft-karp/) is $O(E\sqrt{V})$ |
| 2-SAT to strongly connected components | $2n$ vertices, $2m$ arcs | $O(n + m)$ |
| LIS to LCS | two sequences of length at most $n$ | $O(n^2)$, against $O(n \log n)$ by [patience sorting](/patience-sorting/) |
| Tseitin encoding of $f_n$ | $3n + 1$ clauses, $3n$ variables | against $2^n$ clauses for any equivalent CNF |
| AHU code of a rooted tree | one string or one integer label per node | $O(n^2)$ with strings, $O(n)$ with integer labels |
| [Capacity scaling](/capacity-scaling/) | the same network, threshold $\Delta$ | at most $2m(\lfloor \lg C \rfloor + 1)$ augmentations, $O(m^2 \log C)$ |
| [Gabow's bit scaling](/gabow-scaling-sssp/) | the same graph, lengths $w_k$ | $O((n + m) \log W)$, against $O(m + nW)$ for [Dial's algorithm](/dial-algorithm/) |
| Linear program by Karmarkar's method | $n$ variables, bit length $L$ | $O(n^{3.5} L)$ arithmetic operations |
| [Vertex splitting](/vertex-splitting/) | $2n - 2$ vertices, $m + n - 2$ edges | the bound of the flow algorithm, up to a constant factor |
| [Bipartite double cover](/bipartite-double-cover/) | $2n$ vertices, $2m$ edges | BFS in $O(n + m)$; shortest odd cycle in $O(n(n + m))$ |

: For the reductions, $n$ and $m$ are the sizes of the input: variables and clauses for 2-SAT, vertices and edges for the graphs. $C$ is the largest capacity and $W$ the largest length.

## Choosing a method

- If the question is about equal values or neighbours in value order, sort first. If an array indexed by large values is needed, compress them.
- If the problem looks like one with a known algorithm, reduce to it, and check that the answer maps back and that the new instance is not much larger.
- If you want to show a problem is hard, reduce a known hard problem to it, not the other way round.
- If you must test many objects for equivalence, find a canonical form and hash it. If it is costly, as for graphs, compare cheap invariants first.
- If the problem has linear limits and a linear goal, write a linear program, and check whether its optimum must be whole.
- If an algorithm takes a number of steps that grows with the values, try scaling.
- If a flow problem limits vertices, split them. If it asks about odd or even walks, search the double cover.
