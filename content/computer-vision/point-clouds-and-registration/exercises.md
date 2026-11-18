1. ◦ Run [voxel grid downsampling](/voxel-grid-downsampling/) with voxel size 0.5 and origin $(0, 0)$ on the planar points $(0.1, 0.2)$, $(0.4, 0.4)$, $(0.6, 0.1)$, $(0.9, 0.3)$ and $(0.2, 0.7)$. List the output points. Repeat with the origin moved to $(0.25, 0)$.

2. ◦ Compute the [chamfer distance](/point-set-chamfer-distance/) between $S_1 = \{(0,0), (1,0), (5,0)\}$ and $S_2 = \{(0,1), (3,0)\}$ in the sum form with squared distances. Give both one-sided sums, the mean form and the Hausdorff distance.

3. ◦ Six points lie on a line: five with spacing 1, and one 6 away from its nearest neighbor. With $k = 1$, the mean nearest distances are $d = (1, 1, 1, 1, 1, 6)$. Apply [statistical outlier removal](/statistical-outlier-removal/) with the sample standard deviation and $\alpha = 1, 2, 3$. Which settings remove the far point? How many points can be removed at most when $\alpha = 1$?

4. ◦ [Estimate the normal](/point-cloud-normal-estimation/) of the neighborhood $(0, 0, 0)$, $(2, 0, 1)$, $(0, 2, 0)$, $(2, 2, 1)$. Give the centroid, the covariance matrix (divided by 4), its eigenvalues, the unit normal and the surface variation. Orient the normal toward a sensor at $(0, 0, 10)$.

5. ◦ A sensor has $f = 500$ pixels and principal point $(320, 240)$. Pixel $(420, 240)$ of a [range image](/range-image/) holds 2.0 m. Give the 3D point if the value is the distance along the ray, and if it is the depth $Z$.

6. ◦ A [spin image](/spin-images/) is built at $p = (0, 0, 0)$ with normal $n = (0, 0, 1)$. Give the coordinates $(\alpha, \beta)$ of the points $(3, 4, 2)$ and $(-4, 3, 2)$. What changes when the normal is flipped?

7. ◦ For the [4PCS](/four-points-congruent-sets/) base $a = (0, 0)$, $b = (6, 0)$, $c = (1, -2)$, $d = (3, 4)$ in a plane, find the crossing point $e$ of the segments $ab$ and $cd$, the ratios $r_1 = |a - e|/|a - b|$ and $r_2 = |c - e|/|c - d|$, and the lengths $d_1 = |a - b|$ and $d_2 = |c - d|$. Apply the affine map $(x, y) \mapsto (2x + y, y)$ and recompute the four numbers.

8. ◦ [Geometric hashing](/geometric-hashing/) in the plane stores, for each of $K$ models of $m$ points, every point in the coordinates of every ordered basis of three of its points. How many entries does the table hold for $K = 10$ and $m = 20$? How many for bases of two points, which suffice for similarity maps?

9. ◦ [Fast global registration](/fast-global-registration/) uses $\rho(x) = \mu x^2/(\mu + x^2)$ and the weight $l = (\mu/(\mu + x^2))^2$. With $\mu = 1$, compute $\rho$ and $l$ for the residuals 0.1 and 2, and check that $l x^2 + \mu(\sqrt{l} - 1)^2 = \rho(x)$ for both.

10. ◦ An [NDT](/normal-distributions-transform/) cell holds the points $(0, 0)$, $(2, 0)$, $(0, 2)$ and $(2, 2)$. Compute its mean and covariance (divided by the number of points), and the score term of the scan points $(1, 1)$ and $(2, 1)$.

11. • Run [iterative closest point](/iterative-closest-point/) with translation only on the line, with source $P = \{0, 2, 4\}$ and target $Q = \{1.2, 3.2, 5.2, 9\}$. The fit for fixed matches is $t = \frac{1}{3}\sum_i (q_{c(i)} - p_i)$. Start at $t = 0$, then at $t = 0.5$. Give the matches, the mean squared errors and the final $t$ in each case, and show that the first result is a local minimum of the cost.

12. • In [point-to-plane ICP](/point-to-plane-icp/), the $6 \times 6$ matrix is singular when the target can slide on itself. Give the dimension of the space of such small motions, and the motions themselves, when the target is a plane, a sphere and an infinite circular cylinder.

13. • The source is $P = \{0, 2, 4, 10\}$ on a line and the target is $Q = \{1.2, 3.2, 5.2\}$; the point 10 has no partner. At $t = 1$, compute the next translation of plain ICP and of [trimmed ICP](/trimmed-icp/) with $\xi = 0.75$.

14. • [Efficient RANSAC](/efficient-ransac-shape-detection/) with uniform draws picks three points per candidate. A cloud has $10^5$ points and the smallest wanted shape has 500. How many draws give probability 0.99 of at least one draw with all three points on that shape? Explain how drawing the second and third points from one octree cell around the first changes this.

15. • In the first step of [TEASER](/teaser-registration/), with scale 1, a pair of matches $(i, j)$ passes when $\big||b_j - b_i| - |a_j - a_i|\big| \le 2\beta$. Take $\beta = 0.05$, $a = ((0,0), (1,0), (0,2), (3,3), (4,1))$ and $b = ((1,1), (1,2), (-1,1), (-2,4), (-1,6))$. Find the pairs that pass and the maximum clique. Which match is an outlier, and which of its pairs still passes?

16. • In [coherent point drift](/coherent-point-drift/) on the line with no outlier term ($w = 0$), $\sigma^2 = 1$, data $X = \{0, 3\}$ and centroids $Y = \{0, 1\}$, compute the posteriors $P_{ki}$. Then find the translation $t$ that minimizes $\sum_{k,i} P_{ki}(x_i - y_k - t)^2$.

17. • Show that ICP lowers, step by step, the one-sided chamfer distance from the moved source to the target, and that a chamfer distance of zero in both directions means the two sets coincide.

18. • A cloud has $n$ points with mean neighbor distance 1, and $j$ outliers with a large mean distance. Use the bound of statistical outlier removal, at most $n/(1 + \alpha^2)$ removed points, to show that with $\alpha = 3$ some outliers survive whenever they make up more than 10% of the cloud.

19. • In an NDT cell of a straight wall the points are $(0,0)$, $(1,0)$, $(2,0)$ and $(3,0)$. The covariance is singular; raise its smaller eigenvalue to 0.001 times the larger. Compute the score terms of $(1.5, 0.1)$ and $(3, 0)$, and explain what the result says about sliding along a wall.

20. • [Consistent normal orientation](/consistent-normal-orientation/) on a planar example: the normals are $n_1 = (0, 1)$, $n_2 = (0.28, -0.96)$, $n_3 = (-0.6, 0.8)$ and $n_4 = (-0.8, -0.6)$, and the neighbor graph has the edges $12, 23, 34, 13, 24$ with weights $1 - |n_i \cdot n_j|$. Find the minimum spanning tree, keep $n_1$, propagate along the tree, and give the final normals.

21. • A cloud has 9 points on a grid with spacing 1, and two outliers that lie 0.5 apart from each other and far from the grid. It is cleaned by statistical outlier removal with $k = 1$. Explain why they survive any $\alpha$, and what change of $k$ catches them.

22. ★ In the plane, the best rotation for centered point pairs $(x_i, y_i) \mapsto (x'_i, y'_i)$ maximizes $\sum_i \langle R(\theta) p_i, p'_i \rangle$. Prove that $\theta = \operatorname{atan2}\big(\sum (x_i y'_i - y_i x'_i), \sum (x_i x'_i + y_i y'_i)\big)$. Apply it to $(0,0), (2,0), (0,2) \mapsto (1,1), (1,3), (-1,1)$ and find the translation.

23. ★ [Robust point matching](/robust-point-matching/) normalizes a positive matrix by alternating row and column scaling (Sinkhorn). For a $2 \times 2$ matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$, show that $ad/(bc)$ does not change under the scalings, and find the doubly stochastic limit of $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$.

24. ★ TEASER finds a maximum clique exactly, with a worst case that grows like $3^{m/3}$. Show that some graph on $m = 3k$ vertices has $3^k$ maximal cliques. How many is that for $m = 30$?

25. ★ Show that the chamfer distance with squared distances satisfies no relaxed triangle inequality: for every $C$ there are finite sets with $d(S_1, S_3) > C\,(d(S_1, S_2) + d(S_2, S_3))$.

26. ★ For translation-only registration on the line, with sources $p_1, \ldots, p_n$ and sorted targets $q_1 < \cdots < q_m$, show that $E(t) = \sum_i \min_j (p_i + t - q_j)^2$ is a piecewise quadratic function with at most $n(m-1)$ breakpoints, and give an $O(nm \log(nm))$ algorithm that finds its global minimum exactly.
