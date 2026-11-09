## What to remember

- **Distances are well defined exactly when no negative cycle is reachable from the source.** Then every vertex that can be reached has a shortest path that is simple, with at most $n - 1$ edges, and all of them fit in one [shortest-path tree](/shortest-path-tree/).
- **Relaxation is safe.** Lowering $d(v)$ to $d(u) + w(u, v)$ never takes an estimate below the true distance $\delta(s, v)$, and the estimates equal the distances exactly when $d(v) \le d(u) + w(u, v)$ holds on every edge.
- **[Bellman-Ford](/bellman-ford/)** relaxes all $m$ edges in $n - 1$ rounds, in $O(nm)$ time, for any weights. If a further round still lowers an estimate, a negative cycle is reachable from $s$.
- **On a DAG**, relaxing the out-edges of each vertex in topological order gives all distances in $\Theta(n + m)$ time, with negative weights allowed. Negating the weights gives longest paths.
- **[Dijkstra's algorithm](/dijkstra/)** needs $w \ge 0$. The unfinished vertex with the least estimate has its final distance, so each vertex is finished once: $O((n + m) \log n)$ time with a binary heap, $O(m + n \log n)$ with a Fibonacci heap, $\Theta(n + m)$ for weights 0 and 1 with a deque.
- **[Floyd-Warshall](/floyd-warshall/)** computes all pairs in $\Theta(n^3)$ time and $\Theta(n^2)$ space by allowing the intermediate vertices $1, \ldots, k$ for $k = 1, \ldots, n$. A negative entry on the diagonal reveals a negative cycle.
- **Potentials preserve shortest paths.** For any $h$, the weight $w(u, v) + h(u) - h(v)$ changes the weight of every $s$–$t$ path by the same amount $h(s) - h(t)$. With $h$ the distances from an added source, all new weights are nonnegative, which is how [Johnson's algorithm](/johnson/) reaches $O(nm + n^2 \log n)$.
- **The sorting barrier is broken.** Thorup's algorithm solves undirected graphs with integer weights in $O(m + n)$ time, and the 2025 algorithm of Duan, Mao, Mao, Shu and Yin solves directed graphs with real weights in $O(m \log^{2/3} n)$.

## The algorithms side by side

| Algorithm | Weights | Time | Extra space |
|---|---|---|---|
| [Bellman-Ford](/bellman-ford/) | any | $O(nm)$ | $\Theta(n)$ |
| [SPFA](/spfa/) | any | $O(nm)$ | $\Theta(n)$ |
| [DAG shortest paths](/dag-shortest-paths/) | any, graph acyclic | $\Theta(n + m)$ | $\Theta(n)$ |
| [Dijkstra](/dijkstra/), binary heap | $\ge 0$ | $O((n + m) \log n)$ | $O(n + m)$ |
| [0-1 BFS](/zero-one-bfs/) | 0 or 1 | $\Theta(n + m)$ | $O(n + m)$ |
| [Dial](/dial-algorithm/) | integers in $[0, C]$ | $O(m + nC)$ | $\Theta(n + m + C)$ |
| [Gabow scaling](/gabow-scaling-sssp/) | integers in $[0, N]$ | $O((n + m) \log N)$ | $O(n + m)$ |
| [Goldberg scaling](/goldberg-scaling-sssp/) | integers $\ge -N$ | $O(\sqrt{n}\, m \log N)$ | $O(n + m)$ |
| [Thorup](/thorup-undirected-sssp/) | positive integers, undirected | $O(m + n)$ | $O(m + n)$ |
| [Floyd-Warshall](/floyd-warshall/), all pairs | any | $\Theta(n^3)$ | $\Theta(n^2)$ |
| [Repeated squaring](/apsp-repeated-squaring/), all pairs | any | $\Theta(n^3 \log n)$ | $\Theta(n^2)$ |
| [Johnson](/johnson/), all pairs | any | $O(nm + n^2 \log n)$ | $O(n^2 + m)$ |

: Worst-case bounds from the entries, for $n$ vertices and $m$ edges; every method except Dijkstra, Dial, Gabow and Thorup also reports a negative cycle. Johnson's bound uses Fibonacci heaps.

## Choosing an algorithm

- Unit weights: [breadth-first search](/breadth-first-search/). Weights 0 and 1: 0-1 BFS. Small integer weights: Dial's buckets.
- Nonnegative weights, one source: Dijkstra with a binary heap. For one target, stop when the target is finished, or search from both ends.
- Negative weights, or a cycle to detect: Bellman-Ford, or a queue-based variant with a cycle check; if the graph is a DAG, the topological method.
- All pairs: Floyd-Warshall for dense graphs and small $n$, as it is three short loops; Johnson, or Dijkstra from each vertex when no weight is negative, for sparse graphs.
- Many queries on one fixed road network: preprocess, with contraction hierarchies or hub labels.
