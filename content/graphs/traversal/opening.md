Almost every graph algorithm starts by walking the graph. To find out whether a road network is connected, which web pages a crawler can reach from its seed, which cells of an image a paint bucket fills, or in which order a build system may compile its files, a program visits the vertices one by one along the edges, and records what it sees. This chapter is about the two ways of doing that walk which matter most, breadth-first search and depth-first search, and about what each one leaves behind.

Both searches visit each vertex once and look at each edge once or twice, so on adjacency lists they run in $\Theta(n + m)$ time for $n$ vertices and $m$ edges. They differ in the order of the visit, and the order is the point. [Breadth-first search](/breadth-first-search/) reaches vertices in order of their distance from the start, so it finds shortest paths when edges have no weights. [Depth-first search](/depth-first-search/) goes deep first, and its discovery and finish times carry enough structure to sort a directed acyclic graph, to find the strong components of Chapter 7.5 and to find the cut vertices of a network.

## What the chapter covers

The chapter is in seven groups, read in order.

1. **Reaching every vertex.** The [traversal](/graph-traversal/) task and the [reachability](/graph-reachability/) problem it solves.
2. **Breadth-first search.** The algorithm, its [layers](/bfs-layers/) and its [tree](/bfs-tree/), which give distances and shortest paths, [multi-source BFS](/multi-source-bfs/) for the distance to the nearest of many sources, and [level-order traversal](/level-order-traversal/) of a tree.
3. **Two colours.** Deciding whether a graph is bipartite, by one search that either 2-colours it or finds an odd cycle.
4. **Depth-first search.** The recursive and the [nonrecursive](/iterative-depth-first-search/) forms, the [depth-first forest](/dfs-forest/), [Trémaux's maze walk](/tremaux-traversal/) and [flood fill](/flood-fill/).
5. **The structure of a depth-first search.** [Discovery and finish times](/discovery-and-finish-times/), the [parenthesis theorem](/parenthesis-theorem/), the [white-path theorem](/white-path-theorem/), the [classification of edges](/edge-classification/) into tree, back, forward and cross edges, and the [preorder, postorder and reverse postorder](/depth-first-orders/).
6. **Topological order.** The [problem](/topological-ordering/), the [theorem](/topological-ordering-theorem/) that a directed graph has such an order exactly when it is acyclic, [Kahn's algorithm](/kahns-algorithm/) and the DFS-based [topological sort](/topological-sort/).
7. **Other search orders.** The generic [whatever-first search](/whatever-first-search/), [lexicographic BFS](/lexicographic-bfs/) and [maximum cardinality search](/maximum-cardinality-search/), [Morris traversal](/morris-traversal/) of binary trees in constant extra space, and online [graph exploration](/graph-exploration/).

## A first reading

For a first reading, take these entries in order: [graph traversal](/graph-traversal/), [breadth-first search](/breadth-first-search/), [BFS layers](/bfs-layers/), [the breadth-first tree](/bfs-tree/), [bipartiteness checking](/bipartiteness-check/), [depth-first search](/depth-first-search/), [discovery and finish times](/discovery-and-finish-times/), [the parenthesis theorem](/parenthesis-theorem/), [edge classification](/edge-classification/), [topological ordering](/topological-ordering/), [Kahn's algorithm](/kahns-algorithm/) and [topological sort](/topological-sort/). The white-path theorem and the depth-first orders are needed before Chapter 7.5, not before. The last group can wait: lexicographic BFS and maximum cardinality search belong with the chordal graphs of Chapter 7.8, and graph exploration is an online problem.

Three entries cover the bipartite test: [bipartiteness checking](/bipartiteness-check/), [bipartite graph recognition](/bipartite-graph-recognition/) and [two-colouring](/bipartite-testing/). Read the first and skim the others; Chapter 7.8 has two more. Likewise [graph reachability](/graph-reachability/) here and [reachability](/reachability/) in Chapter 7.5 are one problem.

## Before you start

You need the [queue](/queue/) and the [stack](/stack/) from Volume 3, and [recursion](/recursion/) from Volume 1, since depth-first search is most often written as a recursive procedure. The graphs are stored as [adjacency lists](/adjacency-list/), from Chapter 7.1, and the costs assume that form. Proofs here are by induction on time or on distance, as in [loop invariants](/loop-invariant/). [Level-order](/level-order-traversal/) and [Morris](/morris-traversal/) traversal use [binary trees](/binary-tree/) from Chapter 7.10, and Morris traversal also the [threaded binary tree](/threaded-binary-tree/) of Volume 3.
