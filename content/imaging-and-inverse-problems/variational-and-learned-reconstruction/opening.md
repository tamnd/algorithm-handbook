Classical regularization asks for a solution that is small or smooth. Variational reconstruction generalizes this: minimize a data fidelity term, which measures how well a candidate image explains the measurements, plus a regularizer that encodes what images look like. With total variation as regularizer, edges survive and noise does not; with an l1 norm of wavelet coefficients, sparse images are preferred. Compressed sensing showed that such sparsity priors allow exact recovery from far fewer measurements than unknowns, under conditions on the measurement matrix that can be proved for random matrices.

The last decade added learned priors. A denoiser trained on examples can stand in for the proximal step of an optimization method, an iterative algorithm can be unrolled into a network whose parameters are learned, and a generative model can describe the set of plausible images. These methods give the best reconstructions on many benchmarks; their guarantees are weaker, and the chapter separates what is proved, for the convex variational methods and for compressed sensing, from what is measured.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Variational regularization.** The data fidelity term, variational regularization, total generalized variation, analysis and synthesis sparsity, and convergence rates in the Bregman distance.
2. **Algorithms.** Chambolle's projection algorithm, the Chambolle-Pock primal-dual algorithm, Bregman iteration and the split Bregman method.
3. **Sparse recovery.** The Candès-Romberg-Tao theorem, the null space property, mutual coherence, the Donoho-Tanner phase transition, iterative hard thresholding, CoSaMP and approximate message passing.
4. **Dictionaries and imaging hardware.** Dictionary learning, K-SVD, convolutional sparse coding, the single-pixel camera and coded aperture imaging.
5. **Learned reconstruction.** Plug-and-play priors, regularization by denoising, algorithm unrolling, learned ISTA, learned primal-dual reconstruction, bilevel learning of regularizers, the deep image prior, compressed sensing with generative models and diffusion posterior sampling.

## What to read meanwhile

Compressed sensing has its own written entries in Volume 28: [compressed sensing](/compressed-sensing/), [basis pursuit](/basis-pursuit/), the [restricted isometry property](/restricted-isometry-property/), [orthogonal matching pursuit](/orthogonal-matching-pursuit/) and [iterative shrinkage-thresholding](/iterative-shrinkage-thresholding/). [Total variation denoising](/total-variation-denoising/) is in the same volume. The optimization methods are in Volume 15: the [proximal operator](/proximal-operator/), the [proximal gradient method](/proximal-gradient-method/), [FISTA](/fista/) and [ADMM](/admm/), of which split Bregman is a special case. The [lasso](/lasso-regression/) of Volume 25 is basis pursuit with noise, and the [exact matrix completion theorem](/exact-matrix-completion-theorem/) in Volume 35 is the low-rank analogue of exact sparse recovery.
