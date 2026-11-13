## What to remember

- A [Bézier curve](/bezier-curve/) is $C(t) = \sum_{i=0}^n P_i B_i^n(t)$ with $B_i^n(t) = \binom{n}{i} t^i (1 - t)^{n-i}$. The weights are nonnegative on $[0, 1]$ and sum to 1, which gives the convex hull and variation diminishing properties. The [de Casteljau algorithm](/de-casteljau-algorithm/) makes $n(n + 1)/2$ interpolations, $\Theta(n^2 d)$ in $\mathbb{R}^d$, and splits the curve as it goes. In floating point each coordinate is within $\gamma_{3n} \sum_i |P_i| B_i^n(t)$ of the exact value.
- A [rational Bézier curve](/rational-bezier-curve/) gives conics exactly. For a quadratic, the shape factor $w_1^2 / (w_0 w_2)$ is below 1 for an ellipse, equal to 1 for a parabola and above 1 for a hyperbola.
- A degree-$p$ [knot vector](/knot-vector/) for $n + 1$ control points has $n + p + 2$ knots and the domain $[t_p, t_{n+1}]$. At a knot of multiplicity $\mu$ the curve is $C^{p - \mu}$. The B-splines sum to 1 only on the domain. They form a basis of the spline space ([Curry-Schoenberg](/curry-schoenberg-theorem/)). Interpolation at sites $\tau_0 < \dots < \tau_n$ is uniquely solvable exactly when every $N_i(\tau_i) \ne 0$ ([Schoenberg-Whitney](/schoenberg-whitney-theorem/)).
- [De Boor's algorithm](/de-boor-algorithm/) takes $\Theta(p^2 d + \log n)$. [Boehm's insertion](/boehm-knot-insertion/) replaces $p - 1$ control points by $p$ points on the old polygon and leaves the curve unchanged. Both results are exact identities.
- [Chaikin](/chaikin-corner-cutting/) is within $D / (8 \cdot 4^k)$ of its limit after $k$ rounds, where $D$ is the largest second difference. [Lane-Riesenfeld](/lane-riesenfeld-algorithm/) of degree $d \ge 2$ is within $c_d D / 4^k$, with $c_d = (d + 1)(d + 3)/8$. The [four-point scheme](/four-point-scheme/) interpolates. It is continuous for $|w| < \tfrac14$ and $C^1$ for $0 < w < 0.19273$; that range is cited, not proved.
- The [natural cubic spline](/natural-cubic-spline/) has the least $\int |C''|^2$ among $C^2$ interpolants. [Catmull-Rom](/catmull-rom-spline/) is local and only $C^1$.
- [Catmull-Clark](/catmull-clark-subdivision/) and [Loop](/loop-subdivision/) surfaces are $C^2$ on the regular part. They are $C^1$ at extraordinary vertices, a result the entries cite. Every scheme keeps $V - E + F$.
- [Marching tetrahedra](/marching-tetrahedra/) returns the exact level set of the piecewise linear interpolant. [Marching cubes](/marching-cubes/) has 256 cases, 15 classes under rotation and complement, and ambiguous faces. Reconstruction from points has guarantees only for dense enough samples.
- [Ramer-Douglas-Peucker](/ramer-douglas-peucker/) stays within [Hausdorff distance](/hausdorff-distance/) $\varepsilon$, but its output is not the smallest. [Visvalingam-Whyatt](/visvalingam-whyatt/) and [quadric error metrics](/quadric-error-metrics/) have no bound; their quality is measured.

| Method | Model | Time | Guarantee |
|---|---|---|---|
| de Casteljau | real, floating point | $\Theta(n^2 d)$ | exact; rounding bound |
| de Boor | real | $\Theta(p^2 d + \log n)$ | exact |
| Boehm insertion | real | $\Theta(\log n + p d + n d)$ | exact, same curve |
| Chaikin | real, limit | $\Theta(2^k m)$ | within $D / (8 \cdot 4^k)$ |
| Catmull-Clark, Loop | real, limit | $\Theta(V + E + F)$ per step | $C^2$ regular, $C^1$ cited |
| Marching cubes | sampled | $\Theta(n)$ | at most 5 triangles per cell |
| Marching tetrahedra | sampled | $\Theta(n)$ | exact level set of the interpolant |
| Poisson reconstruction | sampled | $O(n + m^4)$ | measured |
| Ramer-Douglas-Peucker | real | $\Theta(n^2 d)$ worst | Hausdorff $\le \varepsilon$, not minimal |
| Quadric error metrics | real | $O(n \log n)$, bounded degree | measured |

: The main methods. $n$ is a degree, a number of points or a number of grid cells; $p$ is a B-spline degree, $d$ the dimension, $k$ the rounds on an $m$-point polygon, and $m^3$ the Poisson grid.

## Choosing a method

Use de Casteljau to evaluate a Bézier curve and de Boor to evaluate a B-spline; every step of both is a convex combination. To fit a curve through points, choose the [parameter values](/curve-interpolation/) first. Then use Catmull-Rom for local control, or the natural cubic spline when you need $C^2$. Use [NURBS](/nurbs/) only when the curve must be an exact conic.

On meshes of any topology, use Catmull-Clark for quads and Loop for triangles, and the [butterfly](/butterfly-subdivision/) scheme when the surface must pass through the vertices. For a sampled field, marching cubes is the default. Prefer marching tetrahedra when the output must be a closed manifold, and [dual contouring](/dual-contouring/) when sharp edges matter. To thin a polyline with a hard bound, use Ramer-Douglas-Peucker. To reduce a mesh, use quadric error metrics and measure the result.
