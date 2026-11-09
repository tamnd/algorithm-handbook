## What to remember

- **Components in linear time.** Any traversal finds the [connected components](/connected-components/) of an undirected graph in $\Theta(n + m)$ time. A [disjoint-set](/union-find-connectivity/) structure does it in $O((n + m)\, \alpha(n))$ when the edges arrive one at a time.
- **In an undirected DFS every non-tree edge joins a vertex to an ancestor.** A subtree can leave only by a back edge, and $\mathrm{low}(v)$, the least discovery time reachable from the subtree of $v$ by one back edge, says how far up it can go.
- **The two tests.** A tree edge $uv$, with $u$ the parent, is a bridge exactly when $\mathrm{low}(v) > d(u)$. A non-root $u$ is an articulation point exactly when some child $v$ has $\mathrm{low}(v) \ge d(u)$; the root is one exactly when it has two or more children.
- **Blocks share only cut vertices,** and the blocks and cut vertices of a connected graph form a tree, the [block-cut tree](/block-cut-tree/). Removing the bridges leaves the 2-edge-connected components.
- **A graph has a strongly connected orientation exactly when it is connected and bridgeless** (Robbins). Directing DFS tree edges down and back edges up gives one.
- **Strongly connected components** are found in $\Theta(n + m)$ by [Kosaraju-Sharir](/kosaraju-sharir/) (two passes, the second on the transpose in decreasing finishing time), by [Tarjan](/tarjan-scc/) and by [Gabow](/gabow-path-based-scc/) (one pass each). The [condensation](/condensation-graph/) is a DAG.
- **Transitive closure** costs $\Theta(n^3)$ by [Warshall's algorithm](/warshall-algorithm/), or $n$ searches in $O(n(n + m))$; the transitive reduction of a DAG is unique and costs as much as the closure.
- **Menger's theorem:** the least number of vertices separating two non-adjacent vertices equals the most internally disjoint paths between them, and the same holds for edges. Always $\kappa \le \lambda \le \delta$.

## The algorithms side by side

| Problem | Method | Time | Extra space |
|---|---|---|---|
| [Components](/connected-components/) | BFS or DFS | $\Theta(n + m)$ | $\Theta(n)$ |
| Components, edges online | [union-find](/union-find-connectivity/) | $O((n + m)\, \alpha(n))$ | $\Theta(n)$ |
| [Bridges](/bridge-finding/), [cut vertices](/articulation-point-finding/), [blocks](/biconnected-components/) | DFS with low-links | $\Theta(n + m)$ | $\Theta(n + m)$ |
| [Block-cut tree](/block-cut-tree/) | from the blocks | $\Theta(n + m)$ | $\Theta(n)$ |
| Strong components | [Kosaraju-Sharir](/kosaraju-sharir/) | $\Theta(n + m)$ | $\Theta(n + m)$ |
| Strong components | [Tarjan](/tarjan-scc/), [Gabow](/gabow-path-based-scc/) | $\Theta(n + m)$ | $\Theta(n)$ |
| [Transitive closure](/transitive-closure/) | [Warshall](/warshall-algorithm/) | $\Theta(n^3)$ | $\Theta(n^2)$ |
| [Edge connectivity](/edge-connectivity/) | flows or contraction | $O(nm + n^2 \log n)$ | $O(n + m)$ |
| [Vertex connectivity](/vertex-connectivity/) | [Even-Tarjan](/even-tarjan-vertex-connectivity/) | $O((k + 1) n^{3/2} m)$ | $\Theta(n + m)$ |
| [Sparse certificate](/nagamochi-ibaraki-certificate/) | scan-first forests | $\Theta(n + m)$ | $\Theta(n + m)$ |

: Bounds from the entries; $k$ is the vertex connectivity, and the strong-component space counts the stacks and labels beyond the graph, except for Kosaraju-Sharir, which builds the transpose.

## Choosing an algorithm

- Components of a fixed graph: one traversal. Edges that keep arriving: union-find. Edges that are also deleted: see Chapter 7.12.
- Single points of failure: one DFS with low-links gives bridges, cut vertices and blocks together.
- Strong components: Tarjan's or Gabow's algorithm when one pass and no transpose matter; Kosaraju-Sharir when clarity matters more.
- Reachability between many pairs: condense first, then compute the closure of the smaller DAG, by bit-parallel Warshall when it is dense.
- Connectivity numbers above 2: maximum flow, after a sparse certificate has cut the graph down to $O(kn)$ edges.
