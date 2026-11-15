## What to remember

- The foot point of $p$ on a surface $r$ solves $(r - p) \cdot r_u = (r - p) \cdot r_v = 0$. [Newton point inversion](/newton-point-inversion/) solves it from the best point of a coarse grid. Newton finds stationary points, which can be saddles or maxima of the distance.
- A rational patch of bidegree $(m, n)$ has an implicit equation of degree at most $2mn$, which is $18$ for a bicubic. [Implicitization](/implicitization/) is exact but costly. [Algebraic surface intersection](/algebraic-surface-intersection/) substitutes a patch into an implicit surface and traces the plane curve with exact sign tests. [Levin's method](/levin-quadric-intersection/) intersects two quadrics through a ruled quadric of their pencil.
- [Lattice evaluation](/lattice-evaluation-intersection/) misses any closed loop that falls inside one cell or only touches the lattice. The [interval projected polyhedron](/interval-projected-polyhedron/) solver loses no root, but a box it returns is not a proof of a root. The [Sederberg-Meyers test](/sederberg-meyers-loop-detection/) proves that no loop exists when the normal cones satisfy $\alpha_1 + \alpha_2 < \varphi$. It is sufficient, not necessary, and never passes at a [tangential intersection](/tangential-surface-intersection/).
- [Curvature combs](/curvature-comb/), [isophotes](/isophote/) and [reflection lines](/reflection-lines/) show defects: a $G^1$ join gives a comb with a jump and reflection lines with a kink. They show where a defect is, not its size. [Lines of curvature](/lines-of-curvature/) form an orthogonal net that breaks down at [umbilic points](/umbilic-point/).
- Patches share a tangent plane when $b_u = \alpha a_u + \beta c'$ with $\alpha > 0$ along the common edge. At a corner the two twists must agree; when they do not, the [Gregory patch](/gregory-patch/) blends them rationally. An [n-sided hole](/n-sided-patch/) has no general polynomial filling; the [generalized Bézier patch](/generalized-bezier-patch/) fills it with $n \cdot l(d + 1 - l) + 1$ control points.
- Every fairing method minimizes a model. [Energy-based fairing](/energy-based-surface-fairing/) solves a linear system for a quadratic energy, [knot removal](/knot-removal-fairing/) lowers the largest jump of the third derivative, and the [minimum variation](/minimum-variation-surface/) energy, which is not quadratic, is zero on spheres, cylinders, cones, tori and cyclides.
- A [developable surface](/developable-surface/) has zero Gaussian curvature and is made of cylinders, cones and tangent surfaces. A sphere is not, so [strips](/developable-surface-approximation/) of width $r$ approximate it with an error of order $k r^2$. A [geodesic](/geodesics-on-parametric-surfaces/) between two points is found by shooting, which fails at conjugate points.
- An offset at distance $d$ moves with $\gamma' = (1 - d\kappa) c'$, so it has cusps where $d\kappa = 1$ and loops that [offset trimming](/offset-trimming/) removes. [Pythagorean hodograph curves](/pythagorean-hodograph-curve/) have polynomial arc length and rational offsets. [PH quintic Hermite interpolation](/ph-quintic-hermite-interpolation/) gives four solutions, and the choice among them is a heuristic.

| Method | Model | Time | Guarantee |
|---|---|---|---|
| Newton point inversion | real RAM, floats | $O(n^2 m)$ for the grid, then $O(m)$ per step | local; converges from a good start |
| Algebraic surface intersection | exact rationals | $O(T k^3 m^2 n^2)$, then $O(D^3)$ per box | every branch, to the box size |
| Levin's method | real RAM with square roots | $O(N)$ for $N$ samples | closed form; rounding near singular points |
| Lattice evaluation | floats | $O(N^2 D)$ | misses loops inside a cell |
| Interval projected polyhedron | rounded interval arithmetic | $O(m n N d)$ per box | no root lost; boxes not certified |
| Sederberg-Meyers test | real RAM | $O(1)$ per pair of cones | no loop if it passes; sufficient only |
| Knot removal fairing | floats | $O(R n^3)$, or $O(\log n)$ per step | lowers the largest jump; heuristic |
| Geodesic shooting | Runge-Kutta and Newton | error $O(n^{-4})$ per solve | local; fails at conjugate points |
| Offset trimming | exact orientation tests | $\Theta(m \log m + K + (I + 1) n)$ | exact on the polyline; sampling measured |

: The main methods, with the symbols of each entry: $m$ and $n$ sizes of the input, $k$, $d$ and $D$ degrees, $T$ terms, $N$ samples or lattice size, $K$ crossings, $R$ rounds, $I$ self-intersections.

## Choosing a method

Start point projection from the nearest grid point and keep the best of several starts. Intersect two quadrics with Levin's method, and a patch with an implicit surface by substitution and exact sign tests. For two freeform patches, subdivide until the Sederberg-Meyers test excludes loops in each pair, then march. Where the surfaces may touch, use an interval method.

Inspect with isophotes, reflection lines and combs of sections. Join patches with tangent plane continuity on each edge, and use a Gregory patch where the corner twists disagree. Fair with a quadratic energy for speed, with knot removal for one bad curve, and with minimum variation for circles and cylinders. For sheet metal, fit developable strips.
