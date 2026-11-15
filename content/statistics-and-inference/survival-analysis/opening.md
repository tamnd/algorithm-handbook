In the leukemia trial of Freireich and colleagues, 21 patients in remission received 6-mercaptopurine and 21 received a placebo, and the outcome was the time to relapse. All 21 placebo patients relapsed during the study. On the drug, only 9 relapsed, and the other 12 were still in remission when their follow-up ended, at times between 6 and 35 weeks. For those 12 the data say only that the relapse time is larger than the last visit. Dropping them throws away the patients who did best, and treating their last visit as a relapse makes the drug look worse than it is. Survival analysis is the set of methods that use such partial times correctly. With them the 6-MP data give a median remission of 23 weeks, against 8 weeks on placebo, and a log-rank test that rejects equal hazards with a p-value of about $4 \times 10^{-5}$.

The same structure appears whenever the outcome is a waiting time and observation can stop first: time to failure of a component on a test bench that ends after 1000 hours, time to default of a loan that is still being repaid, time to a customer leaving a service, time to the onset of a disease found only at periodic examinations. The methods of this chapter are also short algorithms. Most are one sort followed by a pass over the risk sets, the sets of subjects still under observation at each event time, and their cost is $\Theta(n \log n)$.

Two habits run through the chapter. The first is to keep the estimator apart from the theorem that justifies it. The Kaplan-Meier curve is the nonparametric maximum likelihood estimate, but its confidence intervals are asymptotic. The log-rank p-value comes from a chi-squared approximation. The Cox model estimates hazard ratios only if the hazards are in fact proportional. The second habit is to keep track of the assumption about censoring. Every method here assumes that the subjects still under observation have the same hazard as the ones who left, and [censoring](/censoring/) explains why the data cannot test that assumption.

## What the chapter covers

1. **Event times and censoring.** The [survival function](/survival-function/) $S(t) = P(T > t)$, the kinds of [censoring](/censoring/) and their likelihood, and the [hazard function](/hazard-function/) $h = f/S$ with $S = \exp(-H)$ in continuous time.
2. **Estimating a survival curve.** The [Kaplan-Meier estimator](/kaplan-meier-estimator/), the [Nelson-Aalen estimator](/nelson-aalen-estimator/) of the cumulative hazard, [Greenwood's formula](/greenwood-formula/) for the variance and pointwise confidence intervals, and the [Turnbull estimator](/turnbull-estimator/) for interval-censored data.
3. **Comparing groups.** The [log-rank test](/log-rank-test/), its weighted versions, and the number of events a trial needs.
4. **The Cox model.** The [proportional hazards model](/cox-proportional-hazards-model/), its [partial likelihood](/cox-partial-likelihood/) and the rules for ties, the [Breslow estimator](/breslow-estimator/) of the baseline hazard, and the [Schoenfeld residuals](/schoenfeld-residuals/) that check proportionality.
5. **Other models and prediction.** The [accelerated failure time model](/accelerated-failure-time-model/), where covariates stretch time, the [frailty model](/frailty-model/) for clustered data and unobserved heterogeneity, and [Harrell's C](/harrell-c-index/) for the ranking quality of a risk score.
6. **Competing risks.** [Competing risks](/competing-risks/) and the cumulative incidence function, the [Aalen-Johansen estimator](/aalen-johansen-estimator/), and the [Fine-Gray model](/fine-gray-model/) for covariate effects on the cumulative incidence.

## A first reading

A first course reads these entries in order:

1. [Survival function](/survival-function/)
2. [Censoring](/censoring/)
3. [Hazard function](/hazard-function/)
4. [Kaplan-Meier estimator](/kaplan-meier-estimator/)
5. [Nelson-Aalen estimator](/nelson-aalen-estimator/)
6. [Greenwood's formula](/greenwood-formula/)
7. [Log-rank test](/log-rank-test/)
8. [Cox proportional hazards model](/cox-proportional-hazards-model/)
9. [Cox partial likelihood](/cox-partial-likelihood/)
10. [Competing risks](/competing-risks/)

The Breslow estimator and the Schoenfeld residuals come next, when you fit Cox models in practice. The Turnbull estimator, the frailty model, the Aalen-Johansen estimator and the Fine-Gray model can wait until you meet interval-censored, clustered or multistate data. The proofs in the Greenwood and log-rank entries use martingale limit theorems and can be skipped at first; their statements are what the rest of the chapter needs.

## Before you start

The chapter assumes [random variables](/random-variable/), [probability distributions](/probability-distribution/), [densities](/probability-density-function/) and [conditional probability](/conditional-probability/) from Volume 1, and the [central limit theorem](/central-limit-theorem/) for the large-sample results. The counting process proofs use [martingales](/martingale/), also in Volume 1. From earlier chapters of this volume it uses the [likelihood function](/likelihood-function/), the [score function](/score-function/), the [delta method](/delta-method/) and [Slutsky's theorem](/slutsky-theorem/), the [empirical distribution function](/empirical-distribution-function/), and [hypothesis tests](/statistical-hypothesis-test/) with their [p-values](/p-value/). [Maximum likelihood estimation](/maximum-likelihood-estimation/) and the [EM algorithm](/expectation-maximization/) are in Volume 25, and [Newton's method](/newton-raphson-method/), used to fit the Cox model, is in Volume 12. The Fine-Gray model uses [inverse probability weighting](/inverse-probability-weighting/) from the chapter on causal inference.
