A hospital chain wants to open clinics so that every town is near one, at the least total cost of building and travel. A telecom firm wants the cheapest set of cables that keeps every pair of offices connected after any one cable fails. A factory assigns jobs to machines that run them at different speeds and wants every machine to finish early. Each of these problems is NP-hard, and each can be written as an integer program. Drop the condition that the variables are integers, and what is left is a linear program, which can be solved in polynomial time.

That is the start of every algorithm in this chapter. Solve the [LP relaxation](/lp-relaxation/) to get a [fractional solution](/fractional-solution/) $x^*$ of cost $\text{LP}^*$. For a minimization problem $\text{LP}^* \le \text{OPT}$, because every integral solution is also a fractional one. Then turn $x^*$ into an integral solution and prove that the rounding raises the cost by at most a factor $\rho$. The answer costs at most $\rho \cdot \text{LP}^* \le \rho \cdot \text{OPT}$, so the [approximation ratio](/approximation-ratio/) is $\rho \ge 1$. For a maximization problem the bound reads $\text{ALG} \ge \alpha \cdot \text{LP}^* \ge \alpha \cdot \text{OPT}$ with $\alpha \le 1$. No rounding can beat the [integrality gap](/integrality-gap/) of the LP, the worst ratio between OPT and $\text{LP}^*$, so part of the work is to choose a strong LP.

The ways to round differ. Weighted vertex cover keeps every vertex with $x_v \ge 1/2$ and pays at most twice the LP. Set cover picks each set with probability $x_S$, repeats about $\ln n$ times, and pays $O(\log n)$ times the LP. Survivable network design picks the edges with $x_e \ge 1/2$, solves the LP again on the rest, and pays at most twice the LP. The primal-dual schema never solves the LP at all: it grows a feasible dual and buys the primal items whose dual constraints become tight.

## What the chapter covers

1. **The method.** The [fractional solution](/fractional-solution/) and its vertices, the general [LP rounding](/linear-programming-rounding/) template, and the meaning of a ratio for a [randomized approximation algorithm](/randomized-approximation-algorithm/).
2. **Threshold rounding.** [Threshold rounding](/threshold-rounding/), [LP rounding for vertex cover](/lp-rounding-vertex-cover/) with ratio 2, the [half-integrality](/half-integrality/) of the vertex cover LP, and [frequency rounding](/frequency-rounding-set-cover/) for set cover with ratio $f$.
3. **Randomized rounding.** [Randomized rounding](/randomized-rounding/) and its Chernoff analysis, [LP rounding for set cover](/lp-rounding-set-cover/) with ratio $\ln n + 2$, the [random assignment](/random-assignment-max-3-sat/) for MAX-3SAT with ratio $7/8$, and [LP rounding for MAX-SAT](/max-sat-lp-rounding/) with ratio $3/4$.
4. **Duality without solving the LP.** The [primal-dual schema](/primal-dual-schema/), the [Bar-Yehuda-Even algorithm](/bar-yehuda-even-vertex-cover/) for weighted vertex cover, and [dual fitting](/dual-fitting/).
5. **Steiner forest and its relatives.** [Steiner forest](/steiner-forest/), the [Goemans-Williamson algorithm](/goemans-williamson-steiner-forest/) with ratio $2 - 2/k$, and the [prize-collecting Steiner tree](/prize-collecting-steiner-tree/).
6. **Iterative rounding.** [Iterative rounding](/iterative-rounding/), [survivable network design](/survivable-network-design/), the [generalized Steiner network](/generalized-steiner-network/) problem, [Jain's algorithm](/jain-iterative-rounding-network-design/) with ratio 2, and [iterative relaxation](/iterative-relaxation/).
7. **Assignment, scheduling and bin packing.** [Bicriteria approximation](/bicriteria-approximation/), the [generalized assignment problem](/generalized-assignment-problem/) and the [Shmoys-Tardos algorithm](/shmoys-tardos-gap/) for it, [makespan on unrelated machines](/unrelated-machine-scheduling-makespan/), the [configuration LP](/configuration-lp/) and the [Karmarkar-Karp algorithm](/karmarkar-karp-bin-packing/) for bin packing.
8. **Facility location.** The [filtering technique](/filtering-technique/), the [Shmoys-Tardos-Aardal algorithm](/shmoys-tardos-aardal-facility-location/), the [Jain-Vazirani algorithm](/jain-vazirani-facility-location/) with ratio 3, and [capacitated facility location](/capacitated-facility-location/).
9. **Dependent rounding.** [Dependent rounding](/dependent-rounding/) on bipartite graphs, [pipage rounding](/pipage-rounding/) and [swap rounding](/swap-rounding/) for matroids.

## A first reading

For a first pass, read these entries in order:

1. [Fractional solution](/fractional-solution/)
2. [LP rounding](/linear-programming-rounding/)
3. [Threshold rounding](/threshold-rounding/)
4. [LP rounding for vertex cover](/lp-rounding-vertex-cover/)
5. [Randomized rounding](/randomized-rounding/)
6. [LP rounding for set cover](/lp-rounding-set-cover/)
7. [LP rounding for MAX-SAT](/max-sat-lp-rounding/)
8. [Primal-dual schema](/primal-dual-schema/)
9. [Dual fitting](/dual-fitting/)
10. [Steiner forest](/steiner-forest/)
11. [Goemans-Williamson algorithm](/goemans-williamson-steiner-forest/)
12. [Iterative rounding](/iterative-rounding/)
13. [Shmoys-Tardos algorithm for GAP](/shmoys-tardos-gap/)
14. [Jain-Vazirani algorithm](/jain-vazirani-facility-location/)

These cover the four ways to use an LP: round at a threshold, round at random, round one step at a time, and build a dual in place of solving. Skip at first the network design entries beyond Steiner forest, the configuration LP and Karmarkar-Karp, capacitated facility location, and the three entries on dependent rounding, which need matroids.

## Before you start

From Volume 15 you need the [linear programming problem](/linear-programming-problem/), the [LP relaxation](/lp-relaxation/) and its [integrality gap](/integrality-gap/), the [dual linear program](/dual-linear-program/), [weak duality](/weak-duality/), [complementary slackness](/complementary-slackness/) and the [basic feasible solution](/basic-feasible-solution/); the entries on network design also use the [separation oracle](/separation-oracle/). From Volume 13 you need the [extreme point](/extreme-point/). From Volume 1 you need [linearity of expectation](/linearity-of-expectation/), [Markov's inequality](/markov-inequality/), the [union bound](/union-bound/) and the [Chernoff bound](/chernoff-bound/). From Volume 7 you need [bipartite matching](/bipartite-matching/) and the [max-flow min-cut theorem](/max-flow-min-cut-theorem/), and from Volume 2 the [matroid](/matroid/) for the last group.

Chapter 18.1 is the natural first step. It introduces [set cover](/set-cover/), [weighted vertex cover](/weighted-vertex-cover/) and the [primal-dual method](/primal-dual-approximation/) on single problems; this chapter turns them into general tools.
