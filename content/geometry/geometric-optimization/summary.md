## What to remember

- **The optimum is fixed by a few points.** The [minimum enclosing circle](/minimum-enclosing-circle/) is unique and passes through two or three input points; in $\mathbb{R}^d$ the [smallest ball](/minimum-enclosing-ball/) is fixed by at most $d + 1$ points and the [smallest ellipsoid](/minimum-volume-enclosing-ellipsoid/) by at most $d(d+3)/2$.
- **Random order gives linear time.** [Welzl's algorithm](/welzls-algorithm/) adds the points in random order. By backwards analysis the $i$-th point falls outside the current circle with probability at most $3/i$, which gives at most $10n$ expected containment tests in the plane and $\lfloor (e-1)(d+1)! \rfloor\, n$ in $\mathbb{R}^d$.
- **LP-type problems share the method.** A problem with monotonicity, locality and combinatorial dimension $\delta$ is solved in expected $O(n)$ time for fixed $\delta$. A random sample of $r$ constraints leaves at most $\delta(n-r)/(r+1)$ violators in expectation, which drives [Clarkson's algorithm](/clarksons-algorithm/). [Prune and search](/prune-and-search/) gets $O(n)$ deterministically.
- **Calipers measure a convex polygon in $O(n)$.** A convex $n$-gon has between $n$ and $\lfloor 3n/2 \rfloor$ [antipodal pairs](/antipodal-pairs/). The [diameter](/polygon-diameter/) is at one of them; the [width](/polygon-width/) and the [smallest enclosing rectangle](/minimum-area-enclosing-rectangle/) have a side flush with an edge. That rectangle and the [smallest enclosing triangle](/minimum-area-enclosing-triangle/) each have at most twice the area of the polygon.
- **High dimension needs approximation.** The [Bădoiu–Clarkson algorithm](/badoiu-clarkson-algorithm/) takes $\lceil 1/\varepsilon^2 \rceil$ steps toward the farthest point, and the points it touches form a [coreset](/coreset/) whose size depends on neither $n$ nor $d$. [Khachiyan's algorithm](/khachiyans-algorithm/) does the same for the ellipsoid.
- **Sums of distances have no formula.** The [Fermat point](/fermat-point/) sees the three sides at 120 degrees, or is the corner whose angle is at least 120 degrees. The [geometric median](/geometric-median/) of five or more points is in general not expressible in radicals; [Weiszfeld's algorithm](/weiszfelds-algorithm/) lowers the cost at every step and converges linearly when the median is not a data point.
- **Shortest networks are hard.** The [Euclidean Steiner tree](/euclidean-steiner-tree-problem/) is NP-hard, its Steiner points have degree 3 with angles of 120 degrees, and it has a PTAS. The [rectilinear version](/rectilinear-steiner-tree-problem/) has an optimum on the Hanan grid. The [Steiner ratio](/steiner-ratio/) is at least $1/2$ in every metric, $2/3$ in the $L_1$ plane, and between $0.824$ and $\sqrt{3}/2$ in the Euclidean plane.
- **Shortest paths bend at corners.** Among polygonal obstacles the shortest path is a path in the [visibility graph](/visibility-graph/), and the best methods take $O(n \log n)$ time without building it. Inside a simple polygon the [funnel walk](/lee-preparata-algorithm/) takes $\Theta(n)$ time with a linear-time triangulation.

## The problems side by side

| Problem | Best exact bound | Simple method | Approximation |
|---|---|---|---|
| [Smallest circle](/minimum-enclosing-circle/) | $O(n)$, Megiddo 1983 | Welzl, $O(n)$ expected | |
| [Smallest ball](/minimum-enclosing-ball/) in $\mathbb{R}^d$ | $O(n)$ for fixed $d$ | Welzl, $O((d+1)!\, n)$ expected | $1 + \varepsilon$ in $O(nd/\varepsilon^2)$ |
| [Smallest ellipsoid](/minimum-volume-enclosing-ellipsoid/) in $\mathbb{R}^d$ | $O(n)$ expected for fixed $d$ | | Khachiyan, volume within $(1+\varepsilon)^{(d+1)/2}$ |
| [Thinnest annulus](/minimum-width-annulus/) | $O(n^{3/2+\varepsilon})$ expected | $O(n^2)$ from two Voronoi diagrams | |
| [Diameter](/polygon-diameter/), [width](/polygon-width/), [rectangle](/minimum-area-enclosing-rectangle/) | $\Theta(n)$ for a convex polygon | rotating calipers | |
| [Largest inscribed triangle](/maximum-area-inscribed-triangle/) | $O(n)$ for a convex polygon | $O(n^2)$ two-pointer walk | |
| [Geometric median](/geometric-median/) | no formula in radicals | Weiszfeld, linear convergence | $1 + \varepsilon$ in $O(nd \log^3(1/\varepsilon))$ |
| [Euclidean Steiner tree](/euclidean-steiner-tree-problem/) | NP-hard | spanning tree, factor at most $1/0.824$ | PTAS |
| [Rectilinear Steiner tree](/rectilinear-steiner-tree-problem/) | NP-complete | spanning tree, factor $3/2$ | PTAS |
| [Shortest path among obstacles](/euclidean-shortest-path/) | $O(n \log n)$; $O(n + h \log h)$ after triangulation | visibility graph, $O(n^2 \log n)$ | |
| [Minimum link path](/minimum-link-path/) in a simple polygon | $O(n)$ after triangulation | | |
| [Largest empty rectangle](/largest-empty-rectangle/) | $O(n \log^2 n)$ | sweep, $O(n^2)$ | |

: The main problems of the chapter, in the plane unless $d$ appears. $n$ is the number of points or vertices and $h$ the number of obstacles; times are worst case unless marked expected.

## Choosing a method

- For a smallest circle or ball in low dimension, write Welzl's algorithm with a random shuffle. It is short and exact with rational arithmetic.
- For a convex polygon, one caliper walk gives the diameter, the width and the smallest rectangle.
- When $d$ is in the tens or hundreds, use Bădoiu–Clarkson for a ball and Khachiyan's method for an ellipsoid.
- For the geometric median, run Weiszfeld's iteration from the centroid and guard the steps that land on a data point.
- For a short network, take the minimum spanning tree first. Use an exact solver such as GeoSteiner only when the last percent matters.
- For many path queries among few obstacles, build the visibility graph once. For one path inside a simple polygon, triangulate and walk the funnel.
