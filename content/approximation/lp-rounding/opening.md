Most hard covering and packing problems can be written as integer programs. Drop the integrality, and the [LP relaxation](/lp-relaxation/) can be solved in polynomial time; its optimum LP* bounds OPT. LP rounding turns the fractional optimum into an integral solution and proves that the rounding loses at most a factor $\rho$, so the answer is within $\rho \cdot \text{LP}^* \le \rho \cdot \text{OPT}$. No rounding of an LP can beat its [integrality gap](/integrality-gap/), so part of the work is to find a strong LP.

This is the most general method of the field. One LP and a few rounding rules give good ratios for vertex cover, set cover, satisfiability, facility location, network design and scheduling, and the same LP also tells you how good the answer is on each input.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Deterministic rounding.** Threshold rounding, the LP-rounding algorithms for vertex cover and for set cover, and half-integrality.
2. **Randomized rounding.** Rounding each variable with its LP value as a probability, its use for set cover and MAX-SAT, and the dependent, pipage and swap rounding methods that keep a constraint exact.
3. **Iterative rounding.** Jain's method of fixing one variable at a time and solving the LP again, with its ratio 2 for survivable network design.
4. **Duality-based methods.** The primal-dual schema in general, with the Steiner forest algorithm of Goemans and Williamson, and dual fitting.
5. **Applications.** Facility location, the generalized assignment problem, the configuration LP and the Karmarkar-Karp algorithm for bin packing, and bicriteria approximation.

## What to read meanwhile

Chapter 18.1 already uses most of these ideas. [Weighted vertex cover](/weighted-vertex-cover/) rounds its LP at $1/2$, and the [element frequency](/element-frequency/) entry explains why threshold rounding gives ratio $f$ for set cover. The [primal-dual method](/primal-dual-approximation/) and the [primal-dual set cover](/set-cover-primal-dual/) algorithm show duality at work, and [greedy set cover](/greedy-set-cover/) is proved by dual fitting. The [covering integer program](/covering-integer-program/) and [packing integer program](/packing-integer-program/) entries use randomized rounding with the [Chernoff bound](/chernoff-bound/) of Volume 1.

For the LP itself, read the [dual linear program](/dual-linear-program/), [complementary slackness](/complementary-slackness/), [basic feasible solutions](/basic-feasible-solution/) and [total unimodularity](/total-unimodularity/) in Volume 15, and the [cutting stock problem](/cutting-stock-problem/) with [column generation](/column-generation/) for the configuration LP. [MAX-SAT](/max-sat/) in Volume 16 shows how the better of a random assignment and LP rounding reaches $3/4$, and the [method of conditional expectations](/method-of-conditional-expectations/) in Volume 17 removes the coin flips. The [facility location problem](/facility-location-problem/) of Volume 15 is a main application. [Semidefinite programming](/semidefinite-programming/), also in Volume 15, and [maximum cut](/maximum-cut/) show rounding beyond linear programs.
