This chapter collects the algorithms for targets other than standard-cell logic. On a field-programmable gate array the lookup tables, logic clusters and routing switches are fixed in silicon, and a design is mapped into lookup tables, packed into clusters, placed and routed on that fixed fabric. Channel widths are fixed, so routability is a hard limit. Analog circuits have few devices, but each is sized to continuous specifications such as gain and noise, and matched devices are laid out in symmetric patterns. Three-dimensional chips stack tiers of devices joined by through-silicon vias. Reversible circuits need synthesis from reversible gates, and a quantum device needs a placement of qubits that respects which pairs can interact.

Exact results are few and specific. FlowMap maps a $K$-bounded network into $K$-input lookup tables with the least depth in polynomial time, and CutMap and DAOmap keep that depth while reducing area by heuristics. Geometric programming finds the global optimum of a sizing problem whose specifications are written as posynomials, an optimum of the model, not of the circuit. Packing, placement, routing, 3D partitioning and qubit mapping are done by heuristics such as annealing, negotiated congestion and lookahead search, judged on benchmarks.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **FPGA architecture.** The island-style FPGA, the logic cluster, switch blocks and the universal switch block, the routing resource graph and the minimum channel width.
2. **FPGA mapping, packing, placement and routing.** The Chortle-crf, CutMap and DAOmap mappers; packing by T-VPack and AAPack; timing-driven annealing placement and HeAP; and SAT-based detailed routing.
3. **Analog sizing and analysis.** Analog circuit sizing by annealing and by geometric programming, symbolic and approximate symbolic analysis, determinant decision diagrams and the Pelgrom mismatch model.
4. **Analog layout.** Symmetry constraints, symmetric-feasible sequence pairs, the ASF-B*-tree and common-centroid layout.
5. **Three-dimensional ICs.** Stacked chips and through-silicon vias, tier partitioning, thermal-driven 3D floorplanning and the Shrunk-2D flow.
6. **Reversible and quantum circuits.** Reversible logic synthesis and its transformation-based method, qubit mapping and the SABRE mapper.

## What to read meanwhile

For FPGAs, the chapter on logic synthesis has [LUT mapping](/lut-mapping/), [k-feasible cuts](/k-feasible-cut/), [FlowMap](/flowmap/) and [priority cuts](/priority-cuts/), and the routing chapter has [negotiated congestion routing](/negotiated-congestion-routing/), the PathFinder router, which works on the routing resource graph of an FPGA. FPGA placers specialize [simulated annealing placement](/simulated-annealing-placement/) and [quadratic placement](/quadratic-placement/), and analog placement extends the [sequence pair](/sequence-pair/) and the [B*-tree](/b-star-tree-floorplan/).

For analog sizing, read [TILOS](/tilos/), where delay is a posynomial, [asymptotic waveform evaluation](/asymptotic-waveform-evaluation/), the fast analysis inside annealing-based sizing, and [geometric programming](/geometric-programming/) (Volume 15). For reversible and quantum circuits, read the [quantum circuit model](/quantum-circuit-model/), [reversible computation](/reversible-computation/) and the [Toffoli gate](/toffoli-gate/) in Volume 30, and [exact synthesis](/exact-synthesis/) in this volume.
