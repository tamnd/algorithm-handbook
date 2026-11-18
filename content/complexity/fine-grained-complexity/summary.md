## What to remember

- A fine-grained reduction from $(A, a(n))$ to $(B, b(n))$ guarantees that for every $\varepsilon > 0$ there is a $\delta > 0$ such that an $O(b(n)^{1-\varepsilon})$ algorithm for $B$ gives an $O(a(n)^{1-\delta})$ algorithm for $A$. Its own running time must stay below $a(n)^{1-\delta}$.
- SETH says that for every $\varepsilon > 0$ there is a $k$ such that $k$-SAT on $n$ variables has no $O(2^{(1-\varepsilon)n})$ algorithm. ETH says that 3-SAT has no $2^{o(n)}$ algorithm. SETH implies ETH, and ETH implies $\mathsf{P} \ne \mathsf{NP}$; all three are open.
- Split and list: cutting $N$ variables into two halves gives $n = 2^{N/2}$ vectors with one coordinate per clause, and after sparsification $d = O(\log n)$. An $O(n^{2-\varepsilon})$ algorithm for orthogonal vectors would decide CNF-SAT in time $2^{(1-\varepsilon/2)N}$ times a polynomial, so SETH implies OVH.
- Under OVH, and so under SETH, edit distance, LCS and the Fréchet distance of two sequences of length $N$ have no $O(N^{2-\delta})$ algorithm.
- APSP, the min-plus product and negative triangle detection are equivalent under subcubic reductions: an $O(n^{3-\varepsilon})$ algorithm for one gives one for all three.
- 3SUM takes $O(n^2)$ time by sorting and two pointers, and Convolution 3SUM is equivalent to it. Preprints of October 2026, not yet refereed, give deterministic $O(n^{1.9992})$ time for integer 3SUM and $O(n^{2.9995})$ for APSP with polynomial weights; if they hold, the 3SUM and APSP conjectures are false.
- Under the OMv conjecture, no dynamic $s$-$t$ shortest path algorithm with polynomial preprocessing has update time $m^{1/2-\varepsilon}$ and query time $m^{1-\varepsilon}$.
- The algorithmic method: a satisfiability algorithm for a circuit class $\mathcal{C}$ that beats $2^n$ by a superpolynomial factor implies $\mathsf{NEXP} \not\subseteq \mathcal{C}$. Williams used it in 2011 to prove $\mathsf{NEXP} \not\subseteq \mathsf{ACC}^0$, an unconditional result.

## The hypotheses

| Hypothesis | Claimed bound | Typical consequences | Status in late 2026 |
|---|---|---|---|
| ETH | 3-SAT needs $2^{\Omega(n)}$ | no $f(k) n^{o(k)}$ for clique | open |
| SETH | $k$-SAT needs $2^{(1-o(1))n}$ as $k$ grows | OV, edit distance, LCS | open |
| OVH | OV in dimension $c \log n$ needs $n^{2-o(1)}$ | edit distance, LCS, diameter | open |
| 3SUM | $n^{2-o(1)}$ | collinear points, many geometry problems | refuted if the preprints hold |
| APSP | $n^{3-o(1)}$ with polynomial weights | negative triangle, min-plus product | refuted if the preprint holds |
| Zero and min-weight $k$-clique | $n^{k-o(1)}$ | exact and minimum weight triangle | refuted if the preprint holds |
| OMv | $n^{3-o(1)}$ online | dynamic reachability, shortest paths | open, not affected |
| Combinatorial BMM | $n^{3-o(1)}$ for combinatorial algorithms | combinatorial triangle detection | open |
| Triangle detection | $m^{4/3-o(1)}$ | approximate short cycles, distance oracles | open, not affected |
| Set cover | $2^{(1-o(1))n}$ for bounded set size | Steiner tree, subset sum | open; not known to follow from SETH |
| Hyperclique | $n^{k-o(1)}$ for $d \ge 3$ | Max-3-SAT and related problems | open |

: The hypotheses of the chapter, in the forms the entries use. "Refuted if the preprints hold" refers to the unrefereed preprints of October 2026 that the entries cite.

## Using the chapter

To explain why a problem with a simple $n^2$ or $n^3$ algorithm resists improvement, start from the problem whose structure is closest. Pairs of objects that must agree in every coordinate suggest orthogonal vectors, and so a bound under OVH and SETH; prefer OVH, since it is the weaker assumption. Path, distance and matrix problems with a cubic algorithm suggest negative triangle. Problems where an object changes and is queried suggest OMv. A bound from 3SUM or APSP is still a valid reduction, but after the 2026 preprints it should be stated as a relation between problems, not as evidence of hardness.

Check three things in any reduction. Its running time must be smaller than the bound it transfers. The size of the new instance fixes the loss in the exponent: a map from $n$ vectors to strings of length $N = n \cdot d^{O(1)}$ keeps the quadratic bound, a map to length $n^{1.5}$ does not. And the statement must name its hypothesis, because the hypotheses are of different strength and some are known not to follow from others.
