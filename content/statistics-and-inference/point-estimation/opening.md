Five measurements of the same quantity come back as 3, 7, 7, 9 and 14. Their mean is 8, their [sample variance](/sample-variance/) with divisor $n - 1$ is 16, and the [standard error](/standard-error/) of the mean is $4/\sqrt 5 \approx 1.79$. Each of these numbers comes from a rule applied to the data, and a second set of five measurements would give different numbers. Point estimation studies such rules. It asks what a rule estimates, how far its output tends to fall from the target, whether it gets closer as the sample grows, and whether some other rule does better.

The answers depend on what is assumed. The mean of iid data is unbiased for the population mean under any law with a finite mean, and its standard error needs only a finite variance. If the data are Poisson, the total $\sum x_i = 40$ carries all the information about the rate, and no unbiased estimator of the rate has a smaller variance than $\bar x$. If the data are normal and the mean is large compared with the spread, the formula $\sum x_i^2 - n\bar x^2$ for the sum of squares can return a negative number in floating point, and [Welford's algorithm](/welford-algorithm/) does not. The chapter keeps these levels apart: results that hold exactly at every $n$, results that hold only as $n \to \infty$, and results that need regularity conditions on the model.

## What the chapter covers

1. **Estimators and their errors.** The [estimator](/estimator/) as a rule, its [sampling distribution](/sampling-distribution/), [bias](/estimator-bias/), [standard error](/standard-error/) and [consistency](/consistent-estimator/).
2. **Computing the variance in one pass and in parallel.** [Welford's algorithm](/welford-algorithm/) and the [Chan-Golub-LeVeque merge](/chan-parallel-variance/), with exact results in exact arithmetic and measured rounding errors in floating point.
3. **Likelihood and information.** The [likelihood function](/likelihood-function/), the [Kullback-Leibler divergence](/kullback-leibler-divergence/), the [score](/score-function/) and its variance, and [Fisher scoring](/fisher-scoring/) for computing the maximum likelihood estimate.
4. **Sufficiency and the best unbiased estimator.** [Sufficient statistics](/sufficient-statistic/), the [factorization theorem](/fisher-neyman-factorization-theorem/), the [Cramér-Rao bound](/cramer-rao-bound/), the [Rao-Blackwell](/rao-blackwell-theorem/) and [Lehmann-Scheffé](/lehmann-scheffe-theorem/) theorems, [completeness](/complete-statistic/) and the [minimum variance unbiased estimator](/minimum-variance-unbiased-estimator/).
5. **Large-sample theory.** [Slutsky's theorem](/slutsky-theorem/), the [delta method](/delta-method/) and the [asymptotic normality of the MLE](/asymptotic-normality-of-mle/).
6. **Estimating equations.** The [method of moments](/method-of-moments/), [M-estimators](/m-estimator/) with the sandwich covariance, the [generalized method of moments](/generalized-method-of-moments/) and [empirical likelihood](/empirical-likelihood/).
7. **Decision theory and shrinkage.** [Statistical decision theory](/statistical-decision-theory/), [admissibility](/admissible-estimator/) and the [James-Stein estimator](/james-stein-estimator/).
8. **Sampling designs and missing data.** The [Horvitz-Thompson estimator](/horvitz-thompson-estimator/), the [missing-data mechanism](/missing-data-mechanism/), [multiple imputation](/multiple-imputation/) and [multiple imputation by chained equations](/multiple-imputation-by-chained-equations/).

## A first reading

For a first pass, read these entries in order:

- [Estimator](/estimator/)
- [Bias of an estimator](/estimator-bias/)
- [Standard error](/standard-error/)
- [Consistent estimator](/consistent-estimator/)
- [Welford's algorithm](/welford-algorithm/)
- [Likelihood function](/likelihood-function/)
- [Score function](/score-function/)
- [Sufficient statistic](/sufficient-statistic/)
- [Cramér-Rao bound](/cramer-rao-bound/)
- [Rao-Blackwell theorem](/rao-blackwell-theorem/)
- [Delta method](/delta-method/)
- [Asymptotic normality of the MLE](/asymptotic-normality-of-mle/)
- [M-estimator](/m-estimator/)
- [Missing-data mechanism](/missing-data-mechanism/)

They give the vocabulary of the chapter, one algorithm, the two classical routes to a good estimator (exact theory for unbiased estimators and large-sample theory for the MLE), and the estimating-equation view that covers most estimators used in practice. The rest of the chapter fills in the theorems behind these entries and the methods built on them.

## Before you start

The chapter uses the probability of Volume 1, Chapter 1.6: [random variables](/random-variable/), [expected value](/expected-value/), [variance](/variance/), [conditional expectation](/conditional-expectation/), [Jensen's inequality](/jensens-inequality/), [Chebyshev's inequality](/chebyshev-inequality/), the [law of large numbers](/law-of-large-numbers/) and the [central limit theorem](/central-limit-theorem/). From Volume 25 it uses [maximum likelihood estimation](/maximum-likelihood-estimation/), the [loss function](/loss-function/), [mean squared error](/mean-squared-error/) and the [exponential family](/exponential-family-distribution/); the entries here prove the properties of these objects and do not define them again. The two variance algorithms assume the [floating-point model](/floating-point-model/) of Volume 12. Calculus is needed throughout, and the vector forms of the theorems use matrices, inverses and positive definite quadratic forms.
