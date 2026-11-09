## What to remember

- **A spanning tree of a connected graph has $n - 1$ edges.** Adding any other edge closes exactly one cycle, its [fundamental cycle](/fundamental-cycle/), and removing any tree edge splits the tree into two parts. Forests are the independent sets of the [graphic matroid](/graphic-matroid/).
- **Cut property.** For any cut, a lightest edge crossing it belongs to some minimum spanning tree; when the lightest edge is unique, it belongs to every one.
- **Cycle property.** If an edge is strictly heaviest on some cycle, it belongs to no minimum spanning tree. With distinct weights the minimum spanning tree is unique.
- **A spanning tree $T$ is minimum exactly when** every non-tree edge is at least as heavy as each edge on the path in $T$ between its ends. This makes [verification](/mst-verification/) possible in $\Theta(m)$ time, and the best tree other than $T$ differs from it by one swap.
- **The classical algorithms** run in $O(m \log n)$ time: [Kruskal](/kruskal/) by sorting plus near-constant disjoint-set operations, [Prim](/prim/) with a binary heap, $O(m + n \log n)$ with a Fibonacci heap, and [Borůvka](/boruvka/) in at most $\lceil \lg n \rceil$ rounds of $O(m)$.
- **The faster bounds** are $O(m \, \alpha(m, n))$ deterministic ([Chazelle](/chazelle-mst/)) and $O(m)$ expected ([Karger, Klein and Tarjan](/karger-klein-tarjan-mst/)). Whether $O(m)$ is possible deterministically is open.
- **Directed graphs need a different method.** The [minimum arborescence](/minimum-arborescence/) is found by [Edmonds' algorithm](/edmonds-arborescence/) in $O(mn)$ time by contracting cycles of cheapest incoming arcs.
- **Spanning trees can be counted.** By the [matrix-tree theorem](/matrix-tree-theorem/), their number is any cofactor of the Laplacian, which takes $O(n^3)$ time; for $K_n$ it is $n^{n-2}$.

## The algorithms side by side

| Algorithm | Idea | Time | Extra space |
|---|---|---|---|
| [Kruskal](/kruskal/) | edges by weight, disjoint sets | $O(m \log m)$ | $O(n + m)$ |
| [Prim](/prim/), binary heap | grow one tree | $O((n + m) \log m)$ | $O(n + m)$ |
| [Borůvka](/boruvka/) | all components at once | $O((n + m) \log n)$ | $O(n + m)$ |
| [Reverse-delete](/reverse-delete/) | drop heaviest non-bridges | $O(m(n + m))$ | $O(n + m)$ |
| [Yao](/yao-mst/) | Borůvka with selection | $O(m \log \log n + n)$ | $O(n + m)$ |
| [Fredman-Tarjan](/fredman-tarjan-mst/) | Prim on Fibonacci heaps, in phases | $O(m \, \beta(m, n))$ | $O(n + m)$ |
| [Karger-Klein-Tarjan](/karger-klein-tarjan-mst/) | sampling and verification | $O(m)$ expected | $O(n + m)$ |
| [Chazelle](/chazelle-mst/) | soft heaps | $O(m \, \alpha(m, n))$ | $O(m)$ |
| [Edmonds](/edmonds-arborescence/), arborescence | contract cycles | $O(mn)$ | $O(mn)$ |
| [Counting](/counting-spanning-trees/) | Laplacian determinant | $O(n^3)$ | $O(n^2)$ |
| [Wilson](/wilson-algorithm/), uniform sample | loop-erased walks | $O(mn)$ expected | $O(n + m)$ |

: Bounds from the entries for a graph with $n$ vertices and $m$ edges; $\alpha$ is the inverse Ackermann function and $\beta(m, n) \le \log^\ast n$.

## Choosing an algorithm

- Edges in a list, or a sparse graph: Kruskal. The sort dominates, and if the edges come sorted the rest is almost linear.
- A dense graph given by a matrix, or one with $m$ near $n^2$: Prim with an array of keys in $O(n^2)$, which needs no heap at all.
- Parallel or external-memory settings, and planar graphs: Borůvka, whose rounds are independent and shrink the graph.
- One tree to check, or to update after a weight changes: the path-maximum test of verification, not a new run.
- Directed graphs with a root: Edmonds' algorithm. Greedy choices from the root can fail there.
- Connecting only some of the vertices: this is the Steiner tree problem, which is NP-hard; an MST of the terminal distances costs at most twice the optimum.
