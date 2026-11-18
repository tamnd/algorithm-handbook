1. $Z = 700 \cdot 0.12 / 28 = 3$ m, $X = 140 \cdot 3 / 700 = 0.6$ m and $Y = 60 \cdot 3/700 \approx 0.257$ m. The depth error is about $9 \cdot 0.2 / 84 \approx 0.021$ m. At 0.5 m the disparity is $84 / 0.5 = 168$, so $D = 169$.

2. Left: $10101001_2 = 169$. Right: $10111001_2 = 185$. They differ in one bit, so the Hamming cost is 1. The sum of absolute differences is 24 and becomes 171 when the right window is doubled, while the right census string does not change, because doubling keeps the order of the values.

3. At $u = 4$ the costs for $d = 0, 1, 2, 3$ are $180, 110, 0, 80$, so $d = 2$. At $u = 8$ all four costs are 0: the row is constant there, and the winner is decided by the tie rule, not by the data.

4. The parabola gives $\delta = (7 - 4)/(2(7 - 6 + 4)) = 0.3$, so $d = 12.3$, with minimum value $3 - (7-4)^2/(8 \cdot 5) = 2.775$. The equiangular fit uses $m = \max(7, 4) - 3 = 4$ and $\delta = 3/8$, so $d = 12.375$.

5. Pixels 0, 3 and 6 are invalid. Pixel 0 points outside the right image; for pixel 3, $d_R(1) = 1 \ne 2$; for pixel 6, $d_R(5) = 0 \ne 1$.

7. The first light gives $g_z = 0.5$; then $g_x = (0.7 - 0.3)/0.8 = 0.5$ and $g_y = (0.1 - 0.3)/0.8 = -0.25$. So $\rho = |g| = 0.75$, $n = (2/3, -1/3, 2/3)$, $p = -n_x/n_z = -1$ and $q = -n_y/n_z = 0.5$.

9. With $\eta = Z - 1.50$, the readings give $0.6$, $-0.2$ and $1$ (truncated from 2.4). The reading 1.42 gives $\eta = -0.08 < -\mu$, so the voxel lies far behind that surface and is skipped. The fused value is $1.4/3 \approx 0.467$.

10. $\delta = \tfrac12 (\ln 20 - \ln 40)/(\ln 20 - 2 \ln 50 + \ln 40) \approx 0.304$, so the depth is $2.00 + 0.05 \cdot 7.304 \approx 2.365$ m.

12. The start has energy 15. The order $1, \ldots, 8$ ends after two sweeps at $(0,0,1,1,0,0,0,0)$, and the reverse order at $(1,1,1,1,0,0,1,1)$, both with energy 10. The unique minimum is $(1,1,1,1,0,0,0,0)$ with energy 7.

15. $F = x_1 + x_2 + 2(1 - x_1)x_2$. The energies of $(0,0), (0,1), (1,0), (1,1)$ are $2, 6, 1, 3$. The graph has $s \to v_1$ of capacity 1, $s \to v_2$ of capacity 2, $v_1 \to t$ of capacity 2 and $v_1 \to v_2$ of capacity 2. The minimum cut is $S = \{s, v_2\}$ with value 1, the labeling $(1, 0)$.

17. Let $M_i(\ell)$ be the least cost of the first $i$ sites with $\ell_i = \ell$. Then $M_i(\ell) = D_i(\ell) + \min\big(M_{i-1}(\ell),\ \min_k M_{i-1}(k) + \lambda\big)$, and the inner minimum is computed once per site.

25. Given a graph with terminals $t_1, \ldots, t_k$, give each terminal a data cost that forces label $i$ on $t_i$, give the other vertices zero data cost, and use the edge weights as Potts weights. A labeling of cost $E$ is a multiway cut of weight $E$ and the reverse also holds.

26. In the chain of $p$, the edge between nodes $\ell$ and $\ell + 1$ carries $D_p(\ell)$ plus a large constant, and reverse edges of infinite capacity force one cut per chain. Edges of weight $w$ join node $\ell$ of $p$ to node $\ell$ of $q$ in both directions; exactly $|\ell_p - \ell_q|$ of them cross the cut.

27. If $P$ is outside the convex hull, a separating line through $P$ misses $S$. If $P$ is inside, every line through $P$ has points of $S$ on both closed sides, and a connected set that meets both sides meets the line. Two discs of radius 1 centred at $(\pm 3, 0)$ give a counterexample: the line $x = 0$ misses both.

28. Integrate $fb/(d + \varepsilon)$ over $\varepsilon$; the bias is positive by Jensen's inequality, since $1/x$ is convex. Expand $\ln\frac{1 + 1/(2d)}{1 - 1/(2d)}$. For $fb = 50$ and $d = 10$ the mean is about 5.0042 m, against 5 m.

29. The path costs are $L_1 = (0, 1)$ and $L_2 = (5, 1)$, so winner takes all picks $(0, 1)$ with energy 3, while the minimizer is $(1, 1)$ with energy 1. The path cost at the last pixel is the least prefix energy ending in each disparity minus constants, so following the minimizing predecessors back gives the exact row minimizer.
