Electronic design automation, or EDA, is the set of programs that turn a description of a chip into the masks that a factory prints. A designer writes what the chip should compute. Programs then choose the gates, give each gate a place on the die, draw the wires, check that every signal arrives in time, check that the layout matches the circuit, and generate the tests that sort good dies from bad ones. A modern chip has billions of transistors, so none of these steps can be done by hand, and each one is an algorithm problem with its own models and its own limits.

This volume follows that flow. It starts with synthesis, from a behaviour to a register-transfer design and from there to a network of gates. Then come simulation and verification, which check the design before it is built. Then the physical steps: partitioning, floorplanning and placement, then routing. Then timing, physical verification and test, and the effects that can still break a correct design: power, noise, wear and yield. The last chapter turns to targets other than standard cells, such as programmable logic and analog circuits.

## Why electronic design automation gets a volume of its own

The problems of chip design are classical problems at a very large size, and almost all of them are NP-hard. So the subject is a long lesson in what can still be done exactly, and in how to say plainly what is only measured. In this volume you will meet:

- **Exact answers on a restricted form.** [FlowMap](/flowmap/) maps a network into $K$-input lookup tables with the least depth for the given structure, while the least number of tables is NP-hard. The [left-edge algorithm](/left-edge-algorithm/) routes a channel in as many tracks as its [channel density](/channel-density/) when no net must lie above another. [Tree covering](/tree-covering-technology-mapping/) is optimal for each tree, not for the whole network.
- **Boolean reasoning at scale.** The [and-inverter graph](/and-inverter-graph/) is the common form of logic in synthesis tools, and [SAT sweeping](/sat-sweeping/) finds its equivalent nodes with a [SAT](/sat/) solver. The same idea, a circuit and its copy joined at the outputs, gives [SAT-based test generation](/sat-based-atpg/).
- **Graphs and linear programs.** A netlist is a [hypergraph](/hypergraph/). Timing is longest paths in a DAG, so [static timing analysis](/static-timing-analysis/) runs in linear time. [Retiming](/retiming/) and [clock skew scheduling](/clock-skew-scheduling/) are systems of [difference constraints](/difference-constraints/), and [minimum-area retiming](/minimum-area-retiming/) is the dual of a min-cost flow.
- **Models that are not the truth.** The [half-perimeter wirelength](/half-perimeter-wirelength/) estimates the routed length of a net, and the [Elmore delay](/elmore-delay/) is an upper bound on the 50 percent delay of an RC tree, not the delay itself. [Rent's rule](/rents-rule/) is an empirical law. Each entry says which model it uses.
- **Heuristics judged on benchmarks.** [Espresso](/espresso/), [simulated annealing placement](/simulated-annealing-placement/), [multilevel hypergraph partitioning](/multilevel-hypergraph-partitioning/) and [negotiated congestion routing](/negotiated-congestion-routing/) carry no proof of how close they come to the optimum. Their value is measured on standard circuits.

## The chapters

Four chapters are written in this edition: 32.2, 32.5, 32.6 and 32.7. The other six are not written yet. Each of them has an opening page that lists what it will cover and points to the written entries you can read meanwhile.

**Chapter 32.1, High-level synthesis and scheduling**, is not written yet. It will cover control data flow graphs, scheduling, allocation and binding, and the synthesis of controllers. Until then, read [high-level synthesis](/high-level-synthesis/), [ASAP and ALAP scheduling](/asap-alap-scheduling/) and [force-directed scheduling](/force-directed-scheduling/), which sit in Chapter 32.2.

**Chapter 32.2, Logic synthesis and technology mapping**, is written. It starts with [two-level minimization](/two-level-logic-minimization/): [prime implicants](/prime-implicant/), the exact [Quine-McCluskey method](/quine-mccluskey/) and the heuristic Espresso. It goes on to [multi-level synthesis](/multi-level-logic-synthesis/) with [algebraic kernels](/algebraic-kernel/), to [technology mapping](/technology-mapping/) with [k-feasible cuts](/k-feasible-cut/), and to and-inverter graphs, [state assignment](/state-assignment/) and retiming.

**Chapter 32.3, Logic and circuit simulation**, is not written yet. It will cover event-driven logic simulation and circuit simulation in the line of SPICE: modified nodal analysis, Newton's method and implicit integration of stiff equations.

**Chapter 32.4, Hardware verification**, is not written yet. It will cover stimulus generation and coverage, assertions, combinational and sequential equivalence checking, symbolic simulation and the verification of arithmetic circuits. Meanwhile, [Boolean equivalence checking](/boolean-equivalence-checking/) and [binary decision diagrams](/binary-decision-diagram/) in Volume 16, and SAT sweeping in Chapter 32.2, give the core methods.

**Chapter 32.5, Partitioning, floorplanning and placement**, is written. It cuts the netlist with [hypergraph partitioning](/hypergraph-partitioning/), shapes the floorplan with the [slicing floorplan](/slicing-floorplan/), the [sequence pair](/sequence-pair/) and the [B*-tree](/b-star-tree-floorplan/), and places cells by [min-cut](/min-cut-placement/), [quadratic](/quadratic-placement/) and [electrostatics-based placement](/electrostatics-based-placement/), followed by [legalization](/placement-legalization/).

**Chapter 32.6, Routing**, is written. It joins two pins by [Lee's maze router](/lee-maze-routing/), which finds a shortest path when one exists, and many pins by trees close to the rectilinear Steiner tree, with [Hanan's theorem](/hanan-theorem/) and [Hwang's 3/2 ratio](/hwang-rectilinear-steiner-ratio/). It covers [global routing](/global-routing/), [rip-up and reroute](/rip-up-and-reroute/) and the [channel routing problem](/channel-routing-problem/).

**Chapter 32.7, Timing, verification and test**, is written. It covers the [RC tree](/rc-tree/), static timing analysis with [false paths](/false-path/), [clock tree synthesis](/clock-tree-synthesis/), [gate sizing](/gate-sizing/) and [buffer insertion](/van-ginneken-buffer-insertion/). It checks layouts by [design rule checking](/design-rule-checking/) and [layout versus schematic](/layout-versus-schematic/), and tests chips with the [stuck-at fault model](/stuck-at-fault-model/), [PODEM](/podem/) and [scan design](/scan-design/).

**Chapter 32.8, Power, reliability and manufacturability**, is not written yet. It will cover power estimation and reduction, power grids and noise, electromigration and aging, yield models and lithography.

**Chapter 32.9, Test and diagnosis**, is not written yet. It extends the test entries of Chapter 32.7 with delay faults, faster test generation and fault simulation, test compression, memory test and diagnosis.

**Chapter 32.10, FPGA, analog and emerging technologies**, is not written yet. It will cover the mapping, packing, placement and routing of field-programmable gate arrays, analog sizing and layout, three-dimensional chips, and reversible and quantum circuits. For FPGAs, [LUT mapping](/lut-mapping/) and [priority cuts](/priority-cuts/) in Chapter 32.2 are the place to start.

## How to read this volume

If this is your first course, read these entries in order. From Chapter 32.2: [sum of products](/sum-of-products/), prime implicants, the Quine-McCluskey method, Espresso, the and-inverter graph, k-feasible cuts, FlowMap and retiming. From Chapter 32.5: the half-perimeter wirelength, hypergraph partitioning and quadratic placement. From Chapter 32.6: Lee's maze router, the left-edge algorithm and Hanan's theorem. From Chapter 32.7: the [timing graph](/timing-graph/), static timing analysis, the Elmore delay, the stuck-at fault model and PODEM. Do the exercises marked ◦ and • at the end of these chapters. That is a first pass through the whole flow, from logic to test.

If you already know the flow, start with the opening page of a chapter. It names the families of methods and says which results are exact, which are bounds and which are measured. The entries marked *Advanced* and *Research* go deeper.

Each entry stands on its own. Its facts box lists what it needs, with the number of the entry where each prerequisite is explained. Entries in other volumes are cited by number too.

## What you need first

You should be able to read a short program and follow a proof by induction, and you should know what it means for a problem to be NP-hard. From Volume 1 you need [asymptotic notation](/asymptotic-notation/) and [Boolean circuits](/boolean-circuit/). From Volume 7 you need [directed acyclic graphs](/directed-acyclic-graph/), [topological sort](/topological-sort/), [breadth-first search](/breadth-first-search/), [minimum spanning trees](/minimum-spanning-tree/) and the [max-flow problem](/max-flow-problem/). From Volume 16 you need [Boolean functions](/boolean-function/) and SAT. From Volume 15 the [linear programming problem](/linear-programming-problem/), [simulated annealing](/simulated-annealing/) and the [Kernighan-Lin](/kernighan-lin/) method help with the physical chapters. No knowledge of electronics is assumed beyond the idea of a gate and a wire; the entries define the circuit models they use.

## The exercises

Each chapter ends with exercises in three bands. Exercises marked ◦ check that you read the entries closely; you should be able to do them in a few minutes. Exercises marked • ask you to use an idea in a new place; each takes some thought, and some need a short program. Exercises marked ★ are harder; some are results from research papers. Hints for many exercises are in the appendix *Hints to the exercises* at the end of the volume.
