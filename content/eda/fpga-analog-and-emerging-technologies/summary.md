## What to remember

- In an [island-style FPGA](/island-style-fpga/) the tracks, clusters and switches are fixed. A [universal switch block](/universal-switch-block/) with $6W$ switches routes every requirement with at most $W$ nets per side, no block with fewer does, and the planar pattern with the same count fails on some. The [minimum channel width](/minimum-channel-width/) found by a heuristic router is only an upper bound.
- [CutMap](/cutmap/) and [DAOmap](/daomap/) keep FlowMap's optimal depth, which is proved, and save area by cost rules, which is measured. [Chortle-crf](/chortle-crf/) is stated to use the fewest tables on fanout-free trees for $K \le 5$ and is a heuristic on networks with fanout.
- [FPGA packing](/fpga-packing/) is NP-complete for $N = 3$ and a maximum matching for $N = 2$. [T-VPack](/t-vpack/) and [AAPack](/aapack/) are greedy and can miss the optimum.
- FPGA placers and routers, [annealing](/fpga-timing-driven-annealing-placement/) and [HeAP](/heap-fpga-placement/) among them, are judged by measured results. [SAT-based routing](/sat-based-fpga-routing/) is exact only for one global routing at one width.
- Mismatch follows $\sigma^2(\Delta P) = A_P^2/(WL) + S_P^2 D^2$ ([Pelgrom](/pelgrom-mismatch-model/)), so halving $\sigma$ costs four times the area. [Geometric programming](/geometric-programming-circuit-sizing/) gives the global optimum of a posynomial model, which is only as good as the model; [annealing](/annealing-analog-sizing/) has no optimality proof.
- The terms of a symbolic transfer function grow like Fibonacci numbers for a ladder. [Determinant decision diagrams](/determinant-decision-diagram/) share the minors and are canonical for a fixed entry order; [approximate symbolic analysis](/approximate-symbolic-analysis/) bounds its error only at the nominal point.
- A [common-centroid layout](/common-centroid-layout/) cancels every linear gradient exactly when the centroids coincide. [Symmetric-feasible sequence pairs](/symmetric-feasible-sequence-pair/) and the [ASF-B*-tree](/asf-b-star-tree/) give symmetric packings by construction; the plain ASF-B*-tree packing need not be one connected island.
- [Tier partitioning](/tier-partitioning/) is NP-hard for two tiers. Two tiers shrink planar distances by at most $1/\sqrt{2}$, the 29.3% bound of [Shrunk-2D](/shrunk-2d/), and heat is the main cost of stacking.
- Every 3-bit function has an optimal [reversible circuit](/reversible-logic-synthesis/) of at most 8 NCT gates; the [transformation-based method](/transformation-based-reversible-synthesis/) uses at most $(n-1)2^n + 1$. [Qubit mapping](/qubit-mapping/) is NP-complete, and [SABRE](/sabre-qubit-mapping/) is a measured heuristic.

| Method | Problem | Time | Guarantee |
|---|---|---|---|
| Chortle-crf | LUT mapping | $O(m \log m)$ with heaps | fewest LUTs on trees, $K \le 5$ (cited) |
| CutMap, DAOmap | LUT mapping | cut enumeration | optimal depth; area measured |
| T-VPack | packing | $O(n^2 N K)$ | legal clusters; count measured |
| AAPack | packing | $O(n^2 N R)$ | legal by an inner route; measured |
| Annealing placement | FPGA placement | $O(n^{4/3} F + P)$ per temperature | none; measured |
| HeAP | FPGA placement | $O(t(n + Q) + S \log^2 S)$ per iteration | none; measured |
| SAT-based routing | detailed routing | exponential worst case | exact for one global routing |
| Geometric programming | sizing | polynomial (interior point) | global optimum of the model |
| DDD | symbolic determinant | $O(nM)$ build, $O(V)$ evaluate | exact, canonical for the order |
| Symmetric-feasible SP | symmetric placement | $O(n)$ test, $O(n^2)$ pack | every packing symmetric |
| ASF-B*-tree | symmetric placement | $O(n)$ pack | every packing symmetric |
| Shrunk-2D | tier partitioning | $O(Pp + B)$ split | balanced per bin; power measured |
| Transformation-based | reversible synthesis | $O(n 4^n)$ | at most $(n-1)2^n + 1$ gates |
| SABRE | qubit mapping | $O(g(l + N) N D (N + e))$ per pass | valid output; SWAPs measured |

: Main methods. The letters are those of each entry; $n$ counts BLEs, cells or lines, and $N$ the cluster size or the physical qubits.

## Choosing a method

For an FPGA, map with DAOmap or the priority cuts of Chapter 32.2, pack with AAPack for architectures with modes or sparse local routing and T-VPack for the classic cluster, place with annealing for quality or HeAP for speed, and route with negotiated congestion. Use SAT-based routing to prove that a global routing cannot be completed at a width, and compare channel widths only for one router.

For sizing, use geometric programming when the square-law model is good enough, and check the optimum by simulation; anneal when the specifications need a simulator. Size matched devices from the Pelgrom constants first. For layout, use common centroid for devices made of unit cells, and symmetric-feasible sequence pairs or the ASF-B*-tree for mirror symmetry, the tree when each group should stay together.

For 3D, partition blocks with the floorplan when the vias are TSVs, and gates after a 2D placement, as in Shrunk-2D, when they are monolithic. Synthesize reversible functions of 3 bits exactly and larger ones by transformation and templates. Map qubits with SABRE, and exactly on small devices.
