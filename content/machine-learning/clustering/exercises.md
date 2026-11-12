1. ◦ Take the points 0, 1, 2, 6 and 12 on a line and $k = 2$. Find the clustering with the least [k-means cost](/k-means-problem/) and the clustering with the least [k-median cost](/k-median-problem/), with their costs. What does each clustering cost under the other objective?

2. ◦ Run [Lloyd's algorithm](/k-means/) on the points 0, 1, 10, 11, 20 and 21 with $k = 3$, starting from the centers 0, 1 and 10. Give the clusters and the cost at the fixed point, and compare them with the optimal 3-means clustering.

3. ◦ For the points 0, 1, 4, 9 and 16 on a line, list the merge heights of [single linkage](/single-linkage-clustering/) and of [complete linkage](/complete-linkage-clustering/). What is the largest spacing of a clustering into 2 clusters, and into 3 clusters?

4. ◦ The classes of six items are $U = \{\{1, 2, 3\}, \{4, 5, 6\}\}$, and a clustering is $V = \{\{1, 2\}, \{3, 4\}, \{5, 6\}\}$. Compute the [purity](/cluster-purity/) of $V$, the [Rand index](/rand-index/) and the [adjusted Rand index](/adjusted-rand-index/).

5. ◦ The points 0, 2, 5, 6 and 10 on a line are clustered as $\{0, 2\}$ and $\{5, 6, 10\}$. Compute the [silhouette](/silhouette-coefficient/) value of each point and the mean silhouette.

6. ◦ Run [DBSCAN](/dbscan/) on the points 0, 1, 2, 3, 5, 6, 7 and 10 on a line with $\varepsilon = 1.5$ and $\mathit{MinPts} = 3$, where $\mathit{MinPts}$ counts the point itself. Which points are core points, border points and noise, and what are the clusters? What changes with $\mathit{MinPts} = 4$?

7. ◦ Two centers sit at 0 and 6, and a point at 2. Give the membership of the point in the first cluster under [fuzzy c-means](/fuzzy-c-means/) with $m = 2$ and with $m = 3$. Then give its posterior probability for the first component of a [Gaussian mixture](/gaussian-mixture-model/) with equal weights, these means and a shared variance $\sigma^2 = 4$, and again with $\sigma^2 = 1$.

8. ◦ Run the farthest-first traversal on the points 0, 3, 4, 9, 10 and 20 with $k = 3$, starting at 0. What radius does it reach, and what is the least radius of 3 centers chosen among the points? Is the ratio within the bound of [k-center hardness](/k-center-hardness/)?

9. ◦ [Ward's method](/ward-method/) considers merging the clusters $\{0, 2\}$ and $\{5, 6, 7\}$ of points on a line. Compute the merge cost $\Delta$ from the sizes and centroids, and check it against the sums of squares before and after the merge.

10. • For the points 1, 2, 6, 7, 8 and 15 on a line, find the optimal k-means cost $W_k$ for $k = 1, 2, 3$, and the optimal clusters for $k = 3$. How many clusterings into 3 intervals of the sorted points are there?

11. • The points 0, 1, 2, 4 and 9 lie on a line, clustered as $\{0, 1, 2\}$ and $\{4, 9\}$. Show that this is a fixed point of Lloyd's algorithm. Then show that the [Hartigan-Wong](/hartigan-wong-algorithm/) test moves one point, and give the new cost.

12. • Seed $k = 2$ centers with [k-means++](/k-means-plus-plus/) on the points 0, 2 and 10. Compute the exact expected cost of the seeds, and compare it with the optimal cost and with the bound $8(\ln k + 2)$.

13. • Three clusters $i$, $j$, $k$ have the sizes $n_i = 2$, $n_j = 1$, $n_k = 3$ and the dissimilarities $d(i, k) = 4$, $d(j, k) = 7$, $d(i, j) = 2$. After $i$ and $j$ merge, use the [Lance-Williams formula](/lance-williams-formula/) to compute the dissimilarity of $i \cup j$ to $k$ for single, complete, average and weighted linkage, and with the Ward coefficients.

14. • Four objects have the dissimilarities $d(a, b) = 2$, $d(a, c) = 6$, $d(a, d) = 10$, $d(b, c) = 5$, $d(b, d) = 9$ and $d(c, d) = 4$. Is $d$ an [ultrametric](/ultrametric/)? Give the cophenetic distances of single linkage and of complete linkage on $d$.

15. • Take the path $a - b - c - d$ with unit weights. Find the second smallest eigenvalue of $(D - W)y = \lambda D y$ and its eigenvector, and the [normalized cut](/normalized-cut/) of each of the three threshold cuts along it. Which cut does the method return, and how does $\lambda_2$ compare with it?

16. • Four items carry $+$ on every pair except $ab$, which carries $-$. Find the optimal number of disagreements of [correlation clustering](/correlation-clustering/) and the expected number for the [pivot algorithm](/pivot-algorithm/).

17. • The eleven points $0, 1, \ldots, 9$ and 11 lie on a line. Find the [maximum spacing](/maximum-spacing-k-clustering/) clustering for $k = 2$ and its k-means cost, and the optimal k-means cost for $k = 2$.

18. • Run [mean shift](/mean-shift/) with a flat kernel of radius $h = 2$ on the points 0, 1, 2, 6, 7 and 9: each step moves to the mean of the data points within distance 2, inclusive. Where does the walk from each point stop? Which points share a stopping point?

19. • The points 0, 1, 5, 9, 10 and 16 on a line are clustered as $\{0, 1, 5\}$, $\{9, 10\}$ and $\{16\}$. Compute the [Dunn index](/dunn-index/), the [Davies-Bouldin index](/davies-bouldin-index/) with $q = 1$ and $p = 2$, and the [Calinski-Harabasz index](/calinski-harabasz-index/). Is the clustering compact and well separated in Dunn's sense?

20. • Run the SWAP phase of [partitioning around medoids](/partitioning-around-medoids/) by hand on the points 0, 1, 2, 3, 4 and 5 with the distance $|x - y|$, $k = 2$, and the medoids 0 and 3. Does any single swap lower the cost? What is the optimal cost?

21. ★ A star has a center joined to $n - 1$ leaves by edges of weight 1, and no other edges. Find the least [Dasgupta cost](/dasgupta-cost/) of a hierarchy on its $n$ vertices, and a tree that reaches it.

22. ★ A clustering function on four points is scale invariant and consistent, in the sense of [Kleinberg's theorem](/kleinberg-impossibility-theorem/). How many partitions can its range hold at most? Give a function that reaches the bound.

23. ★ Let $m$ be even, and put points at $0, 1, \ldots, m - 1$ and at $m + 1$. Show that the k-means cost of the maximum spacing 2-clustering, divided by the optimal 2-means cost, tends to 4 as $m$ grows.

24. ★ Points $x_1 < x_2 < \cdots < x_n$ lie on a line, and all gaps $x_{i+1} - x_i$ are different. How many different hierarchies can [single linkage](/single-linkage-clustering/) produce on them as the gaps vary? Compare the count with the $(2n - 3)!!$ binary hierarchies on $n$ labeled leaves for $n = 4$.

25. ★ The points 0, 1, $L$ and $L + 1$ form two pairs on a line. Find the limit, as $L \to \infty$, of the expected cost of the k-means++ seeds for $k = 2$, divided by the optimal cost. Why is the limit above 1 even though the seeds land in different pairs with probability tending to 1?
