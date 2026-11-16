Two machines share a buffer with one slot. Machine 1 puts a finished part into the buffer, and machine 2 takes it out. A controller can start a machine, but it cannot stop a machine from finishing. So it must hold machine 1 back whenever the buffer is full, because a part finished into a full buffer is lost. Nothing here is a differential equation. The state is a list of facts (idle or working, empty or full), and it changes only when an event occurs. The theory of this chapter finds the least restrictive controller for such a plant, and for this one the answer is two rules: do not start machine 1 while the buffer is full, and do not start machine 2 while it is empty.

Many plants mix the two kinds of state. A thermostat switches a heater on and off, a car changes gear, a ball falls and bounces. Between events the state moves by a differential equation, and at an event it jumps or the equation changes. These hybrid systems behave in ways that neither part shows alone. Two stable modes can give an unstable system when the switching is chosen badly, and a model can make infinitely many jumps in finite time.

The chapter builds on Volume 16, which holds the automata models of verification: [hybrid automata](/hybrid-automata/), [timed automata](/timed-automata/), [Petri nets](/petri-net/), [region graphs](/region-graph/), [bisimulation](/bisimulation/) and [parity games](/parity-game/). Those entries ask whether a model meets a property. The entries here ask the control questions: how to restrict a plant so that it does meet the property, how to detect a fault from what a sensor sees, how fast a timed system runs, and when a switched system is stable.

## What the chapter covers

1. **Discrete-event systems and supervisors.** A [discrete-event system](/discrete-event-system/) is an automaton with controllable and uncontrollable events. [Supervisory control theory](/supervisory-control-theory/) and the [supremal controllable sublanguage](/supremal-controllable-sublanguage/) give the least restrictive supervisor, and [monitor places](/supervision-based-on-place-invariants/) do the same for linear constraints on Petri nets.
2. **Control under partial observation.** [Observable](/observable-language/) and [normal](/normal-language/) languages are the conditions when the supervisor does not see every event.
3. **Fault diagnosis.** [Diagnosability](/diagnosability/), the [diagnoser](/diagnoser-automaton/) and the polynomial [twin plant test](/twin-plant-diagnosability-test/).
4. **Max-plus algebra and timed event graphs.** Synchronization becomes linear in the [max-plus algebra](/max-plus-algebra/), and the [eigenvalue theorem](/max-plus-eigenvalue-theorem/) gives the cycle time of a [timed event graph](/timed-event-graph/).
5. **Switched systems.** [Switched systems](/switched-system/), [common Lyapunov functions](/common-lyapunov-function/), the [joint spectral radius](/joint-spectral-radius/) and the [dwell-time theorem](/dwell-time-theorem/).
6. **Hybrid models and hybrid predictive control.** [Zeno behavior](/zeno-behavior/), [piecewise affine](/piecewise-affine-system/) and [mixed logical dynamical](/mixed-logical-dynamical-system/) models, and [hybrid MPC](/hybrid-mpc/).
7. **Reachability and safety.** [Reachable set computation](/reachable-set-computation/), [zonotopes](/zonotope-reachability/), [Hamilton-Jacobi reachability](/hamilton-jacobi-reachability/) and [barrier certificates](/barrier-certificate/).
8. **Abstraction and event-based implementation.** [Symbolic control](/symbolic-control/) and [event-triggered control](/event-triggered-control/).

## A first reading

A first pass through the chapter takes these entries, in order:

1. [Discrete-event system](/discrete-event-system/)
2. [Supervisory control theory](/supervisory-control-theory/)
3. [Controllable language](/controllable-language/)
4. [Supremal controllable sublanguage](/supremal-controllable-sublanguage/)
5. [Diagnosability](/diagnosability/)
6. [Twin plant diagnosability test](/twin-plant-diagnosability-test/)
7. [Max-plus algebra](/max-plus-algebra/)
8. [Timed event graph](/timed-event-graph/)
9. [Switched system](/switched-system/)
10. [Common Lyapunov function](/common-lyapunov-function/)
11. [Dwell-time theorem](/dwell-time-theorem/)
12. [Piecewise affine system](/piecewise-affine-system/)
13. [Reachable set computation](/reachable-set-computation/)

Partial observation, the diagnoser, the Petri net monitors and the eigenvalue proof can wait. So can the research entries of the last two groups (zonotopes, Hamilton-Jacobi reachability, barrier certificates, symbolic and event-triggered control) and hybrid MPC, which need the reachability and predictive control entries first.

## Before you start

The discrete-event half uses automata from Volume 9: [deterministic finite automata](/deterministic-finite-automaton/), [regular languages](/regular-language/), the [product construction](/product-construction/) and the [subset construction](/subset-construction/). Its algorithms are graph searches from Volume 7: [breadth-first search](/breadth-first-search/), [strongly connected components](/strongly-connected-components/), [topological sort](/topological-sort/) and [Karp's minimum mean cycle](/karp-minimum-mean-cycle/). The verification side is in Volume 16 ([reachability](/reachability-problem/), [symbolic reachability](/symbolic-reachability/)), and the game view of supervision is [reactive synthesis](/reactive-synthesis/) in Volume 34. The continuous half uses this volume's [state-space models](/state-space-representation/), [Lyapunov functions](/lyapunov-function/), [exponential stability](/exponential-stability/), [sum-of-squares programming](/sum-of-squares-programming/) and [linear MPC](/linear-mpc/), with the [spectral radius](/spectral-radius/), [matrix norms](/matrix-norms/) and [Lyapunov equations](/lyapunov-equation/) of Volume 12, and the [big-M formulation](/big-m-formulation/), [mixed-integer programming](/mixed-integer-programming/) and [semidefinite programming](/semidefinite-programming/) of Volume 15. A first course in linear algebra and ordinary differential equations is assumed.
