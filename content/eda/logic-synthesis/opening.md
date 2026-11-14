Logic synthesis turns a description of what a circuit computes into a network of gates that a chip or an FPGA can hold. The input may be a truth table, a set of Boolean equations, a finite state machine or a data flow graph. The output is a netlist of library cells or lookup tables, and the aim is a small, fast circuit with exactly the same behaviour. A full adder shows the range of choices. Written as a minimum sum of products, its sum output needs four cubes of three literals. As an [and-inverter graph](/and-inverter-graph/), the sum and the carry together take 7 AND nodes, because the carry reuses two nodes of the sum. As a [majority-inverter graph](/majority-inverter-graph/) they take 3 nodes. Each form suits a different step of the flow.

Most problems in this chapter are hard. Choosing a minimum [sum of products](/sum-of-products/) is NP-complete from a truth table, mapping a network onto the fewest lookup tables is NP-hard, and minimizing an incompletely specified state machine is NP-hard. So the chapter keeps four kinds of result apart. Some methods are exact and fast on their own terms: [tree covering](/tree-covering-technology-mapping/) is optimal on each tree, [FlowMap](/flowmap/) finds a lookup table mapping of least depth in polynomial time, and [retiming](/retiming/) finds the least clock period over all legal register moves. Some are exact and exponential, such as [Petrick's method](/petricks-method/) and [exact synthesis](/exact-synthesis/). Some keep the function and lower a cost without any bound on the distance to the optimum, such as [Espresso](/espresso/), [kernel extraction](/kernel-extraction/) and [AIG rewriting](/aig-rewriting/). And the claims about how well these heuristics do come from measurements on benchmark circuits, not from proofs.

The chapter follows the usual flow. Two-level methods come first, since they give the vocabulary of cubes, primes and covers. Multi-level networks, technology mapping and and-inverter graphs follow. The chapter ends with sequential circuits and with the scheduling steps of high-level synthesis.

## What the chapter covers

1. **Two-level forms and cubes.** [Sum of products](/sum-of-products/), [implicants](/implicant/), [don't-cares](/dont-care-condition/), [prime implicants](/prime-implicant/) and [unate functions](/unate-function/).
2. **Exact two-level minimization.** The [problem](/two-level-logic-minimization/), the [Karnaugh map](/karnaugh-map/), [Quine-McCluskey](/quine-mccluskey/) and Petrick's method for the covering table.
3. **Heuristic two-level minimization.** The [unate recursive paradigm](/unate-recursive-paradigm/) and Espresso, which gives a cover of primes with no redundant cube.
4. **Multi-level networks and algebraic methods.** [Boolean networks](/boolean-network/), [multi-level synthesis](/multi-level-logic-synthesis/), [algebraic division](/algebraic-division/), [kernels](/algebraic-kernel/), kernel extraction, [observability don't-cares](/observability-dont-care/) and [Ashenhurst-Curtis decomposition](/ashenhurst-curtis-decomposition/).
5. **Technology mapping and cuts.** [Technology mapping](/technology-mapping/), tree covering, [Boolean matching](/boolean-matching/), [$k$-feasible cuts](/k-feasible-cut/), [cut enumeration](/cut-enumeration/), [LUT mapping](/lut-mapping/), FlowMap and [priority cuts](/priority-cuts/).
6. **And-inverter graphs.** The graph itself, [balancing](/aig-balancing/), rewriting, [SAT sweeping](/sat-sweeping/), majority-inverter graphs and exact synthesis.
7. **Sequential synthesis.** [State assignment](/state-assignment/), the [binate covering problem](/binate-covering-problem/), [incompletely specified FSM minimization](/incompletely-specified-fsm-minimization/), retiming and [minimum-area retiming](/minimum-area-retiming/).
8. **High-level synthesis.** [High-level synthesis](/high-level-synthesis/), [ASAP and ALAP scheduling](/asap-alap-scheduling/) and [force-directed scheduling](/force-directed-scheduling/).

## A first reading

These twelve entries give the main line from a truth table to a mapped circuit.

1. Sum of products, for cubes and the positional notation used in the rest of the chapter.
2. Prime implicant, for Quine's theorem.
3. Quine-McCluskey, the exact method that lists the primes and sets up the covering table.
4. Two-level logic minimization, for what is exact, what is hard and why.
5. Espresso, the heuristic that replaced exact two-level methods in practice.
6. Boolean network, the model of multi-level logic.
7. Algebraic kernel, the divisors that algebraic synthesis tries.
8. And-inverter graph, the main form of modern synthesis tools.
9. Technology mapping, for the problem of covering a network with library parts.
10. Tree covering technology mapping, the dynamic program that is optimal on trees.
11. FlowMap, the depth-optimal lookup table mapper and its max-flow test.
12. Retiming, which moves registers to shorten the clock period.

## Before you start

The chapter assumes [Boolean functions](/boolean-function/), [cofactors](/cofactor/) and the [Shannon expansion](/shannon-expansion/) from Volume 16, and [directed acyclic graphs](/directed-acyclic-graph/) and [topological sort](/topological-sort/) from Volume 7. The covering steps rest on [set cover](/set-cover/) from Volume 18. FlowMap uses the [max-flow min-cut theorem](/max-flow-min-cut-theorem/), and retiming uses [difference constraints](/difference-constraints/) and [Bellman-Ford](/bellman-ford/), all from Volume 7. SAT sweeping and exact synthesis call a [SAT](/sat/) solver, and the state machine entries use [Mealy machines](/mealy-machine/) and [DFA minimization](/dfa-minimization/) from Volume 9. Retiming also uses [static timing analysis](/static-timing-analysis/) from Chapter 32.7.
