Oil moves through pipelines, trains through a rail network and packets through the internet, and each link has a limit on how much it can carry per hour. The [maximum flow problem](/max-flow-problem/) asks how much can be sent from a source to a sink in all. Its partner, the [minimum cut problem](/min-cut-problem/), asks for the cheapest set of links whose removal separates the two. The [max-flow min-cut theorem](/max-flow-min-cut-theorem/) says the two numbers are always equal, and the proof is an algorithm.

That algorithm is [Ford-Fulkerson](/ford-fulkerson/). Keep a flow, look for a path from source to sink in the [residual graph](/residual-graph/), which contains the spare capacity of each edge and a reverse edge for each unit already sent, and push flow along it. When no path remains, the vertices still reachable from the source form a cut whose capacity equals the flow. With integer capacities each step gains at least one unit, so the flow found is [integral](/integrality-theorem/). This makes flows a tool for counting disjoint paths, matching people to jobs, scheduling aircraft and deciding sports standings. The choice of path decides the speed: shortest paths give [Edmonds-Karp](/edmonds-karp/) in $O(nm^2)$, blocking flows give [Dinic's algorithm](/dinic/) in $O(n^2 m)$, and [push-relabel](/push-relabel/) gives $O(n^3)$.

## What the chapter covers

The chapter is in nine groups, read in order.

1. **Networks, flows and cuts.** [Flow networks](/flow-network/), [flows](/s-t-flow/), [conservation](/flow-conservation/), [cuts](/cut/) and their [capacity](/cut-capacity/), and [flow decomposition](/flow-decomposition/).
2. **Augmenting paths and the max-flow min-cut theorem.** The [residual graph](/residual-graph/), [augmenting paths](/augmenting-path-flow/), [Ford-Fulkerson](/ford-fulkerson/), the [theorem](/max-flow-min-cut-theorem/), its [LP duality](/min-cut-max-flow-duality/) and [integrality](/integrality-theorem/).
3. **Choosing the augmenting path.** [Edmonds-Karp](/edmonds-karp/), the [fattest path](/fattest-augmenting-path/), [capacity scaling](/capacity-scaling/), [level graphs](/level-graph/), [blocking flows](/blocking-flow/), [Dinic](/dinic/) and [MPM](/mpm-algorithm/).
4. **Preflows and push-relabel.** [Preflows](/preflow/), [push-relabel](/push-relabel/), and [parametric](/parametric-max-flow-problem/) and [dynamic](/dynamic-max-flow-problem/) flows.
5. **Modelling with flows.** [Vertex capacities](/vertex-capacities-flow/), [disjoint paths](/edge-disjoint-paths/), [circulations](/circulation-problem/), and applications from [baseball](/baseball-elimination/) to [image segmentation](/image-segmentation-graph-cuts/).
6. **Minimum-cost flow.** The [problem](/min-cost-flow-problem/), [cycle canceling](/cycle-canceling/), [successive shortest paths](/successive-shortest-path/), [network simplex](/network-simplex/), [cost scaling](/cost-scaling/) and [almost-linear flow](/almost-linear-max-flow/).
7. **Global minimum cuts.** [Karger](/karger-min-cut/), [Karger-Stein](/karger-stein/), [Stoer-Wagner](/stoer-wagner/) and [Hao-Orlin](/hao-orlin/).
8. **Cuts between all pairs.** The [Gomory-Hu tree](/gomory-hu-tree/) and [isolating cuts](/isolating-cuts/).
9. **Several commodities.** [Multicommodity flow](/multi-commodity-flow-problem/), [multiway cut](/multiway-cut-problem/), [multicut](/multicut-problem/) and [sparsest cut](/sparsest-cut-problem/).

## A first reading

For a first reading, take these entries in order: [flow network](/flow-network/), [s-t flow](/s-t-flow/), [cut capacity](/cut-capacity/), [residual graph](/residual-graph/), [augmenting path](/augmenting-path-flow/), [Ford-Fulkerson](/ford-fulkerson/), [max-flow min-cut theorem](/max-flow-min-cut-theorem/), [integrality](/integrality-theorem/), [Edmonds-Karp](/edmonds-karp/), [Dinic's algorithm](/dinic/), [edge-disjoint paths](/edge-disjoint-paths/), [circulations with demands](/circulation-problem/), [baseball elimination](/baseball-elimination/) and [Karger's algorithm](/karger-min-cut/). Then [push-relabel](/push-relabel/) and [min-cost flow](/min-cost-flow-problem/) for a second pass.

Two pairs of entries are duplicates. The [integrality theorem](/integrality-theorem/) and the [flow integrality theorem](/flow-integrality-theorem/) state the same result; read the first. The [fattest augmenting path](/fattest-augmenting-path/) and the [maximum-capacity augmenting path](/maximum-capacity-augmenting-path/) describe the same rule of Edmonds and Karp; read either.

## Before you start

From Chapter 7.2 you need [breadth-first search](/breadth-first-search/) and its [layers](/bfs-layers/), which become the level graph. From Chapter 7.3 you need [Bellman-Ford](/bellman-ford/), [Dijkstra's algorithm](/dijkstra/) and [potentials](/potential-function-reduced-costs/) for the minimum-cost group. From Volume 2 the [greedy method](/greedy-algorithm/) shows by contrast why reverse edges are needed. Linear programming duality helps with group 2 and group 9, but the chapter proves what it uses by flows.
