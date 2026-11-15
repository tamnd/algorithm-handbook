Take ten daily readings, $3, 5, 6, 4, 2, 1, 3, 6, 7, 5$. Their mean is $4.2$, and their sample autocorrelation at lag 1 is $69/140 \approx 0.49$: a high day tends to follow a high day. The usual formulas of statistics assume independent observations, and here they fail. The variance of the mean is not $\sigma^2/n$, a regression of one random walk on another unrelated one looks significant far too often, and a forecast must use the order of the data. Time series analysis gives models in which the dependence is the object of study: the [autoregression](/autoregressive-model/), the [moving average](/moving-average-model/) and the [ARMA model](/arma-model/), with their fitting and checking algorithms.

The second half of the chapter is about data that arrive over time and decisions made while they arrive. A clinical trial that tests at the 5% level at each of five equally spaced looks has an overall false positive rate of about $0.14$, not $0.05$. A factory wants an alarm soon after a machine goes out of adjustment, and few false alarms before. An online experiment is watched every day by people who stop when the result looks good. [Sequential tests](/sequential-probability-ratio-test/), [group sequential designs](/group-sequential-design/), [change-point detection](/change-point-detection/) and [test martingales](/test-martingale/) answer these problems, each with a guarantee that holds under stated assumptions.

## What the chapter covers

1. **Stationary processes and linear models.** A [stationary process](/stationary-process/) has a mean and autocovariances that do not change over time. The AR, MA and ARMA models describe such processes with a few parameters, the [partial autocorrelation](/partial-autocorrelation-function/) helps identify the order, and the [Wold decomposition](/wold-decomposition-theorem/) shows that every stationary series is an infinite moving average of its own one-step prediction errors plus a deterministic part.
2. **Fitting a linear model.** The [Yule-Walker equations](/yule-walker-equations/) fit an autoregression in $\Theta(np)$ time. The [innovations algorithm](/innovations-algorithm/) computes the exact Gaussian likelihood and the one-step predictors, and the [Whittle likelihood](/whittle-likelihood/) approximates the likelihood with the periodogram.
3. **Trends, seasons and model building.** The [ARIMA model](/arima-model/) differences a series to remove a trend. [Holt-Winters smoothing](/holt-winters-method/) and [STL](/stl-decomposition/) split a series into level, trend and season. The [Box-Jenkins method](/box-jenkins-method/) identifies, fits and checks a model, with the [Ljung-Box test](/ljung-box-test/) as its residual check, and the [GARCH model](/garch-model/) describes a variance that changes over time.
4. **Several series at once.** A [vector autoregression](/vector-autoregression/) models several series together, and [Granger causality](/granger-causality/) tests whether one series helps predict another.
5. **Unit roots and cointegration.** The [augmented Dickey-Fuller test](/augmented-dickey-fuller-test/) and the [KPSS test](/kpss-test/) ask whether a series has a unit root. [Cointegrated](/cointegration/) series share a stochastic trend, and the [Engle-Granger](/engle-granger-test/) and [Johansen](/johansen-test/) tests find the stationary combinations.
6. **Sequential tests and group sequential trials.** Wald's [SPRT](/sequential-probability-ratio-test/) tests two simple hypotheses one observation at a time. Group sequential designs with [O'Brien-Fleming boundaries](/obrien-fleming-boundary/) or an [alpha spending function](/alpha-spending-function/) allow a few planned looks at level $\alpha$.
7. **Change points.** Offline methods split a series into segments: the exact dynamic program, [PELT](/pelt-algorithm/) and [binary segmentation](/binary-segmentation/). Online methods raise an alarm: [CUSUM](/cusum/) and the [Bayesian online changepoint detector](/bayesian-online-changepoint-detection/).
8. **Anytime-valid inference.** [Ville's inequality](/ville-inequality/) turns a test martingale into a test that is valid at every stopping time. It gives [confidence sequences](/confidence-sequence/) and the [mixture SPRT](/mixture-sequential-probability-ratio-test/).

## A first reading

Read these in order:

- [Stationary process](/stationary-process/)
- [Autoregressive model](/autoregressive-model/)
- [Moving-average model](/moving-average-model/)
- [ARMA model](/arma-model/)
- [Partial autocorrelation function](/partial-autocorrelation-function/)
- [ARIMA model](/arima-model/)
- [Box-Jenkins method](/box-jenkins-method/)
- [Augmented Dickey-Fuller test](/augmented-dickey-fuller-test/)
- [Change-point detection](/change-point-detection/)
- [CUSUM](/cusum/)
- [Sequential probability ratio test](/sequential-probability-ratio-test/)
- [Group sequential design](/group-sequential-design/)
- [Test martingale](/test-martingale/)

The fitting algorithms of the second group, the Wold decomposition, cointegration and the Johansen test can wait until a model has to be fitted by hand or a proof has to be read. A reader who only needs sequential methods can start at the sixth group after the first three entries of the list.

## Before you start

The chapter uses probability from Volume 1: [random variables](/random-variable/), [martingales](/martingale/), the [optional stopping theorem](/optional-stopping-theorem/), [Markov's inequality](/markov-inequality/) and [Wald's equation](/walds-equation/), with the [law of large numbers](/law-of-large-numbers/) and the [central limit theorem](/central-limit-theorem/). From Volume 25 it uses [ordinary least squares](/ordinary-least-squares/), the [covariance matrix](/covariance-matrix/) and [maximum likelihood estimation](/maximum-likelihood-estimation/). From Volume 12 come the [Cholesky decomposition](/cholesky-decomposition/), the [Levinson-Durbin recursion](/levinson-durbin-recursion/) and [numerical integration](/numerical-integration/), and from Volume 28 [autocorrelation](/autocorrelation/), the [periodogram](/periodogram/) and [linear prediction](/linear-prediction/). The tests build on the [hypothesis tests](/statistical-hypothesis-test/), [p-values](/p-value/), [type I and type II errors](/type-i-and-type-ii-errors/) and [likelihood ratio tests](/likelihood-ratio-test/) of this volume. Complex numbers appear in the conditions on the roots of polynomials.
