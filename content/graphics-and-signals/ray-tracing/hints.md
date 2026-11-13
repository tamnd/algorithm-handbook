1. Here $f = o - c = (-0.6, 0, 5)$, $b = f \cdot d = -5$ and $k = \lvert f \rvert^2 - 1 = 24.36$. The discriminant is $b^2 - k = 0.64$, so $t = 5 \mp 0.8$: the roots are 4.2 and 5.8. The first hit is $(0, 0, 0.8)$, and the normal is $(p - c)/r = (-0.6, 0, 0.8)$.

2. The reciprocal direction is $(0.5, 1, +\infty)$, and the z slab never cuts, since $o_z = 1$ lies inside $[0, 2]$. The first ray gives $[0.5, 1.5]$ from $x$, and $y$ does not shrink it. The second gives $[0.5, 0.5]$: it touches the edge where the faces $x = 1$ and $y = 2$ meet, at the point $(1, 2, 1)$. The test misses only when $t_0 > t_1$, so a single point counts as a hit. The third gives $t_0 = 0.5 > t_1 = 0.4$, a miss.

3. With $e_1 = (-1, 1, 0)$ and $e_2 = (-1, 0, 1)$, you get $p = d \times e_2 = (2, -4, 2)$ and $\det = -6$. Then $s = (-1, 0, 0)$, $u = 1/3$, $q = s \times e_1 = (0, 0, -1)$, $v = 1/2$ and $t = 1/6$. The hit is $(1/6, 1/3, 1/2)$, which has the weights $1/6, 1/3, 1/2$ on $v_0, v_1, v_2$. The determinant is negative, so the ray meets the back face, and the culling version returns a miss.

4. $R_0 = (0.333/2.333)^2 = 0.0204$. From air at $60°$, the refraction angle is $40.52°$, the exact $R$ is 0.0597, and Schlick gives 0.0510. Inside the water at $45°$, the light leaves at $70.49°$ with $R = 0.1395$. The critical angle is $48.61°$, so at $50°$ all the light is reflected.

9. $L = L_e/(1 - \rho) = 5 L_e$. After $k$ bounces the relative error is $\rho^{k+1}$, and $0.8^{k+1} \le 0.01$ first holds at $k = 20$. A depth limit of 5 keeps the terms $k = 0, \ldots, 5$, which sum to $1 - 0.8^6 = 0.738$ of the truth. The image is 26% too dark, and more samples do not fix it.

10. The standard error falls as $1/\sqrt{N}$. Dividing it by 8 takes 64 times the samples, so 1024 per pixel. The standard error estimates the standard deviation of a random error, so the [central limit theorem](/central-limit-theorem/) gives only a probability, about 95% for two standard errors. Any single pixel can still be further off.

11. (a) Unbiased and consistent. (b) Biased, too dark, and not consistent as $N$ grows. (c) Biased and not consistent. (d) Biased and consistent. (e) Biased, and not consistent with a fixed clamp. (f) Biased and not consistent. (g) Biased, too dark near shadows. (h) Biased by the start-up, but consistent. (i) Unbiased and consistent for $A(x)$, and biased as an estimate of the real light, because it leaves out interreflection.

12. The root box has $S = 42$, and a single cube has $S = 6$. The split $\{0\} \mid \{1, 8, 9\}$ costs $1 + (6 + 38 \cdot 3)/42 = 3.857$, and so does $\{0, 1, 8\} \mid \{9\}$. The split $\{0, 1\} \mid \{8, 9\}$ costs $1 + (10 \cdot 2 + 10 \cdot 2)/42 = 1.952$. A leaf costs 4, so it wins only when $c_t > (4 - 40/42)\,c_i \approx 3.048\,c_i$.

15. With the balance heuristic, both terms become $f/(p_1 + p_2) = 3x^2/(1 + 2x)$, with the means 0.412 and 0.588. The variances are 0.8 and 0.125 for one density alone, 0.168 with the balance heuristic and 0.164 with the power heuristic. Two samples from $p_2$ give 0.0625, and the plain average gives $(0.8 + 0.125)/4 = 0.231$. At $x = 0.25$ the weights of $p_1$ are $2/3$ and $0.8$. MIS does not beat the best density used alone. It only protects against a bad density.

17. Delta tracking samples the true free-flight distance, so the probability is $1 - e^{-1} = 0.632$, and the transmittance is $e^{-(1 + 3)} = 0.0183$. The walk is still alive at $t$ with probability $T(t)$, and tentative points arrive at the rate 3. So the expected count is $\int_0^2 3\,T(t)\,dt = 3(1 - e^{-1}) + e^{-1}(1 - e^{-3}) \approx 2.246$. Ratio tracking visits a Poisson number of points with the mean $3 \cdot 2 = 6$.

22. The equations are $B_1 = 1 + 0.1 B_2$ and $B_2 = 0.1 B_1$. They give $B_1 = 1/0.99 = 1.0101$ and $B_2 = 0.10101$. The sweeps give $(1, 0.1)$, $(1.01, 0.1)$ and $(1.01, 0.101)$. The iteration matrix has the entries 0.1 off the diagonal, so the largest error falls by 0.1 per sweep. That factor is $\rho$ times the row sum of $F$, well below the bound $\rho_{\max} = 0.5$, since most light escapes.

24. Each candidate gets the weight $\hat p/p = 2f$, which is 6 or 2. The estimate is $\frac{f(y)}{\hat p(y)} \cdot \frac1M \sum_j w_j = \frac1M \sum_j w_j$, because $f = \hat p$. So it does not depend on $y$. It is a mean of $M$ independent values 6 or 2, with mean 4, which is the true sum, and variance $4/M$.

25. One path gives $X = L_e \sum_{j=0}^{K} (\rho/q)^j$, where $P(K = k) = q^k(1 - q)$. Sum the geometric series in $E[X^2]$. It converges exactly when $\rho^2/q < 1$. At $q = \rho$ every term is $L_e$, so $X = L_e(K + 1)$, and the variance is $\rho/(1 - \rho)^2 L_e^2 = 2 L_e^2$. The path has $1/(1 - q)$ vertices on average, and the product is $\rho^2/((1 - \rho)^2(q - \rho^2))$. In the furnace every path carries the same light, so roulette only adds noise. It pays where the albedo varies.

26. The root has $S = 26$. The splits cost 3.308, 3.154 and 3.308, so the greedy build takes $\{0, 2\} \mid \{3, 5\}$. Each pair then splits, since $1 + 12/14 = 1.857 < 2$, and the tree costs $1 + 2 \cdot \frac{14}{26} \cdot \frac{13}{7} = 3$. The tree $\{0\} \mid (\{2, 3\} \mid \{5\})$, with $\{2, 3\}$ as a leaf, costs $1 + \frac{6}{26} + \frac{18}{26}(1 + \frac{20}{18} + \frac{6}{18}) = \frac{38}{13} \approx 2.923$.

27. The measure of lines that meet $K$ is proportional to its mean projected area, which is $S/4$ by Cauchy's formula. For each direction, the chords integrate over the plane of projection to $V$. So the mean chord is $V/(S/4) = 4V/S$. That is $2/3$ for the unit cube, and a simulation gives 0.6668. For a ball it is $4r/3$.

28. Each crossing point lies in some leaf, and that leaf must reference both triangles. A leaf with $a$ horizontal and $b$ vertical references has $a + b \le c$, so it holds at most $ab \le c^2/4$ crossings. The $n^2$ crossings then need at least $4n^2/c^2$ leaves. A BVH references each triangle once. A binary tree with $2n$ leaves has $4n - 1$ nodes.

29. For $m \ge 3$ cubes the range is $[1, 2^{m-1}]$, and each bin is $(2^{m-1} - 1)/4$ wide. Bin 0 holds the cubes up to $2^{m-3}$, bin 1 holds $2^{m-2}$, bin 2 is empty and bin 3 holds $2^{m-1}$. Shifting every centroid by $1/2$ changes nothing. Every boundary leaves at least the $m - 2$ cubes of bin 0 on the left, and they have the same pattern, so the left spine alone bins $n + (n - 2) + \cdots \ge n^2/4$ primitives.
