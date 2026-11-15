## What to remember

- $R^2 = 1 - \mathrm{RSS}/\mathrm{TSS}$ never decreases when a column is added, and $\mathrm{VIF}_j = 1/(1 - R_j^2)$ is the exact factor by which collinearity inflates $\operatorname{Var}(\hat b_j)$; both describe the data, not whether the model is right. For nested models with $q$ restrictions, $F = \frac{(\mathrm{RSS}_0 - \mathrm{RSS}_1)/q}{\mathrm{RSS}_1/(n - p)}$ has the $F_{q, n-p}$ law exactly under the null with normal errors of equal variance ([F-test](/regression-f-test/)).
- $\mathrm{AIC} = -2\log L + 2k$ and $\mathrm{BIC} = -2\log L + k\log n$; only differences on the same data mean anything. BIC pays more once $n \ge 8$ and picks the true model with probability tending to 1 when it is in a fixed finite list. [Stepwise regression](/stepwise-regression/) stops at a subset that no single move improves; [leaps and bounds](/leaps-and-bounds/) finds the best subset of each size exactly.
- The [hat matrix](/hat-matrix/) $H = X(X^\top X)^{-1}X^\top$ is a projection with trace $p$, so the leverages $h_{ii}$ average $p/n$; $h_{ii} > 2p/n$ is a common flag. $\operatorname{Var}(e_i) = \sigma^2(1 - h_{ii})$, and the leave-one-out prediction error is $e_i/(1 - h_{ii})$. The external [studentized residual](/studentized-residual/) has the $t_{n-p-1}$ law under normal errors; [Cook's distance](/cooks-distance/) $D_i = \frac{r_i^2}{p}\frac{h_{ii}}{1 - h_{ii}}$ has no null law.
- The [Gauss-Markov theorem](/gauss-markov-theorem/): with mean-zero, uncorrelated errors of equal variance, least squares has the least covariance among linear unbiased estimators, without normality. With $\operatorname{Cov}(\varepsilon) = \sigma^2V$ for a known $V$, the best one is [generalized least squares](/generalized-least-squares/), $\hat b = (X^\top V^{-1}X)^{-1}X^\top V^{-1}y$, and [weighted least squares](/weighted-least-squares/) is its diagonal case.
- Under [heteroscedasticity](/heteroscedasticity/) least squares stays unbiased, but $s^2(X^\top X)^{-1}$ is the wrong covariance. The sandwich $(X^\top X)^{-1}X^\top\operatorname{diag}(\omega_i)X(X^\top X)^{-1}$, with $\omega_i = e_i^2$ for HC0 and $e_i^2/(1 - h_{ii})^2$ for HC3, is consistent; summing $x_ie_i$ within clusters gives the [cluster-robust](/cluster-robust-standard-errors/) version, whose theory needs many clusters and which uses $t_{G-1}$.
- In the [linear mixed model](/linear-mixed-model/) $y = Xb + Zu + e$, [Henderson's equations](/henderson-mixed-model-equations/) of order $p + q$ give the GLS $\hat b$ and the BLUP of $u$ for known covariances. [REML](/restricted-maximum-likelihood/) estimates the covariances from contrasts free of $b$, which for one normal sample gives the divisor $n - 1$.
- Classical tests of a model chosen from the same data reject too often. Sample splitting, simultaneous PoSI intervals and conditioning on the selection are exact under their assumptions; the [polyhedral lemma](/polyhedral-lemma/) gives the conditional law, a truncated normal, when $y$ is normal with known covariance and the selection event is a polyhedron.

| Method | Guarantee | Holds under | Time |
|---|---|---|---|
| F-test | size $\alpha$, exact | normal errors of equal variance | $\Theta(np^2)$ |
| Stepwise regression | a local optimum only | none | $\Theta(nm^2 + sm^2)$ |
| Leaps and bounds | best subset of each size, exact | none | $\Theta(nm^2 + 2^mm^2)$ worst |
| Durbin-Watson test, Monte Carlo | size $\alpha$, exact when $\alpha(B + 1)$ is an integer | normal errors, fixed $X$ | $\Theta(np^2 + Bnp)$ |
| Breusch-Pagan test, $nR^2$ form | size $\to \alpha$ | independent errors | $\Theta(n(p^2 + q^2))$ |
| HC standard errors | consistent | independent errors, any variances | $\Theta(np^2)$ |
| Weighted least squares | best linear unbiased | variances known up to a factor | $\Theta(np^2)$ |
| Generalized least squares | best linear unbiased | $V$ known up to a factor | $\Theta(n^3)$ dense |
| Cluster-robust standard errors | consistent as $G \to \infty$ | independent clusters | $\Theta(np^2)$ |
| Henderson's equations | GLS $\hat b$ and BLUP | known $G$ and $R$ | $\Theta(n(p + q)^2 + (p + q)^3)$ diagonal |
| REML by Fisher scoring | restricted likelihood never decreases; global maximum not proved | normal mixed model | $\Theta(tkn^3)$ dense |
| Iteratively reweighted least squares | a root of the score equations when it converges | GLM whose MLE exists | $\Theta(knp^2)$ |

: The main methods. $n$ observations, $p$ columns, $m$ candidate columns, $s$ stepwise steps, $B$ simulated samples, $q$ variance variables or random effects, $G$ clusters; for REML $k$ covariance parameters and $t$ evaluations, for IRLS $k$ passes.

## Choosing a method

Look before testing: a Q-Q plot of the residuals, residuals against fitted values, leverages and Cook's distances. If the variance grows with the mean, transform or weight; if you only need valid standard errors, keep the fit and use HC3, or cluster-robust errors when rows come in many groups. With few clusters use the wild cluster bootstrap. For repeated measures, a mixed model fitted by REML models the covariance. Choose a model by AIC for prediction and by BIC to find a small true model, and do not report the classical tests of the chosen model as if it had been fixed in advance.
