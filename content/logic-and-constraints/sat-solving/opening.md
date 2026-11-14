Take three switches $x_1, x_2, x_3$ and three rules: $x_1$ or not $x_2$; not $x_1$, or $x_2$, or $x_3$; and not $x_3$. Each rule is a clause, a list of literals of which at least one must be true. The third clause forces $x_3$ false, the second then says that $x_1$ true needs $x_2$ true, and the first says that $x_2$ true needs $x_1$ true. So the clauses hold exactly when $x_1 = x_2$ and $x_3$ is false. Finding such a setting, or proving that none exists, is the satisfiability problem. With three variables, eight settings can be tried by hand. A formula from hardware verification can have a million variables and $2^{1000000}$ settings, and solvers still decide many industrial formulas with millions of clauses.

[SAT](/sat/) was the first problem shown NP-complete, by Cook in 1971 and Levin in 1973, so no algorithm is known that is fast on every formula. The chapter is about why solvers work anyway. Most of it builds conflict-driven clause learning, the method inside nearly every modern solver, from its parts. The rest covers the easy special cases, the encodings that bring problems into clause form, local search, proofs of unsatisfiability, and the optimization and counting problems built on SAT.

## What the chapter covers

The chapter is in ten groups, read in order.

1. **Clauses and the problem.** Literals, clauses, [conjunctive normal form](/conjunctive-normal-form/) and the DIMACS format. Then the problem, its restriction to clauses of $k$ literals, and [unit propagation](/unit-propagation/), the rule that every solver applies first.
2. **Classes solved in polynomial time.** [2-SAT](/2-sat/) by strongly connected components in $\Theta(n + m)$ time, [Horn-SAT](/horn-sat/) by forward chaining, and [XOR-SAT](/xor-sat/) by Gaussian elimination over GF(2).
3. **Encodings.** The [Tseitin transformation](/tseitin-transformation/), which turns a circuit into clauses of linear size, its one-polarity form, and encodings of cardinality and pseudo-Boolean constraints.
4. **Davis-Putnam and DPLL.** Elimination by resolution, then [DPLL](/dpll/), the backtracking search with unit propagation of 1962, and lookahead methods that spend more work on each split.
5. **Clause learning.** The [implication graph](/implication-graph/), the first UIP cut, learned clauses, the backjump, two watched literals, and [CDCL](/cdcl/), which joins them.
6. **CDCL heuristics and engineering.** [VSIDS](/vsids/), phase saving, restarts, the learned clause database and its cleaning, and incremental and parallel solving.
7. **Simplifying formulas.** Subsumption, [bounded variable elimination](/bounded-variable-elimination/), blocked clauses, equivalent literals, autarkies and backbones.
8. **Proofs and lower bounds.** The [DRAT](/drat-proof/) and LRAT proof formats, Haken's exponential lower bound for the pigeonhole formulas, and the result that CDCL can simulate resolution.
9. **Local search, random formulas and exponential bounds.** GSAT, [WalkSAT](/walksat/), probSAT, [Schöning's algorithm](/schoning-algorithm/) and PPSZ, then the satisfiability threshold of random formulas and survey propagation.
10. **MaxSAT, cores, counting and quantifiers.** [MaxSAT](/max-sat/) and its partial and weighted forms, minimal unsatisfiable and correction subsets, core-guided MaxSAT, [model counting](/model-counting/) and [QBF](/qbf/).

## A first reading

For a first reading, take these fourteen entries in order: [SAT](/sat/), [conjunctive normal form](/conjunctive-normal-form/), [unit propagation](/unit-propagation/), [2-SAT](/2-sat/), [the 2-SAT algorithm](/two-sat-algorithm/), [Horn-SAT](/horn-sat/), [the Tseitin transformation](/tseitin-transformation/), [DPLL](/dpll/), [the implication graph](/implication-graph/), [first UIP](/first-uip/), [clause learning](/clause-learning/), [CDCL](/cdcl/), [WalkSAT](/walksat/) and [MaxSAT](/max-sat/). They give the problem, the easy cases, the main encoding, the two search methods and the main optimization variant. Skip groups 6 to 8 on a first pass: they explain why real solvers are fast and how they prove their answers, and they make most sense after CDCL is clear. Skip also the exponential bounds of group 9 and the counting and quantified problems of group 10.

## Before you start

The chapter needs [NP-completeness](/np-complete/) from Volume 38 to place SAT among the hard problems, and [backtracking](/chronological-backtracking/) from Volume 2 as the base of DPLL. The 2-SAT algorithm uses [strongly connected components](/strongly-connected-components/) from Volume 7. XOR-SAT uses [Gaussian elimination](/gaussian-elimination/) from Volume 11. The Davis-Putnam procedure, clause learning and the proof entries use [resolvents](/resolvent/) and [binary resolution](/binary-resolution/), which Chapter 16.5 treats in full; the definition of a resolvent is all that is needed here. Local search builds on [local search](/local-search/) in Volume 15, and the analysis of random walks uses [linearity of expectation](/linearity-of-expectation/) from Volume 1.
