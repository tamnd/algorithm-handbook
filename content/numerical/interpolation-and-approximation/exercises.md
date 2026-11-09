1. ◦ Find the polynomial of degree at most 2 through $(0, 1)$, $(1, 3)$ and $(2, 7)$ with the [Lagrange](/lagrange-interpolation/) basis, and expand it in powers of $x$.

2. ◦ Build the table of [divided differences](/divided-differences/) for $f(x) = x^3$ at $0, 1, 2, 3$. Write the [Newton form](/newton-interpolation/) of the interpolant and check that it expands to $x^3$.

3. ◦ Tabulate $k^3$ for $k = 0, 1, 2, 3, 4$ and form the [finite differences](/finite-differences/) up to the fourth. Which column is constant, and how does its value relate to the third derivative?

4. ◦ [Piecewise linear interpolation](/piecewise-linear-interpolation/) of $\sin x$ on $[0, \pi]$ uses equal steps $h$. Give the error bound for $h = 0.1$, and the number of intervals needed for an error below $10^{-6}$.

5. ◦ Compute $T_2$, $T_3$ and $T_4$ from the recurrence of the [Chebyshev polynomials](/chebyshev-polynomials/), and check $T_4(\cos t) = \cos 4t$ at $t = \pi/3$.

6. ◦ For three nodes on $[-1, 1]$, compare $\max|\omega(x)|$ for the equispaced nodes $-1, 0, 1$ with that for the [Chebyshev nodes](/chebyshev-nodes/), the zeros of $T_3$.

7. ◦ A unit grid cell has values $1, 2, 3, 5$ at $(0, 0)$, $(1, 0)$, $(0, 1)$, $(1, 1)$. Compute the [bilinear interpolant](/bilinear-interpolation/) at $(0.5, 0.5)$ and at $(0.25, 0.75)$.

8. ◦ The partial sums of $1 - \frac12 + \frac13 - \cdots$ converge to $\ln 2$. Apply one step of [Aitken's process](/aitken-delta-squared/) to $s_0 = 1$, $s_1 = 0.5$, $s_2 = 5/6$, and compare the errors before and after.

9. • Compute the weights of the [barycentric formula](/barycentric-interpolation/) for the nodes $0, 1, 2, 3$. Use the second (true) barycentric form to evaluate the interpolant of $x^3$ at $x = 1.5$.

10. • Find the cubic $p$ with $p(0) = 0$, $p'(0) = 1$, $p(1) = 1$ and $p'(1) = 0$ by [Hermite interpolation](/hermite-interpolation/).

11. • Interpolate $e^x$ at $0$, $0.5$ and $1$ by a quadratic. Use the [error theorem](/polynomial-interpolation-error-theorem/) to bound the maximum error on $[0, 1]$, and compare with the actual maximum error.

12. • Use [Neville's algorithm](/neville-algorithm/) to evaluate at $x = 2$ the quadratic that interpolates $\sqrt x$ at $1$, $4$ and $9$. Give the whole table and compare the result with $\sqrt 2$.

13. • Find the natural [cubic spline](/cubic-spline-interpolation/) through $(0, 0)$, $(1, 1)$ and $(2, 0)$: give the second derivative at the middle knot and the value of the spline at $x = 1/2$.

14. • Find the best linear approximation to $x^2$ on $[0, 1]$ in the $L^2$ norm by [least squares](/least-squares-approximation/), and the best one in the maximum norm by [minimax approximation](/minimax-approximation/). Give the maximum error of each.

15. • Compute the [Lebesgue constant](/lebesgue-constant/) of the nodes $-1, 0, 1$ and the point where the Lebesgue function reaches it.

16. • Find the [Padé approximant](/pade-approximation/) of type $(1, 1)$ of $\ln(1 + x)$. Compare its value at $x = 1$ with that of the Taylor polynomial of degree 2 and with $\ln 2$.

17. • Use [Chebyshev economization](/chebyshev-economization/) to replace $x^3$ on $[-1, 1]$ by a polynomial of degree at most 2. What is the error, and why is no polynomial of degree 2 better?

18. • [Shepard interpolation](/shepard-interpolation/) with power 2 uses the data $(0, 0)$, $(1, 1)$, $(3, 0)$. Compute its value at $x = 2$.

19. ★ Show that $T_n$ reaches $\pm 1$ with alternating signs at $n + 1$ points of $[-1, 1]$. Use the [equioscillation theorem](/chebyshev-equioscillation-theorem/) to prove that the best approximation to $x^n$ by polynomials of degree less than $n$ is $x^n - 2^{1-n}T_n(x)$, and write it out for $n = 4$.

20. ★ Prove that Aitken's process is exact on $s_k = s + c\lambda^k$ with $\lambda \ne 1$. Then apply it to $s_k = 1/k$ and find a closed form for the result. What does the answer say about logarithmic convergence?

21. ★ Prove that among all $C^2$ functions on $[a, b]$ that interpolate given data, the natural cubic spline minimizes $\int_a^b g''(x)^2\,dx$.

22. ★ The function $1/(x - 2)$ is analytic except at $x = 2$. Find the parameter $\rho$ of the largest Bernstein ellipse for $[-1, 1]$ inside which it is analytic, predict the degree at which [Chebyshev interpolation](/chebyshev-interpolation/) reaches an error of $10^{-15}$, and check the prediction by computing the error for a few degrees.
