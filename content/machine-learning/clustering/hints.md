1. The k-means optimum is $\{0, 1, 2\}, \{6, 12\}$ with cost $2 + 18 = 20$. The k-median optimum is $\{0, 1, 2, 6\}, \{12\}$ with cost 7, with the median 1 or 2. The k-median cost of the k-means clustering is $2 + 6 = 8$. The k-means cost of the k-median clustering is $83/4$, since the mean of 0, 1, 2 and 6 is $9/4$. The outlier 12 pulls k-means harder than k-median.

3. Single linkage merges at the gaps 1, 3, 5 and 7, in that order. Complete linkage merges $\{0, 1\}$ at 1, adds 4 at 4, merges $\{9, 16\}$ at 7, and joins everything at 16. The largest spacing is 7 for two clusters and 5 for three: cut the largest gaps.

4. There are 15 pairs. Six pairs share a class, three share a cluster, and two, $\{1, 2\}$ and $\{5, 6\}$, share both. So 2 pairs are together in both and 8 are apart in both, and the Rand index is $10/15 = 2/3$. The expected index is $6 \cdot 3 / 15 = 6/5$ and the maximum is $(6 + 3)/2 = 9/2$, so the ARI is $(2 - 6/5)/(9/2 - 6/5) = 8/33$. The purity is $(2 + 1 + 2)/6 = 5/6$.

6. With $\mathit{MinPts} = 3$ the core points are 1, 2 and 6. The clusters are $\{0, 1, 2, 3\}$ and $\{5, 6, 7\}$. The points 0, 3, 5 and 7 are border points, and 10 is noise. With $\mathit{MinPts} = 4$ no neighborhood holds four points, so every point is noise.

11. Each point is nearest to its own center: 4 is 2.5 from 6.5 and 3 from 1. Moving 4 from $\{4, 9\}$ to $\{0, 1, 2\}$ removes $\tfrac{2}{1} \cdot 2.5^2 = 12.5$ and adds $\tfrac{3}{4} \cdot 3^2 = 6.75$. The size factors make the move pay. The cost falls from $29/2$ to $35/4$, which is the optimum.

12. Condition on the first seed. From 0 the expected cost is $82/13$, from 2 it is $128/17$, and from 10 it is 4. The mean of the three is $1314/221 \approx 5.95$. The optimal cost is 2, so the ratio is about 2.97, far below $8(\ln 2 + 2) \approx 21.5$.

15. The eigenvalue is $\lambda_2 = 1/2$ with $y = (1, 1/2, -1/2, -1)$. The three threshold cuts have the normalized cuts $6/5$, $2/3$ and $6/5$, so the method returns $\{a, b\} \mid \{c, d\}$. The relaxation gives a lower bound: $\lambda_2 = 1/2 \le 2/3$.

16. One cluster with all four items has one disagreement, the pair $ab$, and no clustering has zero. A pivot at $c$ or $d$ takes all four items, with cost 1. A pivot at $a$ takes $\{a, c, d\}$ and leaves $b$ alone, cutting $bc$ and $bd$, with cost 2; $b$ is symmetric. The expectation is $(1 + 1 + 2 + 2)/4 = 3/2$.

21. The answer is $(n - 1)(n + 2)/2$. Peel one leaf off at each level and keep the center to the bottom: the edge to the first leaf peeled off pays $n$, the next $n - 1$, and the last pays 2. For the lower bound, order the leaves by the size of their lowest common ancestor with the center. The $i$-th leaf's ancestor holds the center and at least $i$ leaves.

22. Kleinberg's proof shows that the range is an antichain: no partition in it refines another. Four points have 7 partitions into two blocks and 6 into three. Each three-block partition lies below 3 two-block partitions, and each two-block partition lies above at most 3 three-block partitions. Count the neighbors of any set of three-block partitions to show that no antichain beats the 7 two-block partitions. Single linkage stopped at two clusters reaches 7.

23. The gap of 2 is the only largest gap, so the maximum spacing clustering is $\{0, \ldots, m - 1\}, \{m + 1\}$ with cost $m(m^2 - 1)/12$. Splitting near the middle gives two runs of about $m/2$ points, each costing about $m^3/96$. The ratio tends to $(m^3/12)/(m^3/48) = 4$.

24. On a line single linkage only merges neighboring clusters, so every hierarchy keeps the leaves in line order, and each internal node stands for the gap it closes. Any ordered binary tree arises: give each internal node a gap that grows with its height. The count is the Catalan number $C_{n-1}$, which is 5 of 15 for $n = 4$.

25. The optimal cost is 1. Say the first seed is 0. The second seed lands in the far pair with probability tending to 1, and then the cost is 2, since seeds are data points, not means. It lands on 1 with probability $1/(1 + L^2 + (L + 1)^2)$, and then the cost is about $2L^2$, so this rare event adds about 1. The limit is 3.
