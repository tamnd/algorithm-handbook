A graph is a set of points, called vertices, and a set of links between pairs of them, called edges. That is enough to describe a road map, the links between web pages, the calls between functions in a program, the friendships in a social network, the moves of a puzzle and the tasks of a project with the order they must be done in. Once a problem is drawn as a graph, the same few questions come up. Can I get from here to there? What is the shortest way? Which links hold the network together? How much can flow through it? Which pairs can be matched? This volume collects the algorithms that answer them.

The volume starts with how a graph is stored and how it is explored. Then come the classic optimization problems on graphs: shortest paths, minimum spanning trees, connectivity, flows and cuts, and matchings. After them come problems on special structure: colorings and cliques, paths and cycles that visit everything, trees, and graphs that can be drawn in the plane. The last three chapters leave the static, single-graph setting: graphs that change over time, the question of whether two graphs are the same, and the measurement of large real networks.

## Why graphs get a volume of its own

Graph algorithms are where the ideas of the earlier volumes meet a wide range of problems. In this one volume you will meet:

- **Search as the basic step.** [Breadth-first search](/breadth-first-search/) and [depth-first search](/depth-first-search/) visit every vertex and edge in $\Theta(n + m)$ time, where $n$ is the number of vertices and $m$ the number of edges. Many linear-time algorithms in this volume are one of these two searches with a little bookkeeping added: [topological sort](/topological-sort/), [strongly connected components](/strongly-connected-components/), [articulation points](/articulation-point/), [Hierholzer's algorithm](/hierholzer-algorithm/) for Euler tours.
- **Greedy algorithms with proofs.** [Dijkstra's algorithm](/dijkstra/), [Kruskal's algorithm](/kruskal/) and [Prim's algorithm](/prim/) each make the locally best choice and never undo it. The [cut property](/cut-property/) and the correctness proof of Dijkstra's algorithm say exactly why this is safe.
- **Dynamic programming over paths.** [Bellman-Ford](/bellman-ford/) and [Floyd-Warshall](/floyd-warshall/) build shortest paths from shorter ones, and they still work when some weights are negative.
- **Duality.** The [max-flow min-cut theorem](/max-flow-min-cut-theorem/) says the largest flow equals the smallest cut. [Kőnig's theorem](/konig-theorem/) and [Menger's theorem](/menger-theorem/) are the same idea in other dress: a maximum of one kind of object equals a minimum of another, and the algorithm that finds one also finds the other as a proof.
- **Augmenting paths.** [Ford-Fulkerson](/ford-fulkerson/), [Hopcroft-Karp](/hopcroft-karp/) and [Edmonds' blossom algorithm](/edmonds-blossom/) improve a solution step by step along a path in an auxiliary graph, and stop when no such path exists.
- **Data structures inside algorithms.** The running time of Dijkstra's algorithm depends on its [priority queue](/priority-queue/); Kruskal's depends on a [disjoint-set](/disjoint-set/) structure. [Link-cut trees](/link-cut-tree/) were invented to speed up flow algorithms.
- **Hard problems next to easy ones.** An Euler tour is found in linear time; a Hamiltonian cycle is NP-hard to find. A 2-coloring is easy; a 3-coloring is not.

## The chapters

**Chapter 7.1, Graph representation**, gives the vocabulary of graphs and the ways to store one: the [adjacency matrix](/adjacency-matrix/), the [adjacency list](/adjacency-list/), the [edge list](/edge-list/) and packed forms such as [compressed sparse row](/compressed-sparse-row/). The choice sets the cost of every later algorithm.

**Chapter 7.2, Traversal**, covers [breadth-first search](/breadth-first-search/) and [depth-first search](/depth-first-search/), the structure DFS leaves behind (discovery and finish times, edge classes), and [topological sort](/topological-sort/) of a directed acyclic graph, both by DFS and by [Kahn's algorithm](/kahns-algorithm/).

**Chapter 7.3, Shortest paths**, starts from [edge relaxation](/edge-relaxation/) and builds [Bellman-Ford](/bellman-ford/) in $O(nm)$ time, [Dijkstra's algorithm](/dijkstra/) in $O((n + m) \log n)$ for nonnegative weights, [Floyd-Warshall](/floyd-warshall/) in $\Theta(n^3)$ and [Johnson's algorithm](/johnson/) for all pairs. It ends with speed-up techniques for road networks and recent results such as [breaking the sorting barrier](/breaking-sorting-barrier-sssp/).

**Chapter 7.4, Spanning trees**, finds the cheapest set of edges that connects a graph. [Kruskal's algorithm](/kruskal/), [Prim's algorithm](/prim/) and [Borůvka's algorithm](/boruvka/) all follow from the [cut property](/cut-property/). The chapter also counts spanning trees with the [matrix-tree theorem](/matrix-tree-theorem/) and samples them at random.

**Chapter 7.5, Connectivity**, asks which vertices can reach which, and which single vertex or edge would cut a graph apart. [Kosaraju-Sharir](/kosaraju-sharir/) and [Tarjan's algorithm](/tarjan-scc/) find [strongly connected components](/strongly-connected-components/) in $\Theta(n + m)$; [low-link](/low-link/) values find [articulation points](/articulation-point/) and [bridges](/bridge/).

**Chapter 7.6, Flows and cuts**, moves as much as possible from a source to a sink through edges of limited capacity. It proves the [max-flow min-cut theorem](/max-flow-min-cut-theorem/), develops [Ford-Fulkerson](/ford-fulkerson/), [Edmonds-Karp](/edmonds-karp/), [Dinic's algorithm](/dinic/) and [push-relabel](/push-relabel/), and shows many problems that reduce to a flow, from [baseball elimination](/baseball-elimination/) to [image segmentation](/image-segmentation-graph-cuts/).

**Chapter 7.7, Matching**, pairs up vertices along edges. In bipartite graphs, [Hopcroft-Karp](/hopcroft-karp/) finds a maximum matching and the [Hungarian algorithm](/hungarian-algorithm/) a cheapest assignment. [Gale-Shapley](/gale-shapley/) finds a [stable matching](/stable-matching/). In general graphs, [Edmonds' blossom algorithm](/edmonds-blossom/) handles odd cycles.

**Chapter 7.8, Coloring and cliques**, assigns colors so that neighbours differ, and looks for groups of vertices that are all adjacent. Most of these problems are NP-hard, so the chapter mixes bounds such as [Brooks' theorem](/brooks-theorem/), fast heuristics such as [greedy coloring](/greedy-coloring/), exact exponential algorithms such as [Bron-Kerbosch](/bron-kerbosch/), and classes where the problems become easy, such as [chordal graphs](/chordal-graph/).

**Chapter 7.9, Paths and cycles**, contrasts [Eulerian circuits](/eulerian-circuit/), which use every edge once and are found in linear time, with [Hamiltonian cycles](/hamiltonian-cycle/), which visit every vertex once and are hard. It also covers cycle detection, longest paths in DAGs, the [Chinese postman problem](/chinese-postman-problem/) and the enumeration of cycles.

**Chapter 7.10, Tree algorithms**, works on trees, where most problems become easy. It covers [diameter](/tree-diameter/) and [center](/tree-center/), [lowest common ancestors](/lowest-common-ancestor/), [heavy-light decomposition](/heavy-light-decomposition/) and [centroid decomposition](/centroid-decomposition/), and [tree decompositions](/tree-decomposition/), which extend tree methods to graphs that are nearly trees.

**Chapter 7.11, Planar graphs**, studies graphs that can be drawn without crossings. [Euler's formula](/euler-formula/) bounds their edges, [planarity testing](/planarity-testing/) runs in linear time, the [four color theorem](/four-color-theorem/) bounds their colorings, and the [planar separator theorem](/planar-separator-theorem/) splits them into balanced pieces.

**Chapter 7.12, Dynamic graphs**, keeps answers correct while edges are inserted and deleted. [Euler tour trees](/euler-tour-tree/) and [link-cut trees](/link-cut-tree/) maintain forests in $O(\log n)$ expected or amortized time per operation, and the [Holm-de Lichtenberg-Thorup](/holm-de-lichtenberg-thorup/) structure maintains connectivity of a general graph in $O(\log^2 n)$ amortized time.

**Chapter 7.13, Graph isomorphism**, asks whether two graphs are the same up to renaming of vertices. Trees are easy, by the [AHU algorithm](/ahu-algorithm/); general graphs are handled in practice by the colour refinement of [Weisfeiler-Leman](/weisfeiler-leman/) and [individualization-refinement](/individualization-refinement/), and in theory by [Babai's quasipolynomial algorithm](/babai-quasipolynomial-algorithm/).

**Chapter 7.14, Network analysis**, measures large real networks: who is central ([betweenness](/betweenness-centrality/), [PageRank](/pagerank/)), how tightly knit they are ([clustering coefficient](/clustering-coefficient/), [k-cores](/k-core/)), which groups they contain ([community detection](/community-detection/)), and which random models produce networks that look like them.

## How to read this volume

If this is your first course on graph algorithms, read these entries in this order: [graph](/graph/), [adjacency list](/adjacency-list/), [adjacency matrix](/adjacency-matrix/), [breadth-first search](/breadth-first-search/), [depth-first search](/depth-first-search/), [topological sort](/topological-sort/), [connected components](/connected-components/), [strongly connected components](/strongly-connected-components/), [edge relaxation](/edge-relaxation/), [Bellman-Ford](/bellman-ford/), [Dijkstra's algorithm](/dijkstra/), [Floyd-Warshall](/floyd-warshall/), [minimum spanning tree](/minimum-spanning-tree/), [the cut property](/cut-property/), [Kruskal's algorithm](/kruskal/), [Prim's algorithm](/prim/), [Ford-Fulkerson](/ford-fulkerson/), [the max-flow min-cut theorem](/max-flow-min-cut-theorem/) and [bipartite matching](/bipartite-matching/). Do the exercises marked ◦ and • in Chapters 7.1 to 7.6 as you go. That is a complete first unit on graphs. A second unit could add [Hopcroft-Karp](/hopcroft-karp/), [Euler circuits](/hierholzer-algorithm/) and [lowest common ancestors](/lowest-common-ancestor/).

If you already know the basic algorithms, start with the opening page of each chapter. It names the groups of the chapter and the order to read them. The entries marked *Advanced* and *Research* in each chapter are the place to go deeper. Chapters 7.12, 7.13 and 7.14 assume most of the first six.

Each entry stands on its own. Its facts box lists what it needs, with the number of the entry where each prerequisite is explained. Entries in other volumes are cited by number too: [asymptotic notation](/asymptotic-notation/) is in Volume 1 and the [binary heap](/binary-heap/) in Volume 3.

## What you need first

You should be able to read a short program and follow a proof by induction or by contradiction. From Volume 1 you need [asymptotic notation](/asymptotic-notation/), [loop invariants](/loop-invariant/) and, for the randomized algorithms, [linearity of expectation](/linearity-of-expectation/). From Volume 2 you need the [greedy method](/greedy-algorithm/) and, for spanning trees, the [matroid](/matroid/). From Volume 3 you need [queues](/queue/) and [stacks](/stack/) for the searches, [binary heaps](/binary-heap/) and [priority queues](/priority-queue/) for Dijkstra and Prim, and the [disjoint-set](/disjoint-set/) structure for Kruskal. A little linear algebra helps in a few places: matrix products for all-pairs shortest paths, and [eigenvalues](/eigenvalue/) (Volume 12) for the Laplacian and for PageRank.

## The exercises

Each chapter ends with exercises in three bands. Exercises marked ◦ check that you read the entries closely; you should be able to do them in a few minutes. Exercises marked • ask you to use an idea in a new place; each takes some thought, and some need a short program. Exercises marked ★ are harder; some are results from research papers. Hints for many exercises are in the appendix *Hints to the exercises* at the end of the volume.
