Take two integers $x$ and $y$ with $x - y = 1$, $x + y \le 5$, and $x \ge 4$ or $y \ge 4$. A SAT solver cannot read this formula: to it, the four atoms are four letters $p, q, r, s$, and $p \wedge q \wedge (r \vee s)$ has models. An SMT solver gives the letters their meaning. Its SAT part proposes $p, q, r$ true. Its arithmetic part checks $x - y = 1$, $x + y \le 5$ and $x \ge 4$, finds that the first two give $x \le 3$, and returns the clause $\neg p \vee \neg q \vee \neg r$. The SAT part then tries $s$, the arithmetic part refutes $p, q, s$ in the same way, and the formula is unsatisfiable. This loop between a Boolean search and a theory solver is the core of the chapter.

Satisfiability modulo theories extends [SAT](/sat/) from Boolean variables to integers, reals, bit-vectors, arrays, strings and functions. It is the back end of program verifiers, symbolic execution, test generation and synthesis tools, which state their questions as formulas in the SMT-LIB language and pass them to a solver. Each theory needs its own decision procedure, and the chapter shows how these procedures work, how they join a CDCL solver, and how solvers for different theories cooperate.

## What the chapter covers

The chapter is in eight groups, read in order.

1. **The problem.** The [SMT problem](/smt-problem/), [decision procedures](/decision-procedure/), the [SMT-LIB](/smt-lib/) standard and the [Boolean abstraction](/boolean-abstraction/) of a formula, with unsat cores and incremental solving.
2. **Equality and uninterpreted functions.** [EUF](/euf-satisfiability/), [congruence closure](/congruence-closure/) in $O(n \log n)$ expected time, the [e-graph](/e-graph/), and arrays.
3. **Arithmetic.** [Difference logic](/difference-logic-satisfiability/) by negative cycles, [linear real arithmetic](/linear-real-arithmetic-satisfiability/) and [linear integer arithmetic](/linear-integer-arithmetic-satisfiability/), Presburger arithmetic and the [omega test](/omega-test/), nonlinear real arithmetic, Tarski's theorem and δ-satisfiability.
4. **Bit-vectors and eager encodings.** [Bit-vectors](/bit-vector-satisfiability/), [Ackermannization](/ackermannization/), [bit-blasting](/bit-blasting/), the eager approach and floating point.
5. **Lazy solving and DPLL(T).** The [lazy approach](/lazy-smt/), the [DPLL(T)](/dpll-t/) rules, conflict explanations, theory propagation, [CDCL(T)](/cdcl-t/) and the [simplex method for SMT](/simplex-for-smt/).
6. **Combining theories.** [Convex](/convex-theory/) and [stably infinite](/stable-infiniteness/) theories, the [Nelson-Oppen](/nelson-oppen/) method, Shostak's method and model-based combination.
7. **Quantifiers.** [Quantifier instantiation](/quantifier-instantiation/) and [e-matching](/e-matching/).
8. **Optimization, strings and synthesis.** [MaxSMT](/maxsmt/), optimization modulo theories, string constraints, syntax-guided synthesis and [CEGIS](/cegis/).

## A first reading

For a first reading, take these eleven entries in order: [the SMT problem](/smt-problem/), [SMT-LIB](/smt-lib/), [Boolean abstraction](/boolean-abstraction/), [EUF](/euf-satisfiability/), [congruence closure](/congruence-closure/), [difference logic](/difference-logic-satisfiability/), [linear real arithmetic](/linear-real-arithmetic-satisfiability/), [bit-blasting](/bit-blasting/), [the lazy approach](/lazy-smt/), [CDCL(T)](/cdcl-t/) and [Nelson-Oppen](/nelson-oppen/). They give one theory of each kind, the two ways of joining a theory to SAT, and the combination of theories. Skip the decidability results of group 3, the formal rules of DPLL(T), and Shostak's and model-based combination on a first pass. Groups 7 and 8 can wait until the lazy loop is clear.

## Before you start

The chapter assumes the previous one: [CNF](/conjunctive-normal-form/), [unit propagation](/unit-propagation/), the [Tseitin transformation](/tseitin-transformation/) and, above all, [CDCL](/cdcl/) with its [implication graph](/implication-graph/) and first UIP. Congruence closure uses the [disjoint-set](/disjoint-set/) structure of Volume 3. Difference logic uses [Bellman-Ford](/bellman-ford/) and [negative cycles](/negative-cycle/) from Volume 7. The arithmetic entries use the [simplex method](/simplex-method/), [Fourier-Motzkin elimination](/fourier-motzkin-elimination/) and [Farkas' lemma](/farkas-lemma/) from Volume 15, and [quantifier elimination](/quantifier-elimination/) from Volume 11. Bit-vectors need [two's complement](/twos-complement/) from Volume 2, and floating point needs [IEEE 754](/ieee-754/) from Volume 12.
