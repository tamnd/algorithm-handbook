Greedy set cover returns a cover at most $\ln n + 1$ times the smallest one, and no polynomial-time algorithm is known with ratio $c \ln n$ for a constant $c < 1$. This chapter shows why none exists unless P = NP: Dinur and Steurer proved in 2014 that ratio $(1 - \varepsilon)\ln n$ is NP-hard. Theorems of the same kind say that a random assignment, which satisfies $7/8$ of the clauses of a formula with three literals per clause, is the best polynomial algorithm for MAX E3SAT, and that ratio 2 for [k-center](/k-center-problem/) cannot be improved. A hardness result tells a designer when to stop looking for a better constant and to turn to special inputs or more time.

Every proof in the chapter has the same core. Map each instance of an NP-complete problem, in polynomial time, to an instance of the optimization problem, so that yes instances get a large optimum and no instances a small one. This is a [gap problem](/gap-problem/). An algorithm with a ratio better than the gap would tell the two cases apart and so decide the NP-complete problem. For the [general TSP](/general-tsp-inapproximability/) the map takes a few lines. For a constant gap in MAX 3SAT it is the PCP theorem, which says that every NP statement has a proof that a verifier can check by reading a constant number of its bits. Where P $\ne$ NP is not yet known to give tight constants, the Unique Games Conjecture often does.

The chapter is in seven groups, read in order.

## What the chapter covers

1. **Gap problems and the first bounds.** The class [NPO](/npo-class/) of optimization problems and the [gap problem](/gap-problem/), then four bounds from NP-complete problems alone: no ratio at all for the [general TSP](/general-tsp-inapproximability/), $3/2$ for [bin packing](/bin-packing-inapproximability/), 2 for [k-center](/k-center-inapproximability/), and the bounds for [makespan scheduling](/scheduling-makespan-inapproximability/).
2. **Reductions and the class APX.** [Approximation-preserving reductions](/approximation-preserving-reduction/), [gap-preserving reductions](/gap-preserving-reduction/), the [L-reduction](/l-reduction/) and the [PTAS-reduction](/ptas-reduction/); the class [APX](/apx-class/) and its [complete problems](/apx-completeness/), which have no PTAS unless P = NP; and the [approximation threshold](/approximation-threshold/) of a problem.
3. **Constant gaps from the PCP theorem.** The gap for [MAX 3SAT](/max-3sat-inapproximability/) and its consequences for [vertex cover](/vertex-cover-inapproximability/), [Steiner tree](/steiner-tree-inapproximability/) and the [metric TSP](/metric-tsp-inapproximability/). [Gap amplification](/gap-amplification/) turns a constant gap into a polynomial one for [clique](/clique-inapproximability/) and [graph colouring](/graph-coloring-inapproximability/).
4. **Two-prover games and label cover.** [Two-prover one-round games](/two-prover-one-round-game/), [label cover](/label-cover/) and the [parallel repetition theorem](/parallel-repetition-theorem/); from them the bound $(1 - \varepsilon)\ln n$ for [set cover](/set-cover-inapproximability/) and [dominating set](/dominating-set-inapproximability/), $1 - 1/e$ for [maximum coverage](/max-coverage-inapproximability/) and $1 + 2/e$ for [k-median](/k-median-inapproximability/).
5. **Boolean functions and tight bounds.** [Fourier analysis](/fourier-analysis-of-boolean-functions/), the [linearity test](/linearity-test/), the [low-degree test](/low-degree-test/), the [long code](/long-code/) and the [dictatorship test](/dictatorship-test/). Together they give [Håstad's 3-bit PCP](/hastad-3bit-pcp/), with the tight bounds $1/2 + \varepsilon$ for Max 3LIN and $7/8 + \varepsilon$ for MAX E3SAT, and the bound for the [nearest codeword problem](/nearest-codeword-inapproximability/).
6. **The Unique Games Conjecture.** The [conjecture](/unique-games-conjecture/) and what follows from it: the Goemans-Williamson ratio is optimal for [max cut](/max-cut-ugc-hardness/), many predicates are [approximation resistant](/approximation-resistance/), the basic SDP is optimal for every CSP by [Raghavendra's theorem](/raghavendra-theorem/), and [multiway cut](/multiway-cut-inapproximability/) and [sparsest cut](/sparsest-cut-ugc-hardness/) get their bounds. The [subexponential algorithm](/unique-games-subexponential-algorithm/) shows how delicate the conjecture is.
7. **Hardness beyond polynomial time.** The [Gap Exponential Time Hypothesis](/gap-eth/) and [parameterized inapproximability](/parameterized-inapproximability/), for algorithms that may spend time $f(k) \cdot n^{O(1)}$.

## A first reading

For a first pass, read these entries in order:

1. [NPO](/npo-class/)
2. [Gap problem](/gap-problem/)
3. [General TSP inapproximability](/general-tsp-inapproximability/)
4. [Bin packing inapproximability](/bin-packing-inapproximability/)
5. [k-center inapproximability](/k-center-inapproximability/)
6. [Gap-preserving reduction](/gap-preserving-reduction/)
7. [L-reduction](/l-reduction/)
8. [APX-completeness](/apx-completeness/)
9. [MAX 3SAT inapproximability](/max-3sat-inapproximability/)
10. [Vertex cover inapproximability](/vertex-cover-inapproximability/)
11. [Clique inapproximability](/clique-inapproximability/)
12. [Label cover](/label-cover/)
13. [Set cover inapproximability](/set-cover-inapproximability/)
14. [Unique Games Conjecture](/unique-games-conjecture/)
15. [Max cut under the UGC](/max-cut-ugc-hardness/)

These show the gap method, the role of the PCP theorem, the three sizes of threshold, a constant, $\ln n$ and $n^{1 - \varepsilon}$, and one threshold that rests on the conjecture. Skip at first the group on Boolean functions, which is the technical heart of the tight results, the low-degree test, Raghavendra's theorem, the subexponential algorithm and the last group.

## Before you start

Read the algorithms for the problems first: the [approximation ratio](/approximation-ratio/), the [PTAS](/ptas/) and [APX](/apx/) from Chapter 18.5; [set cover](/set-cover/), [maximum coverage](/max-coverage/), [vertex cover](/vertex-cover/), [bin packing](/bin-packing/), [maximum cut](/maximum-cut/) and [k-center](/k-center-problem/) from Chapter 18.1; [makespan minimization](/makespan-minimization/) from Chapter 18.2; and the [metric TSP](/metric-tsp/) from Chapter 18.3. From Volume 16 you need [3-SAT](/3-sat/), [MAX-SAT](/max-sat/) and [Boolean functions](/boolean-function/). From Volume 7 you need the [Hamiltonian cycle problem](/hamiltonian-cycle-problem/), [maximum clique](/maximum-clique/) and the [chromatic number](/chromatic-number/). Group 5 uses [linearity of expectation](/linearity-of-expectation/) from Volume 1, the [Walsh-Hadamard transform](/walsh-hadamard-transform/) from Volume 11 and the [Schwartz-Zippel lemma](/schwartz-zippel-lemma/) from Volume 17. Group 6 uses [semidefinite programming](/semidefinite-programming/) and the [integrality gap](/integrality-gap/) from Volume 15.

The entries also use NP-hardness, NP-completeness, polynomial-time reductions, probabilistically checkable proofs and the PCP theorem, whose entries are not yet written; their definitions are in any textbook on computational complexity. The chapter uses the PCP theorem without proof. [MAX 3SAT inapproximability](/max-3sat-inapproximability/) turns it into the form used most: for some constant $\varepsilon_0 > 0$, it is NP-hard to tell satisfiable 3-CNF formulas from those in which every assignment leaves at least an $\varepsilon_0$ fraction of the clauses false. The partition problem, 3-colouring, the Hadamard and Reed-Muller codes and fixed-parameter tractability are not yet written either; any textbook on complexity or on coding theory has them.
