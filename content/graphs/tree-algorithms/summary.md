## What to remember

- **Trees have many definitions.** Connected and acyclic, connected with $n - 1$ edges, acyclic with $n - 1$ edges, and a unique path between every two vertices all say the same thing ([free tree properties](/free-tree-properties/)). The [Prüfer code](/pruefer-code/) turns labeled trees into sequences and counts them as $n^{n-2}$.
- **Postorder is bottom-up.** Most tree algorithms are one [postorder pass](/postorder-traversal/) that combines the values of the children, as with [subtree sizes](/subtree-sizes/). Preorder and postorder with inorder determine a binary tree; preorder with postorder alone may not.
- **Two searches give the diameter.** The vertex farthest from any start is an end of a longest path, so the [double sweep](/tree-diameter-double-sweep/) finds the diameter in $\Theta(n)$. The [center](/tree-center-leaf-peeling/) is the middle of any longest path, and the [centroid](/centroid/), which leaves pieces of at most $n/2$, is a different vertex in general.
- **Tree DP keeps a few values per vertex.** For the heaviest [independent set](/independent-set-on-trees/), keep the best with and without the vertex. [Rerooting](/rerooting-technique/) gives the answer for every root in linear time.
- **LCA has four standard solutions.** [Binary lifting](/lca-binary-lifting/) uses $\Theta(n \log n)$ space and $O(\log n)$ per query. The [Euler tour with a sparse table](/euler-tour-lca/) answers in $O(1)$. [Tarjan's offline method](/tarjan-offline-lca/) runs in $O((n + q)\alpha(n))$ for a batch, and [ladders](/ladder-decomposition/) answer level ancestors in $O(1)$.
- **Subtrees are ranges; paths are $O(\log n)$ ranges.** The [Euler tour](/euler-tour-technique/) makes each subtree an interval. [Heavy-light decomposition](/heavy-light-decomposition/) cuts each root path into $O(\log n)$ heavy paths, and [centroid decomposition](/centroid-decomposition/) has depth $O(\log n)$.
- **Dominator trees** record which vertices every path from the start must pass. [Lengauer-Tarjan](/lengauer-tarjan-algorithm/) builds them in near-linear time from semidominators.
- **Treewidth measures closeness to a tree.** Dynamic programming over a [nice tree decomposition](/dp-on-tree-decompositions/) solves many NP-hard problems in time $f(k) \cdot n$ for width $k$. Computing the treewidth is NP-hard, but fixed-parameter tractable.

## The algorithms side by side

| Algorithm | Problem | Preprocessing | Query |
|---|---|---|---|
| [Double sweep](/tree-diameter-double-sweep/) | diameter | $\Theta(n)$ | |
| [Leaf peeling](/tree-center-leaf-peeling/) | center | $\Theta(n)$ | |
| [Tree DP](/independent-set-on-trees/) | heaviest independent set | $\Theta(n)$ | |
| [Binary lifting](/lca-binary-lifting/) | LCA, $k$-th ancestor | $\Theta(n \log n)$ | $O(\log n)$ |
| [Euler tour + RMQ](/euler-tour-lca/) | LCA | $\Theta(n \log n)$ | $O(1)$ |
| [Tarjan offline](/tarjan-offline-lca/) | $q$ LCA queries at once | $O((n + q)\alpha(n))$ total | |
| [Ladders](/ladder-decomposition/) | level ancestor | $\Theta(n \log n)$ | $O(1)$ |
| [Heavy-light](/heavy-light-decomposition/) | path queries with updates | $\Theta(n)$ | $O(\log^2 n)$ |
| [Lengauer-Tarjan](/lengauer-tarjan-algorithm/) | dominator tree | $O(m \log n)$ | |
| [Zhang-Shasha](/zhang-shasha-algorithm/) | tree edit distance | $O(n^4)$ | |
| [Reingold-Tilford](/reingold-tilford-layout/) | tree layout | $\Theta(n)$ | |
| [FRT](/frt-tree-embedding/) | tree embedding of a metric | $O(n^2 \log \Delta)$ | $O(\log \Delta)$ |

: Bounds from the entries; heavy-light with a segment tree. The Zhang-Shasha bound drops to $O(n^2 \log^2 n)$ for balanced trees.

## Choosing an algorithm

- A few LCA queries on a static tree: binary lifting, which also gives $k$-th ancestors and path maxima and minima along the jumps.
- Many LCA queries with no updates: the Euler tour with a sparse table; offline, Tarjan's method with union-find.
- Subtree sums with updates: Euler tour and a Fenwick tree. Path sums or path assignments with updates: heavy-light with a segment tree.
- Counting pairs of vertices by distance or path property: centroid decomposition.
- Queries on several small key sets: build a virtual tree for each set and run the tree DP on it.
- A graph that is almost a tree: compute a tree decomposition with a heuristic and run the DP over it if the width is small.
