## What to remember

- If $f$ is $L_f$-[smooth](/smoothness/), then $f(y) \le f(x) + \nabla f(x)^\top(y - x) + \frac{L_f}{2}\|y - x\|^2$. A [gradient descent](/gradient-descent/) step $\alpha \le 1/L_f$ lowers $f$ by at least $\frac{\alpha}{2}\|\nabla f(x)\|^2$; a fixed step $\alpha > 2/L_f$ can diverge.
- With step $1/L_f$, gradient descent gives $f(x_k) - f^* \le L_fR^2/(2k)$ on convex functions, with $R = \|x_0 - x^*\|$, and $f(x_k) - f^* \le (1 - 1/\kappa)^k(f(x_0) - f^*)$ on strongly convex ones. The [Polyak-Lojasiewicz condition](/polyak-lojasiewicz-condition/) $\frac12\|\nabla f\|^2 \ge \mu(f - f^*)$ is enough for the linear rate. Without convexity, $\min_{j \le k}\|\nabla f(x_j)\| \le \varepsilon$ after $2L_f(f(x_0) - f^*)/\varepsilon^2$ steps.
- No method that moves in the span of past gradients can beat $3L_fR^2/(32(k+1)^2)$ for $k \le (n-1)/2$, or the factor $\left(\frac{\sqrt\kappa - 1}{\sqrt\kappa + 1}\right)^k$ on strongly convex functions ([lower bound](/first-order-lower-bound/)). [Nesterov's method](/nesterov-accelerated-gradient/) attains $2L_fR^2/(k+1)^2$, within the factor $64/3$, and $(1 - 1/\sqrt\kappa)^k$.
- The [Armijo condition](/armijo-condition/) $f(x + \alpha d) \le f(x) + c\alpha\nabla f(x)^\top d$ holds for every $\alpha \le 2(1 - c)/L_f$ when $d = -\nabla f(x)$. So [backtracking](/backtracking-line-search/) accepts a step of at least $\min(\alpha_0, 2\rho(1 - c)/L_f)$ and keeps the rates without knowing $L_f$. The curvature part of the [Wolfe conditions](/wolfe-conditions/) guarantees $y^\top s > 0$.
- The [proximal operator](/proximal-operator/) of $\lambda\|x\|_1$ is soft thresholding, $\operatorname{sign}(x_i)\max(|x_i| - t\lambda, 0)$. [Projected gradient descent](/projected-gradient-descent/) and the [proximal gradient method](/proximal-gradient-method/) keep the $O(1/k)$ rate of gradient descent and [FISTA](/fista/) keeps $O(1/k^2)$; treating the objective as merely nonsmooth gives $O(1/\sqrt k)$.
- [Quasi-Newton methods](/quasi-newton-method/) impose the secant equation $B_{k+1}s_k = y_k$. [BFGS](/bfgs/) costs $O(n^2)$ per step and converges superlinearly; [L-BFGS](/limited-memory-bfgs/) stores $m$ pairs and needs $4mn + n$ multiplications per direction.
- [Stochastic gradient descent](/stochastic-gradient-descent/) reaches $O(GR/\sqrt k)$ on convex and $O(1/(\mu k))$ on strongly convex problems, the best possible orders for [stochastic optimization](/stochastic-optimization/). On a [finite sum](/finite-sum-minimization/) of $N$ terms, [SVRG](/svrg/) and [SAGA](/saga/) need $O((N + \kappa)\log(1/\varepsilon))$ component gradients against $O(N\kappa\log(1/\varepsilon))$ for gradient descent.
- [AdaGrad](/adagrad/), [RMSProp](/rmsprop/) and [Adam](/adam/) divide each coordinate of the step by a running root mean square of its gradients. AdaGrad has a regret bound; the original proof for Adam is wrong, and with constant $\beta_2$ RMSProp and Adam can fail on convex problems.

| method | cost per step | extra memory | convex, smooth | strongly convex |
|---|---|---|---|---|
| [gradient descent](/gradient-descent/), step $1/L_f$ | 1 gradient, $O(n)$ | none | $L_fR^2/(2k)$ | $(1 - 1/\kappa)^k$ |
| [heavy ball](/momentum-method/), tuned | 1 gradient, $O(n)$ | $n$ | $O(1/k)$, averaged iterate | $\approx\left(\frac{\sqrt\kappa - 1}{\sqrt\kappa + 1}\right)^k$ on quadratics only |
| [Nesterov](/nesterov-accelerated-gradient/) | 1 gradient, $O(n)$ | $n$ | $2L_fR^2/(k+1)^2$ | $(1 - 1/\sqrt\kappa)^k$ |
| [proximal gradient](/proximal-gradient-method/) | 1 gradient, 1 prox | none | $L_fR^2/(2k)$ | linear |
| [FISTA](/fista/) | 1 gradient, 1 prox | $n$ | $2L_fR^2/(k+1)^2$ | |
| [BFGS](/bfgs/) | gradients in a line search, $O(n^2)$ | $n^2$ | | superlinear near $x^*$ |
| [L-BFGS](/limited-memory-bfgs/) | gradients in a line search, $4mn + n$ | $2mn$ | | R-linear |
| [SGD](/stochastic-gradient-descent/) | 1 stochastic gradient | none | $RG/\sqrt k$, averaged | $O(1/k)$ |
| [SVRG](/svrg/), [SAGA](/saga/) | 1 component gradient (SVRG: plus full passes) | $n$ (SVRG), $Nn$ (SAGA) | | $O((N + \kappa)\log(1/\varepsilon))$ total |
| [Adam](/adam/) | 1 stochastic gradient, $O(n)$ | $2n$ | no general guarantee | no general guarantee |

: First-order methods in dimension $n$. $R = \|x_0 - x^*\|$, $\kappa = L_f/\mu$, $G$ bounds the stochastic gradients, $m$ is the L-BFGS memory and $N$ the number of terms of a finite sum. Rates bound $f(x_k) - f^*$.

## Choosing a method

For a smooth deterministic problem, use [L-BFGS](/limited-memory-bfgs/) with a strong Wolfe line search, or [BFGS](/bfgs/) when the dense $n \times n$ matrix fits in memory. [Nonlinear conjugate gradient](/nonlinear-conjugate-gradient/) needs even less memory.

With simple constraints or a nonsmooth regularizer with a cheap prox, use [FISTA](/fista/) or the proximal gradient method with backtracking. On the simplex with gradients bounded in the max norm, [mirror descent](/mirror-descent/) with the entropy gains a factor of about $\sqrt{n/\log n}$ over the Euclidean projection.

When $L_f$ and $\mu$ are known, accelerated gradient with constant momentum $(\sqrt\kappa - 1)/(\sqrt\kappa + 1)$ needs within a constant factor of the fewest possible steps. If $f^*$ is known, the [Polyak step](/polyak-step-size/) needs no other constant.

For an expectation or a very large sum, use SGD with mini-batches and a decreasing step. For a finite sum that allows a few passes over the data, SVRG or SAGA converge linearly; the gradient table of SAGA costs one number per term for linear models. For neural networks, Adam with its default constants and SGD with momentum are the usual choices, on the strength of experience more than of theorems.
