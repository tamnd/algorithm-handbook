1. ◦ Let $x = (1, 2, 2)$, $y = (2, 1, 2)$ and $z = (2, 4, 4)$. Compute the [cosine similarity](/cosine-similarity/) of $x$ and $y$, the angle between them in degrees, and the squared Euclidean distance between $x/\lVert x \rVert$ and $y/\lVert y \rVert$. Then compare $\cos(x, z)$ with $\lVert x - z \rVert$, and say what the pair $x$, $z$ shows about the two measures.

2. ◦ On the real numbers, which of these are metrics: $d_1(x, y) = (x - y)^2$, $d_2(x, y) = \sqrt{|x - y|}$ and $d_3(x, y) = |x - y| / (1 + |x - y|)$? For each one that is not a [metric](/metric-space/), give three numbers that break the [triangle inequality](/triangle-inequality/).

3. ◦ Let $A = \{1, 2, 3, 4\}$, $B = \{3, 4, 5\}$ and $C = \{4, 5, 6, 7\}$. Compute the three [Jaccard](/jaccard-similarity/) distances $1 - J$ between them and check the triangle inequality for each of the three possible middle sets.

4. ◦ The points are $(0, 0)$, $(3, 5)$, $(1, 1)$, $(5, 0)$, $(2, 3)$, $(6, 6)$, $(0, 4)$ and $(4, 2)$, in this order, and the query is $q = (2, 2)$. Run [brute-force nearest neighbor search](/brute-force-nearest-neighbor-search/) for $k = 3$ with a max-heap of squared distances, replacing the top only when a new distance is strictly smaller. Give the answer and the number of replacements. Then answer the [similarity range query](/similarity-range-query/) with radius 3.

5. ◦ Four points are at distances 3, 4.5, 7 and 9 from a query. Which of them are 2-approximate nearest neighbors? For the $(c, r)$-near neighbor problem with $c = 1.5$, list the correct outputs when $r = 4$, when $r = 2$ and when $r = 1.5$.

6. ◦ Insert the words sort, port, sorts, heap, sport, short, cheap and heat, in this order, into a [BK-tree](/bk-tree/) with the edit distance. Draw the tree with its edge keys. Then answer the range query with radius 1 for the word spot: list the nodes whose distance is computed and the subtrees that are skipped.

7. ◦ [Bit-sampling LSH](/bit-sampling-lsh/) stores $n = 10^6$ strings of $d = 32$ bits, with $r = 4$ and $c = 2$. Compute $p_1$, $p_2$ and the exponent $\rho$, and then the parameters $k = \lceil \ln n / \ln(1/p_2) \rceil$ and $L = \lceil n^\rho / p_1 \rceil$ of [locality-sensitive hashing](/locality-sensitive-hashing/).

8. ◦ An index uses keys of $k = 5$ hash functions and $L = 20$ tables. A near pair collides under one function with probability 0.8, and a far pair with probability 0.4. With what probability does each pair become a candidate? How many far pairs out of a million become candidates, in expectation?

9. ◦ The universe is $\{0, 1, 2, 3, 4, 5\}$, $A = \{0, 2, 3\}$ and $B = \{1, 2, 3, 4\}$. Three random orders of the universe are $(3, 1, 0, 4, 2, 5)$, $(4, 0, 5, 1, 3, 2)$ and $(2, 5, 1, 0, 4, 3)$, first element first. Build the [MinHash](/minhash/) signatures of $A$ and $B$ under these orders, give the estimate of $J(A, B)$, and compare it with the true value.

10. ◦ Two vectors make an angle of $60°$. With [random hyperplane LSH](/random-hyperplane-lsh/), what is the probability that one bit agrees, and that a key of 16 bits agrees? How many tables are needed for the pair to share a key in at least one of them with probability 0.9? What is the expected Hamming distance between their 64-bit [SimHash](/simhash/) fingerprints when the votes are Gaussian?

11. • A [ball tree](/ball-tree/) search for the nearest neighbor of $q = (0, 0)$ has found a point at distance 3. Three nodes are left: ball $A$ with center $(5, 0)$ and radius 1.5, ball $B$ with center $(2, 2)$ and radius 1, and ball $C$ with center $(0, 6)$ and radius 3.5. Which of them can be pruned? If the search visits $B$ first and finds a point at distance 2.1 there, which of the others must it still visit?

12. • How many hash functions does MinHash need so that the estimate of $J$ is within $0.05$ of the true value with probability at least $0.99$, by the bound $1 - 2e^{-2k\varepsilon^2}$? How many does it need for $\varepsilon = 0.01$? What does the answer say about the use of MinHash to tell $J = 0.80$ from $J = 0.81$?

13. • Use [prefix filtering](/prefix-filtering/) for a Jaccard self-join with $t = 0.6$ on the sets $x_1 = \{a, c, d, e, f\}$, $x_2 = \{c, d, e, f, g\}$, $x_3 = \{a, b, g, h\}$ and $x_4 = \{e, f, g, h\}$, with the global order $a \prec b \prec \dots \prec h$. Give each prefix, the candidate pairs, and the output. How many of the six pairs are never compared?

14. • In [PPJoin](/ppjoin/) with $t = 0.7$, a set $x$ of size 10 is probed against an indexed set $y$ of size 8. Does the pair pass the size filter? Compute the required overlap $\alpha$, the probing prefix of $x$ and the indexing prefix of $y$. The first shared element is at position $i$ of $x$ and $j$ of $y$. Decide whether the positional filter keeps the pair for $(i, j) = (3, 1)$ and for $(i, j) = (4, 2)$.

15. • An [inverted file index](/inverted-file-index/) holds $n = 10^6$ vectors in $m = 1024$ cells of equal size and probes $n_{\text{probe}} = 8$ cells per query. How many distances does one query compute? With $n_{\text{probe}} = 8$ fixed, which number of cells minimizes this count, and what is the minimum?

16. • A [product quantizer](/product-quantization/) splits vectors of $\mathbb{R}^4$ into two blocks of two coordinates, with the codebooks $\{(0, 0), (2, 2)\}$ for the first block and $\{(1, 0), (3, 1)\}$ for the second. Encode $x = (1.8, 2.1, 0.8, 0.2)$. For the query $q = (1, 1, 2, 1)$, build the two lookup tables of squared distances and compute the asymmetric estimate of $\lVert q - x \rVert^2$; compare it with the exact value. Then find the memory for $10^9$ vectors of dimension 96 stored as 32-bit floats, and as codes with $m = 12$ blocks and $k^* = 256$ centroids, codebooks included.

17. • Let $a = (5, 0)$, $b = (2, 2)$, $c = (0, 1)$ and $q = (1, 1)$. Find the answer to [maximum inner product search](/maximum-inner-product-search/), the nearest neighbor of $q$, and the stored vector of greatest cosine similarity with $q$. Show that when all stored vectors have the same length, the three questions always have the same answer.

18. • The points $0, 2, 3, 7, 12$ lie on a line. Answer the [reverse nearest neighbor](/reverse-nearest-neighbor-search/) query for $q = 5$ and for $q = 9.6$. Then prove that on a line no query has more than two reverse nearest neighbors, when ties do not occur.

19. • Build the [2-nearest neighbor graph](/k-nearest-neighbor-graph/) of the points $0, 1, 2, 10, 11, 12$ on a line. Run greedy search for the query 11 from the point 0, moving each time to the neighbor closest to the query while it improves. Where does it stop? Which single added edge lets greedy search reach 11 from 0, and which entry of the chapter builds such edges on purpose?

20. • For the points $0, 3, 7, 9, 10, 15$ on a line and $k = 2$, compute the $k$-occurrence $N_2(x)$ of every point. Check that the mean is 2, and name the hub and the anti-hub. Explain in one sentence why the anti-hub is the point it is.

21. • An [HNSW](/hnsw/) index holds $n = 10^6$ elements with $M = 16$, so that $\Pr[\ell \ge j] = 16^{-j}$. Find the expected number of elements on layers 1 to 5 and the expected top level. With at most $M_0 = 32$ links on layer 0 and $M$ links on each upper layer, bound the expected number of links, and the memory for them with 4-byte identifiers.

22. • For the points $0, 1, 3, 4, 8$ on a line, someone proposes the [cover tree](/cover-tree/) levels $C_3 = \{0\}$, $C_2 = \{0, 8\}$, $C_1 = \{0, 4, 8\}$, $C_0 = \{0, 3, 4, 8\}$ and $C_{-1} = \{0, 1, 3, 4, 8\}$. Check nesting, covering and separation level by level. Find the invariant that fails, repair the levels, and give the parent of each point at the level where it first appears.

23. • Solve the all-pairs form of [fixed-radius near neighbors](/fixed-radius-near-neighbors/) with $r = 1$ for the points $(0.2, 0.3)$, $(0.9, 0.8)$, $(1.6, 0.4)$, $(2.5, 2.2)$, $(1.1, 1.9)$, $(3.4, 0.1)$ and $(2.7, 1.4)$, with a grid of unit cells in which each point is compared with the points of its own cell and the eight cells around it. Give the cell of each point, the number of distances computed, and the pairs found. Compare with a scan of all pairs.

24. ★ Use random hyperplanes to prove that the angle $\theta(x, y)$ between nonzero vectors satisfies the triangle inequality, by comparing the probabilities that a random hyperplane separates $x$ from $z$, $x$ from $y$ and $y$ from $z$. Then explain why the same proof does not apply to $1 - \cos(x, y)$.

25. ★ The expansion constant of a finite set $S$ is the least $c$ with $|B(p, 2r)| \le c\,|B(p, r)|$ for all $p \in S$ and $r > 0$, using closed balls. Compute it for $S = \{1, 2, \dots, 10\}$ and for $S = \{1, 2, 4, \dots, 2^m\}$. What does the second set show about the use of the expansion constant as a measure of [intrinsic dimensionality](/intrinsic-dimensionality/)?

26. ★ A crawler keeps $2^{34}$ SimHash fingerprints of 64 bits and must find all fingerprints within Hamming distance 3 of a new one. One design splits the bits into 4 blocks of 16 and keeps 4 sorted copies, each keyed by one block. Another splits them into 6 blocks of 11, 11, 11, 11, 10 and 10 bits and keeps one copy for each choice of 3 blocks as the key. Prove that both designs find every match, and compare the number of copies and the expected number of fingerprints checked per query, treating the stored fingerprints as random.

27. ★ To save space, a MinHash signature keeps only the lowest bit of each minimum. Assume that when two minima differ, their lowest bits agree with probability $1/2$, independently of everything else. Show that the bits agree with probability $(1 + J)/2$, and turn this into an estimator of $J$. Two signatures of 64 bits agree in 52 positions: estimate $J$. At $J = 0.6$, compare the variance of this estimator with that of plain MinHash over the same number of positions, and decide which needs less memory for the same variance when a plain minimum takes 32 bits.

28. ★ Take the setting of Exercise 7, $n = 10^6$, $p_1 = 0.875$ and $p_2 = 0.75$. Model the work of one query as $L(k + n p_2^k)$: $kL$ hash evaluations plus the expected number of far points that collide with the query, with $L = p_1^{-k}$ tables, not rounded. Evaluate it at $k = 49$, then find the $k$ that minimizes it, and explain why the choice $k = \lceil \ln n / \ln(1/p_2) \rceil$ is not the best one for this cost.
