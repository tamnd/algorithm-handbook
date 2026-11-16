## What to remember

- **Transforms and diagrams are exact for linear time-invariant models.** The [Laplace transform](/laplace-transform/) turns the differential equation into a rational $G(s)$. [Block diagram reduction](/block-diagram-reduction/) and [Mason's gain formula](/masons-gain-formula/) give the same overall gain; Mason's $\Delta$ is $\det(I - W)$. A pole-zero cancellation can hide an unstable mode.
- **Linearization is local.** The Jacobians at an [equilibrium](/equilibrium-point/) give a linear model whose eigenvalues decide local stability only when the equilibrium is hyperbolic. For a [time-varying system](/linear-time-varying-system/), stable frozen eigenvalues do not imply stability.
- **Sampling with a zero-order hold is exact at the samples.** $A_d = e^{Ah}$ and $B_d = \int_0^h e^{As}\,ds\, B$ come from one [matrix exponential](/matrix-exponential/) of a block matrix. Poles map by $z = e^{sh}$; zeros do not, and for relative degree 3 or more short sampling periods give a zero outside the unit circle.
- **Poles and zeros of a matrix are not those of its entries.** The [Smith-McMillan form](/smith-mcmillan-form/) defines them with multiplicities, and its McMillan degree is the order of a minimal realization.
- **An identification method is consistent only under its stated conditions.** The usual conditions: the model set contains the true system, the input is [persistently exciting](/persistent-excitation/) of high enough order, and the noise is what the method assumes. [Least squares on ARX](/least-squares-arx-identification/) is biased for colored equation noise, and input-based instruments and output error fits can be biased in [closed loop](/closed-loop-identification/).
- **The Hankel matrix carries the order.** The block Hankel matrix of exact [Markov parameters](/markov-parameters/) has rank equal to the minimal order. [Ho-Kalman](/ho-kalman-algorithm/) uses the exact rank; [ERA](/eigensystem-realization-algorithm/), [MOESP](/moesp/) and [N4SID](/n4sid/) look for a gap in the singular values, which is a judgment, not a test.
- **Accuracy has a price.** Under its conditions the prediction error method reaches the [Cramér-Rao bound](/cramer-rao-bound/) asymptotically for Gaussian noise, but it needs a local search. Subspace and IV methods need no search and have larger variance.

| Method | Data | Result | Cost | Consistent or exact when |
|---|---|---|---|---|
| [Process reaction curve](/process-reaction-curve/) | one step response | $K$, $L$, $T$ | $O(n)$ | exact for a true FOPDT response |
| [ETFE](/empirical-transfer-function-estimate/) | $u$, $y$ | $\hat G(e^{i\omega})$ at DFT frequencies | $O(N \log N + NM)$ | raw estimate not consistent, its variance does not shrink with $N$; smoothing trades bias for variance |
| [Least-squares ARX](/least-squares-arx-identification/) | $u$, $y$ | $A$, $B$ | $O(Nd^2 + d^3)$ | ARX data, white noise, PE input, open loop |
| [Instrumental variables](/instrumental-variable-identification/) | $u$, $y$ | $A$, $B$ | $O(Nd^2 + d^3)$ | open loop, noise independent of $u$, nonsingular $\mathbb{E}\,\zeta\varphi^T$ |
| [Prediction error method](/prediction-error-method/) | $u$, $y$ | any structure, noise model | $O(I(Nd^2 + d^3))$ | true system in the model set, informative data, global minimum |
| [Ho-Kalman](/ho-kalman-algorithm/) | exact Markov parameters | minimal $(A, B, C, D)$ | $O(N^2mnp + n^3)$ | noise-free data |
| [ERA](/eigensystem-realization-algorithm/) | measured impulse response | balanced $(A, B, C, D)$ | $O(N^3mp(m+p))$ | exact on noise-free data; biased under noise |
| [MOESP](/moesp/), [N4SID](/n4sid/) | $u$, $y$ | $(A, B, C, D)$, N4SID also noise covariances | QR and SVD, no search | MOESP: white output noise; N4SID: innovation noise, and this basic version needs a white input |
| [Kernel-based](/kernel-based-identification/) | $u$, $y$ | long impulse response | $O(Nd^2 + Gd^3)$ | posterior mean under the Gaussian prior |
| [DMD](/dynamic-mode-decomposition/) | state snapshots | eigenvalues and modes | $O(qM\min(q, M) + qMr + r^4)$ | exact for linear data with an invariant range |
| [SINDy](/sindy/) | states and derivatives | sparse $\dot x = \Xi^T\theta(x)$ | $O(nMp^3)$ | exact derivatives, full-rank library, threshold below the smallest true coefficient |

: Identification methods of the chapter. The last column gives the conditions stated in each entry.

## Choosing a method

For a first model of a stable plant, read $K$, $L$ and $T$ off the [process reaction curve](/process-reaction-curve/); PID tuning rules need no more. To see the frequency response first, compute a smoothed [ETFE](/empirical-transfer-function-estimate/). For a parametric model, design the input first: a [PRBS](/prbs-input/) of period $M$ is persistently exciting of order $M$. Then fit [ARX by least squares](/least-squares-arx-identification/). If the residuals are correlated, refit with [instrumental variables](/instrumental-variable-identification/), or with the [prediction error method](/prediction-error-method/) on an [ARMAX](/armax-model/), [output error](/output-error-model/) or Box-Jenkins structure, started from the least squares or IV estimate. With several inputs and outputs, or an unknown order, start from a subspace method such as [N4SID](/n4sid/). For data from a running loop, add an external reference signal and see [closed-loop identification](/closed-loop-identification/). For a measured impulse response, use [ERA](/eigensystem-realization-algorithm/). For short records of a stable system, a [kernel-based](/kernel-based-identification/) FIR estimate avoids choosing an order. Snapshots of a large field call for [DMD](/dynamic-mode-decomposition/), and a nonlinear system with a library of plausible terms for [SINDy](/sindy/).
