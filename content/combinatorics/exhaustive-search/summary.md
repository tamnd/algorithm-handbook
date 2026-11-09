## What to remember

- **The space sets the cost.** Brute force over a [search space](/search-space/) $S$ with a test of cost $t$ takes $\Theta(|S| \cdot t)$ time. For eight queens, $\binom{64}{8} \approx 4.4 \times 10^9$ placements shrink to $8! = 40\,320$ permutations and to 2,057 nodes of a backtracking tree.
- **Explosion.** With $2^n$ candidates, a machine $s$ times faster solves instances only $\lg s$ larger; with $n^b$ steps, $s^{1/b}$ times larger.
- **Exact cover** asks for options that hold every primary item exactly once and every secondary item at most once. [Algorithm X](/algorithm-x/) branches on the item with the fewest remaining options, and [dancing links](/dancing-links/) undo each deletion in $O(1)$ time.
- **Enumeration costs** are measured by total time, incremental time and delay. Polynomial delay implies incremental polynomial time, which implies polynomial total time. If deciding whether a solution exists is NP-complete, no listing runs in polynomial total time unless $\mathrm{P} = \mathrm{NP}$.
- **Reverse search** walks a tree of parent links with space independent of the number of objects. Printing at even depth on the way down and at odd depth on the way up bounds the delay.
- **Counting shapes.** Fixed polyominoes grow like $\lambda^n$ with $\lambda \approx 4.0626$, and $a(m)\,a(n) \le a(m + n)$. Self-avoiding walks on the square lattice grow like $\mu^n$ with $\mu \approx 2.638$, and $c_{m+n} \le c_m c_n$.
- **Maximal independent sets.** A graph on $n$ vertices has at most $3^{n/3}$ of them (Moon and Moser), and disjoint triangles reach the bound. The [Tsukiyama algorithm](/tsukiyama-algorithm/) lists them with delay $O(n(n + m))$.
- **Minimal transversals** form the dual of a hypergraph, and $\mathrm{Tr}(\mathrm{Tr}(H)) = H$ for a simple hypergraph. No algorithm of polynomial total time is known; the [Fredman-Khachiyan algorithm](/fredman-khachiyan-algorithm/) lists them in incremental quasi-polynomial time.
- **Beating brute force.** A branching rule with recurrence $T(n) \le \sum_i T(n - t_i)$ costs $O^*(\lambda^n)$, where $\sum_i \lambda^{-t_i} = 1$. The [Held-Karp algorithm](/held-karp-algorithm/) replaces $(n-1)!/2$ tours by $O(n^2 2^n)$ steps.

## The methods side by side

| Method | Task | Time | Extra space |
|---|---|---|---|
| [Brute-force search](/brute-force-search/) | best or any candidate of $S$ | $\Theta(\lvert S \rvert \cdot t)$ | one candidate |
| Bitwise backtracking for [n queens](/n-queens-problem/) | count all solutions | $O(1)$ word operations per child | $O(n)$ words |
| [Algorithm X](/algorithm-x/) with [dancing links](/dancing-links/) | all exact covers | $O(T(n + s))$ for $T$ nodes | $O(n + s)$ |
| Dynamic programming for [exact cover](/exact-cover/) | count exact covers | $O(2^n m)$ | $O(2^n)$ |
| [Reverse search](/reverse-search/) | all objects of an implicit graph | $O(N\delta(t_A + t_f))$; delay $O(\delta(t_A + t_f))$ | two objects and an index |
| [Redelmeier's algorithm](/redelmeier-algorithm/) | fixed polyominoes up to $n$ cells | $O(nA)$ | $O(n^2)$, or $O(n)$ with a shared stack |
| [Tsukiyama algorithm](/tsukiyama-algorithm/) | maximal independent sets | delay $O(n(n + m))$; total $O(n(n + m)k)$ | $O(n^2)$, or $O(n + m)$ in the original |
| [Fredman-Khachiyan algorithm](/fredman-khachiyan-algorithm/) | duality test of monotone DNFs | $n^{O(1)} m^{O(\log^2 m)}$ | $O(n^2 m)$ |
| [Held-Karp algorithm](/held-karp-algorithm/) | shortest tour | $O(n^2 2^n)$ | exponential |

: The main methods of the chapter. For exact cover, $n$ items, $m$ options of total size $s$. For reverse search, $N$ objects, degree at most $\delta$, and oracle and local-search costs $t_A$ and $t_f$. $A$ counts the fixed polyominoes with at most $n$ cells, and $k$ the maximal independent sets. For Fredman-Khachiyan, $m$ terms over $n$ variables.

## Choosing a method

- When the space has up to about $10^9$ candidates and the test is cheap, write the brute-force loop first. It is the reference for checking every faster program.
- When a partial candidate can already fail, use [backtracking](/generic-backtracking-algorithm/), and build the easy constraints, such as one queen per row and column, into the space.
- When the problem is to place pieces, fill a grid or match items so that each item is used exactly once, write it as an exact cover and run Algorithm X. Secondary items take care of "at most once" constraints.
- When every solution is wanted, ask for a bound on the delay. Use reverse search if each object has a parent given by a local rule, and a flashlight search if "does this partial solution extend?" has a fast answer.
- When the aim is a count of shapes such as polyominoes or walks, generate each shape once by a canonical rule, such as Redelmeier's ordered untried set, rather than storing shapes and removing repeats. For large sizes, the [transfer-matrix method](/transfer-matrix-method/) counts without listing.
- When no listing is feasible and the problem is NP-hard, look for a smaller base of the exponent: careful branching, dynamic programming over subsets, inclusion-exclusion, or meet in the middle with the [Horowitz-Sahni algorithm](/horowitz-sahni-algorithm/).
