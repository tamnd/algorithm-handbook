1. The trace is 7 and the determinant 6, so the eigenvalues are 6 and 1. The first direction is $(2, 1)/\sqrt5$. It keeps $6/7 \approx 85.7\%$ of the variance, and the mean squared reconstruction error is the discarded eigenvalue, 1.

2. Kaiser's rule keeps the three eigenvalues 3.2, 2.0 and 1.2, which explain $6.4/8 = 80\%$. The cumulative fractions are 40, 65, 80, 87.5 and 92.5%, so 90% needs $k = 5$.

5. $\mathrm{KL} = -\tfrac12\big[(1 + 0 - 1 - 1) + (1 + \ln\tfrac12 - 0 - \tfrac12)\big] = \tfrac14 + \tfrac12\ln 2 \approx 0.597$ nats.

7. $\ln 10^4 \approx 9.2103$. For $\varepsilon = 0.25$ the denominator is $0.03125 - 0.00521 = 0.02604$, so $k \ge 1414.7$ and the least $k$ is 1415. For $\varepsilon = 0.1$ it is $0.005 - 0.00033 = 0.00467$, so $k \ge 7894.6$ and the least $k$ is 7895. The bound does not contain $d$, so the answer does not change.

10. The chord of $45°$ is $2\sin 22.5° \approx 0.765$, of $90°$ is $\sqrt2 \approx 1.414$, and of $135°$ is about 1.848. With $\varepsilon = 1$ only consecutive points are joined, and the graph distance is $8\sin(\pi/8) \approx 3.061$, close to the arc length $\pi \approx 3.142$; the straight line is 2. With $\varepsilon = 1.5$ the $90°$ chords are edges too, and the path $0° \to 90° \to 180°$ has length $2\sqrt2 \approx 2.828$: a larger $\varepsilon$ cuts corners.

11. $\sigma^2$ is the mean of the discarded eigenvalues. For $q = 1$, $\sigma^2 = (4 + 1 + 1)/3 = 2$ and $W = \sqrt{10 - 2}\, u_1 = 2\sqrt2\, u_1$; the fitted covariance has the eigenvalues 10, 2, 2, 2. For $q = 2$, $\sigma^2 = 1$ and $W = (3u_1, \sqrt3\, u_2)R$ for any orthogonal $R$; the fit has the eigenvalues 10, 4, 1, 1 and equals $S$. The models have $dq - q(q-1)/2 + 1 = 5$ and 8 free parameters, against $d(d+1)/2 = 10$.

13. The first row of $B$ is $(3/4, 1/4, -5/4, 1/4)$, and the others are its cyclic shifts. The eigenvalues are 2, 2, 0 and $-1$. The negative one shows that the distances are not Euclidean: a triangle with sides 1, 1 and 2 is flat, so both middle objects would sit at the midpoint of the same pair. In two dimensions classical MDS returns the square $(\pm1, 0), (0, \pm1)$. It keeps the opposite distances 2, but puts neighbors at $\sqrt2$ instead of 1.

14. The centered start is $(-4/3, -1/3, 5/3)$, with distances $d_{12} = 1$, $d_{13} = 3$ and $d_{23} = 2$. So $b_{12} = -2$, $b_{13} = -2/3$, $b_{23} = -1$, and the diagonal is $(8/3, 3, 5/3)$. The step gives $X^+ = \tfrac13 BX = (-4/3, 0, 4/3)$. The stress falls from $1 + 1 + 0 = 2$ to $3 \cdot (2/3)^2 = 4/3$. For the positions $-a, 0, a$ the stress is $2(2-a)^2 + (2-2a)^2$, which is least at $a = 4/3$. The decrease $2/3$ equals $n\|X - X^+\|_F^2 = 3 \cdot 2/9$, so the sandwich inequality of the SMACOF entry holds with equality here.

17. The input 2-neighbor sets are $\{1, 3\}$ for 0, $\{0, 3\}$ for 1, $\{1, 0\}$ for 3, $\{3, 1\}$ for 7, $\{7, 3\}$ for 15 and $\{15, 7\}$ for 31. In the map the moved point, now at 10, becomes a neighbor of 7 and of 15. In the input it has rank 5 from each of them, so each adds $5 - 2 = 3$, and $T(2) = 1 - \frac{2 \cdot 6}{6 \cdot 2 \cdot 5} = 4/5$. The point 7 loses 1, which has rank 3 from it in the map, and 15 loses 3, also at rank 3. So $C(2) = 1 - 2/30 = 14/15$.

19. $H \leftarrow H \circ (W^\top V)/(W^\top W H) = (1, 1) \circ (4, 6)/(2, 2) = (2, 3)$. The error falls from 14 to 4. Then $W \leftarrow W \circ (VH^\top)/(WHH^\top) = (1, 1)^\top \circ (8, 18)^\top/13 = (8/13, 18/13)^\top$, and the error is $2/13 \approx 0.154$. The best rank-one error is the square of the second singular value of $V$, about 0.134.

21. The degrees are $(2, 3, 2)$ and $\pi = (2, 3, 2)/7$. The rows of $P$ are $(\tfrac12, \tfrac12, 0)$, $(\tfrac13, \tfrac13, \tfrac13)$ and $(0, \tfrac12, \tfrac12)$, so $D_1(1, 3)^2 = 2 \cdot (\tfrac12)^2/(2/7) = 7/4$. The eigenvalues are $1, \tfrac12, -\tfrac16$. The eigenvector for $\tfrac12$ is $c(1, 0, -1)$ with $c^2 = 7/4$, and it gives $(\tfrac12)^2 (2c)^2 = 7/4$. The one for $-\tfrac16$ is proportional to $(3, -4, 3)$ and takes equal values at the two ends.

23. Each $U_k(i)$ has at most $k$ points, all of rank greater than $k$ in the input, with distinct ranks. The sum $\sum_{j \in U_k(i)} (r(i, j) - k)$ is largest when the ranks are $n - 1, \ldots, n - k$. This gives $\sum_{j=1}^{k}(n - j - k) = k(n - k) - k(k + 1)/2 = k(2n - 3k - 1)/2$. All these ranks exceed $k$ because $k < n/2$. Sum over the $n$ points.

24. The centered columns lie in the $(n-1)$-dimensional subspace orthogonal to $\mathbf 1$. By the dimension formula, the column spaces of $X$ and $Y$ meet in a subspace of dimension at least $p + q - (n - 1)$. Every unit vector $z = Xa = Yb$ in it gives a pair with correlation 1, and an orthonormal basis gives that many uncorrelated pairs. For $n = 10$, $p = 6$, $q = 7$, at least 4.

25. If $A$ has rank $r$ with nonzero eigenvalues $\lambda_1, \ldots, \lambda_r$, Cauchy-Schwarz gives $(\sum \lambda_i)^2 \le r \sum \lambda_i^2$. Apply it to the Gram matrix of the $v_i$. Its rank is at most $k$, its trace is $n$, and $\operatorname{tr}(A^2) = \sum_{i,j}\langle v_i, v_j\rangle^2 \le n + n(n-1)\varepsilon^2$. For $n = 10^6$ and $\varepsilon = 0.01$ the bound is $10^6/100.9999 \approx 9900.9999$, so $k \ge 9901$.

27. By linearity, $4\langle f(x), f(y)\rangle = \|f(x+y)\|^2 - \|f(x-y)\|^2 \le (1 + \varepsilon)\|x+y\|^2 - (1 - \varepsilon)\|x-y\|^2 = 4\langle x, y\rangle + 4\varepsilon$, since $\|x+y\|^2 + \|x-y\|^2 = 4$. The lower bound is the same. Apply the projection to the $2n$ points $\pm v_i$: the distance from $f(v_i)$ to $f(-v_j)$ is $\|f(v_i + v_j)\|$. So $n$ becomes $2n$ in the bound, and $k$ grows by $4\ln 2/(\varepsilon^2/2 - \varepsilon^3/3)$.
