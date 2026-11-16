A reduction turns the instances of one problem into instances of another so that an algorithm for the second solves the first. It is the tool behind every hardness proof: to show a new problem NP-hard, you reduce a known NP-complete problem to it, in polynomial time and keeping the answer. A proof of this kind is a piece of design. You build small gadgets, one for each variable or clause of the source instance, and you show that the target has a solution exactly when the source does.

Different reductions keep different things. A Karp reduction maps one instance to one instance. A Cook reduction may call an algorithm for the target many times. A Levin reduction also maps certificates both ways, and a parsimonious one keeps the number of solutions. This chapter sorts these kinds and collects the standard proofs, so that a reader faced with a new problem can choose a source problem and a gadget.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Kinds of reduction.** Polynomial-time (Karp) reductions, Cook reductions, Levin and parsimonious reductions, and the transitivity that lets reductions chain.
2. **Search and decision.** Search problems, search-to-decision reductions and self-reducibility, which recover a solution from a yes-or-no answer.
3. **Gadgets and proof patterns.** Gadget reductions and the shape of an NP-completeness proof.
4. **Logic and circuit sources.** Circuit satisfiability, the circuit value problem, not-all-equal SAT, one-in-three SAT and zero-one equations.
5. **Graph and number targets.** Clique, 3-coloring, the Hamiltonian cycle, the traveling salesman decision problem, 0-1 knapsack and 3-partition.

## What to read meanwhile

Chapter 39.2 is written and holds the base of the catalogue. The [Cook-Levin theorem](/cook-levin-theorem/) makes SAT NP-complete, and [Karp's 21 NP-complete problems](/karps-21-np-complete-problems/) gives five reductions in full. [Three-dimensional matching](/three-dimensional-matching/), [exact cover by 3-sets](/exact-cover-by-3-sets/), the [subset sum problem](/subset-sum-problem/) and the [partition problem](/partition-problem/) are the usual sources for set and number problems.

The general [reduction](/reduction/) and [polynomial-time equivalence](/polynomial-time-equivalence/) are written in Volume 2. Volume 16 has [3-SAT](/3-sat/), the most common source of all. The [Hamiltonian cycle problem](/hamiltonian-cycle-problem/) and [graph coloring](/graph-coloring/), NP-complete for each fixed $k \ge 3$, are in Volume 7, and the [traveling salesman problem](/traveling-salesman-problem/) in Volume 15 gives its reduction from Hamiltonian cycle. Reductions that keep approximation ratios, the [gap-preserving reduction](/gap-preserving-reduction/) and the [L-reduction](/l-reduction/), are in Volume 18.
