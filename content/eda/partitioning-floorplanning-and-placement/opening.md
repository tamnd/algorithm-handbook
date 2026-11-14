A modern chip holds a few hundred large blocks, such as memories and processor cores, and several million standard cells, the small gates of the logic. Before any wire is drawn, every block and every cell needs a place. Partitioning cuts the netlist into parts with few wires between them. [Floorplanning](/floorplanning/) gives each large block a rectangle on the die. [Placement](/placement-problem/) puts the cells into rows of fixed height so that no two overlap and the wires are short. Routing and timing come later in the volume, and both depend on how good the placement is: a wire that is long here stays long.

Almost every problem in the chapter is NP-hard. Balanced bisection, rectangle packing, floorplan sizing for general floorplans and the best ordering of cells in a single row all are. So the pages separate three kinds of result. Some are exact and proved. The [half-perimeter wirelength](/half-perimeter-wirelength/) equals the rectilinear Steiner length for two or three pins. [Stockmeyer's algorithm](/stockmeyer-floorplan-sizing/) sizes a slicing floorplan optimally. A [sequence pair](/sequence-pair/) exists for every packing. [Abacus](/abacus-legalization/) places a row optimally for a fixed order of cells. Some are bounds: the second Laplacian eigenvalue bounds the bisection width and the ratio cut from below, and the [log-sum-exp model](/log-sum-exp-wirelength/) lies within $4\gamma \ln p$ of the half perimeter. The rest are measured. [Kernighan-Lin](/kernighan-lin/), [Fiduccia-Mattheyses](/fiduccia-mattheyses/), the [multilevel partitioners](/multilevel-graph-partitioning/), [annealing](/simulated-annealing-placement/), and [analytical](/analytical-placement/) and [force-directed placement](/force-directed-placement/) are heuristics with no approximation ratio, and their quality comes from benchmarks. [Rent's rule](/rents-rule/) is itself an empirical law.

## What the chapter covers

1. **Wirelength and net models.** The half-perimeter wirelength, the [clique net model](/clique-net-model/) and the [log-sum-exp wirelength](/log-sum-exp-wirelength/).
2. **Netlist partitioning.** [Hypergraph partitioning](/hypergraph-partitioning/), the [ratio cut](/ratio-cut/), Rent's rule, [spectral partitioning](/spectral-partitioning/), [multilevel graph partitioning](/multilevel-graph-partitioning/) and [multilevel hypergraph partitioning](/multilevel-hypergraph-partitioning/).
3. **Floorplans and their structure.** [Floorplanning](/floorplanning/), the [horizontal and vertical constraint graphs](/floorplan-constraint-graphs/), the [slicing floorplan](/slicing-floorplan/), the [mosaic floorplan](/mosaic-floorplan/) and [mosaic floorplans and Baxter numbers](/mosaic-floorplan-baxter-theorem/).
4. **Slicing floorplans.** The [normalized Polish expression](/normalized-polish-expression/), the [shape function](/shape-function/), Stockmeyer's floorplan sizing and [Wong-Liu floorplanning](/wong-liu-floorplanning/).
5. **Packing representations.** The sequence pair, the [B*-tree](/b-star-tree-floorplan/) and the [O-tree](/o-tree-floorplan/).
6. **The placement problem.** [Placement](/placement-problem/), [placement legalization](/placement-legalization/) and [detailed placement](/detailed-placement/).
7. **Min-cut and annealing placement.** [Min-cut placement](/min-cut-placement/), [terminal propagation](/terminal-propagation/) and [simulated annealing placement](/simulated-annealing-placement/).
8. **Analytical global placement.** [Quadratic placement](/quadratic-placement/), [force-directed placement](/force-directed-placement/), [analytical placement](/analytical-placement/), [electrostatics-based placement](/electrostatics-based-placement/) and [SimPL](/simpl-placement/).
9. **Legalization, detailed placement and timing.** [Tetris legalization](/tetris-legalization/), [Abacus legalization](/abacus-legalization/), [independent set matching](/independent-set-matching/) and [timing-driven placement](/timing-driven-placement/).

## A first reading

Read these in order:

1. [Half-perimeter wirelength](/half-perimeter-wirelength/)
2. [Hypergraph partitioning](/hypergraph-partitioning/)
3. [Spectral partitioning](/spectral-partitioning/)
4. [Multilevel graph partitioning](/multilevel-graph-partitioning/)
5. [Floorplanning](/floorplanning/) and [constraint graphs](/floorplan-constraint-graphs/)
6. [Slicing floorplan](/slicing-floorplan/)
7. [Normalized Polish expression](/normalized-polish-expression/)
8. [Stockmeyer's floorplan sizing](/stockmeyer-floorplan-sizing/)
9. [Sequence pair](/sequence-pair/)
10. [Placement](/placement-problem/)
11. [Quadratic placement](/quadratic-placement/)
12. [Placement legalization](/placement-legalization/)
13. [Abacus legalization](/abacus-legalization/)
14. [Detailed placement](/detailed-placement/)

Skip at first the Baxter numbers, the O-tree, electrostatics-based placement and SimPL. They refine the core and read more easily after it. Terminal propagation needs min-cut placement, and Wong-Liu floorplanning needs both the Polish expressions and annealing.

## Before you start

The partitioning entries build on the [graph partitioning problem](/graph-partitioning-problem/), [Kernighan-Lin](/kernighan-lin/) and [Fiduccia-Mattheyses](/fiduccia-mattheyses/) in the optimization volume, and on the [Laplacian matrix](/laplacian-matrix/), [maximal matching](/maximal-matching/) and the [hypergraph](/hypergraph/) in the graphs volume. The floorplanning entries use [longest paths in a DAG](/dag-longest-path/), the [binary tree](/binary-tree/), [reverse Polish notation](/reverse-polish-notation/) and the [longest common subsequence](/longest-common-subsequence/). The approximation volume treats [rectangle packing](/rectangle-packing/) and the [guillotine cut technique](/guillotine-cut-technique/) as problems in their own right. [Simulated annealing](/simulated-annealing/) with the [Metropolis criterion](/metropolis-criterion/) and the [cooling schedule](/cooling-schedule/) is defined once in the optimization volume and used here in three places. Analytical placement needs the [conjugate gradient method](/conjugate-gradient-method/), the [Poisson equation](/poisson-equation/), the [log-sum-exp trick](/log-sum-exp-trick/) and [Nesterov's accelerated gradient](/nesterov-accelerated-gradient/). Legalization uses [pool adjacent violators](/pool-adjacent-violators/) and the [Hungarian algorithm](/hungarian-algorithm/). The [rectilinear Steiner tree problem](/rectilinear-steiner-tree-problem/) explains what the half perimeter estimates, and [static timing analysis](/static-timing-analysis/) in the timing chapter supplies the slacks that timing-driven placement uses.
