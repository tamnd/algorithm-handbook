## What to remember

- **The model is fidelity plus regularizer.** [Variational regularization](/variational-regularization/) minimizes a [data fidelity term](/data-fidelity-term/) plus $\lambda R(x)$. The fidelity is the negative log likelihood of the noise. Under convexity and coercivity hypotheses, minimizers exist, are stable, and converge when $\lambda \to 0$ and $\delta^2/\lambda \to 0$.
- **Rates are measured in a Bregman distance.** Under the source condition $A^*w \in \partial R(x^\dagger)$ and $\lambda \sim \delta$, the [Bregman distance](/bregman-distance-convergence-rates/) to $x^\dagger$ is of order $\delta$. The distance is weak: for $\ell_1$ or total variation it is 0 between $x^\dagger$ and $tx^\dagger$.
- **Nonsmooth solvers split the terms.** The [Chambolle-Pock algorithm](/chambolle-pock-algorithm/) converges for $\tau\sigma\|K\|^2 < 1$ with an ergodic gap of order $1/N$. The [split Bregman method](/split-bregman-method/) is ADMM and converges for every $\mu > 0$. [Bregman iteration](/bregman-iteration/) restores contrast and must be stopped when the data are noisy.
- **The null space property is the exact condition for basis pursuit.** Basis pursuit recovers every $s$-sparse vector exactly when the [null space property](/null-space-property/) of order $s$ holds, and checking it is NP-hard. [Mutual coherence](/mutual-coherence/) is easy to compute and gives recovery for $s < \tfrac12(1 + 1/\mu)$, but by the Welch bound this stops near $\sqrt m/2$ when $n \gg m$.
- **Random measurements beat the square-root bottleneck.** The [Candès-Romberg-Tao theorem](/candes-romberg-tao-theorem/) recovers an $s$-sparse signal from about $s\log N$ random Fourier samples with high probability. For Gaussian matrices the [Donoho-Tanner phase transition](/donoho-tanner-phase-transition/) is sharp as the dimension grows and blurred in small dimensions.
- **Greedy methods have restricted isometry guarantees.** [Iterative hard thresholding](/iterative-hard-thresholding/) contracts the error by $2\delta_{3s}$ per step when $\delta_{3s} < 1/2$, and [CoSaMP](/cosamp/) reaches a noise floor under $\delta_{4s} \le 0.1$. [Approximate message passing](/approximate-message-passing/) is predicted exactly by state evolution, but only for Gaussian matrices in the large system limit, and it can diverge for structured matrices.
- **Learned dictionaries are hard to learn exactly.** [Dictionary learning](/dictionary-learning/) is NP-hard and identifiable at best up to $2^K K!$ signed permutations. [K-SVD](/k-svd/) never increases its objective if the sparse coder is exact.
- **Learned methods inherit guarantees only from their base method.** An [unrolled network](/algorithm-unrolling/) with the base parameters is the base method, so [LISTA](/lista/) with the ISTA weights has the ISTA bound. [Plug-and-play](/plug-and-play-priors/) converges when the denoiser meets stated conditions, [RED](/regularization-by-denoising/) has the gradient $x - D(x)$ only for a locally homogeneous denoiser with a symmetric Jacobian, and [diffusion posterior sampling](/diffusion-posterior-sampling/) does not sample the posterior even with the exact score. Beyond that, performance is measured on named data sets.

| Method | Guarantee | Condition | Notes |
|:--|:--|:--|:--|
| Basis pursuit | exact recovery of every $s$-sparse vector | null space property of order $s$ | checking the condition is NP-hard |
| Iterative hard thresholding | linear convergence to a noise floor | $\delta_{3s} < 1/2$ | not scale invariant |
| CoSaMP | geometric decrease to a noise floor | $\delta_{4s} \le 0.1$ | scale invariant |
| Approximate message passing | state evolution is exact | Gaussian matrix, large system limit | can diverge for structured matrices |
| Chambolle-Pock | convergence, ergodic gap $O(1/N)$ | convex $F$, $G$; $\tau\sigma\|K\|^2 < 1$ | a proximal point method in a fixed metric |
| Plug-and-play ADMM | convergence | stated conditions on the denoiser | trained denoisers are measured |
| LISTA, learned primal-dual | the base bound | the weights of the base method | trained weights are measured |
| Generative compressed sensing | an error bound | set-restricted eigenvalue condition | measured on MNIST and CelebA |
| Diffusion posterior sampling | a bound on the Jensen gap | the assumptions of that bound | measured on FFHQ and ImageNet |

: The main methods of the chapter, what is proved about them and under which condition, and where the evidence is measured instead.

## Choosing a method

- **Edges matter and the noise is Gaussian.** Use total variation, solved by [Chambolle's projection algorithm](/chambolle-projection-algorithm/) for denoising and by Chambolle-Pock otherwise. If ramps turn into staircases, use [total generalized variation](/total-generalized-variation/).
- **The noise is Poisson or impulsive.** Use a Kullback-Leibler or $\ell_1$ [fidelity](/data-fidelity-term/).
- **Contrast is lost.** Run a few steps of [Bregman iteration](/bregman-iteration/) and stop by the discrepancy principle.
- **The signal is sparse in a known basis and the matrix is random.** Use basis pursuit, [IHT](/iterative-hard-thresholding/) or [CoSaMP](/cosamp/). Use [AMP](/approximate-message-passing/) only when the matrix is close to i.i.d. Gaussian.
- **No basis makes the signal sparse.** Learn one with [K-SVD](/k-svd/), or with [convolutional sparse coding](/convolutional-sparse-coding/) for whole images.
- **Training pairs are available.** Unroll a method with a guarantee, such as [learned primal-dual](/learned-primal-dual/).
- **Only a denoiser is available.** Use [plug-and-play](/plug-and-play-priors/) or [RED](/regularization-by-denoising/).
- **A posterior is wanted.** [Diffusion posterior sampling](/diffusion-posterior-sampling/) gives plausible samples, not exact posterior draws.
