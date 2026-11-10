The algorithms of this volume prove upper bounds on the ratio: greedy covers within $H_d$, farthest-first traversal within 2. Hardness of approximation proves the matching lower bounds: no polynomial-time algorithm has a better ratio unless P = NP, or unless some other standard conjecture fails. Together the two sides often meet. For [k-center](/k-center-problem/) the ratio 2 is both reached and best possible, and for [maximum coverage](/max-coverage/) the same is true of $1 - 1/e$.

The simplest proofs are gap reductions. Bin packing cannot have ratio below $3/2$ because a reduction from partition makes instances where OPT is either 2 or at least 3, and telling them apart is NP-hard. The deep results need the PCP theorem, which says that every proof of an NP statement can be checked by reading only a few of its bits.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Gaps and reductions.** Gap problems, gap-preserving reductions and L-reductions, the class APX and APX-completeness.
2. **Probabilistically checkable proofs.** The PCP theorem, Håstad's three-bit test, the long code, Label Cover and parallel repetition.
3. **Conjectures.** The Unique Games Conjecture, Raghavendra's theorem on constraint satisfaction, and the exponential time hypothesis for gaps.
4. **Results for single problems.** Inapproximability of set cover, vertex cover, clique, graph colouring, MAX-3SAT, maximum cut, $k$-center, the TSP, the Steiner tree, bin packing and makespan scheduling.

## What to read meanwhile

Chapter 18.1 states many of these results, with the reductions that are short. Read [bin packing NP-hardness](/bin-packing-np-hardness/) for the $3/2$ gap. [Set cover](/set-cover/) and [greedy set cover](/greedy-set-cover/) give the $(1 - \varepsilon)\ln n$ threshold of Dinur and Steurer, and [vertex cover](/vertex-cover/) gives the bounds $\sqrt 2 - \varepsilon$ and, under the Unique Games Conjecture, $2 - \varepsilon$. [k-center](/k-center-problem/) reduces [dominating set](/dominating-set/) to a gap of 2, and [set packing](/set-packing/) inherits the $n^{1 - \varepsilon}$ bound of [independent set](/independent-set/). [Maximum cut](/maximum-cut/) shows that $16/17 + \varepsilon$ is NP-hard and that the Goemans-Williamson ratio is best possible under the Unique Games Conjecture.

For the problems behind the reductions, read [SAT](/sat/) and [3-SAT](/3-sat/) in Volume 16, and [MAX-SAT](/max-sat/), where the ratio $7/8$ is best possible for formulas with exactly three literals per clause. The [traveling salesman problem](/traveling-salesman-problem/) in Volume 15 shows why the general TSP has no ratio at all. The definitions of NP-hardness and of reductions are in any textbook on computational complexity.
