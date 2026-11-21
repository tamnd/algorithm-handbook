Classical regularization asks for a solution that is small or smooth in a quadratic sense, and its answers are linear in the data. Variational reconstruction drops the quadratic: minimize a data fidelity term, which measures how well a candidate image explains the measurements, plus a regularizer that encodes what images look like. With total variation as the regularizer, edges survive and noise does not. With an $\ell_1$ norm of wavelet coefficients, sparse images win. The price is that the objective is nonsmooth, so the solvers are proximal and primal-dual methods instead of linear algebra, and the convergence theory measures errors in a Bregman distance instead of a norm.

Sparsity also changed what counts as enough data. Compressed sensing showed that an $s$-sparse vector can be recovered exactly from far fewer measurements than unknowns, under conditions on the measurement matrix: the null space property, small coherence, or the restricted isometry property. These conditions can be proved for random matrices, and for Gaussian matrices the boundary between success and failure is known as the dimension grows.

The last part adds learned priors. A denoiser trained on examples can stand in for the proximal step of an optimization method, an iterative algorithm can be unrolled into a network whose parameters are learned, and a generative model can describe the set of plausible images. These methods give the best reconstructions on many benchmarks. Their guarantees hold only under stated assumptions, such as a denoiser that is a proximal map or a generator whose range satisfies a set-restricted eigenvalue condition, and otherwise their performance is measured on named data sets. The entries keep the two apart, and so does this chapter.

## What the chapter covers

1. **Variational models.** The [data fidelity term](/data-fidelity-term/), [variational regularization](/variational-regularization/), [total generalized variation](/total-generalized-variation/), [analysis and synthesis sparsity](/analysis-and-synthesis-sparsity/) and [convergence rates in the Bregman distance](/bregman-distance-convergence-rates/).
2. **Solvers for nonsmooth models.** [Chambolle's projection algorithm](/chambolle-projection-algorithm/), the [Chambolle-Pock algorithm](/chambolle-pock-algorithm/), [Bregman iteration](/bregman-iteration/) and the [split Bregman method](/split-bregman-method/).
3. **When sparse recovery works.** The [null space property](/null-space-property/), [mutual coherence](/mutual-coherence/), the [Candès-Romberg-Tao theorem](/candes-romberg-tao-theorem/) and the [Donoho-Tanner phase transition](/donoho-tanner-phase-transition/).
4. **Sparse recovery algorithms.** [Iterative hard thresholding](/iterative-hard-thresholding/), [CoSaMP](/cosamp/) and [approximate message passing](/approximate-message-passing/).
5. **Learned dictionaries.** [Dictionary learning](/dictionary-learning/), [K-SVD](/k-svd/) and [convolutional sparse coding](/convolutional-sparse-coding/).
6. **Imaging set-ups.** [Coded aperture imaging](/coded-aperture-imaging/) and the [single-pixel camera](/single-pixel-camera/).
7. **Learning inside a method.** [Bilevel learning of regularizers](/bilevel-learning-of-regularizers/), [algorithm unrolling](/algorithm-unrolling/), [LISTA](/lista/) and [learned primal-dual](/learned-primal-dual/) reconstruction.
8. **Priors from networks.** [Plug-and-play priors](/plug-and-play-priors/), [regularization by denoising](/regularization-by-denoising/), the [deep image prior](/deep-image-prior/), [compressed sensing with generative models](/compressed-sensing-generative-models/) and [diffusion posterior sampling](/diffusion-posterior-sampling/).

## A first reading

1. [Data fidelity term](/data-fidelity-term/), for why the noise law picks the misfit term.
2. [Variational regularization](/variational-regularization/), for the model and its existence, stability and convergence.
3. [Chambolle-Pock algorithm](/chambolle-pock-algorithm/), the solver that most of the chapter uses.
4. [Bregman distance convergence rates](/bregman-distance-convergence-rates/), for what replaces the norm rates.
5. [Null space property](/null-space-property/), for the exact condition behind basis pursuit.
6. [Mutual coherence](/mutual-coherence/), the condition that can be checked.
7. [Donoho-Tanner phase transition](/donoho-tanner-phase-transition/), for what happens with random matrices.
8. [Iterative hard thresholding](/iterative-hard-thresholding/), the simplest recovery algorithm with a guarantee.
9. [Algorithm unrolling](/algorithm-unrolling/), for how a method becomes a network.
10. [Plug-and-play priors](/plug-and-play-priors/), for how a denoiser becomes a prior.
11. [Diffusion posterior sampling](/diffusion-posterior-sampling/), for the current generative approach and its approximation.

## Before you start

The previous chapter of this volume, on regularization of inverse problems, is the linear theory that this one extends. Read at least its pages on the [regularization method](/regularization-method/), [spectral filter factors](/spectral-filter-factors/) and the [discrepancy principle](/morozov-discrepancy-principle/). From Volume 15 you need [convex functions](/convex-function/), the [subdifferential](/subdifferential/), the [proximal operator](/proximal-operator/), the [convex conjugate](/convex-conjugate/), the [proximal gradient method](/proximal-gradient-method/), [FISTA](/fista/) and [ADMM](/admm/). Volume 28 has [compressed sensing](/compressed-sensing/), [basis pursuit](/basis-pursuit/), the [restricted isometry property](/restricted-isometry-property/), [iterative shrinkage-thresholding](/iterative-shrinkage-thresholding/) and [total variation denoising](/total-variation-denoising/). For the learned methods, [backpropagation](/backpropagation/) and the [variational autoencoder](/variational-autoencoder/) are in Volume 25.
