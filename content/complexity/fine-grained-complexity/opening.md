Edit distance has had an $O(n^2)$ algorithm since the 1970s, and no one has found one in $O(n^{2-\varepsilon})$ time for any $\varepsilon > 0$. NP-hardness says nothing here, because the problem is already in P. Fine-grained complexity asks instead whether the exponent of a polynomial algorithm can be lowered. It answers with reductions that keep exponents: if a faster algorithm for one problem would give a faster algorithm for a problem that many people have tried to speed up, the first problem is hard in that precise sense.

All such lower bounds are conditional. They rest on a few hypotheses that are open, chiefly the Strong Exponential Time Hypothesis (SETH) about $k$-SAT, the conjecture that 3SUM needs about $n^2$ time, and the conjecture that all-pairs shortest paths needs about $n^3$ time. A result of the form "no $O(n^{2-\varepsilon})$ algorithm unless SETH fails" ties a problem to one of them, and many problems turn out to be tied to the same one.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Hypotheses.** SETH, the orthogonal vectors hypothesis, the 3SUM and APSP conjectures, the combinatorial Boolean matrix multiplication conjecture, and the hypotheses on triangles, cliques and hypercliques.
2. **Reductions.** Fine-grained reductions, conditional lower bounds, fine-grained equivalence classes, and the proof that SETH implies the orthogonal vectors lower bound.
3. **Quadratic problems.** Orthogonal vectors, 3SUM, $k$-SUM and convolution 3SUM, with the SETH lower bounds for edit distance and longest common subsequence.
4. **Cubic problems.** Negative triangles, min-plus convolution, and the equivalence between all-pairs shortest paths and negative triangle detection.
5. **Dynamic and online problems.** Online matrix-vector multiplication, its conjecture, and the lower bounds it gives for dynamic problems.

## What to read meanwhile

The SETH results are written in other volumes. [Edit distance hardness](/edit-distance-hardness/) in Volume 8 and the [SETH lower bound for LCS](/backurs-indyk-lcs-lower-bound/) in Volume 6 prove that a strongly subquadratic algorithm would refute SETH, by reductions from orthogonal vectors. The [Fréchet distance](/frechet-distance/) in Volume 13 and [regular expression matching hardness](/backurs-indyk-regex-hardness/) in Volume 9 give more examples. Volume 16 states ETH and SETH in [k-SAT](/k-sat/).

For 3SUM, read the quadratic [3SUM scan](/three-sum-two-pointer-scan/) in Volume 2 and [collinear points](/collinear-points/) in Volume 13, the founding example of 3SUM-hardness. The [reduction lower bound](/reduction-lower-bound/) in Volume 1 explains how such reductions transfer bounds. For the cubic side, [min-plus matrix multiplication](/min-plus-matrix-multiplication/) in Volume 11 is equivalent to all-pairs shortest paths, and [Boolean matrix multiplication](/boolean-matrix-multiplication/) states the combinatorial conjecture.
