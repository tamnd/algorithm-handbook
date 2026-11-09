## What to remember

- **An isomorphism is a relabeling.** Two graphs are [isomorphic](/graph-isomorphism-definition/) when a bijection of their vertices maps edges to edges and non-edges to non-edges. An [invariant](/isomorphism-invariant/) that differs proves non-isomorphism; invariants that agree prove nothing.

- **Symmetry is the same question turned inward.** The isomorphisms from a graph to itself form its [automorphism group](/graph-automorphism-group/). The group splits the vertices into [orbits](/automorphism-orbit/), and the number of isomorphisms between two isomorphic graphs equals the order of this group.

- **Most graphs have no symmetry at all.** [Almost every graph is asymmetric](/almost-all-graphs-asymmetric/), and almost every graph is identified by its degrees and one round of refinement. The hard instances are rare, highly regular graphs.

- **Trees are easy.** The [AHU algorithm](/ahu-algorithm/) gives each rooted subtree a code built from the sorted codes of its children, and solves [tree isomorphism](/tree-isomorphism/) in linear time. Free trees are rooted at their center first.

- **Finding a pattern inside a graph is much harder than matching two whole graphs.** [Subgraph isomorphism](/subgraph-isomorphism/) is NP-complete, and so are its cousins [maximum common subgraph](/maximum-common-subgraph/) and [graph edit distance](/graph-edit-distance/). [Ullmann](/ullmann-algorithm/) and [VF2](/vf2-algorithm/) are backtracking searches with pruning.

- **Color refinement does most of the work in practice.** [Weisfeiler-Leman](/weisfeiler-leman/) repeatedly splits vertex colors by the colors of the neighbours until the partition is [equitable](/equitable-partition/). It fails on regular graphs. The [$k$-dimensional version](/k-dimensional-weisfeiler-leman/) colors $k$-tuples and is stronger, but [Cai, Fürer and Immerman](/cai-furer-immerman-construction/) showed that no fixed $k$ suffices.

- **Practical tools search a tree of refinements.** [Individualization-refinement](/individualization-refinement/) fixes one vertex, refines again, and branches. [nauty](/nauty/) and [bliss](/bliss/) prune this tree with automorphisms they discover along the way and output a [canonical labeling](/canonical-labeling/).

- **The exact complexity is open.** [Graph isomorphism](/graph-isomorphism-problem/) is in NP and is not known to be in P or to be NP-complete. [Luks](/luks-algorithm/) solved bounded degree in polynomial time with group theory, and [Babai](/babai-quasipolynomial-algorithm/) brought the general problem down to quasi-polynomial time.

## The algorithms side by side

| Algorithm | Problem | Worst-case time | Notes |
|---|---|---|---|
| [AHU](/ahu-algorithm/) | rooted tree isomorphism | $\Theta(n)$ | codes of sorted child codes, radix sorting |
| [Color refinement](/weisfeiler-leman/) | test, not complete | $O(n(n+m)\log n)$ | fails on regular graphs |
| [$k$-WL](/k-dimensional-weisfeiler-leman/) | test, not complete | $O(k\,n^{2k+1}\log n)$ | colors $k$-tuples; 2-WL sees distances |
| [Ullmann](/ullmann-algorithm/) | subgraph isomorphism | $O(n^k k^2 n^2)$ | backtracking with a candidate matrix |
| [VF2](/vf2-algorithm/) | (sub)graph isomorphism | $O(n!\,n^2)$ | state-space search, $\Theta(n)$ memory |
| [nauty](/nauty/) | canonical labeling | $O(n!\,n^4)$ | individualization-refinement with automorphism pruning |
| [bliss](/bliss/) | canonical labeling | $O(n!\,n\,m)$ | same scheme, built for large sparse graphs |
| [Hopcroft-Tarjan](/hopcroft-tarjan-isomorphism/) | 3-connected planar isomorphism | $O(n^2 \log n)$ | $O(n \log n)$ in the best case |
| [Luks](/luks-algorithm/) | bounded-degree isomorphism | $n^{O(d)}$ | group theory, edge stabilizers |
| [Babai](/babai-quasipolynomial-algorithm/) | graph isomorphism | $\exp((\log n)^{O(1)})$ | the best general bound known |

: The main algorithms of the chapter. $n$ is the number of vertices, $m$ the number of edges, $k$ the size of the pattern or the dimension, and $d$ the degree bound. The exponential bounds for nauty and bliss are rarely approached in practice.

## Choosing an algorithm

- To compare two trees, use [AHU](/ahu-algorithm/), rooting free trees at their [center](/tree-center/).
- To compare two planar graphs, use a linear-time [planar isomorphism](/planar-graph-isomorphism/) test, which works on the triconnected components and their unique embeddings.
- To compare or deduplicate general graphs, compute a [canonical labeling](/canonical-labeling/) with [nauty](/nauty/) or [bliss](/bliss/) and compare or hash the canonical forms.
- To reject most non-isomorphic pairs quickly, compare invariants and then run [color refinement](/weisfeiler-leman/). Agreement does not prove isomorphism.
- To find a small pattern inside a large graph, use [VF2](/vf2-algorithm/) or [Ullmann](/ullmann-algorithm/). For a fixed pattern of $k$ vertices, the search is polynomial of degree about $k$.
- To measure how far apart two graphs are, use [graph edit distance](/graph-edit-distance/) or [maximum common subgraph](/maximum-common-subgraph/), exactly for small graphs and with heuristics otherwise.
