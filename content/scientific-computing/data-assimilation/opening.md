A weather forecast starts from an estimate of the present state of the atmosphere: wind, temperature,
pressure and moisture, between $10^7$ and $10^9$ numbers. No instrument measures that state. Satellites,
balloons, aircraft and ground stations give millions of observations a day, unevenly spread,
each with its own error and each measuring some function of the state rather than a grid value. Data
assimilation is the set of methods that combine these observations with a short forecast from the model,
the background, to make the best estimate of the state, called the analysis. The same methods estimate ocean
currents, reservoir properties, the spread of a disease and the parameters of a climate model.

All the methods solve one problem, set out in [the data assimilation problem](/data-assimilation-problem/):
find the distribution of the state given the background and the observations. For a linear model with
Gaussian errors the [Kalman filter](/kalman-filter/) solves it exactly, but its covariance has $n^2$ entries
and costs $\Theta(n^3)$ per cycle: for $n = 10^8$ the covariance alone would have $10^{16}$ entries. The chapter is about the two ways around this.
Variational methods keep a fixed, modelled covariance and solve a large least squares problem with an
adjoint model for the gradient. Ensemble methods carry a few tens of model runs and use their sample
covariance, repaired by inflation and localization. Several weather centres now use hybrids of the two.

## What the chapter covers

1. **The problem and its parts.** The [data assimilation problem](/data-assimilation-problem/), the
   [observation operator](/observation-operator/) and the
   [background error covariance](/background-error-covariance/), which decides how one observation spreads
   to the grid values near it. The [Lorenz-96 model](/lorenz-96-model/) is the chaotic test system of the
   chapter, and an [observing system simulation experiment](/observing-system-simulation-experiment/) is a
   test against a known synthetic truth.
2. **First methods.** [Nudging](/nudging/) relaxes the model towards the observations, and
   [optimal interpolation](/optimal-interpolation/) computes the best linear estimate from nearby
   observations.
3. **Variational assimilation.** [3D-Var](/three-dimensional-variational-assimilation/) minimizes a cost at
   one time, made well conditioned by the [control variable transform](/control-variable-transform/) and
   checked by the [Desroziers diagnostics](/desroziers-diagnostics/).
   [4D-Var](/four-dimensional-variational-assimilation/) fits a time window, with the gradient from the
   [adjoint model](/adjoint-model/), and [incremental 4D-Var](/incremental-4d-var/) is the form used in
   practice.
4. **Model error and the dual form.** [Weak-constraint 4D-Var](/weak-constraint-4d-var/) allows model error,
   and the [representer method](/representer-method/) solves the linear problem with one unknown per
   observation.
5. **The ensemble Kalman filter and its repairs.** The [ensemble Kalman filter](/ensemble-kalman-filter/),
   [covariance inflation](/covariance-inflation/), [covariance localization](/covariance-localization/) and
   the [Gaspari-Cohn function](/gaspari-cohn-function/).
6. **Deterministic ensemble filters and smoothers.** The
   [ensemble square root filter](/ensemble-square-root-filter/), the
   [EAKF](/ensemble-adjustment-kalman-filter/), the [ETKF](/ensemble-transform-kalman-filter/) and the
   [LETKF](/local-ensemble-transform-kalman-filter/); the [ensemble Kalman smoother](/ensemble-kalman-smoother/)
   and [ensemble Kalman inversion](/ensemble-kalman-inversion/).
7. **Hybrid methods.** [Hybrid ensemble-variational assimilation](/hybrid-ensemble-variational/) and
   [4DEnVar](/four-dimensional-ensemble-variational/), which needs no adjoint.
8. **Particle filters in high dimensions.** Why the particle filter
   [collapses](/particle-filter-weight-collapse/) when there are many observations, and how the
   [local particle filter](/local-particle-filter/) avoids it.

## A first reading

Read these in order:

1. [The data assimilation problem](/data-assimilation-problem/)
2. [Observation operator](/observation-operator/)
3. [Background error covariance](/background-error-covariance/)
4. [Optimal interpolation](/optimal-interpolation/)
5. [Lorenz-96 model](/lorenz-96-model/)
6. [3D-Var](/three-dimensional-variational-assimilation/)
7. [Adjoint model](/adjoint-model/)
8. [4D-Var](/four-dimensional-variational-assimilation/)
9. [Ensemble Kalman filter](/ensemble-kalman-filter/)
10. [Covariance inflation](/covariance-inflation/)
11. [Covariance localization](/covariance-localization/)
12. [LETKF](/local-ensemble-transform-kalman-filter/)
13. [Particle filter collapse in high dimensions](/particle-filter-weight-collapse/)

They give the problem, the two families and the main reason why particle filters are not used in weather
prediction. On a first pass, skip the diagnostics, the EAKF, the smoothers, the representer method and the
hybrids, and come back to them when a later entry needs them. [Nudging](/nudging/) is short and can be read
at any time.

## Before you start

The chapter assumes linear algebra and some probability. From Volume 25 you need the
[state-space model](/state-space-model/), [Bayes' theorem](/bayes-theorem/) and the
[covariance matrix](/covariance-matrix/). Read the [Kalman filter](/kalman-filter/) of Volume 28 first: every
method here is an approximation or a reformulation of it. From Volume 12 you need
[positive definite matrices](/positive-definite-matrix/), the
[Cholesky decomposition](/cholesky-decomposition/), the
[conjugate gradient method](/conjugate-gradient-method/) and the
[classical Runge-Kutta method](/classical-runge-kutta-4/). The variational entries use
[automatic differentiation](/automatic-differentiation/) (Volume 25) and the
[Gauss-Newton algorithm](/gauss-newton-algorithm/) (Volume 38). The last group uses the
[particle filter](/particle-filter/) (Volume 25) and the [effective sample size](/effective-sample-size/)
(Volume 17).
