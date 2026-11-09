## What to remember

- **The kind of update decides the difficulty.** With [insertions only](/incremental-graph/), components only merge, and union-find answers [connectivity](/incremental-connectivity/) in $\Theta(\alpha(n))$ amortized time. With [deletions](/decremental-graph/), a component can split, and the problem is to find a replacement edge or prove there is none.
- **Offline is easier than online.** When the whole sequence is [known in advance](/offline-dynamic-graph/), each edge lives on an interval of time. Placing the intervals on a segment tree and walking it with [rollback](/rollback-technique/) union-find answers all queries in $O(T \log T \log n)$ ([offline dynamic connectivity](/offline-dynamic-connectivity/)).
- **Dynamic trees are the building block.** [Link-cut trees](/link-cut-tree/) handle link, cut and path aggregates in $O(\log n)$ amortized time; [Euler tour trees](/euler-tour-tree/) handle link, cut, connectivity and subtree aggregates in $O(\log n)$ expected time. [Top trees](/top-tree/) do both kinds of aggregate in $O(\log n)$ worst case.
- **Fully dynamic connectivity is polylogarithmic.** [Holm, de Lichtenberg and Thorup](/holm-de-lichtenberg-thorup/) keep a spanning forest per level and raise the level of each edge they examine, which gives $O(\log^2 n)$ amortized per update. The [cell-probe lower bound](/dynamic-connectivity-lower-bound/) of $\Omega(\log n)$ holds even when the graph is a union of paths.
- **Minimum spanning forests change by one swap.** An insertion removes the heaviest edge on the cycle it closes; a deletion of a tree edge adds the lightest edge across the cut ([dynamic MST](/dynamic-minimum-spanning-tree/)). [Sparsification](/sparsification/) turns bounds in $m$ into bounds in $n$.
- **Directed reachability is much harder.** One deletion can change $\Theta(n^2)$ pairs of the [transitive closure](/dynamic-transitive-closure/). Under insertions, [Italiano's algorithm](/italiano-dynamic-transitive-closure/) adds each pair once, and the [topological order](/incremental-topological-ordering/) is repaired inside the window between the two ends of the new edge.
- **Decremental distances use the Even-Shiloach tree.** Levels only grow, so each vertex is rescanned at most $D$ times, for $O(mD)$ in total ([Even-Shiloach tree](/even-shiloach-tree/)). [Ramalingam-Reps](/ramalingam-reps/) repairs distances after any change in time that depends on the affected part only.
- **Hard problems are kept approximately.** A maximal matching gives a 2-approximate [vertex cover](/dynamic-vertex-cover/), [Gupta-Peng](/gupta-peng-dynamic-matching/) keeps a $(1 + \epsilon)$-approximate matching by lazy rebuilding, and colorings, cores and dense subgraphs are kept within constant or $(1 + \epsilon)$ factors.

## The algorithms side by side

| Algorithm | Problem | Updates | Time per update |
|---|---|---|---|
| [Union-find](/incremental-connectivity/) | connectivity | insertions | $\Theta(\alpha(n))$ amortized |
| [Offline dynamic connectivity](/offline-dynamic-connectivity/) | connectivity | both, offline | $O(\log T \log n)$ amortized |
| [Online bridge finding](/online-bridge-finding/) | bridges | insertions | $O(\log n)$ amortized |
| [Link-cut tree](/link-cut-tree/) | forest, path queries | link, cut | $O(\log n)$ amortized |
| [Euler tour tree](/euler-tour-tree/) | forest, subtree queries | link, cut | $O(\log n)$ expected |
| [Top tree](/top-tree/) | forest, both queries | link, cut | $O(\log n)$ worst case |
| [Holm-de Lichtenberg-Thorup](/holm-de-lichtenberg-thorup/) | connectivity | both | $O(\log^2 n)$ amortized |
| [Frederickson](/frederickson-topology-trees/) | minimum spanning forest | both | $O(\sqrt{m})$ worst case |
| [Eppstein-Galil-Italiano-Nissenzweig](/eppstein-galil-italiano-nissenzweig/) | minimum spanning forest | both | $O(\sqrt{n})$ worst case |
| [Italiano](/italiano-dynamic-transitive-closure/) | transitive closure | insertions | $O(n)$ amortized |
| [Incremental topological ordering](/incremental-topological-ordering/) | topological order | insertions | $O(K \log K)$ |
| [Even-Shiloach](/even-shiloach-tree/) | distances up to $D$ | deletions | $O(mD + n)$ in total |
| [Ramalingam-Reps](/ramalingam-reps/) | single-source distances | both | $O(A \log A)$ |
| [Demetrescu-Italiano](/demetrescu-italiano-apsp/) | all-pairs distances | both | $O(n^2 \log^3 n)$ amortized |
| [Gupta-Peng](/gupta-peng-dynamic-matching/) | $(1 + \epsilon)$-matching | both | $O(\sqrt{m}/\epsilon^2)$ worst case |

: Bounds from the entries. $T$ is the number of operations, $K$ and $A$ measure the affected part of the graph, and queries are $O(1)$ or $O(\log n)$ in most rows.

## Choosing an algorithm

- Insertions only: union-find for connectivity, parity union-find for bipartiteness, Italiano for reachability, and the window algorithm for topological order.
- The whole sequence known in advance: offline dynamic connectivity with rollback union-find, which is short to write and fast in practice.
- A forest under link and cut: link-cut trees for path queries, Euler tour trees for subtree and connectivity queries, top trees when both are needed.
- Fully dynamic connectivity or minimum spanning forest online: Holm-de Lichtenberg-Thorup; with few updates, recompute from scratch.
- Deletions only with bounded distances: the Even-Shiloach tree; single changes to a shortest path tree: Ramalingam-Reps.
