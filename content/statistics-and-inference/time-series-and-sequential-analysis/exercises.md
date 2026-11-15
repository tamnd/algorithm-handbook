1. ◦ Let $X_t = Z_t + 0.5Z_{t-1} - 0.3Z_{t-2}$ with $Z_t$ white noise of variance 1, a [moving-average model](/moving-average-model/) of order 2. Compute $\gamma(0)$, $\gamma(1)$, $\gamma(2)$, $\rho(1)$ and $\rho(2)$, and give $\rho(h)$ for $h \ge 3$.

2. ◦ For the [autoregressive model](/autoregressive-model/) $X_t = 0.8X_{t-1} + Z_t$ with noise variance 1, give $\gamma(0)$, $\rho(3)$, the [partial autocorrelation](/partial-autocorrelation-function/) $\phi_{22}$, and the variance of the error of the best linear forecast of $X_{n+2}$ from $X_n, X_{n-1}, \ldots$.

3. ◦ Say which of these [ARMA](/arma-model/) equations, with white noise $Z_t$, define a causal process, which are invertible, and which reduce to a simpler model: (a) $X_t = 1.5X_{t-1} - 0.56X_{t-2} + Z_t$; (b) $X_t = X_{t-1} - 0.25X_{t-2} + Z_t + 2Z_{t-1}$; (c) $X_t - 0.5X_{t-1} = Z_t - 0.5Z_{t-1}$.

4. ◦ An [SPRT](/sequential-probability-ratio-test/) tests a coin with $H_0$: heads with probability $0.5$ against $H_1$: heads with probability $0.8$, with $\alpha = 0.05$ and $\beta = 0.2$. Compute Wald's thresholds $a = \log(\beta/(1 - \alpha))$ and $b = \log((1 - \beta)/\alpha)$. What is the smallest number of flips after which the test can reject $H_0$, and the smallest after which it can accept $H_0$?

5. ◦ A [CUSUM](/cusum/) watches for a change from $N(0, 1)$ to $N(1, 1)$, so $Z_t = x_t - 1/2$, with threshold $h = 3$. Run it on $x = (0.4, 1.2, -0.3, 1.5, 1.1, 0.2, 1.8, 1.0)$. At which time does it raise the alarm, and where does the last return to zero place the change?

6. ◦ A series of length $n = 100$ has sample autocorrelations $\hat r_1 = 0.15$, $\hat r_2 = -0.10$ and $\hat r_3 = 0.08$. Compute the [Ljung-Box](/ljung-box-test/) statistic with $h = 3$. Does the test reject at the 5% level if the series is raw data? If it is the residual series of a fitted ARMA(1, 1) model? The 95% points of $\chi^2_1$ and $\chi^2_3$ are $3.841$ and $7.815$.

7. ◦ With four equally spaced analyses, $\alpha = 0.05$ two-sided, the [O'Brien-Fleming boundary](/obrien-fleming-boundary/) has constant $C = 2.0243$. Give the four critical values and the nominal two-sided p-value of the last one. Then, for a two-arm trial with unit variance per observation and a difference $\delta = 0.5$ to detect with power 90%, the fixed design needs $2 \times 10.507/\delta^2$ patients per arm; how many per arm does the maximum sample size need with five looks and the inflation factors $R = 1.0265$ (O'Brien-Fleming) and $R = 1.2065$ (Pocock) of the [group sequential design](/group-sequential-design/) entry?

8. ◦ A bettor tests that a coin is fair with the [test martingale](/test-martingale/) $M_t = \prod_{i \le t}(1 + \lambda(2X_i - 1))$, where $X_i = 1$ for heads, and $\lambda = 1/2$. Compute $M_t$ on the flips HHHTHHT, the anytime-valid p-value $1/\max_{s \le 7} M_s$, and the number of heads in a row from the start that the bettor needs to reject at $\alpha = 0.05$ by [Ville's inequality](/ville-inequality/).

9. ◦ Decide at the 5% level, using the asymptotic critical values quoted in the entries. (a) An [augmented Dickey-Fuller test](/augmented-dickey-fuller-test/) with a constant gives $\tau = -3.1$. (b) The same $\tau = -3.1$ comes from the residuals of a regression of one series on one other, as in the [Engle-Granger test](/engle-granger-test/). (c) A level [KPSS test](/kpss-test/) gives $\eta = 0.30$. (d) A [Johansen test](/johansen-test/) on three series, case "c", gives trace statistics $45.2$, $14.1$ and $2.9$ for $r = 0, 1, 2$. Give the estimated rank and the number of common stochastic trends.

10. ◦ Use the default spans of [STL](/stl-decomposition/) to find $n_l$ and $n_t$ for monthly data ($m = 12$) with $n_s = 7$, and for quarterly data ($m = 4$) with $n_s = 13$.

11. • The sample autocorrelations of a series are $\hat\rho(1) = 0.6$ and $\hat\rho(2) = 0.2$. Run the [Levinson-Durbin recursion](/levinson-durbin-recursion/) to get the [Yule-Walker](/yule-walker-equations/) AR(1) and AR(2) fits, the sample PACF at lags 1 and 2, and the ratio $\hat\sigma^2/\hat\gamma(0)$ for the AR(2) fit. Show that the fitted AR(2) is causal by computing the modulus of its roots.

12. • Run the [innovations algorithm](/innovations-algorithm/) for $n = 1, 2$ on the AR(1) process with $\phi = 0.6$ and noise variance 1. Give $v_0, v_1, v_2$ and $\theta_{11}, \theta_{21}, \theta_{22}$, and show that the predictor $\hat X_3$ it builds from the innovations equals $0.6X_2$, even though $\theta_{22} \ne 0$.

13. • Simple exponential smoothing sets $\ell_t = \alpha y_t + (1 - \alpha)\ell_{t-1}$ and forecasts every future value by $\ell_n$. With $\alpha = 0.3$ and $\ell_0 = 10$, smooth $y = (10, 12, 11, 15)$ and give the forecast of $y_6$. Then show that the one-step errors $e_t = y_t - \ell_{t-1}$ satisfy $y_t - y_{t-1} = e_t - (1 - \alpha)e_{t-1}$, so the method gives the forecasts of an [ARIMA](/arima-model/)(0, 1, 1) model, the simplest case of [Holt-Winters](/holt-winters-method/).

14. • A [vector autoregression](/vector-autoregression/) of order 1 for $(x_t, y_t)$ has coefficient matrix $A = \begin{pmatrix} 0.5 & 0 \\ 0.4 & 0.3 \end{pmatrix}$. Is it stable? Which series [Granger-causes](/granger-causality/) which? Give the response of $y$ at lags 1, 2 and 3 to a unit shock in $x$ at time 0.

15. • Segment $y = (0, 1, 0, 4, 5, 4)$ in mean by the penalized cost of [change-point detection](/change-point-detection/): the residual sum of squares of each segment plus $\beta$ per change. Find the best segmentation and its cost for $\beta = 3$. For which $\beta$ is the single change after the third point the unique best segmentation?

16. • A [GARCH(1, 1)](/garch-model/) model has $\omega = 0.1$, $\alpha = 0.1$ and $\beta = 0.8$. Give the unconditional variance, the half-life of a volatility shock, whether the fourth moment is finite, and the kurtosis of $\varepsilon_t$ for normal $z_t$. If $\sigma_{t+1}^2 = 2$, what is $E[\sigma_{t+5}^2 \mid \mathcal F_t]$?

17. • A [mixture SPRT](/mixture-sequential-probability-ratio-test/) tests a fair coin, $p_0 = 1/2$, with a uniform mixture over $p$. Show that after $h$ heads and $k$ tails the mixture likelihood ratio is $\Lambda = 2^{h+k}h!\,k!/(h + k + 1)!$. How many heads in a row are needed to reject at $\alpha = 0.05$? After 9 heads in 10 flips, compare $\Lambda_{10}$ with the two-sided binomial test p-value at $n = 10$.

18. • Let $X_t = A\cos(\pi t/3) + B\sin(\pi t/3)$, where $A$ and $B$ are uncorrelated with mean 0 and variance 1. Show that $X_t$ is weakly [stationary](/stationary-process/), find $\gamma(h)$ for $h = 0, \ldots, 3$, and show that $X_t = X_{t-1} - X_{t-2}$ for every $t$. What are the two parts of its [Wold decomposition](/wold-decomposition-theorem/)?

19. • Show that with divisor $n$, $|\hat\gamma(1)| < \hat\gamma(0)$ for every series that is not constant, so the Yule-Walker AR(1) fit $\hat\phi = \hat\gamma(1)/\hat\gamma(0)$ is causal. Then compute $\hat\phi$ for $x = (1, -2, 2, -1)$ with divisor $n$ and with divisor $n - h$.

20. • For the coin SPRT of exercise 4, compute the Kullback-Leibler divergences $D(f_0 \,\|\, f_1)$ and $D(f_1 \,\|\, f_0)$ and Wald's approximations of $E_0[N]$ and $E_1[N]$. Then find the smallest fixed number of flips $n$ and the cutoff $c$ such that rejecting when there are at least $c$ heads has size at most 0.05 and power at least 0.8 at $p = 0.8$.

21. • Show that the MA(1) models $X_t = Z_t + 2Z_{t-1}$ with $\operatorname{Var} Z_t = 1$ and $X_t = W_t + 0.5W_{t-1}$ with $\operatorname{Var} W_t = 4$ have the same autocovariance function. Which one is invertible? Show that every MA(1) has $|\rho(1)| \le 1/2$.

22. • For the normal mixture [confidence sequence](/confidence-sequence/) with $\alpha = 0.05$, compute the half-width $w_t$ at $t = 400$ for $\rho = 1$ and for $\rho = 0.1$, and compare with the fixed-sample half-width $1.96/\sqrt{400}$. Which $\rho$ gives the narrower interval at $t = 10$?

23. ★ The VAR(1) $Y_t = AY_{t-1} + \varepsilon_t$ in two dimensions has $A = \begin{pmatrix} 0.7 & 0.3 \\ 0.2 & 0.8 \end{pmatrix}$. Find the eigenvalues of $A$, write $\Pi = A - I = \alpha\beta^\top$, show that $\beta^\top Y_t$ is a stationary AR(1) and give its coefficient, find a combination of $Y_t$ that is a random walk, and compute the long-run impact matrix $C = \lim_{h \to \infty} A^h$ of this [cointegrated](/cointegration/) system.

24. ★ A Haybittle-Peto design for two equally spaced looks stops at the interim look if $|Z_1| \ge 3$. Find the final critical value $c$ such that $P_0(|Z_1| \ge 3 \text{ or } |Z_2| \ge c) = 0.05$, where $(Z_1, Z_2)$ is bivariate normal with correlation $\sqrt{1/2}$. Write the probability as a one-dimensional integral and evaluate it numerically.

25. ★ Write a program that computes exactly, with rational arithmetic, the probability under a fair coin that the Bernoulli mixture SPRT of exercise 17 rejects at $\alpha = 0.05$ within 20 flips. Compute the same probability for the rule that runs the exact two-sided binomial test, with p-value $\min(1, 2P(X \le \min(h, n - h)))$, after every flip and rejects at the first $n \le 20$ with p-value at most 0.05.

26. ★ Let $X_1, X_2, \ldots$ be i.i.d. $N(0, 1)$ and $S_n = X_1 + \cdots + X_n$. Prove that with probability 1 there is some $n$ with $|S_n|/\sqrt n \ge 1.96$, so a fixed-sample z-test repeated after every observation rejects a true null eventually.

27. ★ Show that $\frac{1}{2\pi}\int_{-\pi}^{\pi}\log|1 + \theta e^{-i\omega}|^2\,d\omega$ equals 0 for $|\theta| < 1$ and $\log\theta^2$ for $|\theta| > 1$. Use Kolmogorov's formula $\sigma^2 = 2\pi\exp\{\frac{1}{2\pi}\int_{-\pi}^{\pi}\log f(\omega)\,d\omega\}$ to find the one-step prediction error variance of $X_t = Z_t + 2Z_{t-1}$ with $\operatorname{Var} Z_t = 1$, and compare with exercise 21.
