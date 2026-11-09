## What to remember

- **The words.** A [walk](/walk/) may repeat anything, a [trail](/trail/) no edge, a [path](/simple-path/) no vertex. Every walk from $u$ to $v$ contains a path from $u$ to $v$, so reachability questions can ignore the difference; length and counting questions cannot.
- **Cycles are found in linear time.** Depth-first search finds a cycle in a directed graph exactly when it meets an arc to a vertex still on the stack ([DFS cycle detection](/dfs-cycle-detection/)). A graph with no cycle has a source, which is why topological sorting works.
- **Euler is easy.** A connected graph has an Eulerian circuit exactly when every degree is even, and a trail exactly when 0 or 2 degrees are odd; in a directed graph, in-degree must equal out-degree ([Euler's theorem](/eulers-theorem-eulerian-graphs/)). [Hierholzer's algorithm](/hierholzer-algorithm/) builds the circuit in $\Theta(n + m)$.
- **Postmen pair the odd vertices.** The shortest closed walk through every edge doubles shortest paths between the odd vertices, chosen by a minimum-weight perfect matching ([Edmonds-Johnson](/edmonds-johnson-algorithm/)), in $O(n^3)$.
- **Hamilton is hard.** Deciding whether a [Hamiltonian cycle](/hamiltonian-cycle-problem/) exists is NP-complete for directed and undirected graphs. Dense graphs always have one: minimum degree $n/2$ ([Dirac](/dirac-theorem/)), or degree sum $n$ on non-adjacent pairs ([Ore](/ore-theorem/)). Exact search uses the $O(2^n n^2)$ subset dynamic program of [Held and Karp](/held-karp-algorithm/).
- **Longest paths are easy only without cycles.** In a DAG every path is simple, and one pass in [topological order](/dag-longest-path/) finds the heaviest. In general, the [longest path](/longest-path-problem/) contains the Hamiltonian path problem.
- **Covers and cycles by matching and dynamic programming.** A [minimum path cover](/path-cover-by-bipartite-matching/) of a DAG has $n$ minus a maximum matching paths. The [minimum mean cycle](/karp-minimum-mean-cycle/) comes from the shortest walks of each length $k \le n$.
- **Cycle space.** The cycles form a vector space over GF(2) of dimension $m - n + c$, with the [fundamental cycles](/cycle-basis/) of a spanning forest as a basis.

## The algorithms side by side

| Algorithm | Problem | Time | Extra space |
|---|---|---|---|
| [DFS cycle detection](/dfs-cycle-detection/) | find a cycle | $\Theta(n + m)$ | $\Theta(n)$ |
| [Hierholzer](/hierholzer-algorithm/) | Eulerian circuit or trail | $\Theta(n + m)$ | $\Theta(n + m)$ |
| [Fleury](/fleury-algorithm/) | Eulerian trail | $O(m(n + m))$ | $\Theta(n + m)$ |
| [Edmonds-Johnson](/edmonds-johnson-algorithm/) | Chinese postman | $O(n^3)$ | $O(n^2)$ |
| [DAG longest path](/dag-longest-path/) | heaviest path in a DAG | $\Theta(n + m)$ | $\Theta(n)$ |
| [Path cover by matching](/path-cover-by-bipartite-matching/) | minimum path cover of a DAG | $O(n(n + m))$ | $\Theta(n + m)$ |
| [Itai-Rodeh](/itai-rodeh-girth-algorithm/) | girth, unweighted | $\Theta(n(n + m))$ | $\Theta(n + m)$ |
| [Karp](/karp-minimum-mean-cycle/) | minimum mean cycle | $\Theta(n(n + m))$ | $\Theta(n^2)$ |
| [Read-Tarjan](/read-tarjan-path-enumeration/) | all simple $s$-$t$ paths | $O((n + m)(N + 1))$ | $O(nm)$ |
| [Johnson](/johnson-elementary-cycles-algorithm/) | all simple cycles | $O((n + m)(c + 1))$ | $O(n + m)$ |
| Subset dynamic program | feedback arc set | $O(2^n n^2)$ | $O(2^n)$ |

: Worst-case bounds from the entries. $N$ is the number of $s$-$t$ paths and $c$ the number of cycles, so the Read-Tarjan and Johnson bounds grow with the output.

## Choosing an algorithm

- Is there a cycle, or a topological order: depth-first search with three colors, or Kahn's algorithm from Chapter 7.2.
- A route through every edge: check the degrees, then Hierholzer. Fleury is easier to explain but quadratic. If some degrees are odd and edges may repeat, solve the postman problem.
- A route through every vertex: Held-Karp for up to about 20 vertices, backtracking with pruning beyond; first check whether Dirac's or Ore's condition already settles it.
- A longest path: if the graph is a DAG, the topological-order pass; on trees, Chapter 7.10; otherwise exponential search.
- A shortest cycle: Itai-Rodeh for unweighted graphs; with weights, a Dijkstra run from each vertex.
- Listing: Johnson for cycles and Read-Tarjan for paths, both with linear time per output.
