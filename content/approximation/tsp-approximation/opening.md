A delivery van, a drill moving over a circuit board and a telescope turning from star to star all face the same task: visit every point once and come back, by the shortest round trip. This is the [traveling salesman problem](/traveling-salesman-problem/). With arbitrary costs no polynomial-time algorithm approximates it within any factor unless P = NP. When the costs obey the triangle inequality, a tour can skip a city without getting longer, and this one fact makes constant ratios possible. Most entries of the chapter are about this metric case.

As in the rest of the volume, the ratio of a minimization algorithm is a number $\rho \ge 1$ with ALG $\le \rho \cdot \text{OPT}$ on every input. Each proof compares the tour with a lower bound on OPT. Deleting one edge of an optimal tour leaves a spanning tree, so the minimum spanning tree costs less than OPT. Shortcutting an optimal tour to an even set of cities splits it into two perfect matchings of those cities, so the cheaper one costs at most $\text{OPT}/2$. The subtour LP gives a third bound, which on random points is typically within about one percent of OPT.

The chapter has two strands that meet often. The first asks for proved ratios: 2 from a doubled tree, $3/2$ from Christofides' algorithm, and since 2020 a ratio a tiny constant below $3/2$. The second asks for short tours on large inputs: construction rules and local search, which have weak guarantees or none, but come within a few percent of OPT in practice. The Held-Karp bound serves both strands, as a tool in proofs and as the yardstick against which heuristics are measured.

The chapter is in seven groups, read in order.

## What the chapter covers

1. **The problem and its first lower bound.** [Metric TSP](/metric-tsp/), with the shortcut lemma and the hardness results, and the [MST lower bound](/mst-lower-bound-for-tsp/) with its refinement, the 1-tree.
2. **Building a tour city by city.** The [nearest neighbour](/nearest-neighbor-tsp/) and [greedy edge](/greedy-edge-heuristic/) rules, both with ratio $\Theta(\log n)$, and three insertion rules: [nearest](/nearest-insertion/) and [cheapest insertion](/cheapest-insertion/) with ratio 2, and [farthest insertion](/farthest-insertion/), which is good in practice but has no proved constant ratio.
3. **Tours from a spanning tree.** The [double-tree algorithm](/double-tree-algorithm/) and its form as a [preorder walk](/mst-preorder-walk-tsp/), both with ratio 2, [Christofides' algorithm](/christofides-algorithm/) with ratio $3/2$, and the [MST heuristic family](/mst-tsp-heuristic/), which ends with a 2-opt pass.
4. **The subtour LP and the Held-Karp bound.** The [subtour elimination LP](/subtour-elimination-lp/), the [Held-Karp bound](/held-karp-bound/) that computes its value with 1-trees, and the [Karlin-Klein-Oveis Gharan algorithm](/karlin-klein-oveis-gharan-algorithm/), the first to beat $3/2$.
5. **Improving a tour by local search.** [2-opt](/two-opt/), [3-opt](/three-opt/) and [Or-opt](/or-opt/), then the variable-depth search of [Lin-Kernighan](/lin-kernighan/) and its modern form, [LKH](/lin-kernighan-helsgaun/).
6. **Points in the plane.** The [Euclidean TSP](/euclidean-tsp/), the fast [space-filling curve](/space-filling-curve-tsp/) tour, [Karp's partitioning](/karp-partitioning-tsp/) for random points, and the approximation schemes of [Arora](/arora-euclidean-tsp-ptas/) and [Mitchell](/mitchell-euclidean-tsp-ptas/).
7. **Asymmetric and bottleneck tours.** The [asymmetric TSP](/asymmetric-tsp/) with repeated cycle covers and the thin-tree algorithm of [Asadpour and others](/asadpour-atsp-algorithm/), and the [bottleneck TSP](/bottleneck-tsp/) with its best possible [2-approximation](/bottleneck-tsp-approximation/).

## A first reading

A first pass can take these twelve entries, in this order:

1. [Metric TSP](/metric-tsp/)
2. [MST lower bound](/mst-lower-bound-for-tsp/)
3. [Nearest neighbour](/nearest-neighbor-tsp/)
4. [Nearest insertion](/nearest-insertion/)
5. [Double-tree algorithm](/double-tree-algorithm/)
6. [Christofides' algorithm](/christofides-algorithm/)
7. [2-opt](/two-opt/)
8. [Or-opt](/or-opt/)
9. [Lin-Kernighan](/lin-kernighan/)
10. [Held-Karp bound](/held-karp-bound/)
11. [Euclidean TSP](/euclidean-tsp/)
12. [Asymmetric TSP](/asymmetric-tsp/)

Skip on a first pass the entries at research level (Karlin-Klein-Oveis Gharan, Asadpour and others, LKH and Mitchell's scheme) and the cited parts of Arora's proof. The preorder walk and the MST heuristic family repeat the double-tree idea and can be skimmed.

## Before you start

From Volume 15 you need the general traveling salesman problem itself, the [linear programming problem](/linear-programming-problem/), the [LP relaxation](/lp-relaxation/) and its [integrality gap](/integrality-gap/), [LP duality](/lp-duality/) and [Lagrangian relaxation](/lagrangian-relaxation/), and for group 5 [local search](/local-search/) with its [neighbourhood structure](/neighborhood-structure/) and [local optimum](/local-optimum/). From Volume 7 you need the [minimum spanning tree](/minimum-spanning-tree/) with [Prim's](/prim/) and [Kruskal's](/kruskal/) algorithms, the [Eulerian circuit](/eulerian-circuit/), the [minimum weight perfect matching](/minimum-weight-perfect-matching/), the [Hamiltonian cycle problem](/hamiltonian-cycle-problem/) and, for the later groups, the [spanning tree polytope](/spanning-tree-polytope/) and the [biconnected graph](/biconnected-graph/). The [metric space](/metric-space/) and the [triangle inequality](/triangle-inequality/) of Volume 5 are used on every page. The randomized algorithms use [linearity of expectation](/linearity-of-expectation/) and the [Chernoff bound](/chernoff-bound/) from Volume 1. Group 6 uses the [quadtree](/quadtree/) of Volume 3, and Karp's partitioning solves small cells with the [Held-Karp dynamic program](/held-karp-algorithm/) of Volume 2. The [approximation ratio](/approximation-ratio/) and the [PTAS](/ptas/) are defined in Chapter 18.5.

The entries also use NP-hardness and polynomial-time reductions, whose entries are not yet written; their definitions are in any textbook on computational complexity.
