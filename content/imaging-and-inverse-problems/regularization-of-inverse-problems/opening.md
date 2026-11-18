An inverse problem asks for the cause from the effect: the inside of a body from X-ray projections, the structure of the ground from echoes, a sharp image from a blurred one. The forward map from cause to data is usually smooth, and that is the trouble. A smooth map flattens fine detail, so inverting it amplifies the noise in the data, and the naive solution of the linear system, even when it exists, is dominated by noise. Hadamard called a problem well posed when a solution exists, is unique and depends continuously on the data; most inverse problems fail the third condition.

Regularization replaces the unstable inverse by a family of stable approximate inverses with a parameter, and then chooses the parameter from the data. The singular value decomposition shows what goes wrong and what each method does: truncated SVD and Tikhonov regularization damp the small singular values, and iterative methods such as Landweber iteration and conjugate gradients regularize by stopping early. How to choose the parameter, and how fast the error goes to zero as the noise does, are the central questions of the chapter. The Bayesian view treats the unknown as random and asks for its posterior distribution instead of one answer.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Ill-posedness.** The inverse problem and the forward operator, well-posed problems, Fredholm integral equations of the first kind, the singular value expansion, the Picard condition and the degree of ill-posedness.
2. **Regularization methods.** Regularization methods and their qualification, spectral filter factors, truncated SVD, the approximate inverse, the Backus-Gilbert method and the model resolution matrix.
3. **Iterative regularization.** Landweber iteration, CGLS, LSQR, semi-convergence, hybrid Krylov regularization and the iteratively regularized Gauss-Newton method.
4. **Choosing the parameter.** The Morozov discrepancy principle, the L-curve, generalized cross-validation, the quasi-optimality criterion, the Lepskii balancing principle, Stein's unbiased risk estimate and the unbiased predictive risk estimator, with the Bakushinskii veto on choices that ignore the noise level.
5. **Convergence rates.** Source conditions and the convergence rates of Tikhonov regularization.
6. **Bayesian inverse problems.** The Bayesian formulation, the linear Gaussian case, preconditioned Crank-Nicolson MCMC and randomize-then-optimize.

## What to read meanwhile

The tools are in Volume 12: the [singular value decomposition](/singular-value-decomposition/), the [condition number](/condition-number/), the [least squares problem](/least-squares-problem/), [Tikhonov regularization](/tikhonov-regularization/), the [conjugate gradient method](/conjugate-gradient-method/), [Krylov subspaces](/krylov-subspace/) and the [Lanczos algorithm](/lanczos-algorithm/), which LSQR applies in its Golub-Kahan bidiagonal form, so that the normal equations are never formed. [Ridge regression](/ridge-regression/) and [cross-validation](/cross-validation/) in Volume 25 are the same ideas in statistical dress. For the Bayesian chapter read [maximum a posteriori estimation](/maximum-a-posteriori-estimation/) in Volume 25 and [Metropolis-Hastings](/metropolis-hastings/) in Volume 17.
