Many of the problems that matter in practice are NP-hard. A shipping firm packs parcels into trucks, a city places fire stations, a chip maker drills holes in a board, a cloud provider assigns jobs to machines. For none of these is there a known algorithm that finds the best answer fast on every input, and most likely there is none. Yet the answers are needed today. An approximation algorithm runs in polynomial time and comes with a proof that its answer is within a fixed factor of the best one on every input. That factor is its approximation ratio: an algorithm for a minimization problem has ratio $\rho$ when its cost is at most $\rho \cdot \text{OPT}$, and an algorithm for a maximization problem has ratio $\alpha \le 1$ when its value is at least $\alpha \cdot \text{OPT}$.

This volume collects what is known about such algorithms. It starts with covering and packing problems, where most of the methods were first found. Then come scheduling, the traveling salesman problem, the general method of rounding a linear program, the approximation schemes that come as close to OPT as you like, and the theory that proves some ratios cannot be improved.

This edition contains the entries of the first chapter, *Covering and packing*. The entries of the other five chapters are being written; their opening pages say what each will cover and which entries elsewhere in the set to read meanwhile.

## Why approximation gets a volume of its own

An approximation algorithm is judged by a proof, not only by a run on test data, and the proofs share a small set of ideas. In this volume you will meet:

- **Lower bounds on OPT.** Since OPT is unknown, every proof compares the answer with something that can be computed and is never more than OPT. In [bin packing](/bin-packing/) it is the total size of the items; in [vertex cover](/vertex-cover/) it is the size of a matching; in [k-center](/k-center-problem/) it is a set of points far apart. To read a ratio proof, first find its lower bound.
- **Greedy algorithms.** [Greedy set cover](/greedy-set-cover/) is within $H_d \le \ln d + 1$ of OPT, and [greedy maximum coverage](/greedy-max-coverage/) reaches $1 - 1/e$ of OPT. Both ratios are the best possible in polynomial time unless P = NP.
- **Linear programs and duality.** The [LP relaxation](/lp-relaxation/) of an integer program is a lower bound that can be computed, and by [weak duality](/weak-duality/) so is the value of any feasible solution of its [dual](/dual-linear-program/). The [primal-dual method](/primal-dual-approximation/) builds a solution and a dual together and never solves the LP.
- **Randomized rounding.** A fractional solution can be read as a set of probabilities. Rounding at random and bounding the losses with the [Chernoff bound](/chernoff-bound/) gives the ratios for [covering integer programs](/covering-integer-program/) and [packing integer programs](/packing-integer-program/).
- **Schemes.** Some problems allow a ratio $1 + \varepsilon$ for every $\varepsilon > 0$. The [asymptotic scheme for bin packing](/bin-packing-aptas/) rounds the item sizes, groups them and enumerates the few patterns left.
- **Hardness.** Proofs that no algorithm can do better close the gap from the other side. [Bin packing NP-hardness](/bin-packing-np-hardness/) shows that no algorithm uses fewer than $\frac32 \text{OPT}$ bins on every input unless P = NP, and the same kind of reduction shows that ratio 2 for $k$-center is the best possible.

## The chapters

**Chapter 18.1, Covering and packing**, is the heart of the volume. It starts with bin packing and its simple rules, [next fit](/next-fit-bin-packing/), [first fit](/first-fit-bin-packing/) and [first fit decreasing](/first-fit-decreasing/), and with the relatives of bin packing, such as the [cutting stock problem](/cutting-stock-problem/). Then come [set cover](/set-cover/) and [maximum coverage](/max-coverage/) with their greedy algorithms and the [Nemhauser-Wolsey-Fisher theorem](/nemhauser-wolsey-fisher-theorem/) on submodular functions; vertex cover, with and without [weights](/weighted-vertex-cover/); the primal-dual method and the [local ratio technique](/local-ratio-technique/); [set packing](/set-packing/), independent sets and [maximum cut](/maximum-cut/); the $k$-center problem and [farthest-first traversal](/gonzalez-k-center/); and the general covering and packing integer programs.

**Chapter 18.2, Scheduling approximation**, assigns jobs to machines so that the last job finishes early. It will cover Graham's list scheduling, the longest processing time rule, the scheme of Hochbaum and Shmoys, the LP rounding of Lenstra, Shmoys and Tardos for unrelated machines, precedence constraints and the shop problems.

**Chapter 18.3, TSP approximation**, treats the [traveling salesman problem](/traveling-salesman-problem/) with distances that obey the triangle inequality. It will cover the double-tree algorithm, Christofides' algorithm, the Held-Karp bound, the asymmetric and Euclidean problems, and the local search heuristics 2-opt and Lin-Kernighan.

**Chapter 18.4, LP rounding**, turns the methods of Chapter 18.1 into a general toolkit: threshold and randomized rounding, iterative rounding, the primal-dual schema for network design, dual fitting, and applications to facility location and the generalized assignment problem.

**Chapter 18.5, Approximation schemes**, studies the problems that can be approximated as closely as you like. It will cover rounding and scaling for the [knapsack problem](/knapsack-problem/) and subset sum, the schemes for scheduling and bin packing, Baker's technique for planar graphs, and the schemes of Arora and Mitchell for the Euclidean TSP.

**Chapter 18.6, Hardness of approximation**, proves the lower bounds: gap reductions, the class APX, the PCP theorem, the Unique Games Conjecture, and the thresholds for set cover, vertex cover, clique, satisfiability, maximum cut and the other problems of the volume.

## How to read this volume

If this is your first course, read these entries of Chapter 18.1 in this order: [bin packing](/bin-packing/), [lower bounds for bin packing](/bin-packing-lower-bound/), [next fit](/next-fit-bin-packing/), [first fit decreasing](/first-fit-decreasing/), [set cover](/set-cover/), [greedy set cover](/greedy-set-cover/), [maximum coverage](/max-coverage/), [greedy maximum coverage](/greedy-max-coverage/), [vertex cover](/vertex-cover/), [the maximal matching algorithm](/vertex-cover-2-approximation/), [weighted vertex cover](/weighted-vertex-cover/), [primal-dual weighted vertex cover](/primal-dual-weighted-vertex-cover/), [primal-dual set cover](/set-cover-primal-dual/), [maximum cut](/maximum-cut/), [the k-center problem](/k-center-problem/) and [farthest-first traversal](/gonzalez-k-center/). Then read the [traveling salesman problem](/traveling-salesman-problem/) and the [knapsack problem](/knapsack-problem/) in Volume 15, which state the known ratios for these two problems. Do the exercises marked ◦ and • at the end of Chapter 18.1. That is a complete first unit on approximation algorithms.

If you already know the basic algorithms, start with the opening page of each chapter. It names the groups in the chapter and the order to read them. The entries marked *Advanced* and *Research* are the place to go deeper.

Each entry stands on its own. Its facts box lists what it needs, with the number of the entry where each prerequisite is explained. Entries in other volumes are cited by number too, as the [LP relaxation](/lp-relaxation/) in Volume 15 and the [harmonic series](/harmonic-series/) in Volume 1 are; the number is printed with the link. Some prerequisites, such as NP-hardness and polynomial-time reductions, are not yet written; their definitions are in any textbook on computational complexity.

## What you need first

You should be able to follow a proof by induction and read a short program. From Volume 15 you need the [linear programming problem](/linear-programming-problem/), the LP relaxation, the dual and weak duality, and [complementary slackness](/complementary-slackness/). From Volume 7 you need [independent sets](/independent-set/) and [maximal matchings](/maximal-matching/). From Volume 1 you need [linearity of expectation](/linearity-of-expectation/), the harmonic series and, for the integer programs, the Chernoff bound. From Volume 2 you need the [greedy algorithm](/greedy-algorithm/). The $k$-center problem uses the [metric space](/metric-space/) and the [triangle inequality](/triangle-inequality/) of Volume 5. You should also know what it means for a problem to be NP-hard.

## The exercises

In this edition only Chapter 18.1 has exercises; the other chapters will have them when their entries are written. They come in three bands. Exercises marked ◦ check that you read the entries closely; you should be able to do them in a few minutes. Exercises marked • ask you to use an idea in a new place; each takes some thought, and some need a short program. Exercises marked ★ are harder; some are results from research papers. Hints for many exercises are in the appendix *Hints to the exercises* at the end of the volume.
