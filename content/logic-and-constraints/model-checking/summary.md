## What to remember

- **Model checking is search plus fixed points.** An invariant holds when no bad state is [reachable](/reachability-problem/), which takes linear time in the explicit graph. The temporal operators are least and greatest [fixed points](/fixed-point/): $\mathsf{EF}\,p$ is the least set that contains $p$ and is closed under predecessors, and $\mathsf{EG}\,p$ the greatest subset of $p$ in which every state has a successor in the set.
- **CTL is linear in both inputs; LTL is exponential in the formula.** The [labelling algorithm](/ctl-labelling-algorithm/) checks CTL in $O(|M| \cdot |\varphi|)$ time. [LTL model checking](/ltl-model-checking/) takes $O(|M| \cdot 2^{O(|\varphi|)})$ and is PSPACE-complete, but formulas are short and the cost in $|M|$ is linear.
- **LTL checking is emptiness of a product.** Translate $\neg\varphi$ into a [Büchi automaton](/ltl-to-buchi-translation/) with at most $2^{|\varphi|}$ states in generalized form, build its product with the system, and look for a reachable accepting cycle with [nested depth-first search](/nested-depth-first-search/), in $O(n + m)$ time with two bits per state.
- **The state explosion is the enemy.** $n$ components with $k$ local states can have $k^n$ global states. Each method in the chapter attacks it from one side: [partial-order reduction](/partial-order-reduction/) and [symmetry reduction](/symmetry-reduction/) explore fewer states, [bitstate hashing](/bitstate-hashing/) stores fewer bits, [BDDs](/symbolic-model-checking/) store sets of states, and [abstraction](/cegar/) checks a smaller model.
- **SAT made bounded search practical, and induction made it complete.** [Bounded model checking](/bounded-model-checking/) finds counterexamples up to depth $k$; [k-induction](/k-induction/), [interpolation](/interpolation-based-model-checking/) and [IC3](/ic3-pdr/) prove properties by finding inductive invariants.
- **Equivalences are the reason reductions are sound.** On finite structures [bisimilarity](/bisimulation/) is equality of CTL* formulas and takes $O(m \log n)$ time; [stuttering equivalence](/stuttering-equivalence/) preserves the logics without next, which is what partial-order reduction needs; [trace equivalence](/trace-equivalence/) is PSPACE-complete.
- **Infinite state is sometimes decidable.** Timed automata have a finite [region graph](/region-graph/), pushdown systems have regular sets of predecessors, and Petri net [coverability](/coverability/) is EXPSPACE-complete. Reachability in Petri nets is decidable but Ackermann-complete.

## Problems side by side

| Problem | Complexity |
|---|---|
| [Reachability](/reachability-problem/), [invariants](/invariant-checking/) | linear time; PSPACE-complete for succinct systems |
| [CTL model checking](/ctl-model-checking/) | $O(\lvert M\rvert \cdot \lvert\varphi\rvert)$; P-complete |
| [LTL model checking](/ltl-model-checking/) | $O(\lvert M\rvert \cdot 2^{O(\lvert\varphi\rvert)})$; PSPACE-complete |
| [CTL*](/ctl-star/) model checking | PSPACE-complete |
| [Mu-calculus](/mu-calculus-model-checking/) model checking | in NP $\cap$ co-NP, quasi-polynomial time |
| [LTL satisfiability](/ltl-satisfiability/) | PSPACE-complete |
| [CTL satisfiability](/ctl-satisfiability/) | EXPTIME-complete |
| [Bisimilarity](/equivalence-checking/) | $O(m \log n)$; P-complete |
| [PCTL model checking](/pctl-model-checking/) | polynomial in the chain, linear in the formula |
| [Timed automata](/timed-automata/) reachability | PSPACE-complete |
| [Pushdown reachability](/pushdown-reachability/) | cubic time; P-complete |
| Petri net [coverability](/coverability/) | EXPSPACE-complete |
| Petri net [reachability](/petri-net-reachability-decidability/) | decidable; Ackermann-complete |

: The main decision problems of the chapter and their complexity. $|M|$ is the size of the explicit structure, $\varphi$ the formula, $n$ and $m$ the numbers of states and transitions.

## Choosing a method

- For concurrent protocols and software with small data, use an explicit-state checker on the fly, with [partial-order reduction](/partial-order-reduction/) on, and [bitstate hashing](/bitstate-hashing/) when the states no longer fit.
- For hardware and other systems with much regular data, use SAT-based methods: [bounded model checking](/bounded-model-checking/) to find bugs, then [IC3](/ic3-pdr/) or [k-induction](/k-induction/) to prove safety. Turn liveness into safety with the [liveness-to-safety](/liveness-to-safety/) construction when the tool handles only invariants.
- Use [BDD-based symbolic checking](/symbolic-model-checking/) when a good variable order is known and the property needs full CTL or fairness; for asynchronous systems, [saturation](/saturation-algorithm/) saves much time and peak memory over breadth-first images.
- For programs with infinite data, use predicate abstraction with [CEGAR](/cegar/) or [lazy abstraction](/lazy-abstraction/).
- For multithreaded programs whose state cannot be stored, use [stateless model checking](/stateless-model-checking/) with [dynamic partial-order reduction](/dynamic-partial-order-reduction/).
- For probabilities, solve the linear systems of [PCTL model checking](/pctl-model-checking/) when the chain fits in memory, and use [statistical model checking](/statistical-model-checking/) when it does not or when only a simulator exists.
