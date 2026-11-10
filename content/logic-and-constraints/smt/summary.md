## What to remember

- **An SMT formula** is a Boolean combination of theory atoms. Its [Boolean abstraction](/boolean-abstraction/) replaces each atom by a letter. Every model of the formula gives a model of the abstraction, but not the other way round, and the theory solver closes the gap.
- **EUF** needs only congruence: equal arguments give equal results. [Congruence closure](/congruence-closure/) decides a conjunction of equalities and disequalities in $O(n \log n)$ expected time with union by size, a signature table and a proof forest. With Boolean structure the problem is NP-complete.
- **Arithmetic gets harder step by step.** Difference constraints $x - y \le c$ are satisfiable exactly when the constraint graph has no negative cycle, which [Bellman-Ford](/bellman-ford/) checks in $O(nm)$ time. Linear constraints are polynomial over the reals and NP-complete over the integers. Polynomial constraints are decidable over the reals and undecidable over the integers.
- **The eager approach** translates everything to SAT at once: Ackermannization for functions, at most quadratic in size, and [bit-blasting](/bit-blasting/) for bit-vectors. It suits bit-vectors, where the circuit is the natural meaning.
- **The lazy approach** is what most solvers do. In [CDCL(T)](/cdcl-t/), the SAT solver proposes literals, the theory solver checks them, and a conflict returns an explanation whose negation is learned. Theory propagation sets atoms that the theory implies. Small explanations prune more.
- **The theory solver must be incremental.** The [simplex method for SMT](/simplex-for-smt/) keeps one tableau, asserts and retracts bounds as the search moves, and explains each conflict by the bounds of one row together with the violated bound.
- **Combination needs conditions.** [Nelson-Oppen](/nelson-oppen/) is complete for theories with disjoint signatures that are stably infinite. Convex theories, such as EUF and linear real arithmetic, need to exchange only single equalities. Linear integer arithmetic, arrays and bit-vectors are not convex, so they must exchange disjunctions or split on them.
- **Quantifiers are handled by instances.** First-order logic is undecidable, so [e-matching](/e-matching/) and other instantiation methods are heuristics that may never stop on a satisfiable formula.

## The main procedures side by side

| Procedure | Problem | Time | Space |
|---|---|---|---|
| [Congruence closure](/congruence-closure/) | EUF conjunction | $O(n \log^2 n)$, $O(n \log n)$ expected | $\Theta(n)$ |
| [Bellman-Ford](/difference-logic-satisfiability/) | difference logic conjunction | $O(nm)$ | — |
| [Simplex for SMT](/simplex-for-smt/) | linear real conjunction | $O(6^{n+m} m n)$ | $\Theta(m n)$ |
| [DPLL(T)](/dpll-t/) | SMT formula | $O(2^n n)$ rule applications | $O(n)$ |
| [CDCL(T)](/cdcl-t/) | SMT formula | $O(3^n n)$ trail steps | $O(3^n n)$ |
| [Nelson-Oppen](/nelson-oppen/) | two combined theories | $O(k^{2k+1} t)$ | $O(k(n + k))$ |
| [Shostak](/shostak-combination/) | canonizable theory with EUF | $O(n^3)$ | $O(n^2)$ |
| [E-matching](/e-matching/) | one pattern in an e-graph | $O(m n^m)$ | $O(m n^m)$ |

: Worst-case costs as the entries give them; $n$ and $m$ mean different things in each row. For congruence closure, $n$ counts the nodes of the term DAG and the equations. For Bellman-Ford, $n$ and $m$ are the variables and atoms. For simplex, $n$ counts the original variables and $m$ the slack variables, and the bound is on the pivots of one check. For DPLL(T) and CDCL(T), $n$ is the number of propositional variables, and each step costs a call of the theory solver. For Nelson-Oppen, $k$ is the number of shared variables and $t$ the time of one theory call. For e-matching, $m$ is the size of the pattern and $n$ the number of e-nodes.

## Choosing a method

- For bit-vectors and floating point, bit-blast after word-level simplification. For small widths this is usually the fastest route.
- For formulas with rich Boolean structure over arithmetic or EUF, use a lazy CDCL(T) solver with theory propagation.
- For integer constraints of the form $x - y \le c$ alone, a difference logic solver with incremental negative-cycle detection beats general simplex.
- For general linear integer constraints, rely on simplex with branch and bound and cuts. Use the omega test or Presburger quantifier elimination when quantifiers must be removed.
- For nonlinear real constraints where small numeric errors are acceptable, a δ-complete solver avoids the cost of exact algebraic methods.
- For mixed theories, check convexity and stable infiniteness before trusting a Nelson-Oppen combination.
