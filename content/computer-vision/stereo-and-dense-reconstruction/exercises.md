1. ◦ A rectified pair has $f = 700$ pixels, baseline $b = 0.12$ m and principal point $(320, 240)$. A pixel at $(460, 300)$ in the left image has [disparity](/disparity/) 28. Find its depth $Z$ and its coordinates $X$ and $Y$ in the left camera frame. Estimate the depth error for a disparity error of 0.2 pixels. How many disparities $0, \ldots, D-1$ must the search cover to see points as near as 0.5 m?

2. ◦ Compute the [census transform](/census-transform/) of the centers of the two $3 \times 3$ windows below. Read the 8 neighbors in row-major order and write bit 1 when the neighbor is darker than the center. Give each string as a binary number and in decimal, and give the Hamming cost of the pair. Then compare the sum of absolute differences of the two windows with the one after the right window is multiplied by 2, and say what happens to the census strings.

| left | | | right | | |
|---|---|---|---|---|---|
| 8 | 21 | 13 | 9 | 25 | 16 |
| 17 | 15 | 9 | 14 | 18 | 12 |
| 15 | 30 | 11 | 20 | 31 | 10 |

3. ◦ Run [block matching](/block-matching-stereo/) with the sum of absolute differences on one row, a window of 3 pixels and disparities $0$ to $3$, with the left pixel $u$ matched to the right pixel $u - d$. The left row is $10, 10, 10, 50, 90, 90, 20, 20, 20, 20$ and the right row is $10, 50, 90, 90, 20, 20, 20, 20, 20, 20$ (positions $0$ to $9$). Give the four costs at $u = 4$ and the chosen disparity. Do the same at $u = 8$ and say what goes wrong there.

4. ◦ The costs at disparities 11, 12 and 13 are 7, 3 and 4. Give the [subpixel disparity](/subpixel-disparity-refinement/) found by the parabola fit and the value of the parabola at its minimum. Then give the disparity found by the equiangular line fit.

5. ◦ The left disparity map of one row is $d_L = (0, 1, 1, 2, 2, 2, 1, 1)$ and the right map is $d_R = (1, 1, 2, 2, 2, 0, 1, 1)$, for positions $0$ to $7$. Left pixel $u$ matches right pixel $u - d_L(u)$. Apply the [left-right consistency check](/left-right-consistency-check/) with tolerance 0 and list the invalid left pixels.

6. ◦ One step of [semi-global matching](/semi-global-matching/) along a path: the previous path costs are $L_{\text{prev}} = (5, 2, 4, 9, 3)$ for disparities $0$ to $4$, the matching costs at the new pixel are $C = (3, 6, 1, 2, 7)$, $P_1 = 1$ and $P_2 = 4$. Compute the new path costs, with the minimum of $L_{\text{prev}}$ subtracted.

7. ◦ [Photometric stereo](/photometric-stereo/) at one pixel uses the lights $s_1 = (0, 0, 1)$, $s_2 = (0.8, 0, 0.6)$ and $s_3 = (0, 0.8, 0.6)$ and measures $I = (0.5, 0.7, 0.1)$. Find $g = \rho n$, the albedo $\rho$, the unit normal $n$ and the surface slopes $p = z_x$ and $q = z_y$, with $n \propto (-p, -q, 1)$.

8. ◦ Which of these pair terms on binary variables are regular in the sense of the [Kolmogorov-Zabih theorem](/graph-representable-energies/)? (a) $[x \ne y]$; (b) $[x = y]$; (c) the table $F(0,0) = 1$, $F(0,1) = 4$, $F(1,0) = 2$, $F(1,1) = 3$; (d) the table $F(0,0) = 0$, $F(0,1) = 1$, $F(1,0) = 1$, $F(1,1) = 3$.

9. ◦ In [TSDF fusion](/tsdf-fusion/), a voxel lies on a camera ray at depth 1.50 m, the truncation is $\mu = 0.05$ m and each reading has weight 1. Four depth images give the readings 1.53, 1.49, 1.62 and 1.42 m along this ray. Give the truncated value from each reading that is used and the fused value after all four. Which reading is skipped, and why?

10. ◦ In [shape from focus](/shape-from-focus/), the sharpness of one pixel peaks at image $m = 7$ of the stack, with $F_6 = 20$, $F_7 = 50$ and $F_8 = 40$. Find the Gaussian-fit offset $\delta$. Image $i$ is focused at depth $2.00 + 0.05\, i$ m; give the estimated depth.

11. ◦ Work in the plane. The object is the unit disc, and each view is a parallel projection whose silhouette is a strip of width 2. Find the area of the [visual hull](/visual-hull/) from two views at right angles and from three views at $60°$ to each other, and compare with $\pi$.

12. • Run [iterated conditional modes](/iterated-conditional-modes/) on a chain of 8 binary sites with $y = (1, 0, 1, 1, 0, 0, 1, 0)$, data cost $2[\ell \ne y_i]$ and pair cost $3[a \ne b]$ between neighbors. Start from $y$ and keep the current label on ties. Give the result and its energy for the visiting order $1, \ldots, 8$ and for the order $8, \ldots, 1$, and find the minimum energy.

13. • Show that in a rectified pair a [plane sweep](/plane-sweep-stereo/) with fronto-parallel planes $Z = Z_j$ warps the right image onto the left by a horizontal shift of $fb/Z_j$ pixels. With $fb = 50$ pixel metres and one plane per integer disparity, how many planes lie between 1 m and 2 m, and how many between 4 m and 8 m?

14. • A thin vertical pole stands 1 m in front of a wall 4 m away, seen by a rectified pair with $f = 500$ and $b = 0.1$ m. Find the two disparities. Show that the ordering constraint of [scanline dynamic programming](/scanline-dynamic-programming-stereo/) is violated by points visible in both images exactly when the pole is narrower than a certain width, and find that width in pixels and in centimetres.

15. • A binary energy has unary terms $\theta_1 = (2, 0)$ and $\theta_2 = (0, 1)$ (the costs of labels 0 and 1) and the pair term $F(0,0) = 0$, $F(0,1) = 3$, $F(1,0) = 1$, $F(1,1) = 2$. Check that it is regular, write $F$ as a constant plus unary terms plus a multiple of $(1 - x_1) x_2$, and build the s-t graph, with $x_i = 0$ meaning that $v_i$ is on the source side. Find the minimum cut and check it against all four labelings.

16. • Show that $V(a, b) = \min((a - b)^2, 9)$ is not a metric. For neighbors with $f_p = 0$, $f_q = 2$ and $\alpha = 1$, write the four values of the [alpha-expansion](/alpha-expansion/) pair term and show that it is not regular. For truncated linear $V(a, b) = \min(|a - b|, 3)$ on the labels $0, \ldots, 7$, give $c$ and the approximation bound.

17. • Give a dynamic program that minimizes a Potts energy $\sum_i D_i(\ell_i) + \lambda \sum_i [\ell_i \ne \ell_{i+1}]$ on a chain of $n$ sites with $L$ labels in $O(nL)$ time, not $O(nL^2)$.

18. • In the probabilistic model of [PatchMatch](/patchmatch/), $B$ has $M = 300\,000$ pixels, $C = 25$ offsets lead to the best one and a region has $m = 2000$ pixels. Compute $p$ and the expected number of failed iterations, and compare with the approximation $M/(Cm) - 1/2$. How many random-search samples does one patch get per iteration when the larger side of $B$ is 1024?

19. • Show that box [cost aggregation](/cost-aggregation/) over windows of radius $r$ takes $\Theta(WHD)$ time for every $r$ when each disparity slice of the [cost volume](/cost-volume/) gets its own [integral image](/integral-image/). How many lookups does one window sum need?

20. • Under [shape from shading](/shape-from-shading/) with a Lambertian surface of albedo 1 and the light at the viewer, show that the image is $E = 1/\sqrt{1 + p^2 + q^2}$. Find the image of the hemisphere $z = \sqrt{1 - x^2 - y^2}$ and show that the bowl $z = -\sqrt{1 - x^2 - y^2}$ gives the same image.

21. • [Voxel coloring](/voxel-coloring/) needs an order in which each voxel comes before every voxel it can hide. Show that layers of increasing $z$ give such an order when all camera centers lie in the plane $z = 0$ and the scene lies in $z > 0$. Explain why a ring of cameras around the object admits no such order.

22. • Replace every intensity $I$ of both windows of exercise 2 by $255 - I$. Show that when no neighbor equals its center, a negation complements each census string and leaves the Hamming cost unchanged. Compute the new strings and cost for the windows of exercise 2, and explain the difference.

23. • In TSDF fusion with equal weights, suppose every reading $Z_1, \ldots, Z_N$ along a ray lies within $\mu$ of every voxel near the surface. Show that the zero crossing of the fused function along the ray is at the mean of the readings.

24. • Show that the rectified cameras $K[I \mid 0]$ and $K[I \mid -(b, 0, 0)^{\top}]$, which share one intrinsic matrix $K$, give a fundamental matrix proportional to $\begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & -1 \\ 0 & 1 & 0 \end{pmatrix}$, and that the epipolar constraint then says that the two image points have the same row. Where are the epipoles?

25. ★ Prove that minimizing a Potts energy with $L \ge 3$ labels on a general graph is NP-hard, by a reduction from the [multiway cut problem](/multiway-cut-problem/).

26. ★ Build an s-t graph, with a chain of $L - 1$ nodes per site, whose minimum cut minimizes $\sum_p D_p(\ell_p) + w \sum_{pq} |\ell_p - \ell_q|$ exactly over the labels $0, \ldots, L-1$. Show that each chain is cut once and that the cut edges between the chains of $p$ and $q$ cost $w|\ell_p - \ell_q|$.

27. ★ In the plane, a point is in the external visual hull of a compact set $S$ when every line through it meets $S$. Prove that for a connected $S$ the external visual hull is the [convex hull](/convex-hull/) of $S$. Give a set of two components for which it is not.

28. ★ A disparity $d$ is measured with an error uniform on $[-\tfrac12, \tfrac12]$, and depth is computed as $fb/(d + \varepsilon)$. Show that the mean depth is $fb \ln\frac{2d+1}{2d-1}$, that it is larger than $fb/d$, and that the relative bias is about $1/(12 d^2)$. Give the mean for $fb = 50$ and $d = 10$.

29. ★ A row has two pixels and two disparities, with costs $C_1 = (0, 1)$ and $C_2 = (5, 0)$ and one penalty $P = 3$ for a change ($P_1 = P_2 = 3$). Run semi-global matching with one left-to-right path and take the best disparity at each pixel. Compare with the exact minimizer of $C_1(d_1) + C_2(d_2) + P[d_1 \ne d_2]$. Then show that backtracking from the minimum of the path cost at the last pixel, as in the [Viterbi algorithm](/viterbi-algorithm/), gives the exact minimizer of a single row.
