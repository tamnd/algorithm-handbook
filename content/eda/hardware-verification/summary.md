## What to remember

- A [miter](/miter-circuit/) reduces combinational equivalence to one satisfiability question, which is coNP-complete. [Cutpoints](/cutpoint-equivalence-checking/) split it at proved internal equalities and resolve false negatives by composition, so the method stays exact.
- Sequential equivalence is reachability of a mismatch state in the [product machine](/product-machine/), PSPACE-complete for netlists. [Latch mapping](/latch-mapping/) and [signal correspondence](/signal-correspondence/) are sound and not complete: retiming and re-encoding defeat the first, and equalities that hold only because some states are unreachable can defeat the second. [Safe replaceability](/safe-replaceability/) is a preorder for designs without reset, not an equivalence.
- [Symbolic simulation](/symbolic-simulation/) is exact for $k$ cycles in $O(kPB^2)$ time, with $B$ the largest BDD. The [partitioned relation](/partitioned-transition-relation/) and [Coudert-Madre](/transition-function-image-computation/) both compute the exact image; their size gains are measured, not proved.
- [STE](/symbolic-trajectory-evaluation/) and [GSTE](/generalized-symbolic-trajectory-evaluation/) are sound for binary runs and not complete, because X loses information. A failure can be false, and a contradictory antecedent passes vacuously.
- A multiplier has no small BDD. [Algebraic rewriting](/algebraic-arithmetic-circuit-verification/) gives remainder 0 exactly when the circuit is correct, and a nonzero remainder yields a failing input; the size of the intermediate polynomials is measured. [TEDs](/taylor-expansion-diagram/) are canonical over the rationals, but modulo $2^w$ two different TEDs can denote the same function.
- [Burch-Dill flushing](/burch-dill-flushing/) checks a pipeline against its ISA in EUF, whose validity is coNP-complete. [Positive equality](/positive-equality/) gives fixed constants to terms used only in positive equations; giving them to a negative term is unsound.
- Coverage measures what a suite ran, not that the design is right. Scores depend on the denominator (declared or reachable states, flat or weighted bins). [Tag coverage](/observability-based-coverage/) is a lower bound on observability.
- [Rejection sampling](/rejection-sampling/) of constraints is exactly uniform and needs $2^n/\#C$ tries on average. The [BDD generator](/bdd-constrained-random-generation/) gives an exact uniform or weighted law; a bias on a variable is not its marginal, and `solve before` changes the law.
- The [synchronizer MTBF](/synchronizer-mtbf/) $e^{t_r/\tau}/(T_W f_c f_d)$ grows by $e$ for every $\tau$ of resolution time. It is exact under its model, with $\tau$ and $T_W$ fitted to measurements.

| Method | Question | Cost | Guarantee |
|---|---|---|---|
| Miter and SAT | combinational equivalence | coNP-complete | sound and complete |
| Cutpoints | combinational, shared structure | $O((N + PC)\,4^{n + C})$ worst | exact |
| Latch mapping | registers matched one to one | one combinational check per latch | sound, not complete |
| Product machine | sequential equivalence | PSPACE-complete | sound and complete |
| Signal correspondence | sequential equivalence | $O(V^2 4^{L + 2I})$ worst | sound, not complete |
| Symbolic simulation | behavior for $k$ cycles | $O(kPB^2)$ | exact up to $k$ |
| Image computation | one reachability step | Coudert-Madre $O(2^m m b^2)$ | exact |
| STE | bounded assertion | $O(dPB^2)$ | sound, not complete |
| GSTE | assertion graph | $O(NE^2(N + P)B^2)$ | sound, not complete |
| Algebraic rewriting | multiplier against spec | polynomial size measured | exact |
| Burch-Dill and positive equality | pipeline against ISA | EUF validity, coNP-complete | sound; exact on reachable states |
| Checker synthesis | safety assertion at run time | one flip-flop per NFA state of $r$ and DFA state of $s$ | sound; first bad prefix under a condition |
| Tag coverage | observability of sites | $O(VPn/w)$ | sound, not complete |
| BDD generation | stimulus with a set law | $O(n^2/w)$ per sample after setup | exact law |
| SAT debugging | error location | NP-complete | exact for the given tests |

: Main methods of the chapter. $B$ and $b$ are BDD sizes; other letters as in each entry.

## Choosing a method

For a netlist against its RTL, pair the registers by latch mapping and check the miter with SAT sweeping or cutpoints. If retiming or re-encoding broke the pairing, try signal correspondence, then reachability on the product machine. Use safe replaceability only for designs without a reset state.

For a short property of a large circuit, such as a memory read after a write, use STE; for unbounded time, GSTE. Plain symbolic simulation or bounded model checking suits small control logic where most state matters. For a multiplier, use algebraic rewriting, not BDDs. For a pipelined processor, use Burch-Dill flushing with positive equality.

In simulation, write assertions for the intended behavior, synthesize checkers to reuse them in emulation, and track code, FSM and functional coverage together. Use a BDD generator when the constraints fit in a BDD and the law matters, and a solver otherwise. Check every clock crossing structurally and size each synchronizer with the MTBF formula. When a check fails, SAT-based debugging narrows the search to a few gates.
