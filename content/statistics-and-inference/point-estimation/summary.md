## What to remember

- An [estimator](/estimator/) is a function of the data, and its quality is a property of its [sampling distribution](/sampling-distribution/). The [mean squared error](/mean-squared-error/) is variance plus squared [bias](/estimator-bias/), so a biased estimator can have the smaller error. The [sample variance](/sample-variance/) is unbiased for $\sigma^2$, its square root is not unbiased for $\sigma$.
- In floating point, $\sum x_i^2 - n\bar x^2$ can lose every digit and even turn negative. [Welford's algorithm](/welford-algorithm/) updates the mean and the sum of squared deviations in one pass, and the [Chan-Golub-LeVeque merge](/chan-parallel-variance/) combines two partial results exactly in exact arithmetic. The merge is associative, so a tree of merges has span $\Theta(\log n)$.
- The [likelihood](/likelihood-function/) is a function of the parameter, not a density over it. Under regularity conditions the [score](/score-function/) has mean zero and variance equal to the Fisher information. Maximizing the expected log-likelihood minimizes the [Kullback-Leibler divergence](/kullback-leibler-divergence/) from the true law, and [Fisher scoring](/fisher-scoring/) is Newton's method with the expected information.
- A [sufficient statistic](/sufficient-statistic/) keeps everything the data say about $\theta$, and the [factorization theorem](/fisher-neyman-factorization-theorem/) finds it. [Rao-Blackwell](/rao-blackwell-theorem/) conditioning on it never raises the risk under convex loss. If the statistic is also [complete](/complete-statistic/), [Lehmann-Scheffé](/lehmann-scheffe-theorem/) says the result is the unique [UMVUE](/minimum-variance-unbiased-estimator/). These results are exact at every $n$.
- The [Cramér-Rao bound](/cramer-rao-bound/) $1/(nI(\theta))$ holds only for unbiased estimators under regularity conditions; it fails for the uniform family, whose support moves with $\theta$. The UMVUE need not reach it.
- [Slutsky's theorem](/slutsky-theorem/) and the [delta method](/delta-method/) carry limits through sums, products and smooth maps. If $g'(\theta) = 0$, the second-order term gives a scaled $\chi^2_1$ limit at rate $n$.
- The [asymptotic normality of the MLE](/asymptotic-normality-of-mle/) is a limit theorem with conditions. Hodges's estimator beats it at one point, and in the Neyman-Scott problem, with a parameter per pair, the MLE is not consistent.
- [Method of moments](/method-of-moments/), MLE, least squares and [Huber's estimator](/huber-m-estimator/) are all [M-estimators](/m-estimator/), with the sandwich covariance $A^{-1}BA^{-\top}/n$. [GMM](/generalized-method-of-moments/) weights more moment conditions than parameters, and the J test checks the extra ones. [Empirical likelihood](/empirical-likelihood/) builds a likelihood ratio from the conditions alone. All three are asymptotic.
- In three or more dimensions the sample mean of a normal vector is inadmissible under squared error: the [James-Stein estimator](/james-stein-estimator/) has smaller risk at every $\theta$. Under a design, the [Horvitz-Thompson estimator](/horvitz-thompson-estimator/) is exactly unbiased whenever every inclusion probability is positive. [Multiple imputation](/multiple-imputation/) is valid under its [mechanism](/missing-data-mechanism/), usually MAR, which the data cannot confirm.

| Method | What it needs | Exact or asymptotic | Standard error |
|---|---|---|---|
| [UMVUE](/minimum-variance-unbiased-estimator/) via [Lehmann-Scheffé](/lehmann-scheffe-theorem/) | complete sufficient statistic | exact, unbiased at every $n$ | from the exact sampling law |
| [MLE](/asymptotic-normality-of-mle/) | parametric model, regularity conditions | asymptotic | $1/\sqrt{nI(\hat\theta)}$ or observed information |
| [Method of moments](/method-of-moments/) | as many moments as parameters | consistent; asymptotic normality | delta method or sandwich |
| [M-estimator](/m-estimator/) | estimating function with a unique root | asymptotic | sandwich $A^{-1}BA^{-\top}/n$ |
| [GMM](/generalized-method-of-moments/) | more moment conditions than parameters | asymptotic | $(G^\top S^{-1}G)^{-1}/n$; J test for the extras |
| [Empirical likelihood](/empirical-likelihood/) | moment conditions, no model | asymptotic $\chi^2$ calibration | interval by inverting the ratio |
| [James-Stein](/james-stein-estimator/) | $p \ge 3$ normal means, known $\sigma^2$ | exact risk dominance | not the target; risk is the measure |
| [Horvitz-Thompson](/horvitz-thompson-estimator/) | known $\pi_i > 0$ for every unit | exact unbiasedness | $v_{\mathrm{HT}}$ or $v_{\mathrm{SYG}}$, needs $\pi_{ij}$ |
| [Multiple imputation](/multiple-imputation/) | an imputation model, usually MAR | valid under its assumptions | Rubin's rules $\bar W + (1 + 1/m)B$ |

: The estimators of the chapter: what each assumes, which guarantees hold at every $n$, and the standard error.

## Choosing a method

Start from the model. For a regular parametric family the MLE is the default: compute it by Newton's method or Fisher scoring, report the inverse information as its variance, and check that the normal limit is close enough. If the family has a complete sufficient statistic and unbiasedness matters, condition on it and get the UMVUE.

If the model is not trusted, use an M-estimator for the estimating equations you believe, with the sandwich variance; with more conditions than parameters, use two-step GMM and report the J statistic. For outliers, use Huber's estimator.

When many means are estimated at once and only the total squared error matters, shrink them, toward zero or toward their mean. Under a known design with unequal inclusion probabilities, weight each unit by $1/\pi_i$. When values are missing, state the mechanism first; under MAR, impute several times and pool with Rubin's rules, and under MNAR, report a sensitivity analysis. For the variance itself, use Welford's update in a stream and the Chan merge across threads or machines.
