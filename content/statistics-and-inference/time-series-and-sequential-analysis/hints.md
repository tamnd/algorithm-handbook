3. (a) $1 - 1.5z + 0.56z^2 = (1 - 0.7z)(1 - 0.8z)$ has roots $1/0.7$ and $1.25$, so the process is causal, and it is invertible because it has no MA part. (b) $1 - z + 0.25z^2 = (1 - 0.5z)^2$ has the double root 2, so it is causal, but $1 + 2z$ has the root $-1/2$ inside the unit circle, so it is not invertible. (c) Both sides share the factor $1 - 0.5B$; cancelling it leaves $X_t = Z_t$, white noise.

5. $S = 0, 0.7, 0, 1.0, 1.6, 1.3, 2.6, 3.1$. The alarm comes at $t = 8$. The statistic was last zero at $t = 3$, so the estimated change is between times 3 and 4, and the first changed observation is $x_4$.

6. $Q = 100 \cdot 102\,(0.0225/99 + 0.01/98 + 0.0064/97) = 4.032$. For raw data it is compared with $\chi^2_3$: $4.032 < 7.815$, no rejection ($p \approx 0.26$). For ARMA(1, 1) residuals the degrees of freedom are $3 - 1 - 1 = 1$, and $4.032 > 3.841$ rejects ($p \approx 0.045$). With $n = 100$ both laws are approximations.

8. The factors are $1.5$ for heads and $0.5$ for tails: $M = 1.5, 2.25, 3.375, 1.6875, 2.531, 3.797, 1.898$. The maximum is $243/64$, so the anytime-valid p-value is $64/243 \approx 0.263$. Rejection needs $1.5^n \ge 20$, so $n = 8$, since $1.5^7 = 17.1$ and $1.5^8 = 25.6$.

9. (a) $-3.1 < -2.86$: reject the unit root. (b) The Engle-Granger point for two series is about $-3.34$, and $-3.1 > -3.34$: do not reject no cointegration. Using the Dickey-Fuller point here would be wrong, because the residuals come from a fitted regression. (c) $0.30 < 0.463$: do not reject stationarity. (d) $45.2 > 29.80$ rejects $r = 0$, and $14.1 < 15.49$ does not reject $r = 1$, so $\hat r = 1$ and there are $3 - 1 = 2$ common trends.

11. $\hat\phi_{11} = 0.6$ and $v_1 = 1 - 0.36 = 0.64$. Then $\hat\phi_{22} = (0.2 - 0.6 \cdot 0.6)/0.64 = -0.25$ and $\hat\phi_{21} = 0.6 - (-0.25)(0.6) = 0.75$. The PACF is $0.6$ and $-0.25$, and $\hat\sigma^2/\hat\gamma(0) = 1 - 0.75 \cdot 0.6 + 0.25 \cdot 0.2 = 0.6$. The roots of $1 - 0.75z + 0.25z^2$ are complex with product $1/0.25 = 4$, so both have modulus 2.

15. The best residual sums with $k$ changes are $76/3$, $4/3$, $7/6$, $2/3$, $1/2$ and $0$ for $k = 0, \ldots, 5$. With $\beta = 3$ the best is one change after the third point, cost $4/3 + 3 = 13/3$. One change beats every other $k$ exactly when $1/3 < \beta < 24$: the binding comparisons are with no change ($4/3 + \beta < 76/3$) and with three or five changes ($4/3 + \beta < 2/3 + 3\beta$ and $< 5\beta$).

17. The ratio is $\int_0^1 p^h(1 - p)^k\,dp \,/\, 2^{-(h+k)}$, and the Beta integral is $h!\,k!/(h + k + 1)!$. With $k = 0$, $\Lambda = 2^n/(n + 1)$, which is $16$ at $n = 7$ and $28.4$ at $n = 8$: 8 heads. After 9 heads in 10 flips, $\Lambda_{10} = 1024/110 = 9.31 < 20$, while the binomial p-value is $22/1024 = 0.0215$.

20. $D(f_0 \,\|\, f_1) = 0.2231$ and $D(f_1 \,\|\, f_0) = 0.1927$, so $E_0[N] \approx 6.01$ and $E_1[N] \approx 9.89$. The fixed test needs $n = 18$ flips with $c = 13$: size $0.0481$, power $0.867$. An exact computation over the head counts gives the SPRT's true values $\alpha' = 0.0490$, $\beta' = 0.140$, $E_0[N] = 7.64$ and $E_1[N] = 11.43$; Wald's approximations ignore the overshoot.

23. The trace is $1.5$ and the determinant $0.5$, so the eigenvalues are 1 and $0.5$. $\Pi = \begin{pmatrix} -0.3 & 0.3 \\ 0.2 & -0.2 \end{pmatrix} = \alpha\beta^\top$ with $\alpha = (-0.3, 0.2)^\top$ and $\beta = (1, -1)^\top$. Then $\beta^\top Y_t = (1 + \beta^\top\alpha)\beta^\top Y_{t-1} + \beta^\top\varepsilon_t$ with coefficient $0.5$. The vector $\alpha_\perp = (2, 3)^\top$ has $\alpha_\perp^\top\Pi = 0$, so $2Y_{1t} + 3Y_{2t}$ is a random walk. $C = \beta_\perp(\alpha_\perp^\top\beta_\perp)^{-1}\alpha_\perp^\top$ with $\beta_\perp = (1, 1)^\top$, which is $\begin{pmatrix} 0.4 & 0.6 \\ 0.4 & 0.6 \end{pmatrix}$.

24. Write $Z_2 = \sqrt{1/2}\,Z_1 + \sqrt{1/2}\,W$ with $W$ independent. The probability is $2(1 - \Phi(3)) + \int_{-3}^{3}\phi(z)\,P(|z + W| \ge \sqrt 2\,c)\,dz$, and $2(1 - \Phi(3)) = 0.0027$. Bisection on $c$ with the midpoint rule gives $c \approx 1.967$, nominal p-value $0.049$: the final test loses little.

25. Keep the probabilities of the head counts of the paths that have not yet stopped, flip by flip, as in a dynamic program. The mixture SPRT rejects within 20 flips with probability $501/32768 \approx 0.0153$ (about $0.0233$ within 50 and $0.0276$ within 100, all below the bound $0.05$). The repeated binomial test rejects within 20 flips with probability about $0.107$.

26. By the law of the iterated logarithm, $\limsup_n S_n/\sqrt{2n\log\log n} = 1$ almost surely. So $S_n/\sqrt n \ge \sqrt{\log\log n}$ for infinitely many $n$, and $\sqrt{\log\log n} > 1.96$ once $n > e^{e^{3.85}}$.

27. For $|\theta| < 1$, $\log|1 + \theta e^{-i\omega}|^2 = 2\operatorname{Re}\log(1 + \theta e^{-i\omega})$, and the power series of the logarithm has no constant term, so the mean over $\omega$ is 0. For $|\theta| > 1$, write $1 + \theta e^{-i\omega} = \theta e^{-i\omega}(1 + \theta^{-1}e^{i\omega})$. With $f(\omega) = |1 + 2e^{-i\omega}|^2/(2\pi)$, the formula gives $\sigma^2 = 4$, the noise variance of the invertible form in exercise 21.
