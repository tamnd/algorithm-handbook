A placed and routed chip is not done. Three checks remain, and each has its own algorithms. Timing: every signal must settle before the next clock edge, at every register, at every corner of the process. Layout: the shapes must be wide enough and far enough apart to print, and they must wire up the transistors of the schematic and nothing else. Test: once the wafers come back, a dust particle may have shorted a wire to ground, and the tester has a short time per die to find out. This chapter covers the timing analysis, the physical verification and the manufacturing test that answer them.

The numbers are small and the counts are huge. A wire 100 µm long and 0.1 µm wide, with a sheet resistance of 0.08 Ω per square, has 80 Ω of resistance. At 0.2 µm above a ground plane in oxide, the parallel plate formula gives about 1.7 fF, and the side fields make the real value larger. Its RC product is about 0.14 ps. A chip has millions of such wires and tens of millions of timing paths. So the methods here trade exactness for speed in stated ways. The [Elmore delay](/elmore-delay/) is a model, an upper bound on the 50 percent delay of an RC tree and not the exact delay. [Static timing analysis](/static-timing-analysis/) runs in linear time without input vectors, but it is conservative: it counts [false paths](/false-path/) that no input can exercise. Deciding whether a stuck-at fault can be detected at all is NP-complete, and test generators still finish on real circuits by search, learning and good guesses. The entries say each time what is proved and what is only measured.

## What the chapter covers

1. **Interconnect delay.** The [RC tree](/rc-tree/) as the model of a net, the [Elmore delay](/elmore-delay/) as its first moment, and the higher-order models of [asymptotic waveform evaluation](/asymptotic-waveform-evaluation/) and [PRIMA](/prima/).
2. **Static timing analysis.** The [timing graph](/timing-graph/), [arrival and required times](/arrival-and-required-time/), [setup and hold constraints](/setup-and-hold-constraints/), table-based cell delays in the [nonlinear delay model](/nonlinear-delay-model/), [static timing analysis](/static-timing-analysis/) itself, [false paths](/false-path/) and [statistical timing](/statistical-static-timing-analysis/).
3. **Clock networks.** The [H-tree](/h-tree-clock/), [clock tree synthesis](/clock-tree-synthesis/) with [means and medians](/method-of-means-and-medians/), [Tsay's zero-skew merge](/tsay-zero-skew/) and [deferred-merge embedding](/deferred-merge-embedding/), and [clock skew scheduling](/clock-skew-scheduling/), which uses skew on purpose.
4. **Buffering and sizing.** [Logical effort](/logical-effort/), [van Ginneken's buffer insertion](/van-ginneken-buffer-insertion/), and [gate sizing](/gate-sizing/) by [TILOS](/tilos/) and by [Lagrangian relaxation](/lagrangian-relaxation-gate-sizing/).
5. **Physical verification.** [Circuit extraction](/circuit-extraction/), the [corner-stitched](/corner-stitching/) layout database, [design rule checking](/design-rule-checking/), and [layout versus schematic](/layout-versus-schematic/) with the [Gemini](/gemini-netlist-comparison/) algorithm.
6. **Extraction and manufacturability.** [Parasitic extraction](/parasitic-extraction/), the [floating random walk](/floating-random-walk-capacitance/) for capacitance, [multiple patterning](/multiple-patterning-decomposition/) and [optical proximity correction](/optical-proximity-correction/).
7. **Faults and test generation.** The [stuck-at fault model](/stuck-at-fault-model/), [fault collapsing](/fault-collapsing/), [test generation](/automatic-test-pattern-generation/) by the [D-algorithm](/d-algorithm/), [PODEM](/podem/) and [SAT](/sat-based-atpg/), and the [SCOAP](/scoap/) testability measures.
8. **Fault simulation and design for test.** [Fault simulation](/fault-simulation/), [concurrent fault simulation](/concurrent-fault-simulation/), [scan design](/scan-design/) and [built-in self-test](/built-in-self-test/).

## A first reading

Read these in order:

1. [RC tree](/rc-tree/)
2. [Elmore delay](/elmore-delay/)
3. [Timing graph](/timing-graph/)
4. [Arrival and required time](/arrival-and-required-time/)
5. [Setup and hold constraints](/setup-and-hold-constraints/)
6. [Static timing analysis](/static-timing-analysis/)
7. [False path](/false-path/)
8. [Tsay zero skew](/tsay-zero-skew/)
9. [Van Ginneken buffer insertion](/van-ginneken-buffer-insertion/)
10. [Design rule checking](/design-rule-checking/)
11. [Layout versus schematic](/layout-versus-schematic/)
12. [Stuck-at fault model](/stuck-at-fault-model/)
13. [PODEM](/podem/)
14. [Fault simulation](/fault-simulation/)
15. [Scan design](/scan-design/)

The moment-matching models, statistical timing, corner stitching, the floating random walk and the two lithography entries can wait. So can the D-algorithm, which PODEM and SAT-based ATPG replaced in practice, though it is the clearest place to learn the five-valued logic.

## Before you start

Timing analysis is longest paths in a [directed acyclic graph](/directed-acyclic-graph/), computed in [topological order](/topological-sort/) as in [DAG longest path](/dag-longest-path/) (Volume 7). Clock skew scheduling is a system of [difference constraints](/difference-constraints/), solved with [Bellman-Ford](/bellman-ford/) and cycle ratios as in [Karp's minimum mean cycle](/karp-minimum-mean-cycle/) (Volume 7). Multiple patterning is [graph coloring](/graph-coloring/) and [bipartiteness testing](/bipartiteness-testing/), and LVS is the [graph isomorphism problem](/graph-isomorphism-problem/) with refinement as in [Weisfeiler-Leman](/weisfeiler-leman/), all in Volume 7.

The delay models use the [impulse response](/impulse-response/) and [transfer function](/transfer-function/) of Volume 28, and the reduced models use [Padé approximation](/pade-approximation/), the [Krylov subspace](/krylov-subspace/) and the [Arnoldi iteration](/arnoldi-iteration/) of Volume 12. Table lookup uses [bilinear interpolation](/bilinear-interpolation/) and the random walk [Monte Carlo integration](/monte-carlo-integration/), also in Volume 12. Sizing is [geometric programming](/geometric-programming/) and [Lagrangian relaxation](/lagrangian-relaxation/) (Volume 15), and buffering is [dynamic programming on trees](/tree-dynamic-programming/) (Volume 2).

For test, you need [Boolean circuits](/boolean-circuit/) (Volume 1), [SAT](/sat/) and the [Tseitin transformation](/tseitin-transformation/) (Volume 16), [set cover](/set-cover/) (Volume 18), and the [linear feedback shift register](/linear-feedback-shift-register/) (Volume 12) with [GF(2) polynomial arithmetic](/gf2-polynomial-arithmetic/) (Volume 24). Basic circuit facts are assumed: a CMOS gate charges its load through a resistance, and a register samples its input at a clock edge.
