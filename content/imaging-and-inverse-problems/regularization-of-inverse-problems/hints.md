1. $\sigma_1 = 2/\pi = 0.6366$, $\sigma_5 = 2/(9\pi) = 0.0707$, $\sigma_{10} = 2/(19\pi) = 0.0335$, and $\sigma_1/\sigma_{10} = 19$. Since $\sigma_k \approx 1/(\pi k)$, the decay is $k^{-1}$: mildly ill posed.

3. Tikhonov: $0.990$, $0.900$, $0.0826$. Truncated SVD: $1$, $1$, $0$. Landweber: $1$, $0.99992$, $0.0861$; after 100 steps with $\omega = 1$ it acts like Tikhonov with $\alpha = 1/(\omega k) = 0.01$. Here $\|A\| = 1$, so Landweber converges for $0 < \omega < 2$.

6. The residuals for $k = 0, \ldots, 5$ are $1.0455$, $0.3052$, $0.0563$, $0.0258$, $0.0163$ and $0.0110$. The first one below $\tau\delta = 0.022$ is at $k = 4$.

7. The posterior variance is $\gamma^2\sigma^2/(a^2\gamma^2 + \sigma^2) = 1/5$ and the mean is $a\gamma^2 y/(a^2\gamma^2 + \sigma^2) = 6/5$. Tikhonov with $\alpha = 1$ gives $ay/(a^2 + \alpha) = 6/5$.

13. The residual has components $\alpha b_k/(\sigma_k^2 + \alpha)$, each increasing in $\alpha$. Bisection gives $\alpha = 0.0331$ and $x_\alpha = (0.968, 0.116)$.

14. (a) For $k \ge 1$ the first component is $1.01$ and the second is $2f_k$ with $f_k = 1 - 0.9999^k$, so the error is $(0.01^2 + (2f_k - 1)^2)^{1/2}$. (b) The error is smallest when $f_k = 1/2$, at $k = 6931$, where it is $0.0100$. (c) It tends to $(0.01^2 + 1)^{1/2} = 1.00005$, the error of the unregularized solution. (d) $\delta = 0.01414$ and the residual for $k \ge 1$ is $0.02 \cdot 0.9999^k$, which first drops below $\tau\delta = 0.01556$ at $k = 2513$; the error there is $0.556$. The error falls from about 1 to 0.01 and climbs back to 1, and the discrepancy principle stops before the minimum.

15. $k^{-2\nu} = k\delta$ gives $k = \delta^{-1/(2\nu+1)}$ and an error of order $\delta^{2\nu/(2\nu+1)}$: $k = 1000$ and $10^{-3}$ for $\nu = 1/2$, $k = 100$ and $10^{-4}$ for $\nu = 1$, $k \approx 16$ and $1.6 \cdot 10^{-5}$ for $\nu = 2$. Truncated SVD has infinite qualification, so the rate keeps improving.

17. The values are $5$, $3.68$, $4.29$ and $5.23$. On each interval between consecutive values of $|y_k|$ the estimate is a constant plus $c\lambda^2$, so the minimum is at a left end. The smallest value is $2.04$ at $\lambda = 0.5$, where the count of entries above $\lambda$ drops from 4 to 3.

20. Take $\delta = 0$ first: $y^\delta = y$ is allowed, so $R_{\alpha(y)}y = A^\dagger y$ for every $y$ in the domain. Now let $y_n \to y$ in the domain and treat $y_n$ as noisy data for $y$ with $\delta_n = \|y_n - y\|$. The rule gives $R_{\alpha(y_n)}y_n \to A^\dagger y$, and the left side equals $A^\dagger y_n$.

21. Set $g(t) = t^\nu/(t + \alpha)$. Then $g'(t) = 0$ at $t = \nu\alpha/(1 - \nu)$, and substituting gives the value. The bias of Tikhonov regularization is $\sum_k \frac{\alpha}{\sigma_k^2 + \alpha}\sigma_k^{2\nu}w_k v_k$, so its norm is at most this supremum times $\|w\|$. For $\nu > 1$ the value at $t = \|A\|^2$ alone is $\|A\|^{2\nu}\alpha/(\|A\|^2 + \alpha)$, which is of order $\alpha$, not $\alpha^\nu$.

22. Write $y = Ax + e$. Then $\mathbb{E}\|(I - H)y\|^2 = \|(I - H)Ax\|^2 + \sigma^2\mathrm{tr}((I - H)^2)$ and $\mathbb{E}\|Hy - Ax\|^2 = \|(I - H)Ax\|^2 + \sigma^2\mathrm{tr}(H^2)$. The difference is $\sigma^2(m - 2\,\mathrm{tr}\,H)$, which the last two terms of $mU$ cancel.

23. The smoothing error is $\int |t - p|\,e_p(t)\,dt = 2\int_0^\gamma s\,\gamma^{-1}(1 - s/\gamma)\,ds = \gamma/3$. Setting the derivative to 0 gives $\gamma^{5/2} = \tfrac92\sqrt2\,\delta$, so $\gamma \sim \delta^{2/5}$ and the error is of order $\delta^{2/5}$, slower than $\delta^{4/7}$ because $x$ has a kink at $p$. For $\delta = 10^{-3}$: $\gamma = 0.132$, smoothing error $0.0441$, noise bound $0.0294$, sum $0.0735$.

24. The equation reads $Rx = Q^{\mathsf T}(\bar y + \varepsilon)$, so $x = R^{-1}Q^{\mathsf T}\bar y + R^{-1}Q^{\mathsf T}\varepsilon$ is Gaussian. Its mean is $(G^{\mathsf T}G)^{-1}G^{\mathsf T}\bar y$, because $G^{\mathsf T}G = R^{\mathsf T}R$ and $G^{\mathsf T} = R^{\mathsf T}Q^{\mathsf T}$. Its covariance is $R^{-1}Q^{\mathsf T}QR^{-\mathsf T} = (G^{\mathsf T}G)^{-1}$. These are the mean and covariance of $\pi$.
