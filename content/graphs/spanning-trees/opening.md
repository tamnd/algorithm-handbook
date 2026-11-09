An electricity company must connect a set of towns, a chip designer must join a set of pins, and a clustering program must link a set of points; each wants the links to be as cheap as possible in total. If every pair of sites may be joined at a known cost, the cheapest network that connects them all is a tree, since a cycle always contains an edge that can be dropped. It is a [minimum spanning tree](/minimum-spanning-tree/) of the weighted graph of possible links.

The problem is unusual among optimization problems: greed solves it. Two facts explain why. By the [cut property](/cut-property/), the lightest edge that crosses any division of the vertices into two sides belongs to some minimum tree. By the [cycle property](/cycle-property/), the heaviest edge on any cycle can be left out. Each classical algorithm applies the first fact to a different family of cuts. [Kruskal's algorithm](/kruskal/) sorts the edges and keeps each one that joins two different components, in $O(m \log m)$ time. [Prim's algorithm](/prim/) grows one tree from a start vertex, adding the cheapest edge that leaves it, in $O((n + m) \log m)$ with a binary heap. [Borůvka's algorithm](/boruvka/) lets every component take its cheapest outgoing edge at once, and halves the number of components in each round. Behind all three is the fact that forests form a [matroid](/graphic-matroid/).

## What the chapter covers

The chapter is in nine groups, read in order.

1. **Spanning trees and forests.** [Spanning trees](/spanning-tree/), [spanning forests](/spanning-forest/), [fundamental cycles](/fundamental-cycle/) and the [graphic matroid](/graphic-matroid/).
2. **The minimum spanning tree and its two rules.** The [problem](/minimum-spanning-tree/), the [cut](/cut-property/) and [cycle](/cycle-property/) properties, [safe edges](/safe-edge/), [uniqueness](/mst-uniqueness/), [optimality conditions](/mst-optimality-conditions/), and the [maximum](/maximum-spanning-tree/) and [bottleneck](/minimum-bottleneck-spanning-tree/) versions.
3. **The classical algorithms.** The [generic method](/generic-mst-method/), the [blue and red rules](/greedy-mst-algorithm/), [Kruskal](/kruskal/), [Prim](/prim/), [Borůvka](/boruvka/) and [reverse-delete](/reverse-delete/).
4. **Checking and perturbing a tree.** [Verification](/mst-verification/), [sensitivity analysis](/mst-sensitivity-analysis/), the [second-best tree](/second-best-mst/) and the [lower bound](/mst-lower-bound/).
5. **Faster minimum spanning trees.** From [Yao's algorithm](/yao-mst/) to [Chazelle's](/chazelle-mst/) and the [optimal algorithm](/pettie-ramachandran-mst/) of Pettie and Ramachandran.
6. **Directed graphs.** [Cycle contraction](/cycle-contraction/), the [minimum arborescence](/minimum-arborescence/) and [Edmonds' algorithm](/edmonds-arborescence/).
7. **Counting, listing and sampling.** The [matrix-tree theorem](/matrix-tree-theorem/), [enumeration](/spanning-tree-enumeration/), and the random walks of [Aldous-Broder](/aldous-broder/) and [Wilson](/wilson-algorithm/).
8. **Packing and covering with trees.** [Arboricity](/arboricity/), the theorems of [Nash-Williams](/nash-williams-arboricity-theorem/) and [Nash-Williams and Tutte](/nash-williams-tutte-theorem/), and the [spanning tree polytope](/spanning-tree-polytope/).
9. **Trees with other objectives.** [Steiner trees](/steiner-tree-problem/), degree and leaf constraints, and trees judged by [diameter](/minimum-diameter-spanning-tree/), [routing cost](/minimum-routing-cost-spanning-tree/) or [stretch](/low-stretch-spanning-tree/).

## A first reading

For a first reading, take these entries in order: [spanning tree](/spanning-tree/), [fundamental cycle](/fundamental-cycle/), [minimum spanning tree](/minimum-spanning-tree/), [cut property](/cut-property/), [cycle property](/cycle-property/), [uniqueness](/mst-uniqueness/), [generic method](/generic-mst-method/), [Kruskal's algorithm](/kruskal/), [Prim's algorithm](/prim/), [Borůvka's algorithm](/boruvka/) and [MST verification](/mst-verification/). Then read the [matrix-tree theorem](/matrix-tree-theorem/) and [Edmonds' algorithm](/edmonds-arborescence/), which show how the problem changes when one counts trees or directs the edges.

Two pairs of entries overlap. The [generic method](/generic-mst-method/) and the [greedy MST algorithm](/greedy-mst-algorithm/) present the same framework, the first with safe edges and the second with Tarjan's blue and red rules; read the first. The [matrix-tree theorem](/matrix-tree-theorem/) and [counting spanning trees](/counting-spanning-trees/) state the same result as a theorem and as a problem; read the theorem first.

## Before you start

From Volume 3 you need the [disjoint-set](/disjoint-set/) structure, which carries Kruskal's algorithm, and the [binary heap](/binary-heap/) for Prim's; the [Fibonacci heap](/fibonacci-heap/) and the [soft heap](/soft-heap/) appear in group 5. From Volume 2 you need the [greedy method](/greedy-algorithm/), the [exchange argument](/exchange-argument/) and the [matroid](/matroid/). From this volume you need [graph traversal](/graph-traversal/) and the [cut](/cut/) of Chapter 7.6, which is only a definition. Group 7 uses the [determinant](/determinant/) of Volume 11 and the [Laplacian matrix](/laplacian-matrix/) of Chapter 7.1.
