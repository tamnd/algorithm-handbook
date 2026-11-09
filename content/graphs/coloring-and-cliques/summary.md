## What to remember

- **Cliques bound colorings from below.** A clique needs as many colors as it has vertices, and each color class is an independent set, so $\omega(G) \le \chi(G)$ and $n / \alpha(G) \le \chi(G)$. Neither bound is tight in general: [Mycielski graphs](/mycielski-graph/) have no triangle and need any number of colors.
- **Two colors are easy, three are hard.** A graph is 2-colorable exactly when it has no odd cycle, which [breadth-first search](/bipartiteness-testing/) checks in linear time. [$k$-coloring](/k-coloring/) is NP-complete for every $k \ge 3$, and so are the [clique](/clique-decision/) and independent set problems.
- **Greedy coloring is bounded by the order.** Any order gives at most $\Delta + 1$ colors; the [smallest-last order](/degeneracy-ordering/) gives at most the [degeneracy](/degeneracy/) plus one, which is 6 for planar graphs. Some order gives $\chi$ colors, but finding it is as hard as coloring.
- **Brooks and Vizing.** A connected graph that is neither complete nor an odd cycle needs at most $\Delta$ colors ([Brooks](/brooks-theorem/)). The edges of a simple graph need $\Delta$ or $\Delta + 1$ colors ([Vizing](/vizing-theorem/)), and the proof colors them in polynomial time.
- **Chordal graphs are easy.** A [perfect elimination ordering](/perfect-elimination-ordering/) is found in linear time, and greedy coloring in its reverse uses $\omega$ colors. Chordal graphs are [perfect](/perfect-graph/); for perfect graphs clique, independent set and coloring are all polynomial, through the [Lovász theta function](/lovasz-theta-function/).
- **Exact search.** [Bron-Kerbosch](/bron-kerbosch/) with pivoting lists all maximal cliques in $O(3^{n/3})$, the largest number there can be. The chromatic number takes $O(2.4423^n)$ by [Lawler's](/lawler-chromatic-number/) subset dynamic program and $O^*(2^n)$ by [inclusion-exclusion](/bjorklund-chromatic-number/).
- **Kempe swaps.** Swapping two colors on a connected two-colored piece keeps a coloring proper. This gives the [five color theorem](/five-color-theorem/) and Vizing's algorithm.
- **Counting.** The number of $k$-colorings is the [chromatic polynomial](/chromatic-polynomial/) $P(G, k)$, which satisfies $P(G) = P(G - e) - P(G / e)$. Computing it is #P-hard.

## The algorithms side by side

| Algorithm | Problem | Time | Guarantee |
|---|---|---|---|
| [Greedy](/greedy-coloring/) | coloring | $\Theta(n + m)$ | at most $\Delta + 1$ colors |
| [Smallest-last](/degeneracy-ordering/) | coloring | $\Theta(n + m)$ | at most $d + 1$ colors |
| [Welsh-Powell](/welsh-powell-algorithm/) | coloring | $O(n \log n + nk + m)$ | at most $\max_i \min(d_i + 1, i)$ |
| [DSATUR](/dsatur/) | coloring | $\Theta(n^2)$ | exact on bipartite graphs |
| [RLF](/recursive-largest-first/) | coloring | $O(n^2 + km)$ | heuristic |
| [Chordal coloring](/chordal-graph-coloring/) | coloring chordal graphs | $\Theta(n + m)$ | optimal |
| [Vizing's algorithm](/vizing-algorithm/) | edge coloring | $O(m(n + \Delta^2))$ | at most $\Delta + 1$ colors |
| [Bron-Kerbosch](/bron-kerbosch/) | all maximal cliques | $O(3^{n/3})$, $O(d n 3^{d/3})$ | exact |
| [Tomita](/tomita-maximum-clique/) | maximum clique | $O(2^n n^2)$ | exact |
| [Lawler](/lawler-chromatic-number/) | chromatic number | $O(2.4423^n)$ | exact |
| [Björklund](/bjorklund-chromatic-number/) | chromatic number | $O(2^n n^2)$ | exact |

: Worst-case bounds from the entries. Here $d$ is the degeneracy, $k$ the number of colors used, and $d_i$ the degrees in non-increasing order.

## Choosing an algorithm

- A quick coloring with a guarantee: smallest-last order, which is linear and never worse than the degeneracy plus one. DSATUR is slower and usually uses fewer colors; RLF is slower again and often better still.
- A known class: chordal and interval graphs by elimination orders, bipartite graphs by breadth-first search, planar graphs with at most 5 colors by Kempe swaps.
- All maximal cliques of a sparse graph: Bron-Kerbosch with pivoting, the outer loop in degeneracy order.
- A maximum clique on graphs of a few hundred vertices: branch and bound with coloring bounds, as in Tomita's algorithms.
- The exact chromatic number of a small graph: inclusion-exclusion when $2^n$ fits in memory, otherwise branch and bound with DSATUR order.
- Edges at a vertex must differ: Vizing's algorithm, or exactly $\Delta$ colors by matchings when the graph is bipartite.
