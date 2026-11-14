High-level synthesis starts from a description of what a circuit computes, such as a loop written in C, and builds a register-transfer design: a datapath of functional units, registers and multiplexers, and a controller, a finite state machine that tells the datapath what to do in each clock step. Choices such as how many multipliers to build and how many clock steps a loop body takes set the area and the speed of the design before any gate exists.

The work splits into scheduling, which puts each operation into a control step, allocation, which chooses the units, and binding, which assigns operations to units and values to registers. Scheduling under unit limits is NP-hard in general, so integer programs solve small graphs exactly and heuristics are judged by their schedules on benchmarks. Some parts are solved exactly: with unlimited units the critical path gives the least latency, and for straight-line code with a fixed schedule the fewest registers equals the largest number of values live in one step.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Models of behaviour.** The control data flow graph, the finite state machine with datapath, synchronous dataflow and its static schedules, Kahn process networks and latency-insensitive design.
2. **Scheduling.** Resource-constrained and latency-constrained scheduling, the integer programming formulation, path-based scheduling, operation chaining, speculative code motion, and SDC-based scheduling with its modulo form for pipelined loops.
3. **Allocation and binding.** Module selection, the resource compatibility graph, resource, register and interconnect binding, Tseng and Siewiorek's clique partitioning, and binding by weighted bipartite matching.
4. **Transformations of dataflow graphs.** The iteration bound of a recursive graph, and the folding and unfolding transformations that trade hardware for throughput.
5. **Controller synthesis.** KISS symbolic minimization, the NOVA and MUSTANG state encoders, partition pairs and FSM decomposition.
6. **Widths, memories and interfaces.** Bitwidth analysis, memory partitioning, interface synthesis and hardware-software partitioning.

## What to read meanwhile

The problem is defined in [high-level synthesis](/high-level-synthesis/), and [ASAP and ALAP scheduling](/asap-alap-scheduling/) and [force-directed scheduling](/force-directed-scheduling/) solve its first step. The chapter on logic synthesis, where these sit, also has [state assignment](/state-assignment/), [incompletely specified FSM minimization](/incompletely-specified-fsm-minimization/) and [retiming](/retiming/), which with unfolding reaches the iteration bound. Register binding for straight-line code is solved by the [left-edge algorithm](/left-edge-algorithm/) of the routing chapter and by [interval partitioning](/interval-partitioning/) (Volume 2).

Scheduling theory is in Volume 18: [precedence-constrained scheduling](/precedence-constrained-scheduling/), [list scheduling](/list-scheduling/) with its [$(2 - 1/m)$ bound](/list-scheduling-bound/), and [Hu's algorithm](/hu-algorithm/). Binding uses [graph coloring](/graph-coloring/), [cliques](/clique/) and [bipartite matching](/bipartite-matching/) from Volume 7, and SDC scheduling uses [difference constraints](/difference-constraints/) from the same volume. Volume 15 has [0-1 integer programming](/binary-integer-programming/) and [total unimodularity](/total-unimodularity/), the reason SDC schedules come out integral. Controllers are [Mealy machines](/mealy-machine/) (Volume 9).
