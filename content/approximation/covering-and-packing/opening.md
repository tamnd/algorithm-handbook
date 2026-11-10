A shipping firm loads parcels into trucks of one size and wants to use as few trucks as possible. A city chooses sites for sirens so that each street hears one, at the least cost. A cloud provider picks $k$ data centres so that no user is far from the nearest one. Each of these is a covering or a packing problem, and each is NP-hard, so no known algorithm finds the best answer fast on every input. The algorithms of this chapter find an answer fast and prove that it is within a fixed factor of the best one.

That factor is the approximation ratio. For a minimization problem, an algorithm has ratio $\rho$ when its cost ALG is at most $\rho \cdot \text{OPT}$ on every input; for a maximization problem, when its value is at least $\text{OPT}/\rho$, or at least $\alpha \cdot \text{OPT}$ with $\alpha \le 1$. Each entry states its convention. Since OPT is unknown, every proof has the same shape: find a lower bound on OPT that can be computed, and compare the answer with it. In [bin packing](/bin-packing/) the bound is the total size of the items. In [vertex cover](/vertex-cover/) it is the size of a matching. In most of the chapter it is the value of an [LP relaxation](/lp-relaxation/) or of a feasible solution to its dual. In [k-center](/k-center-problem/) it is a set of $k + 1$ points that are far apart. Learn to spot the lower bound, and the proofs become short.

The chapter is in nine groups, read in order.

## What the chapter covers

1. **Bin packing.** The [problem](/bin-packing/) and its [lower bounds](/bin-packing-lower-bound/); the online rules [next fit](/next-fit-bin-packing/), [first fit](/first-fit-bin-packing/) and [best fit](/best-fit-bin-packing/); the sorted rule [first fit decreasing](/first-fit-decreasing/); the [hardness](/bin-packing-np-hardness/) that rules out ratios below $3/2$ unless P = NP; and the [asymptotic scheme](/bin-packing-aptas/) with $(1 + \varepsilon)\text{OPT} + 1$ bins.
2. **Relatives of bin packing.** [Bin covering](/bin-covering/), the [cutting stock problem](/cutting-stock-problem/) with its configuration LP, [strip packing](/strip-packing/) and [rectangle packing](/rectangle-packing/).
3. **Set cover.** The [problem](/set-cover/), the [greedy algorithm](/greedy-set-cover/) with ratio $H_d$, the [element frequency](/element-frequency/) $f$, and two problems that are set cover in disguise: [dominating set](/dominating-set/) and [hitting set](/hitting-set/).
4. **Maximum coverage and submodular greedy.** [Maximum coverage](/max-coverage/), its [greedy algorithm](/greedy-max-coverage/), and the [Nemhauser-Wolsey-Fisher theorem](/nemhauser-wolsey-fisher-theorem/), which gives $1 - 1/e$ for every monotone submodular function.
5. **Vertex cover.** The [problem](/vertex-cover/), the [maximal matching algorithm](/vertex-cover-2-approximation/) with ratio 2, and [weighted vertex cover](/weighted-vertex-cover/).
6. **Primal-dual and local ratio.** The [primal-dual method](/primal-dual-approximation/), its two linear-time cases for [weighted vertex cover](/primal-dual-weighted-vertex-cover/) and for [set cover](/set-cover-primal-dual/) with ratio $f$, and the [local ratio technique](/local-ratio-technique/), which gives the same algorithms without an LP.
7. **Packings, independent sets and cuts.** [Set packing](/set-packing/), the [Caro-Wei theorem](/caro-wei-theorem/), the [minimum-degree greedy algorithm](/greedy-independent-set/) for independent set, and [maximum cut](/maximum-cut/).
8. **k-center.** The [problem](/k-center-problem/) and [farthest-first traversal](/gonzalez-k-center/), which has ratio 2, the best possible.
9. **Covering and packing integer programs.** The general forms [covering integer program](/covering-integer-program/) and [packing integer program](/packing-integer-program/), solved by randomized rounding of the LP.

## A first reading

For a first pass, read these entries in order:

1. [Bin packing](/bin-packing/)
2. [Lower bounds for bin packing](/bin-packing-lower-bound/)
3. [Next fit](/next-fit-bin-packing/)
4. [First fit decreasing](/first-fit-decreasing/)
5. [Set cover](/set-cover/)
6. [Greedy set cover](/greedy-set-cover/)
7. [Maximum coverage](/max-coverage/)
8. [Greedy maximum coverage](/greedy-max-coverage/)
9. [Vertex cover](/vertex-cover/)
10. [The maximal matching algorithm](/vertex-cover-2-approximation/)
11. [Weighted vertex cover](/weighted-vertex-cover/)
12. [Primal-dual weighted vertex cover](/primal-dual-weighted-vertex-cover/)
13. [The k-center problem](/k-center-problem/)
14. [Farthest-first traversal](/gonzalez-k-center/)

These show the three main lower bounds, total size, the LP and its dual, and a packing of far-apart points, and the two main methods, greedy and primal-dual. Skip at first the geometric packing problems, the asymptotic scheme, the proof of the $1.7$ bound for first fit, and the two integer program entries, which use randomized rounding.

## Before you start

The chapter uses linear programming throughout. From Volume 15 you need the [linear programming problem](/linear-programming-problem/), the [LP relaxation](/lp-relaxation/), the [dual linear program](/dual-linear-program/), [weak duality](/weak-duality/) and [complementary slackness](/complementary-slackness/), and for group 4 the [submodular function](/submodular-function/). From Volume 7 you need [independent sets](/independent-set/), [maximal matchings](/maximal-matching/) and [hypergraphs](/hypergraph/). From Volume 2 you need the [greedy algorithm](/greedy-algorithm/) and the [probabilistic method](/probabilistic-method/). From Volume 1 you need [linearity of expectation](/linearity-of-expectation/), the [harmonic series](/harmonic-series/) and the [Chernoff bound](/chernoff-bound/). The [metric space](/metric-space/) and the [triangle inequality](/triangle-inequality/) of Volume 5 are needed for $k$-center.

The entries also use NP-hardness, NP-completeness and polynomial-time reductions, whose entries are not yet written; their definitions are in any textbook on computational complexity. The approximation ratio itself is defined again in each entry.
