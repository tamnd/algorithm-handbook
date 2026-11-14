## What to remember

- The [half-perimeter wirelength](/half-perimeter-wirelength/) of a net is a lower bound on its rectilinear Steiner length and equal to it for two or three pins. The [clique net model](/clique-net-model/) with weight $2/p$ gives a quadratic cost. The [log-sum-exp wirelength](/log-sum-exp-wirelength/) is convex and smooth and satisfies $\mathrm{HPWL} \le \mathrm{LSE} \le \mathrm{HPWL} + 4\gamma \ln p$.
- Balanced partitioning is NP-hard. The Laplacian gives the lower bounds $n\lambda_2/4$ on the bisection width and $\lambda_2/n$ on the [ratio cut](/ratio-cut/). [Spectral partitioning](/spectral-partitioning/) rounds the Fiedler vector. It has no approximation ratio, and the bounds can be far below the optimum.
- [Multilevel partitioning](/multilevel-graph-partitioning/) coarsens by matchings, partitions the small graph and refines with [Fiduccia-Mattheyses](/fiduccia-mattheyses/) on the way back. Projection keeps the cut and the weights exactly, but the method has no approximation ratio. [hMETIS](/multilevel-hypergraph-partitioning/) does the same on the hypergraph.
- [Rent's rule](/rents-rule/) $T = t g^p$ is a measured law. Landman and Russo found exponents between 0.57 and 0.75 for logic.
- A [slicing floorplan](/slicing-floorplan/) has exactly one [normalized Polish expression](/normalized-polish-expression/). [Stockmeyer's algorithm](/stockmeyer-floorplan-sizing/) adds [shape functions](/shape-function/) up the tree and sizes it optimally in $O(nd)$ time. For general floorplans, choosing orientations is NP-complete.
- [Mosaic floorplans](/mosaic-floorplan/) with $n$ rooms are counted by the [Baxter numbers](/mosaic-floorplan-baxter-theorem/), which grow like $8^n$. Slicing floorplans are counted by the Schröder numbers, which grow like $(3 + 2\sqrt2)^n$. The two counts first differ at five rooms, where the pinwheel and its mirror image are not slicing.
- A [sequence pair](/sequence-pair/) exists for every packing and packs in $O(n \log n)$ time as a weighted longest common subsequence. The [B*-tree](/b-star-tree-floorplan/) and the [O-tree](/o-tree-floorplan/) pack in $O(n)$. Several codes can give the same packing.
- [Quadratic placement](/quadratic-placement/) solves a sparse linear system. When every connected group of cells has a net to a pad, the matrix is positive definite and the minimum is unique. [Abacus](/abacus-legalization/) is exact for a fixed order of the cells in a row. [Independent set matching](/independent-set-matching/) is exact for its set. Everything else in placement, from [annealing](/simulated-annealing-placement/) to [electrostatics](/electrostatics-based-placement/), is measured on benchmarks.

| Method | Model | Time | Guarantee |
|---|---|---|---|
| Spectral bisection | graph, $t$ iterations | $\Theta(t(n + m) + n \log n)$ | lower bound $n\lambda_2/4$; no ratio |
| Multilevel with FM | graph or hypergraph | $O(p(n + m))$ if levels shrink | heuristic, measured |
| Stockmeyer sizing | slicing tree, $d$ shapes per block | $O(nd)$ | optimal area |
| Wong-Liu annealing | Polish expressions | $O(skn^2d)$ | heuristic |
| Sequence pair packing | two permutations | $O(n \log n)$ | exact packing of the pair |
| B*-tree, O-tree packing | ordered tree | $O(n)$ | exact packing of the tree |
| Min-cut placement | hypergraph, $S$ sites | $O(p(n + m + P)\log S)$ | heuristic |
| Quadratic placement | clique or star model, CG | $O(P + E + k(n + E))$ | exact minimum of the quadratic |
| Electrostatic placement | LSE or WA, $M \times M$ grid | $O(k(P + n + M^2 \log M))$ | heuristic, measured |
| Tetris | rows of sites | $O(n \log n + nK)$ | legal if it succeeds |
| Abacus | rows of sites | $O(n \log n + Knk)$ | optimal for the order in a row |
| Independent set matching | sets of $k$ cells | $O(k^3)$ per set | optimal for the set |

: The main methods. $n$ is the number of cells or blocks, $m$ the number of edges, $P$ the number of pins, $E$ the edges of the net model, $K$ the number of rows, $k$ an iteration count or a set size, and $p$ the passes per level or per cut.

## Choosing a method

To partition a netlist, use a multilevel partitioner such as hMETIS or KaHyPar. Use the spectral bound to check how far from optimal a cut might be, and the ratio cut when the parts need not have equal size. To floorplan blocks that must be cut by guillotine lines, anneal over normalized Polish expressions and size with Stockmeyer's algorithm. For general packings of hard blocks, use a B*-tree or a sequence pair; the B*-tree packs faster and has less redundancy.

For cell placement, use an analytical global placer, either quadratic with spreading ([SimPL](/simpl-placement/), [force-directed placement](/force-directed-placement/)) or nonlinear with a density penalty ([analytical placement](/analytical-placement/), electrostatics). Legalize with Abacus, or with [Tetris](/tetris-legalization/) when speed matters more than movement. Then improve with [detailed placement](/detailed-placement/): swaps, reordering and independent set matching. [Min-cut placement](/min-cut-placement/) with [terminal propagation](/terminal-propagation/) still serves for coarse placement and for floorplans with many blocks. When some paths are critical, add net weights or bounds as in [timing-driven placement](/timing-driven-placement/).
