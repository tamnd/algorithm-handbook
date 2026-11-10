Fitting a logistic regression to a million examples, training a neural network, or computing the equilibrium shape of a loaded structure all reduce to the same task: find a point where a smooth function of many variables is as small as possible. The dimension may be in the millions, so the Hessian cannot be stored or factored, but the [gradient](/gradient/) can be computed at a small multiple of the cost of one evaluation of the function, by hand-written derivatives or by [backpropagation](/backpropagation/). The methods of this chapter use only values and gradients. The simplest of them, [gradient descent](/gradient-descent/), moves a short step against the gradient and repeats. Most of the chapter is about how long that step should be, how to make each step count for more, and what to do when the gradient is noisy, the variables are constrained or the function has a nonsmooth part.

Two numbers organize the theory. The [smoothness](/smoothness/) constant $L_f$ bounds how fast the gradient can change, and the [condition number](/condition-number-of-an-optimization-problem/) $\kappa = L_f/\mu$ compares it with the curvature $\mu$ of a strongly convex function. Gradient descent needs about $\kappa\ln(1/\varepsilon)$ steps, accelerated methods about $\sqrt\kappa\ln(1/\varepsilon)$, and no method that uses only gradients can do better than the second in the worst case. On the two-variable function $\frac12(x_1^2 + 10x_2^2)$, with $\kappa = 10$, gradient descent from $(10, 1)$ with step $1/L_f$ takes 153 steps to bring the gradient below $10^{-6}$; with $\kappa = 1000$ (the coefficient 10 replaced by 1000) the same method takes 16111 steps, and the accelerated method with constant momentum takes 595.

## What the chapter covers

1. **The problem and its measures.** The [gradient](/gradient/), [smoothness](/smoothness/), the problem of [unconstrained smooth minimization](/unconstrained-smooth-minimization/), and the vocabulary of [convergence rates](/convergence-rate/) and [condition numbers](/condition-number-of-an-optimization-problem/).
2. **Gradient descent and its guarantees.** [Gradient descent](/gradient-descent/), its $L_fR^2/(2k)$ bound on convex functions ([convergence theorem](/gradient-descent-convergence-theorem/)), its [linear rate](/linear-convergence-strongly-convex/) under strong convexity, the weaker [Polyak-Lojasiewicz condition](/polyak-lojasiewicz-condition/) that gives the same rate, and [coordinate descent](/coordinate-descent/).
3. **Choosing the step.** [Step size selection](/step-size-selection/), the [Armijo condition](/armijo-condition/), [backtracking](/backtracking-line-search/), [exact line search](/exact-line-search/), the [Wolfe conditions](/wolfe-conditions/) and the [Polyak step](/polyak-step-size/).
4. **Momentum and acceleration.** The [heavy ball method](/momentum-method/), the [lower bound](/first-order-lower-bound/) for first-order methods, and [Nesterov's accelerated gradient](/nesterov-accelerated-gradient/), which meets it up to a constant.
5. **Constraints and nonsmooth terms.** [Constrained problems](/constrained-smooth-minimization/) and [projected gradient descent](/projected-gradient-descent/), the [proximal operator](/proximal-operator/), [composite problems](/composite-minimization/) such as the lasso, the [proximal gradient method](/proximal-gradient-method/) and [FISTA](/fista/), and [mirror descent](/mirror-descent/) with its [Bregman divergences](/bregman-divergence/).
6. **Curvature from gradients.** [Nonlinear conjugate gradient](/nonlinear-conjugate-gradient/), [quasi-Newton methods](/quasi-newton-method/), [BFGS](/bfgs/), which converges superlinearly without second derivatives, and [L-BFGS](/limited-memory-bfgs/), which keeps only a few vectors.
7. **Stochastic gradients.** [Stochastic optimization](/stochastic-optimization/), [stochastic gradient descent](/stochastic-gradient-descent/) and its ancestor, the [Robbins-Monro algorithm](/robbins-monro-algorithm/), then [finite sums](/finite-sum-minimization/) and the variance-reduced methods [SVRG](/svrg/) and [SAGA](/saga/).
8. **Adaptive steps and geometry.** [AdaGrad](/adagrad/), [RMSProp](/rmsprop/), [Adam](/adam/), [Adadelta](/adadelta/) and [Rprop](/rprop/), the training methods of deep learning, and [natural gradient descent](/natural-gradient-descent/), which uses the [Fisher information matrix](/fisher-information-matrix/) as its metric.

## A first reading

A first pass through the chapter can follow one path from the basic method to the methods in daily use:

1. [Smoothness](/smoothness/) and the [condition number](/condition-number-of-an-optimization-problem/)
2. [Gradient descent](/gradient-descent/)
3. [Linear convergence under strong convexity](/linear-convergence-strongly-convex/)
4. [Backtracking line search](/backtracking-line-search/)
5. [Momentum](/momentum-method/) and [Nesterov's method](/nesterov-accelerated-gradient/)
6. [Projected gradient descent](/projected-gradient-descent/) and the [proximal gradient method](/proximal-gradient-method/)
7. [BFGS](/bfgs/) and [L-BFGS](/limited-memory-bfgs/)
8. [Stochastic gradient descent](/stochastic-gradient-descent/)
9. [Adam](/adam/)

The proofs of the theorems, the [Wolfe conditions](/wolfe-conditions/), [mirror descent](/mirror-descent/), the [lower bound](/first-order-lower-bound/), the variance-reduced methods and the older adaptive methods ([Adadelta](/adadelta/), [Rprop](/rprop/)) can wait for a second pass.

## Before you start

The chapter uses multivariable calculus and linear algebra: [eigenvalues](/eigenvalue/) of symmetric matrices, [positive definite matrices](/positive-definite-matrix/) and the [singular value decomposition](/singular-value-decomposition/). Several results assume a [convex function](/convex-function/) or [strong convexity](/strong-convexity/), and the nonsmooth parts use the [subgradient](/subgradient/) and the [subdifferential](/subdifferential/), all from the previous chapter. The quasi-Newton methods build on the [secant method](/secant-method/), [Newton's method for systems](/newton-method-for-systems/) and the linear [conjugate gradient method](/conjugate-gradient-method/) from the volume on numerical methods, and the [order of convergence](/order-of-convergence/) is defined there. The stochastic methods use [expected value](/expected-value/), [variance](/variance/) and [conditional expectation](/conditional-expectation/), and AdaGrad is analysed as a method of [online convex optimization](/online-convex-optimization/).
