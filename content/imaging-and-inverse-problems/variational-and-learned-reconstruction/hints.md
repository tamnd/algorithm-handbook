1. Least squares gives the mean $13/3$. The Kullback-Leibler fidelity $\sum_i (x - y_i\log x)$ has derivative $3 - 13/x$, so it also gives $13/3$. The $\ell_1$ fidelity $\sum_i |x - y_i|$ is minimized by the median, 2, which ignores how large the outlier is. It is the negative log likelihood of Laplace noise and the usual choice for impulse noise.

3. Every inner product of a unit vector with a column of $H_4/2$ is $\pm 1/2$, and the columns of $H_4$ are orthogonal, so $\mu = 1/2$. The Welch bound is $\sqrt{4/28} = 0.378$. The condition reads $s < 1.5$, so only $s = 1$ is guaranteed.

4. The null space is $\{v : v_1 + v_2 + v_3 = 0\}$, and $v = (-2, 1, 1)$ has $|v_1| = |v_2| + |v_3|$, so the strict inequality fails. Every $x \ge 0$ with $x_1 + x_2 + x_3 = 1$ has $\|x\|_1 = 1$, the smallest possible value, so the solutions of basis pursuit are the whole triangle and $(1, 0, 0)$ is not the unique one.

7. (a) $2^4 \cdot 4! = 384$. For $K = 256$, $\log_{10}(2^{256}\,256!) \approx 584.0$. (b) $64 \cdot 256/60 = 273.07$, so $N \ge 274$.

9. The optimality condition gives $x^{k+1} = \sigma y^k/(\sigma^2 + \lambda)$. Substituting $y^k = y^{k-1} + (y - \sigma x^k)$ shows by induction that each residual $y - \sigma x^{k+1}$ is $\lambda/(\sigma^2 + \lambda)$ times the previous one. Here the factor is $0.01/0.02 = 1/2$, and the filter factors are $0.5$, $0.75$, $0.875$ and $0.9375$: four steps.

12. With $w = Du = (1, 1, -1, -1)$ the first term is 0 and $\|Dw\|_1 = 2$. With $w = 0$ the cost is $\alpha_1\|Du\|_1 = 4\alpha_1$. A grid search over $w$ finds nothing better, so the value is $\min(4\alpha_1, 2\alpha_0)$: $2$, $4$ and $0.5$, against $\alpha_1\mathrm{TV}(u) = 4$. A kink costs $\alpha_0$ times the change of slope, here 2.

14. Every solution has $|y| = |a^{\mathsf T}x| \le \max_j|a_j|\,\|x\|_1$, with equality only for weight on the columns of largest $|a_j|$. So it recovers $x$ exactly when $|a_1|$ is the strict maximum, which has probability $1/3$ by symmetry. A run with `random.Random(7)` and 200000 draws gave $0.3359$.

15. The iterates are $x = 1.5, 1.25, 1.625, 1.8125$, $d = 0.5, 1.25, 1.625, 1.8125$ and $b = 1$ throughout. From the second step on, $d = x$ and $b = 1$, so $x \leftarrow (2 + x)/2$ and $x - 2$ halves. The limit is $\mathrm{shrink}(3, 1) = 2$.

18. $\delta_5 \le 4/16 = 0.25$. The bound $(3s - 1)/16 < 1/2$ holds for $s \le 2$. The bound $(4s - 1)/16 \le 0.1$ fails already for $s = 1$, so coherence certifies no case of the CoSaMP condition here.

20. Since $Av = 0$, $v_i = -\sum_{j \ne i}\langle a_i, a_j\rangle v_j$, so $|v_i| \le \mu(\|v\|_1 - |v_i|)$. Summing over a set $S$ of size $s$ gives $\|v_S\|_1 \le s\mu\|v\|_1/(1 + \mu)$, which is less than $\tfrac12\|v\|_1$ when $2s\mu < 1 + \mu$.

21. With $\omega = e^{2\pi i/5}$, $P(z) = (z - 1)(z - \omega^{-1}) = z^2 - (1 + \omega^{-1})z + \omega^{-1}$ gives $h = (\omega^{-1}, -(1 + \omega^{-1}), 1, 0, 0)$, whose DFT $\hat h_k = P(\omega^{-k})$ vanishes at $k = 0, 1$ and nowhere else. Take $f = (\omega^{-1}, -(1 + \omega^{-1}), 0, 0, 0)$ and $g = (0, 0, -1, 0, 0)$. Then $|\mathrm{supp}\,h| + |\mathrm{supp}\,\hat h| = 3 + 3 = 6$.

22. Given $x_t$, $x_0 \sim N(\sqrt{\bar\alpha}\,x_t, 1 - \bar\alpha)$, so $y \mid x_t \sim N(\sqrt{\bar\alpha}\,x_t, \sigma^2 + 1 - \bar\alpha)$. DPS uses $N(\hat x_0, \sigma^2)$ with $\hat x_0 = \sqrt{\bar\alpha}\,x_t$ and so drops the variance $1 - \bar\alpha$. Its gradient is $(\sigma^2 + 1 - \bar\alpha)/\sigma^2 = 3$ times too large: $0.828$ against $0.276$.

23. $I/\tau$ is positive definite, so $M$ is positive definite exactly when the Schur complement $I/\sigma - \tau KK^{\mathsf T}$ is. Its smallest eigenvalue is $1/\sigma - \tau\|K\|^2$.

24. For analysis, the problem is strictly convex and symmetric in the two entries, so $x = (t, t)$: the objective $(t - 1)^2 + 0.8t$ gives $t = 0.6$. For synthesis, $D = \frac13\begin{pmatrix} 2 & -1 & 1 \\ -1 & 2 & 1\end{pmatrix}$. Try $z = (0, 0, u)$: $Dz = (u/3, u/3)$ and $(u/3 - 1)^2 + 0.2u$ gives $u = 2.1$. The gradient $D^{\mathsf T}(Dz - y) = (-0.1, -0.1, -0.2)$ confirms optimality. So synthesis gives $(0.7, 0.7)$ and analysis gives $(0.6, 0.6)$.
