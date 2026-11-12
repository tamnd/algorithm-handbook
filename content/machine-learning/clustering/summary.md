## What to remember

- Every method answers a stated **objective**: the [k-means cost](/k-means-problem/) $\sum_x \min_c \|x - c\|^2$, the [k-median cost](/k-median-problem/) $\sum_x \min_c d(x, c)$, the k-center radius, the spacing, a density level or a linkage rule. Optimal k-means is NP-hard for $k = 2$ in general dimension and for general $k$ in the plane, and in a metric k-center has no $(2 - \varepsilon)$-approximation unless P = NP.
- **Lloyd's algorithm** costs $O(nkd)$ per iteration and never raises the cost, but its fixed point can be arbitrarily worse than the optimum, and some inputs in the plane need $2^{\Omega(n)}$ iterations. **k-means++** seeds have expected cost at most $8(\ln k + 2)$ times the optimum, a factor $\Theta(\log k)$ that is tight for the seeding.
- **Single linkage** is Kruskal's algorithm stopped at $k$ components. On every input it gives the largest spacing, the $(k-1)$-th largest edge of the minimum spanning tree, and [SLINK](/slink/) builds its tree in $\Theta(n^2)$ time and $\Theta(n)$ memory.
- The **reducible** linkages, single, complete, average, weighted and Ward, run in $O(n^2)$ time with the [nearest-neighbor chain](/nearest-neighbor-chain/), against $\Theta(n^3)$ naively. Ward merges the pair with the least cost increase $\frac{n_i n_j}{n_i + n_j}\|c_i - c_j\|^2$, greedily, so its cut into $k$ clusters need not be an optimal k-means clustering.
- **Density methods** have no single objective. [DBSCAN](/dbscan/) joins the core points, those with $|N_\varepsilon(p)| \ge \mathit{MinPts}$, into connected groups; [OPTICS](/optics/) and [HDBSCAN](/hdbscan/) answer for all radii at once. [Mean shift](/mean-shift/) climbs a kernel density estimate with no global guarantee.
- **Graph methods.** [Spectral clustering](/spectral-clustering/) is exact when the graph has $k$ connected components, with no general guarantee otherwise. The least [normalized cut](/normalized-cut/) is NP-hard to find and at least $\lambda_2$ of $(D - W)y = \lambda D y$.
- **Scores.** The [adjusted Rand index](/adjusted-rand-index/) is 1 for equal partitions and 0 on average under the permutation model; the Rand index, purity and NMI are not corrected for chance. By [Kleinberg's theorem](/kleinberg-impossibility-theorem/), for $n \ge 2$ no clustering function is scale invariant, rich and consistent at once.

| Method | Objective or model | What is guaranteed | Kind | Time |
|---|---|---|---|---|
| Lloyd's k-means | k-means cost | cost never rises; local optimum only | every run | $O(nkd)$ per iteration |
| k-means++ seeding | k-means cost | $\le 8(\ln k + 2) \cdot \mathrm{OPT}$ | in expectation | $\Theta(nkd)$ |
| Farthest-first traversal | k-center radius | $\le 2 \cdot \mathrm{OPT}$, best possible | every input, metric | $O(nk)$ distances |
| PAM | k-median, medoids | $\le 5 \cdot \mathrm{OPT}$ at a single-swap optimum | every input, metric | $O(k(n-k)n)$ per pass |
| Single linkage (SLINK) | spacing | optimal spacing for every $k$ | every input | $\Theta(n^2)$ |
| NN-chain (Ward, complete, average) | linkage rule | the same tree as the greedy method | every input, no ties | $O(n^2)$ |
| DBSCAN | density, radius $\varepsilon$ | exactly its own clusters | every input | $\Theta(n^2 d)$ |
| HDBSCAN | density, all radii | most stable clusters of its tree | every input | $O(n^2(d + \log n))$ |
| Mean shift | modes of a kernel density | density never falls on a walk | heuristic | $O(Tn^2 d)$ |
| EM for a Gaussian mixture | likelihood | likelihood never falls; local maximum | heuristic | $O(nkd^2 + kd^3)$ per pass |
| Spectral clustering | relaxed normalized cut | exact for $k$ components | special inputs only | $O(n^2 d + n^3 + nk^2 t)$ |
| Pivot algorithm | correlation clustering | $\le 3 \cdot \mathrm{OPT}$ | in expectation, complete graphs | $O(n + m)$ |

: Clustering methods and their guarantees, for $n$ points in dimension $d$, $k$ clusters, $t$ or $T$ iterations and $m$ positive pairs. Times use brute-force distances. DBSCAN is unique up to border points near two clusters.

## Choosing a method

For points in a vector space and a known $k$, run Lloyd's algorithm from k-means++ seeds several times and keep the cheapest run. Use PAM when only a dissimilarity matrix is given, and a Gaussian mixture when clusters are elongated or each point needs a probability of membership. Use mini-batch k-means or BIRCH when full passes are too slow.

When $k$ is unknown or the clusters have odd shapes, use HDBSCAN, or DBSCAN when a radius is natural; both leave outliers as noise. For a graph or a similarity matrix, use spectral clustering, and for $+$ and $-$ judgments on pairs, the pivot algorithm. Use a hierarchical method when the nesting is the answer: Ward for compact clusters, single linkage for chains. Compare with known classes through the adjusted Rand index, not the plain one.
