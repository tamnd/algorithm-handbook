## What to remember

- A function is **convex** when $f(\theta x + (1 - \theta)y) \le \theta f(x) + (1 - \theta)f(y)$, which holds exactly when its epigraph is convex. For a twice differentiable $f$ it is the same as $\nabla^2 f(x) \succeq 0$ everywhere, and **$\mu$-strong convexity** is $\nabla^2 f(x) \succeq \mu I$. For a convex problem, every local minimum is global.
- A **subgradient** $g$ of $f$ at $x$ satisfies $f(y) \ge f(x) + g^\top(y - x)$ for all $y$. It exists at every interior point of the domain, it is the gradient where $f$ is differentiable, and $x^*$ minimizes $f$ exactly when $0 \in \partial f(x^*)$.
- The **dual function** $g(\lambda, \nu) = \inf_x L(x, \lambda, \nu)$ is concave, and $g(\lambda, \nu) \le p^*$ for every $\lambda \ge 0$, convex problem or not. The best bound is $d^*$, and $p^* - d^* \ge 0$ is the duality gap.
- For a convex problem with a strictly feasible point (the **Slater condition**), $d^* = p^*$, and the dual optimum is attained when $p^*$ is finite. The gap can be positive without it, and for nonconvex problems.
- The **KKT conditions** are primal feasibility, dual feasibility $\lambda \ge 0$, complementary slackness $\lambda_i f_i(x) = 0$, and $\nabla_x L = 0$. For a convex problem they are sufficient. Under Slater they are also necessary.
- The **conjugate** $f^*(y) = \sup_x (y^\top x - f(x))$ is always convex, and $f^{**} \le f$, with equality exactly when $f$ is closed and convex. A function is $\mu$-strongly convex exactly when $f^*$ has a $(1/\mu)$-Lipschitz gradient.
- **Interior-point methods** follow the central path. A point of the path with parameter $t$ has duality gap $\nu/t$, and with a $\nu$-self-concordant barrier, $O(\sqrt\nu \log(\nu/(t_0\varepsilon)))$ Newton steps reach a gap of $\varepsilon$.
- **Multiplier methods** update the prices $y$ of the constraints. The augmented Lagrangian method is the proximal point method applied to the dual, so it converges for every fixed penalty $\rho > 0$, and ADMM splits its inner step into one step in $x$ and one in $z$.

## The methods side by side

| Method | Problem | One iteration | Iterations for accuracy $\varepsilon$ |
|---|---|---|---|
| [Subgradient method](/subgradient/) | convex $f$, subgradients bounded by $G$ | one subgradient | $R^2G^2/\varepsilon^2$ |
| [Cutting-plane method](/cutting-plane-method/) | convex $f$ on a box | one oracle call, one LP | $(1 + GD\sqrt n/\varepsilon)^n - 1$ |
| [Bundle method](/bundle-method/) | convex $f$ | one oracle call, $O(n)$ with two cuts | $O(1/\varepsilon^2)$ for fixed $t$ |
| [Proximal point method](/proximal-point-method/) | closed convex $f$ | one proximal map | $\|x_0 - x^*\|^2/(2\lambda\varepsilon)$ |
| [Dual ascent](/dual-ascent/) | $\mu$-strongly convex $f$, linear constraints | one Lagrangian minimization | $\|A\|^2\|y_0 - y^*\|^2/(2\mu\varepsilon)$ |
| [Augmented Lagrangian](/augmented-lagrangian-method/) | convex $f$, $Ax = b$ | one minimization of $L_\rho$ | $\|y_0 - y^*\|^2/(2\rho\varepsilon)$ |
| [ADMM](/admm/) | $f(x) + g(z)$, $Ax + Bz = c$ | one step in $x$, one in $z$ | $O(1/\varepsilon)$ for the averages |
| [Barrier method](/barrier-method/), short step | $\nu$-self-concordant barrier | one Newton step | $O(\sqrt\nu\log(\nu/(t_0\varepsilon)))$ |
| [Interior-point method](/interior-point-method/) | linear program | one Cholesky factorization of $ADA^\top$ | $\lceil 2.5\sqrt n\ln(n\mu_0/\varepsilon)\rceil$ |

: The main methods of the chapter, with the worst-case bounds proved in their entries. The bounds for dual ascent and the augmented Lagrangian method are for the dual gap. The cutting-plane bound is exponential in $n$, but if $f$ is the maximum of $P$ affine pieces the method stops after at most $P + 1$ calls.

## Choosing a method

First write the problem in a standard form and check that it is convex. Then:

- For a linear, quadratic, second-order cone or semidefinite program of moderate size, use an interior-point method. It reaches high accuracy, and each iterate comes with a duality gap that bounds its error.
- When the problem is too large to factor a Newton matrix, but its objective splits into parts with cheap proximal maps, use ADMM. It reaches modest accuracy in tens of iterations and then slows down.
- When the coupling constraints are few and the rest separates, use dual decomposition, or the augmented Lagrangian method if the objective is not strongly convex.
- When $f$ is nonsmooth and known only through an oracle, as with a Lagrangian dual, use a bundle method. The plain subgradient method is simpler but slow.
- When a solver does not converge, check the Slater condition and compute the dual: an infeasible or unbounded problem often shows up there first.
