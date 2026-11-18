1. With origin $(0,0)$: $(0.25, 0.3)$, $(0.75, 0.2)$ and $(0.2, 0.7)$. With origin $(0.25, 0)$: $(0.1, 0.2)$, $(0.5, 0.25)$, $(0.9, 0.3)$ and $(0.2, 0.7)$. Four points instead of three: the output depends on where the grid starts.

2. From $S_1$: $1 + 2 + 4 = 7$. From $S_2$: $1 + 4 = 5$. The sum is 12, the mean form $7/3 + 5/2 \approx 4.833$, and the Hausdorff distance is 2.

3. $\mu = 11/6 \approx 1.833$ and $\sigma \approx 2.041$. The thresholds are about 3.875, 5.916 and 7.957, so $\alpha = 1$ and $\alpha = 2$ remove the far point and $\alpha = 3$ keeps it. With $\alpha = 1$ at most $6/2 = 3$ points can be removed.

4. The centroid is $(1, 1, 0.5)$, and the covariance has $C_{xx} = C_{yy} = 1$, $C_{zz} = 0.25$, $C_{xz} = 0.5$ and zeros elsewhere. The eigenvalues are $0, 1, 1.25$. The normal is $(-1, 0, 2)/\sqrt5$, which already points toward the sensor, and the surface variation is 0: the points lie on the plane $z = x/2$.

5. The ray direction is $(0.2, 0, 1)$. As a distance along the ray: $2 (0.2, 0, 1)/\sqrt{1.04} \approx (0.392, 0, 1.961)$. As a depth: $(0.4, 0, 2)$.

7. $e = (5/3, 0)$, $r_1 = 5/18$, $r_2 = 1/3$, $d_1 = 6$ and $d_2 = \sqrt{40}$. After the map, $e' = (10/3, 0)$, the ratios stay $5/18$ and $1/3$, and the lengths become $12$ and $\sqrt{136}$.

8. $10 \cdot 20 \cdot 19 \cdot 18 \cdot 17 = 1\,162\,800$ entries; with two-point bases, $10 \cdot 20 \cdot 19 \cdot 18 = 68\,400$.

11. From $t = 0$ the matches are $(1.2, 1.2, 3.2)$ with error $0.907$; the fit gives $t = -2/15$ with error $8/9 \approx 0.889$, the matches repeat and ICP stops. Near $-2/15$ every closest point is unique, so the cost is one quadratic with its minimum there: a local minimum. From $t = 0.5$ the matches are correct and the fit gives $t = 1.2$ with error 0.

15. With 1-based numbers, the passing pairs are all six pairs among matches 1 to 4 and the pair $(4, 5)$. The maximum clique is $\{1, 2, 3, 4\}$. Match 5 is the outlier; it agrees in length with match 4 by chance.

20. The tree has the edges $12$ (weight 0.04), $23$ (0.064) and $24$ (0.648); edge $13$ closes a cycle. $n_2$ is flipped to $(-0.28, 0.96)$, $n_3$ is kept, and $n_4$ is flipped to $(0.8, 0.6)$.

22. Write $\langle R(\theta) p, p' \rangle = \cos\theta\,(x x' + y y') + \sin\theta\,(x y' - y x')$ and maximize $A\cos\theta + B\sin\theta$. In the example the centered sums are $A = 0$ and $B = 48/9$, so $\theta = 90°$ and $t = (1, 1)$.

23. Scaling row 1 by $\lambda$ multiplies $a$ and $b$ by $\lambda$, and the ratio $ad/(bc)$ is unchanged; columns likewise. The limit is $\begin{pmatrix} x & 1-x \\ 1-x & x \end{pmatrix}$ with $x^2/(1-x)^2 = 2/3$, so $x \approx 0.4495$.

24. Take the complete $k$-partite graph with parts of 3 vertices (the complement of $k$ disjoint triangles). A maximal clique takes one vertex from each part, so there are $3^k$ of them; for $m = 30$, $3^{10} = 59\,049$.

25. Take $S_1 = \{0\}$, $S_2 = \{0, 1\}$ and $S_3$ made of $N$ points in $[1, 1 + \delta]$. Then $d(S_1, S_2) = 1$, $d(S_2, S_3) \le 1 + N\delta^2$ and $d(S_1, S_3) \ge 1 + N$. Let $N$ grow and $\delta$ shrink.

26. The closest target of $p_i + t$ changes only at $t = (q_j + q_{j+1})/2 - p_i$. Sort these breakpoints and sweep: keep the sums of $q_{c(i)} - p_i$ and of their squares, update one term at each breakpoint, and on each interval take the minimizer of the quadratic, the mean shift, clamped to the interval.
