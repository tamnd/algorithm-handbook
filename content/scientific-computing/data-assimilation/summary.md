## What to remember

- **One update underlies everything.** The analysis is $x^a = x^b + K(y - Hx^b)$ with
  $K = BH^\top(HBH^\top + R)^{-1}$ and covariance $(I - KH)B$. It is the best linear estimate for errors
  with these covariances, and the exact posterior mean only for a linear model with Gaussian errors.
- **The background covariance spreads the observations.** One observation of value $j$ with innovation $d$
  changes the state by $d\,B_{:,j}/(B_{jj} + r)$, a column of $B$. A large system never stores $B$; it
  models it by operators or takes it from an ensemble.
- **Variational methods are least squares.** With the control variable transform the 3D-Var Hessian is
  $I + U^\top H^\top R^{-1}HU$, and conjugate gradients need at most $p + 1$ steps. 4D-Var gets its gradient
  from one forward and one adjoint run. For a linear model it gives the Kalman analysis at the end of the
  window; for a nonlinear model it finds a stationary point.
- **An ensemble covariance is low rank and noisy.** It has rank at most $N - 1$, and the squared sample
  correlation of two independent variables has mean $1/(N - 1)$. Inflation restores the spread;
  localization by $L \circ P$ removes distant correlations and keeps positive semidefiniteness by the Schur
  product theorem when $L$ is positive semidefinite. The Gaspari-Cohn function gives such an $L$ in
  $\mathbb R^3$; with the distance along a ring it can fail, as on the 40-point ring for half-widths
  $c \ge 11$.
- **The stochastic EnKF needs perturbed observations.** Without them the analysis covariance is too small by
  $KRK^\top$. Square root filters (EnSRF, EAKF, ETKF) reach the Kalman covariance by a deterministic
  transform instead.
- **Hybrids mix the two covariances.** $B = \beta_c^2B_c + \beta_e^2\,L \circ (X'X'^\top)$ is full rank
  and follows the flow, and its weights must be tuned. 4DEnVar replaces the adjoint by ensemble trajectories.
- **Global particle filters collapse.** With Gaussian log weights of standard deviation $\tau$ the largest
  weight tends to 1 unless $\log N$ grows like $\tau^2$, and $\tau^2 = \tfrac52 n$ for $n$ independent
  unit-variance observations.
- **Twin experiments are measurements.** A Lyapunov exponent of about 1.7 for Lorenz-96 with $n = 40$,
  $F = 8$, or the error of a filter for one inflation and one radius, holds for that set-up and that seed.

| Method | Covariance used | Adjoint needed | Time of one analysis | Linear Gaussian case |
|---|---|---|---|---|
| [Optimal interpolation](/optimal-interpolation/) | static $B$, local | no | $\Theta(ns^3)$ | Kalman analysis when all observations are used |
| [3D-Var](/three-dimensional-variational-assimilation/) | static $B$ | no | $\Theta(n^3 + p^3 + km(n^2 + np + p^2))$ | Kalman analysis for the given $B$ |
| [4D-Var](/four-dimensional-variational-assimilation/) | static $B$, carried by the model | yes | $\Theta(n^3 + I(Kc + n^2 + np))$ | Kalman analysis at the end of the window |
| [EnKF](/ensemble-kalman-filter/) | ensemble, localized | no | $\Theta(Np(n + p) + p^3)$ | Kalman analysis as $N \to \infty$ |
| [EnSRF](/ensemble-square-root-filter/) | ensemble, localized | no | $\Theta(pN(n + p))$ | Kalman moments of the sample, exactly |
| [LETKF](/local-ensemble-transform-kalman-filter/) | ensemble, local | no | $\Theta(Np + n(p + s^2N + s^3))$ | Kalman moments without localization |
| [Hybrid EnVar](/hybrid-ensemble-variational/) | static and ensemble | no | $\Theta(n^3 + p^3 + m(Nn^2 + pn + p^2))$ | 3D-Var with the hybrid $B$ |
| [4DEnVar](/four-dimensional-ensemble-variational/) | ensemble over the window | no | $\Theta(NKc + n^3 + p^3 + m(KNn^2 + pn))$ | 4D-Var when $X'_0X'^\top_0 = B$, no localization |
| [Local particle filter](/local-particle-filter/) | none (weights) | no | $\Theta(Np + nNq)$ | exact marginals only for independent components |

: The main analysis methods, with dense matrices as in the entries: $n$ state size, $p$ observations, $N$
members, $K$ model steps of cost $c$, $s$ and $q$ local observations, $k$, $m$ and $I$ iteration counts.

## Choosing a method

- **To learn or to test an idea,** run an [observing system simulation experiment](/observing-system-simulation-experiment/)
  on the [Lorenz-96 model](/lorenz-96-model/), and check the code against the exact
  [Kalman filter](/kalman-filter/) on a linear model first.
- **With a maintained adjoint and a good static covariance,** use incremental 4D-Var, which uses every
  observation of the window at its time.
- **With no adjoint,** use the [LETKF](/local-ensemble-transform-kalman-filter/) or a serial
  [EnSRF](/ensemble-square-root-filter/), always with [inflation](/covariance-inflation/) and
  [localization](/covariance-localization/) tuned in twin experiments.
- **With both a variational system and an ensemble,** use a [hybrid](/hybrid-ensemble-variational/), or
  [4DEnVar](/four-dimensional-ensemble-variational/) to drop the adjoint.
- **For parameters of a model you can only run,** use [ensemble Kalman inversion](/ensemble-kalman-inversion/).
- **For non-Gaussian problems,** a [particle filter](/particle-filter/) works in low dimensions; in high
  dimensions only a localized one, such as the [local particle filter](/local-particle-filter/), can.
