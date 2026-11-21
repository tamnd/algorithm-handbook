An inverse problem asks for the cause from the effect: the inside of a body from X-ray projections, the layers of the ground from echoes, a sharp image from a blurred one. The map from cause to data is usually smooth, and that is the trouble. A smooth map flattens fine detail, so inverting it amplifies the noise in the data. For the integration operator on $[0, 1]$ the singular values are $2/((2k-1)\pi)$, and a data error of $10^{-3}$ along the thousandth singular function becomes a solution error of about $3.14$. Hadamard called a problem well posed when a solution exists, is unique and depends continuously on the data. Most inverse problems fail the third condition, and no amount of computing power fixes that.

Regularization replaces the unstable inverse by a family of stable approximate inverses with a parameter, and then picks the parameter. The singular value expansion shows what goes wrong and what each method does. Truncated SVD and Tikhonov regularization damp the small singular values, and iterative methods such as Landweber iteration and CGLS regularize by stopping early. The chapter asks three things of every method: how it filters the singular components, how its parameter is chosen from the data, and how fast its error goes to zero as the noise does. The last part treats the unknown as random and asks for its posterior distribution instead of one answer.

## What the chapter covers

1. **The problem and why it is ill posed.** The [inverse problem](/inverse-problem/) and its [forward operator](/forward-operator/), the [well-posed problem](/well-posed-problem/) of Hadamard, the [Fredholm integral equation of the first kind](/fredholm-integral-equation-first-kind/), the [singular value expansion](/singular-value-expansion/), the [Picard condition](/picard-condition/) and the [degree of ill-posedness](/degree-of-ill-posedness/).
2. **Regularization by filtering and averaging.** The definition of a [regularization method](/regularization-method/), [spectral filter factors](/spectral-filter-factors/), [truncated SVD](/truncated-svd/), the [resolution matrix](/resolution-matrix/), the [Backus-Gilbert method](/backus-gilbert-method/) and the [approximate inverse](/approximate-inverse/).
3. **Choosing the parameter.** An overview of [parameter choice](/regularization-parameter-choice/), the [Morozov discrepancy principle](/morozov-discrepancy-principle/), [generalized cross-validation](/generalized-cross-validation/), the [L-curve](/l-curve-method/), the [quasi-optimality criterion](/quasi-optimality-criterion/), [Stein's unbiased risk estimate](/stein-unbiased-risk-estimate/), the [unbiased predictive risk estimator](/unbiased-predictive-risk-estimator/) and the [Bakushinskii veto](/bakushinskii-veto/).
4. **Iterative and Krylov regularization.** [Semi-convergence](/semi-convergence/), [Landweber iteration](/landweber-iteration/), [CGLS](/cgls/), [LSQR](/lsqr/), [hybrid Krylov regularization](/hybrid-krylov-regularization/) and the [iteratively regularized Gauss-Newton method](/iteratively-regularized-gauss-newton/).
5. **Convergence rates.** [Source conditions](/source-condition/), the [qualification](/qualification-of-regularization/) of a method, [Tikhonov convergence rates](/tikhonov-convergence-rates/) and the [Lepskii balancing principle](/lepskii-balancing-principle/).
6. **The Bayesian view.** The [linear Gaussian inverse problem](/linear-gaussian-inverse-problem/), the general [Bayesian inverse problem](/bayesian-inverse-problem/), [preconditioned Crank-Nicolson MCMC](/preconditioned-crank-nicolson-mcmc/) and [randomize-then-optimize](/randomize-then-optimize/).

## A first reading

The core of the chapter is one example seen through several methods. This path covers it.

1. [Inverse problem](/inverse-problem/), for the model $y = Ax + e$ and the integration example.
2. [Well-posed problem](/well-posed-problem/), for Hadamard's three conditions and his example.
3. [Singular value expansion](/singular-value-expansion/), the tool behind every later page.
4. [Picard condition](/picard-condition/), for when a solution exists at all.
5. [Regularization method](/regularization-method/), for the definition that the later methods satisfy.
6. [Spectral filter factors](/spectral-filter-factors/), which put truncated SVD, Tikhonov and Landweber side by side.
7. [Truncated SVD](/truncated-svd/), the simplest method.
8. [Morozov discrepancy principle](/morozov-discrepancy-principle/), the standard rule when the noise level is known.
9. [Regularization parameter choice](/regularization-parameter-choice/), which compares six rules on one problem.
10. [Semi-convergence](/semi-convergence/), for why an iterative method must stop.
11. [CGLS](/cgls/), the iterative method used in practice.
12. [Tikhonov convergence rates](/tikhonov-convergence-rates/), for what a source condition buys.
13. [Linear Gaussian inverse problem](/linear-gaussian-inverse-problem/), for the Bayesian reading of Tikhonov regularization.

The [Bakushinskii veto](/bakushinskii-veto/) is short and worth reading after the parameter choice pages.

## Before you start

From Volume 12 you need the [singular value decomposition](/singular-value-decomposition/), the [least squares problem](/least-squares-problem/) and its [normal equations](/normal-equations/), the [pseudoinverse](/pseudoinverse/), the [condition number](/condition-number/) and [Tikhonov regularization](/tikhonov-regularization/) in its matrix form. The iterative pages build on the [conjugate gradient method](/conjugate-gradient-method/), [Krylov subspaces](/krylov-subspace/) and the [Golub-Kahan bidiagonalization](/golub-kahan-svd-algorithm/), all in Volume 12. [Gradient descent](/gradient-descent/) in Volume 15 is the same step as Landweber iteration. For the Bayesian pages read [Bayes' theorem](/bayes-theorem/) and [maximum a posteriori estimation](/maximum-a-posteriori-estimation/) in Volume 25 and [Metropolis-Hastings](/metropolis-hastings/) in Volume 17. [Cross-validation](/cross-validation/) and [ridge regression](/ridge-regression/) in Volume 25 are the statistical versions of two ideas here.
