A delivery van, a drill moving over a circuit board and a telescope turning from star to star all need the same thing: an order of visits that makes the whole round trip as short as possible. This is the [traveling salesman problem](/traveling-salesman-problem/). In general no polynomial-time algorithm approximates it within any computable factor unless P = NP. When the distances obey the [triangle inequality](/triangle-inequality/), good ratios become possible, and the algorithms that reach them are among the best known of the field.

As in Chapter 18.1, each proof compares the tour with a lower bound on OPT. Deleting one edge of an optimal tour leaves a spanning tree, so the [minimum spanning tree](/minimum-spanning-tree/) weighs at most OPT. Shortcutting an optimal tour to an even set of cities gives two perfect matchings of them, so the cheaper one weighs at most $\text{OPT}/2$. The LP over subtours gives a third bound, the Held-Karp bound.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Metric TSP.** The double-tree algorithm with ratio 2, Christofides' algorithm with ratio $3/2$, the Held-Karp bound and the subtour LP, and the algorithm of Karlin, Klein and Oveis Gharan, which beats $3/2$ by a tiny constant.
2. **Variants.** The asymmetric TSP, with the algorithm of Asadpour and others, and the bottleneck TSP.
3. **Euclidean TSP.** The approximation schemes of Arora and of Mitchell for points in the plane.
4. **Heuristics.** Tour construction by nearest neighbor, greedy edges and insertion, and tour improvement by 2-opt, 3-opt, Or-opt and Lin-Kernighan, with its modern form LKH.

## What to read meanwhile

Start with the [traveling salesman problem](/traveling-salesman-problem/) in Volume 15, which states the hardness and the known ratios, and the [nearest neighbor heuristic](/nearest-neighbor-heuristic/), whose ratio on metric costs is $\Theta(\log n)$. The general [local search](/local-search/) entry explains the idea behind 2-opt, and the [Clarke-Wright savings](/clarke-wright-savings/) method and the [vehicle routing problem](/vehicle-routing-problem/) take tours to many vehicles.

The pieces of Christofides' algorithm are in Volume 7: the [minimum spanning tree](/minimum-spanning-tree/), the [Eulerian circuit](/eulerian-circuit/) and [Hierholzer's algorithm](/hierholzer-algorithm/), and the [minimum-weight perfect matching](/minimum-weight-perfect-matching/). The [Steiner tree problem](/steiner-tree-problem/) uses the same doubling idea to get ratio 2. For exact answers on small inputs, read the [Held-Karp algorithm](/held-karp-algorithm/) of Volume 2, which runs in $\Theta(n^2 2^n)$ time. In Chapter 18.1, [farthest-first traversal](/gonzalez-k-center/) is another algorithm whose proof rests on the triangle inequality.
