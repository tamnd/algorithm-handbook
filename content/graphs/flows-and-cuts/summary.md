## What to remember

- **Weak duality.** For every flow $f$ and every $s$–$t$ cut $(S, T)$, the value of $f$ equals the net flow across the cut, so it is at most the [capacity](/cut-capacity/) of the cut.
- **Max-flow min-cut.** A flow is maximum exactly when its [residual graph](/residual-graph/) has no $s$–$t$ path; then the vertices reachable from $s$ form a cut whose capacity equals the flow value.
- **Integrality.** With integer capacities, Ford-Fulkerson gains at least one unit per augmentation, stops after at most $F$ augmentations, and returns an integral maximum flow. This is what turns flows into counts of disjoint paths, matchings and schedules.
- **Every flow decomposes** into at most $m$ paths and cycles, which can be found in $O(nm)$ time.
- **The choice of path matters.** Shortest paths give at most $O(nm)$ augmentations ([Edmonds-Karp](/edmonds-karp/), $O(nm^2)$). Blocking flows give at most $n - 1$ phases ([Dinic](/dinic/), $O(n^2 m)$), and push-relabel gives $O(n^3)$. Scaling and fattest paths give bounds in $\log U$.
- **Minimum-cost flow:** a flow of a given value is cheapest exactly when its residual graph has no negative-cost cycle. Potentials keep reduced costs nonnegative, so successive shortest paths can use Dijkstra.
- **Global minimum cuts need no flows.** One run of random contraction keeps a fixed minimum cut with probability at least $\binom{n}{2}^{-1}$. Stoer-Wagner finds a minimum cut deterministically in $O(n^3)$ by maximum adjacency orderings.
- **An undirected graph has at most $n - 1$ distinct pairwise cut values,** and a [Gomory-Hu tree](/gomory-hu-tree/) built from $n - 1$ flows stores all of them.

## The algorithms side by side

| Algorithm | Problem | Time | Note |
|---|---|---|---|
| [Ford-Fulkerson](/ford-fulkerson/) | max flow | $O((n + m) F)$ | integer capacities |
| [Edmonds-Karp](/edmonds-karp/) | max flow | $O(nm^2)$ | BFS paths |
| [Capacity scaling](/capacity-scaling/) | max flow | $O(m^2 \log U)$ | integer capacities |
| [Dinic](/dinic/) | max flow | $O(n^2 m)$ | blocking flows |
| [MPM](/mpm-algorithm/) | max flow | $O(n^3)$ | vertex throughput |
| [Push-relabel](/push-relabel/) | max flow | $O(n^3 + nm)$ | FIFO order |
| [Almost-linear flow](/almost-linear-max-flow/) | max flow, min-cost flow | $m^{1 + o(1)} \log U$ | interior point |
| [Cycle canceling](/cycle-canceling/) | min-cost flow | $O(nm^2 CU)$ | any start flow |
| [Successive shortest paths](/successive-shortest-path/) | min-cost flow | $O(nm + Fm \log n)$ | Dijkstra with potentials |
| [Karger-Stein](/karger-stein/) | global min cut | $O(n^2 \log^3 n)$ | Monte Carlo |
| [Stoer-Wagner](/stoer-wagner/) | global min cut | $O(n^3)$ | deterministic |
| [Hao-Orlin](/hao-orlin/) | directed global min cut | $O(n^2 m)$ | one push-relabel run |
| [Gomory-Hu](/gomory-hu-algorithm/) | all-pairs min cut | $O(nT + nm)$ | $T$ for one flow |

: Bounds from the entries; $F$ is the flow value, $U$ the largest capacity and $C$ the largest absolute cost, all integers where they appear.

## Choosing an algorithm

- Small integer flow value, such as counting disjoint paths: Ford-Fulkerson with any search, in $O(mF)$.
- General maximum flow in code you write yourself: Dinic, which is short and fast on unit and bipartite networks. For large hard instances, push-relabel with the highest-label rule and global relabelling.
- Costs on the arcs: successive shortest paths for small flow values, network simplex or cost scaling in production solvers.
- A minimum cut with no fixed terminals in an undirected graph: Stoer-Wagner when the graph is dense, repeated contraction for a simple randomized code.
- Many pairs of terminals in one undirected network: build a Gomory-Hu tree once.
- Several commodities: a linear program; the integer versions of multicut and sparsest cut are NP-hard and are approximated.
