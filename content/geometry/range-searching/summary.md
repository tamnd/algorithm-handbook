## What to remember

- **The shape of the range decides the cost.** Boxes are answered in polylogarithmic time, $O(\log^{d-1} n + k)$ with a layered range tree. Halfspaces and simplices need about $n^{1-1/d}$ time with linear space The semigroup lower bound $\Omega(n/\sqrt{m})$ for triangles with $m$ words shows that this is inherent.
- **Canonical subsets carry the trees.** A search on $x$ in a balanced tree splits the query interval into at most $2\lceil \log_2 n \rceil$ whole subtrees. A [range tree](/range-tree/) stores at each node its points sorted by $y$, so a box becomes $O(\log n)$ one-dimensional searches, in $O(n \log n)$ space.
- **Fractional cascading removes a logarithm.** The [layered range tree](/layered-range-tree/) does one binary search at the root and follows stored positions down, so a box in the plane costs $O(\log n + k)$ instead of $O(\log^2 n + k)$.
- **Counting reduces to dominance.** With subtraction, a box count is a signed sum of four dominance counts, $D(b_1, b_2) - D(a_1 - 1, b_2) - D(b_1, a_2 - 1) + D(a_1 - 1, a_2 - 1)$ on integer coordinates. Offline, one sweep with a [Fenwick tree](/fenwick-tree/) answers $q$ such queries in $O((n + q) \log(n + q))$ time.
- **Linear space is possible for boxes.** The [kd-tree](/kd-tree-range-search/) answers in $O(\sqrt{n} + k)$, tight on a $\sqrt{n} \times \sqrt{n}$ grid. The [priority search tree](/priority-search-tree/) answers three-sided queries $[a, b] \times (-\infty, c]$ in $O(\log n + k)$.
- **Decomposable problems become dynamic.** If the answer for $A \cup B$ is a fixed combination of the answers for $A$ and $B$, the logarithmic method keeps blocks of sizes $2^i$ and supports insertions, and a query asks each of the $O(\log n)$ blocks.
- **Bounded VC dimension makes samples work.** In a range space of VC dimension $d$, a random sample of $O((d/\varepsilon) \log(1/\varepsilon))$ points hits every range that holds an $\varepsilon$ fraction of the points. This gives $(1/r)$-cuttings, and from them the partition theorem with crossing number $O(r^{1-1/d})$.
- **Reporting is easier than counting for halfspaces.** Duality and [shallow cuttings](/shallow-cutting/) give $O(\log n + k)$ reporting in three dimensions with linear space, and through the lifting map the same for disks in the plane. Counting in three dimensions with linear space stays at $n^{2/3}$.

## The structures side by side

| Structure | Ranges | Space | Query |
|---|---|---|---|
| [Sorted array or balanced tree](/one-dimensional-range-search/) | intervals | $O(n)$ | $O(\log n + k)$ |
| [kd-tree](/kd-tree-range-search/) | boxes in $\mathbb{R}^d$ | $O(n)$ | $O(n^{1-1/d} + k)$ |
| [Range tree](/range-tree-query/) | boxes in $\mathbb{R}^d$ | $O(n \log^{d-1} n)$ | $O(\log^d n + k)$ |
| [Layered range tree](/layered-range-tree/) | boxes in $\mathbb{R}^d$ | $O(n \log^{d-1} n)$ | $O(\log^{d-1} n + k)$ |
| [Priority search tree](/priority-search-tree-query/) | three-sided, $d = 2$ | $O(n)$ | $O(\log n + k)$ |
| [Offline sweep](/offline-orthogonal-range-counting/) | box counting, $d = 2$ | $O(n + q)$ | $O((n + q) \log(n + q))$ for all $q$ |
| [Segment tree with interval trees](/orthogonal-point-enclosure/) | point enclosure, $d = 2$ | $O(n \log n)$ | $O(\log^2 n + k)$ |
| [Convex layers](/halfspace-range-searching/) | halfplane reporting | $O(n)$ | $O(\log n + k)$ |
| [Shallow cuttings](/shallow-cutting/), Afshani and Chan | halfspace reporting, $d = 3$ | $O(n)$ | $O(\log n + k)$ |
| [Partition tree](/partition-tree-query/), Chan | simplex counting | $O(n)$ | $O(n^{1-1/d})$ |
| [Hierarchical cuttings](/geometric-cutting/) | halfspace counting | $O(n^d)$ | $O(\log n)$ |

: Structures for range searching on $n$ points, with $k$ the number of points reported and $d$ fixed. Bounds are worst case on the real RAM. The offline sweep gives the total time for $q$ queries known in advance, and Chan's partition tree is built in $O(n \log n)$ expected time.

## Choosing a method

- In one dimension, use a sorted array for a static set and a balanced search tree for a changing one.
- For boxes in the plane with a static set and fast queries, use a range tree, layered if the logarithm matters. With little memory, use a kd-tree.
- For three-sided queries, or for intervals that contain a query point, use a priority search tree.
- For many counting queries known in advance, sweep with a Fenwick tree; it is the shortest code.
- For points that are inserted and deleted, use the logarithmic method on a static structure or a range tree with weight-balanced skeletons; for counting on a small grid, a [two-dimensional Fenwick tree](/two-dimensional-fenwick-tree/) is simpler.
- For halfplanes, triangles and disks, use a partition tree when space must be linear, cuttings when space is plentiful and queries must be logarithmic, and convex layers or shallow cuttings when only reporting is needed.
