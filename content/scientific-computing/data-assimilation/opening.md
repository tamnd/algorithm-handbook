Every six hours a weather centre starts a new forecast. Its model state has hundreds of millions of variables, and in the last six hours it has received millions of observations from satellites, radiosondes, aircraft and ground stations, each with its own errors and most measuring something other than the model variables. Data assimilation combines the two: it takes the previous forecast as a background, compares it with the observations through an observation operator, and finds the state that best fits both, weighted by their error covariances. The result, the analysis, starts the next forecast.

For a linear model with Gaussian errors the answer is the Kalman filter, but its covariance matrix has the square of the state dimension as its size and cannot even be stored for a weather model. Operational methods get around that in two ways. Variational methods, 3D-Var and 4D-Var, minimize a cost function over the state, or over a whole window of time with the model as a constraint, using an adjoint model for the gradient. Ensemble Kalman filters estimate the covariance from a few dozen model runs and need localization and inflation to keep that small sample from producing spurious correlations and collapsing. Particle filters, which make no Gaussian assumption, collapse in high dimensions unless the number of particles grows exponentially with an effective dimension.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **The problem.** The data assimilation problem, the observation operator, the background error covariance, optimal interpolation and nudging, the Lorenz-96 model and observing system simulation experiments.
2. **Variational assimilation.** Three- and four-dimensional variational assimilation, incremental and weak-constraint 4D-Var, the adjoint model, the control variable transform and the representer method.
3. **Ensemble Kalman filters.** The ensemble Kalman filter and its square root, transform, local transform and adjustment forms, covariance inflation, covariance localization with the Gaspari-Cohn function, the ensemble Kalman smoother and ensemble Kalman inversion.
4. **Hybrids, nonlinearity and diagnostics.** Hybrid ensemble-variational and four-dimensional ensemble-variational assimilation, particle filter collapse in high dimensions, local particle filters and the Desroziers diagnostics.

## What to read meanwhile

Read the [Kalman filter](/kalman-filter/) in Volume 28, the [extended](/extended-kalman-filter/) and [unscented](/unscented-kalman-filter/) Kalman filters, the [Rauch-Tung-Striebel smoother](/rauch-tung-striebel-smoother/) and the [particle filter](/particle-filter/) with [sequential Monte Carlo](/sequential-monte-carlo/) in Volume 25, and the continuous-time [Kalman-Bucy filter](/kalman-bucy-filter/) in Volume 36.

For variational methods, the gradient of a cost through a model comes from [adjoint sensitivity analysis](/adjoint-sensitivity-analysis/) in Volume 32, the same idea as reverse-mode [automatic differentiation](/automatic-differentiation/) in Volume 25, and the minimization uses quasi-Newton methods such as [BFGS](/bfgs/) in Volume 15 or the [conjugate gradient method](/conjugate-gradient-method/) in Volume 12. Optimal interpolation is a close relative of [kriging](/kriging/) (Volume 12).
