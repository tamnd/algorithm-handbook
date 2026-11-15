1. The line is $\hat y = 1.2x$, with $\mathrm{RSS} = 14/5$ and $\mathrm{TSS} = 10$, so $R^2 = 0.72$ and the adjusted $R^2$ is $1 - 0.28 \cdot 3/2 = 0.58$. The F statistic is $7.2/1.4 = 36/7 \approx 5.143$ and $p = 1 - \sqrt{0.72} \approx 0.152$, so the slope is not significant at 0.05, even with $R^2 = 0.72$.

2. With the intercept first, the squared entries of $Q_1^\top y$ after the first one are the sums of squares that each column adds. The partial F is $3^2/(14/7) = 4.5 < 5.59$ (p about 0.072), so $b_2 = 0$ is not rejected. The overall F is $(36 + 9)/2/2 = 11.25 > 4.74$ (p about 0.0065), so it is rejected, and $R^2 = 45/59 \approx 0.763$.

5. $\Delta\mathrm{AIC} = 20\log 0.8 + 2 \approx -2.463$ and $\Delta\mathrm{BIC} = 20\log 0.8 + \log 20 \approx -1.467$, so both prefer the larger model. $F = 10/(40/17) = 4.25 < 4.45$ (p about 0.055), so the F-test keeps the smaller one. The likelihood ratio statistic is $20\log 1.25 \approx 4.463 > 3.84$ and chooses the larger model. Three of the four rules agree.

7. $r_i = 2/\sqrt{2 \cdot 0.5} = 2$. Then $s_{(i)}^2 = \bigl((n - p)s^2 - e_i^2/(1 - h_{ii})\bigr)/(n - p - 1) = (16 - 8)/7 = 8/7$ and $t_i = 2/\sqrt{(8/7)(0.5)} = \sqrt 7 \approx 2.646$. The leave-one-out error is $e_i/(1 - h_{ii}) = 4$, and $D_i = (4/2) \cdot 1 = 2$.

9. $\sum e_t^2 = 12$ and $\sum(e_t - e_{t-1})^2 = 8$, so $d = 2/3$. The lag sum is 7, so $r_1 = 7/12$, and $2(5/12) - 2/12 = 8/12$. A value of $d$ well below 2 points to positive correlation.

12. AIC: 45.589, 31.419, 24.501, 24.100, 25.469, so AIC chooses size 3. BIC: 48.391, 35.623, 30.106, 31.106, 33.876, so BIC chooses size 2. The penalty $\log 30 \approx 3.40$ per column is larger than the gain of $30\log(52/48) \approx 2.40$ from the third column.

16. For a linear estimator $c^\top y$ the variance is $\sum c_i^2x_i$. The least squares slope has $c_i = (x_i - \bar x)/S_{xx}$, which gives $12.5/25 = 1/2$. The weighted slope has variance $\sum w_i/\bigl(\sum w_i\sum w_ix_i^2 - (\sum w_ix_i)^2\bigr) = 25/58$, so the efficiency is $(25/58)/(1/2) = 25/29 \approx 0.862$. For the naive estimate, $E[\mathrm{RSS}] = \operatorname{tr}((I - H)\Sigma) = 10 - 5$, so $E[s^2/S_{xx}] = (5/2)/5 = 1/2$. It is unbiased for this design, by coincidence.

17. The residuals sum to 0 and are orthogonal to $x$, as the normal equations require. The squares are $0, 1, 0, 9, 4$ with mean $\hat\sigma^2 = 2.8$. Their regression on $x$ has slope 1.6, $\mathrm{ESS} = 25.6$ and total sum of squares 58.8. Koenker's form is $5 \cdot 25.6/58.8 \approx 2.177$ (p about 0.140), and the original form is $25.6/(2 \cdot 2.8^2) \approx 1.633$ (p about 0.201). The ratio is $11.76/15.68 = 0.75$.

19. The group means are 4, 7, 9, 3 and $\hat\mu = 5.75$. $\mathrm{MSA} = 2 \cdot 22.75/3 \approx 15.167$ and $\mathrm{MSE} = 6/4 = 1.5$, so $\hat\sigma_u^2 = (15.167 - 1.5)/2 \approx 6.833$ and the intraclass correlation is about 0.82. Each prediction shrinks the group mean deviation by $\hat\sigma_u^2/(\hat\sigma_u^2 + \hat\sigma_e^2/2) \approx 0.901$, which gives $-1.577$, $1.126$, $2.929$ and $-2.478$.

20. The working weight is $\mu = e^b$ and the working response is $b + (y - \mu)/\mu$. Their weighted mean is the update. The iterates are 2, 1.406006, 1.141367, 1.099513, 1.098613, 1.098612, which tend to $\log 3$. The number of correct digits roughly doubles each pass, because for the canonical link IRLS is Newton's method.

22. The naive p-value is $Q(1.8) \approx 0.0359$, where $Q$ is the upper normal tail. Given $Y > 1.2$, the law of $Y$ is a normal truncated to $(1.2, \infty)$, so the selective p-value is $Q(1.8)/Q(1.2) \approx 0.312$. The conditional distribution function at 1.8 is monotone in $\mu$, so each end of the interval is a root found by bisection. This gives $[-4.489, 3.654]$, against the naive $[-0.160, 3.760]$.

23. The residuals lie in the plane orthogonal to $(1, 1, 1)$. On that plane the matrix of $\sum(e_t - e_{t-1})^2$ has the eigenvalues 1 and 3, with eigenvectors $(1, 0, -1)$ and $(1, -2, 1)$. Write $e$ in these coordinates with a uniform angle $\theta$, so $d = 1 + 2\sin^2\theta$. Then $P(d \le 1.5) = 1/3$, and the 5% critical value is $1 + 2\sin^2(\pi/40) \approx 1.0123$.

24. Write $y_1 = ge^{-a}$ and $y_2 = ge^a$ with $g = \sqrt{y_1y_2}$. Then the difference of the transformed values is $2g^\lambda\sinh(\lambda a)/\lambda$, and the powers of $g$ cancel against the Jacobian term. The function $\sinh(\lambda a)/\lambda$ is even and increasing in $|\lambda|$, so $\ell$ has its maximum at 0. For $y = (1, 4)$, $\ell(0) \approx -0.6533$ and $\ell(1) = -2\log 0.75 - \log 4 \approx -0.8109$, so the statistic is about 0.315.

25. The inverse covariance matrix is tridiagonal, with diagonal $1, 1 + \rho^2, \dots, 1 + \rho^2, 1$ and off-diagonal entries $-\rho$. Its row sums are $1 - \rho$ at the ends and $(1 - \rho)^2$ inside, and they add up to $(1 - \rho)(2 + (n - 2)(1 - \rho))$. The variances are $4/5$ against $22/27$ for $n = 3$, and $4/7$ against $89/150$ for $n = 5$. The efficiencies are about 0.982 and 0.963.

26. The estimate is negative when $\mathrm{MSA} < \mathrm{MSE}$. The ratio $\mathrm{MSA}/\mathrm{MSE}$ is $(1 + 2\gamma)$ times an $F_{1,2}$ variable, so the probability is $P(F_{1,2} < 1/(1 + 2\gamma)) = 1/\sqrt{3 + 4\gamma}$. This gives about 0.577, 0.447 and 0.378. In those cases REML returns $\hat\sigma_u^2 = 0$, on the boundary.

27. The submodels are $\{1\}$, $\{2\}$ and $\{1, 2\}$, so the pairs are $(1, \{1\})$, $(1, \{1, 2\})$, $(2, \{2\})$ and $(2, \{1, 2\})$. Because the columns are orthogonal, the coefficient of $x_j$ is the same in every submodel that contains it. So there are only two distinct statistics, and they are independent. The constant solves $(2\Phi(z) - 1)^2 = 0.95$, giving $z \approx 2.2365$, against Bonferroni 2.2414 and Scheffé $\sqrt{5.9915} \approx 2.4477$. The naive coverage is $0.95^2 = 0.9025$.
