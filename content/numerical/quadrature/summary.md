## What to remember

- Every method computes a [quadrature rule](/quadrature-rule/) $Q_n(f) = \sum_{i=1}^n w_i f(x_i)$. With $n$ nodes, the weights alone reach [degree of precision](/degree-of-precision/) $n - 1$, and no rule passes $2n - 1$ when the weight function is positive.
- A [composite rule](/composite-quadrature/) built from a basic rule of degree $d$ has error $O(h^{d+1})$. The [midpoint](/midpoint-rule/) and [trapezoidal](/trapezoidal-rule/) errors are $(b - a)h^2 f''(\xi)/24$ and $-(b - a)h^2 f''(\xi)/12$, and [Simpson's](/simpsons-rule/) is $-(b - a)h^4 f^{(4)}(\xi)/180$.
- By the [Euler-Maclaurin formula](/euler-maclaurin-formula/), the trapezoidal error is a series in even powers of $h$ with coefficients from derivatives at the ends. [Romberg integration](/romberg-integration/) cancels its terms one by one; for a periodic analytic integrand over a period they vanish, and the error falls geometrically.
- [Gaussian quadrature](/gaussian-quadrature/) puts the $n$ nodes at the zeros of the orthogonal polynomial of the weight. It has positive weights and degree $2n - 1$, and converges like $\rho^{-2n}$ for analytic $f$. The [Golub-Welsch algorithm](/golub-welsch-algorithm/) gets the rule from the Jacobi matrix in $O(n^2)$ operations.
- [Clenshaw-Curtis quadrature](/clenshaw-curtis-quadrature/) has about half the degree of Gauss, yet is nearly as accurate for most integrands, with nested nodes and weights in $O(n \log n)$.
- The closed [Newton-Cotes](/newton-cotes-formulas/) rule with 9 points, and every one with 11 or more, has negative weights, and the rules need not converge as $n$ grows. Raise accuracy with more panels or better nodes.
- An error estimate from samples is a heuristic. [Adaptive quadrature](/adaptive-quadrature/) with Simpson pairs costs $5 + 4k$ evaluations after $k$ splits; QUADPACK's [Gauss-Kronrod](/gauss-kronrod-quadrature/) pair G7-K15 costs 15 evaluations per panel for degree 23 and an estimate from $|K - G|$.
- Singularities and oscillations need rules that know about them: a Gauss rule with the singular factor in its weight, the [tanh-sinh](/tanh-sinh-quadrature/) change of variables with error near $e^{-cN/\log N}$, and [Filon](/filon-quadrature/) or [Levin](/levin-method/) methods, whose error falls as the frequency $\omega$ grows.
- In $s$ dimensions a [product rule](/product-quadrature/) needs $n^s$ points. [Monte Carlo](/monte-carlo-integration/) has root mean square error $V\sigma/\sqrt N$ in any dimension, and [quasi-Monte Carlo](/quasi-monte-carlo-integration/) has error at most $V_{HK}(f)\,D_N^*$ by the [Koksma-Hlawka inequality](/koksma-hlawka-inequality/), with $D_N^* = O((\log N)^s/N)$ for Halton and Sobol points.

## Rules side by side

| Rule | Evaluations | Degree | Error for smooth $f$ | Notes |
|---|---|---|---|---|
| Composite midpoint | $m$ | 1 | $\frac{(b-a)h^2}{24} f''(\xi)$ | open, never evaluates the ends |
| Composite trapezoidal | $m + 1$ | 1 | $-\frac{(b-a)h^2}{12} f''(\xi)$ | geometric for periodic analytic $f$ |
| Composite Simpson | $m + 1$, $m$ even | 3 | $-\frac{(b-a)h^4}{180} f^{(4)}(\xi)$ | quadratic interpolation on pairs of panels |
| Romberg, column $k$ | $2^i + 1$ | $2k + 1$ | $O(h_i^{2k+2})$ | positive weights in every column |
| [Gauss](/gaussian-quadrature/), $n$ nodes | $n$ | $2n - 1$ | $O(\rho^{-2n})$, analytic $f$ | nodes and weights in $O(n^2)$ |
| [Gauss-Radau](/gauss-radau-quadrature/), [Gauss-Lobatto](/gauss-lobatto-quadrature/) | $n$ | $2n - 2$, $2n - 3$ | as Gauss | one or both ends fixed |
| Gauss-Kronrod $K_{2n+1}$ | $2n + 1$ | $3n + 1$ ($3n + 2$, odd $n$) | estimate $\lvert K - G \rvert$ | reuses the $n$ Gauss values |
| Clenshaw-Curtis | $n$ | $n - 1$ ($n$, odd $n$) | close to Gauss for most $f$ | nested, FFT in $O(n \log n)$ |
| Tanh-sinh | $N$ | none | about $e^{-cN/\log N}$ | endpoint singularities |
| Monte Carlo | $N$ | none | $V\sigma/\sqrt N$, root mean square | any dimension, random |
| Quasi-Monte Carlo | $N$ | none | $\le V_{HK}(f)\,D_N^*$ | $D_N^* = O((\log N)^s/N)$ |

: One-dimensional rules on $[a, b]$ with $m$ panels of width $h$, and sampling methods in $s$ dimensions. The constants hold when the derivative shown is continuous.

## Choosing a method

- A smooth integrand on a finite interval: Gauss-Legendre, or Clenshaw-Curtis with a doubling test. Little known about $f$: an adaptive Gauss-Kronrod code.
- A periodic integrand over a period, or a fast-decaying one on the real line: the trapezoidal rule.
- Equally spaced data: the composite trapezoidal or Simpson rule, with Romberg extrapolation if the data allow halving.
- A known algebraic singularity or exponential decay: a Gauss rule whose weight holds it, such as Gauss-Jacobi, Gauss-Laguerre or Gauss-Hermite. An unknown or logarithmic endpoint singularity: tanh-sinh.
- A kink or jump inside the interval: split the interval there.
- A fast oscillation $e^{i\omega g(x)}$ with known phase: Filon when the moments are available, Levin's method otherwise.
- Two or three dimensions on a box: a product Gauss rule. Smooth $f$ in moderate dimension: a sparse grid. High dimension or rough $f$: randomized quasi-Monte Carlo, or Monte Carlo with [importance sampling](/importance-sampling/).
