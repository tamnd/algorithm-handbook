## What to remember

- Through $n + 1$ points with distinct abscissas passes exactly one polynomial of degree at most $n$. The Lagrange, Newton and barycentric forms are different ways to write it, not different interpolants. Solving the [Vandermonde](/vandermonde-matrix/) system for monomial coefficients is the one way that should be avoided, since its condition number grows exponentially.
- The [barycentric formula](/barycentric-interpolation/) evaluates the interpolant in $O(n)$ per point after $O(n^2)$ setup, or $O(n)$ setup at Chebyshev points, and it is numerically stable. [Newton's form](/newton-interpolation/) is the convenient one when nodes are added one at a time.
- The [error](/polynomial-interpolation-error-theorem/) at $x$ is $f^{(n+1)}(\xi)\,\omega(x)/(n+1)!$ with $\omega(x) = \prod (x - x_i)$. [Chebyshev nodes](/chebyshev-nodes/) make $\max|\omega|$ as small as possible, $2^{-n}$ on $[-1, 1]$.
- The [Lebesgue constant](/lebesgue-constant/) $\Lambda_n$ bounds both the loss against the best approximation, a factor $1 + \Lambda_n$, and the amplification of errors in the data. It grows like $\frac2\pi\log n$ at Chebyshev points and like $2^{n+1}/(e\,n\log n)$ at equispaced points, which is the [Runge phenomenon](/runge-phenomenon/).
- For $f$ analytic near $[-1, 1]$, [Chebyshev interpolation](/chebyshev-interpolation/) converges geometrically, like $\rho^{-n}$, where $\rho$ is set by the nearest singularity. For $f$ with $k$ derivatives, the best error falls like $n^{-k}$ by [Jackson's theorem](/jackson-theorem/).
- The best uniform approximation of degree $n$ is unique and is recognized by an error that reaches its maximum with alternating signs at $n + 2$ points; the [Remez algorithm](/remez-algorithm/) finds it.
- Splines trade degree for pieces. [Piecewise linear](/piecewise-linear-interpolation/) interpolation has error at most $h^2\max|f''|/8$; the clamped [cubic spline](/cubic-spline-interpolation/) has error at most $\frac{5}{384}h^4\max|f''''|$ and costs one tridiagonal solve.
- In $d$ variables a tensor-product grid needs $n^d$ points. [Sparse grids](/smolyak-sparse-grids/) cut this for smooth functions, and [radial basis functions](/radial-basis-function-interpolation/) handle scattered points at the price of a dense $N \times N$ system.
- [Rational functions](/rational-approximation/) approximate poles and near-singularities far better than polynomials of the same number of coefficients, but the problem is nonlinear and can fail at isolated points.

## Interpolants side by side

| Method | Smoothness | Setup | Per point | Error for smooth $f$ |
|---|---|---|---|---|
| Polynomial, barycentric at Chebyshev nodes | $C^\infty$ | $O(n)$ | $O(n)$ | geometric if $f$ is analytic |
| Polynomial, [Newton](/newton-interpolation/) | $C^\infty$ | $\Theta(n^2)$ | $\Theta(n)$ | depends on the nodes |
| [Nearest neighbour](/nearest-neighbor-interpolation/) | discontinuous | none | $O(\log n)$ | $O(h)$ |
| Piecewise linear | $C^0$ | none | $O(\log n)$ | $h^2\max\lvert f''\rvert/8$ |
| [Cubic Hermite](/cubic-hermite-spline/), exact slopes | $C^1$ | $\Theta(n)$ | $O(\log n)$ | $O(h^4)$ |
| [Fritsch-Carlson](/fritsch-carlson-monotone-interpolation/) | $C^1$, monotone | $\Theta(n)$ | $O(\log n)$ | $O(h^3)$, $O(h^2)$ where slopes are limited |
| Clamped cubic spline | $C^2$ | $\Theta(n)$ | $O(\log n)$ | $\frac{5}{384}h^4\max\lvert f''''\rvert$ |
| [Bilinear](/bilinear-interpolation/) on a grid | $C^0$ | none | 17 flops after search | $O(h^2)$ |
| [Shepard](/shepard-interpolation/), scattered | depends on the power | none | $\Theta(Nd)$ | reproduces constants only |
| Radial basis functions | depends on the kernel | $\Theta(N^3)$ | $\Theta(Nd)$ | high order for smooth kernels |

: Interpolants for $n + 1$ nodes on a line, or $N$ scattered points in $d$ dimensions, with spacing $h$. Per-point costs include the search for the interval.

## Choosing a method

To represent a smooth function on an interval to full accuracy, sample it at Chebyshev points and store the Chebyshev coefficients or the values, evaluated by the barycentric formula. To draw a curve through measured data, use a cubic spline, or a monotone cubic if overshoot would be wrong, such as for a cumulative quantity. Equally spaced data and high degree do not go together; take low-degree pieces instead.

For noisy data, do not interpolate: fit by least squares with few parameters, or use a [smoothing spline](/smoothing-spline/). For a function library, compute the minimax polynomial or rational function with the Remez algorithm on a reduced range. On a grid in two or three variables, bilinear or bicubic interpolation is the default; for scattered points, radial basis functions if $N$ is moderate, [kriging](/kriging/) if an error estimate is needed, and Shepard's method if speed matters more than accuracy. For a function with a pole or a series known only through its Taylor coefficients, try a [Padé approximant](/pade-approximation/).
