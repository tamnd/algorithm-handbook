1. The gain is $K = 2/(2 + 1) = 2/3$, the analysis is $x^a = 4 + \tfrac23(7 - 4) = 6$, and the analysis
variance is $(1 - K) \cdot 2 = 2/3$.

3. The increment is $\frac{d}{B_{33} + r}B_{:,3} = \frac{3}{3}(0.5, 1, 2, 1, 0.5) = (0.5, 1, 2, 1, 0.5)$. The
analysis variance at point 3 is $2 - 2^2/3 = 2/3$.

5. The equilibrium is $gy/(1 + g) = 4g/(1 + g)$, and $4 - 4g/(1 + g) = 4/(1 + g) \le 0.1$ gives $g \ge 39$.
The nudged equation decays at the rate $1 + g = 40$, and the classical Runge-Kutta method is stable for
real decay rates $\lambda$ with $\lambda\,dt$ up to about $2.785$, so $dt < 0.0696$.

6. With $z = r/c$, $\mathrm{GC}(1; 3) = 1639/1944 \approx 0.843$ from the first branch and
$\mathrm{GC}(4; 3) = 71/1458 \approx 0.0487$ from the second. The function is zero for $r \ge 2c = 6$.

9. (a) $\tau^2 = \tfrac52 \cdot 40 = 100$. (b) $\tau^2 = \lambda^2(1 + \tfrac32\lambda^2) = 4 \cdot 7 = 28$.

10. The sample variance is $s = 4$, so $K = 4/4.5 = 8/9$ and $r/(s + r) = 1/9$, which gives
$\alpha = 1/(1 + 1/3) = 3/4$. The mean moves to $3 + \tfrac89 \cdot 1.5 = 13/3$, and the perturbations
$(-2, 0, 2)$ are multiplied by $1 - \alpha K = 1/3$. The members are $11/3, 13/3, 5$, with variance
$4/9 = (1 - K) \cdot 4$.

13. The eigenvalues of a symmetric circulant matrix with first row $(1, 1, 0, 0, 0, 1)$ are
$1 + 2\cos(2\pi k/6)$, $k = 0, \ldots, 5$: that is $3, 2, 0, -1, 0, 2$. The eigenvalue $-1$ (for the
alternating vector) means that the Schur product with a covariance can have negative variances in some
direction.

16. The error obeys $\dot e_1 = e_2 - ge_1$, $\dot e_2 = -e_1$, with characteristic polynomial
$\lambda^2 + g\lambda + 1$. For $g < 2$ the roots have real part $-g/2$; for $g > 2$ the slower root is
$(-g + \sqrt{g^2 - 4})/2$, which tends to 0 as $g$ grows. The best gain is $g = 2$, with the double root
$-1$ and decay like $te^{-t}$.

17. The adjoint run forced at time 1 gives $\lambda_1 = \lambda_0 = 1$, so $r(0) = 1$, $r(1) = 1 + 2 = 3$
and $P = 3$. Then $\beta = 3/(3 + 1) = 3/4$, $x_0 = 3/4$, $\eta = Q\beta = 3/2$ and $x_1 = 9/4$. The strong
constraint gives $x_1 = 3/2$: the model error lets the estimate move further towards the observation.

19. Here $S = 3$. The update gives $\tilde R_1 = 9/4$ and $\tilde R_2 = 27/13$. With $u_j = 1/\tilde R_j$ it
reads $u_{j+1} = \tfrac13 + \tfrac13u_j$, so $u_j \to 1/2$ and $\tilde R_j \to 2 = S - H\tilde BH^\top$. The
unit of background variance missing from $\tilde B$ appears in $\tilde R$.

21. Write the 4D-Var cost as a 3D-Var cost in $x_0$ with the observation operator $HM$. The push-through
identity gives $x^a_0 = x^b + BM^\top H^\top(HMBM^\top H^\top + R)^{-1}(y - HMx^b)$ and
$\mathrm{Cov}(x^a_0) = B - BM^\top H^\top S^{-1}HMB$ with $S = HP^fH^\top + R$. Multiply by $M$ on the left
(and by $M^\top$ on the right for the covariance). No inverse of $M$ appears.

22. Write $P = \sum_k v_kv_k^\top$. Then $z^\top(L \circ P)z = \sum_k (v_k \circ z)^\top L(v_k \circ z)$,
which is 0 only if $v_k \circ z = 0$ for every $k$. That forces $z_i^2P_{ii} = \sum_k z_i^2v_{k,i}^2 = 0$
for every $i$, so $z = 0$.

23. The answer is $c = 11$: the smallest eigenvalue is about $-0.00016$ (at the alternating mode). For
$c \le 10$ the support $2c$ is at most half the ring and all eigenvalues are positive; for $c = 11$ with
the chordal distance the smallest eigenvalue is about $+0.00012$.

24. The error $e = x - \hat x$ obeys $de = -(1 + g)e\,dt + dw - g\,dv$, so its stationary variance is
$(3 + g^2)/(2(1 + g))$. The derivative vanishes when $g^2 + 2g - 3 = 0$, at $g = 1$, with variance 1. The
Riccati equation $0 = -2P + 3 - P^2$ gives $P = 1$ and the gain $P/r = 1$.

25. Spin up first, start the second trajectory $10^{-8}$ away, and average over at least 100 time units.
The exponent is about $1.67$ (seed-dependent in the second decimal), so errors double in about
$\ln 2/1.67 \approx 0.42$ time units.
