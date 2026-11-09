## What to remember

- **Both basic searches are linear.** On adjacency lists, [breadth-first search](/breadth-first-search/) and [depth-first search](/depth-first-search/) run in $\Theta(n + m)$ time and $\Theta(n)$ extra space, because each vertex is visited once and each adjacency list is read once. On an adjacency matrix the same searches take $\Theta(n^2)$.
- **BFS finds distances in edges.** It removes vertices from its queue in nondecreasing order of distance from the source, so the first time it sees a vertex it has found a shortest path to it. The parent pointers form a shortest-path tree, and in an undirected graph every edge joins two vertices whose layers differ by at most 1.
- **Bipartite means no odd cycle.** One search that gives each new vertex the colour opposite to its parent either 2-colours the graph or finds an edge between two vertices of the same colour, which closes an odd cycle. Either answer comes with a certificate.
- **The parenthesis theorem.** The intervals $[d[u], f[u]]$ of discovery and finish times of any two vertices are either nested or disjoint, and $v$ is a descendant of $u$ in the depth-first forest exactly when its interval lies inside that of $u$. The times are the numbers $1, \ldots, 2n$, each used once.
- **Edges have four classes in a directed DFS**, tree, back, forward and cross, and two in an undirected one, tree and back. A directed graph is acyclic exactly when a depth-first search finds no back edge.
- **A directed graph has a topological ordering exactly when it is acyclic.** [Kahn's algorithm](/kahns-algorithm/) outputs vertices of in-degree zero one by one; the DFS method lists vertices in decreasing order of finish time, the reverse postorder. Both take $\Theta(n + m)$ time, and both detect a cycle.
- **One template, many searches.** With a stack as its bag, [whatever-first search](/whatever-first-search/) is a depth-first search; with a queue, a breadth-first search; with a priority queue, a best-first search such as Prim's or Dijkstra's algorithm, at a cost of $O(n + m \log n)$ with a binary heap.

## The searches side by side

| Method | Time | Extra space | What it gives |
|---|---|---|---|
| [Breadth-first search](/breadth-first-search/) | $\Theta(n + m)$ | $\Theta(n)$ | distances in edges, a shortest-path tree, layers |
| [Depth-first search](/depth-first-search/) | $\Theta(n + m)$ | $\Theta(n)$ | discovery and finish times, the depth-first forest, edge classes |
| [Nonrecursive DFS](/iterative-depth-first-search/) | $\Theta(n + m)$ | $\Theta(n)$ | the same as DFS, without a deep call stack |
| [Kahn's algorithm](/kahns-algorithm/) | $\Theta(n + m)$ | $\Theta(n)$ | a topological ordering, or the vertices left on cycles |
| [Topological sort](/topological-sort/) | $\Theta(n + m)$ | $\Theta(n)$ | a topological ordering as reverse postorder |
| [Whatever-first search](/whatever-first-search/) | $O(n + mT)$ | $O(n + m)$ | any search, by the choice of bag |
| [Lexicographic BFS](/lexicographic-bfs/) | $\Theta(n + m)$ | $\Theta(n)$ | a perfect elimination ordering of a chordal graph |
| [Maximum cardinality search](/maximum-cardinality-search/) | $\Theta(n + m)$ | $\Theta(n)$ | the same, by a simpler rule |
| [Flood fill](/flood-fill/) | $\Theta(k)$ | $O(k)$ | the region of $k$ cells around a seed |
| [Morris traversal](/morris-traversal/) | $\Theta(n)$ | $\Theta(1)$ | the inorder of a binary tree, with no stack |

: Worst-case costs on adjacency lists, from the entries. $T$ is the cost of one operation on the bag of whatever-first search. For Morris traversal, $n$ is the number of tree nodes.

## Choosing a search

- For shortest paths in an unweighted graph, or anything measured in numbers of edges, use breadth-first search. With weights 0 and 1 only, the 0-1 BFS of Chapter 7.3 keeps the linear bound.
- For structure, such as cycles, topological order, strong components or cut vertices, use depth-first search and its times.
- For reachability alone, either search will do; choose the one whose memory pattern fits. BFS keeps a whole layer in its queue, DFS keeps one path on its stack.
- On graphs that may have paths of a million vertices, write DFS with an explicit stack; recursion that deep overflows the call stack of most languages.
- For a topological order that must also be lexicographically smallest, or that is built while the input arrives, use Kahn's algorithm with the right queue. For an order derived from a search you already run, use reverse postorder.
