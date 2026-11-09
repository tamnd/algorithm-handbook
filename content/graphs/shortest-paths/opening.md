A map application asked for the fastest route, a network router choosing where to send a packet, a trader looking for a profitable cycle of currency exchanges and a project manager computing the earliest finish date all solve the same problem. Each has a directed graph whose edges carry weights, such as minutes, delays, logarithms of exchange rates or task durations, and each wants a path whose total weight is as small, or as large, as possible.

The chapter builds the classic algorithms from one operation. [Edge relaxation](/edge-relaxation/) lowers the estimate $d(v)$ to $d(u) + w(u, v)$ when that is smaller. Relax every edge $n - 1$ times and you have [Bellman-Ford](/bellman-ford/), which tolerates negative weights and detects negative cycles in $O(nm)$ time. Relax the edges of a directed acyclic graph in topological order and you have a $\Theta(n + m)$ algorithm. Always relax from the closest unfinished vertex, which is safe when no weight is negative, and you have [Dijkstra's algorithm](/dijkstra/), in $O((n + m) \log n)$ time with a binary heap. For all pairs, [Floyd-Warshall](/floyd-warshall/) takes $\Theta(n^3)$ time, and [Johnson's algorithm](/johnson/) takes $O(nm + n^2 \log n)$ by reweighting.

## What the chapter covers

The chapter is in ten groups, read in order.

1. **The problem.** [Shortest paths](/shortest-path/), [negative cycles](/negative-cycle/), [optimal substructure](/shortest-path-optimal-substructure/) and the [shortest-path tree](/shortest-path-tree/).
2. **Relaxation.** The [relaxation step](/edge-relaxation/), the [single-source problem](/single-source-shortest-paths/), the [upper-bound property](/upper-bound-property/), the [optimality conditions](/shortest-path-optimality-conditions/) and the [generic algorithm](/generic-shortest-path-algorithm/) of which the others are refinements.
3. **Negative weights and Bellman-Ford.** [Bellman-Ford](/bellman-ford/), [negative cycle detection](/negative-cycle-detection/), and the label-correcting variants [SPFA](/spfa/), [D'Esopo-Pape](/desopo-pape-algorithm/) and [subtree disassembly](/tarjan-subtree-disassembly/).
4. **Acyclic graphs and longest paths.** [Shortest paths in a DAG](/dag-shortest-paths/), the [reduction of longest paths](/longest-to-shortest-paths-reduction/) and the [critical path method](/pert-chart/).
5. **Nonnegative weights and Dijkstra.** [Dijkstra's algorithm](/dijkstra/) and [its proof](/dijkstra-correctness/), [0-1 BFS](/zero-one-bfs/), [Dial's algorithm](/dial-algorithm/), the [widest path](/widest-path/) and [bidirectional search](/bidirectional-dijkstra/).
6. **Negative cycles at work.** [Arbitrage](/arbitrage-detection/) and [difference constraints](/difference-constraints/).
7. **All pairs.** The [problem](/all-pairs-shortest-paths/), [Floyd-Warshall](/floyd-warshall/), the [min-plus matrix methods](/slow-apsp-matrix-multiplication/), [potentials and reduced costs](/potential-function-reduced-costs/) and [Johnson's algorithm](/johnson/).
8. **Faster single-source algorithms.** The [sorting barrier](/sorting-barrier/) and the scaling, undirected, negative-weight and directed algorithms that go past it.
9. **Queries on large networks.** [ALT](/alt-algorithm/), [contraction hierarchies](/contraction-hierarchies/), [hub labels](/hub-labeling/) and [distance oracles](/distance-oracle/).
10. **Variants of the problem.** [$k$ shortest paths](/k-shortest-paths/), [replacement paths](/replacement-paths/), [resource constraints](/constrained-shortest-path/) and [time-dependent travel times](/time-dependent-shortest-paths/).

## A first reading

For a first reading, take these entries in order: [shortest path](/shortest-path/), [negative cycle](/negative-cycle/), [optimal substructure](/shortest-path-optimal-substructure/), [shortest-path tree](/shortest-path-tree/), [edge relaxation](/edge-relaxation/), [Bellman-Ford](/bellman-ford/), [shortest paths in a DAG](/dag-shortest-paths/), [Dijkstra's algorithm](/dijkstra/), [correctness of Dijkstra's algorithm](/dijkstra-correctness/), [all-pairs shortest paths](/all-pairs-shortest-paths/), [Floyd-Warshall](/floyd-warshall/), [potentials and reduced costs](/potential-function-reduced-costs/) and [Johnson's algorithm](/johnson/). Add [difference constraints](/difference-constraints/) and [0-1 BFS](/zero-one-bfs/) for two quick applications. The label-correcting variants, the matrix-product methods and the last three groups can wait; groups 8 and 9 are research and engineering material.

Three entries describe currency arbitrage: [arbitrage detection](/arbitrage-detection/), [currency arbitrage](/currency-arbitrage/) and [currency arbitrage detection](/currency-arbitrage-detection/). Read the first and skim the others.

## Before you start

From Chapter 7.2 you need [breadth-first search](/breadth-first-search/), which is the shortest-path algorithm for unit weights, and [topological sort](/topological-sort/). From Volume 3 you need the [priority queue](/priority-queue/) and the [binary heap](/binary-heap/); the [Fibonacci heap](/fibonacci-heap/) gives the $O(m + n \log n)$ form of Dijkstra's bound, and the [bucket queue](/bucket-queue/) and the [deque](/deque/) serve the integer-weight variants. From Volume 2 you need [optimal substructure](/optimal-substructure/), since Bellman-Ford and Floyd-Warshall are dynamic programs. The matrix methods use the [min-plus product](/min-plus-matrix-multiplication/) of Volume 11.
