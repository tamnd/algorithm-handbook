## What to remember

- Every triangulation of a [simple polygon](/polygon-triangulation/) with $n$ vertices has $n - 2$ triangles and $n - 3$ diagonals. With $h$ holes and $n$ vertices in all it has $n + 2h - 2$ triangles. For $n$ points with $h$ of them on the hull boundary, every [triangulation](/triangulation-counting-theorem/) has $2n - h - 2$ triangles and $3n - h - 3$ edges.
- Every simple polygon with $n \ge 4$ vertices has [two ears](/two-ears-theorem/), so [ear clipping](/ear-clipping/) never gets stuck. It takes $\Theta(n^2)$ time, and it is the method most programs use for small polygons.
- The [dual tree](/triangulation-dual-tree/) of a polygon triangulation has $n - 2$ nodes of degree at most 3. Its leaves are ears, and $t_1 = t_3 + 2$ for the numbers of nodes of degree 1 and 3.
- The standard $\Theta(n \log n)$ algorithm cuts the polygon into [monotone pieces](/monotone-polygon-partition/) by a sweep and [triangulates each piece](/monotone-polygon-triangulation/) in linear time with a stack. [Chazelle's algorithm](/chazelle-polygon-triangulation/) takes $\Theta(n)$ time and is of theoretical interest only; for a point set or a polygon with holes, $\Omega(n \log n)$ is a lower bound.
- A convex $n$-gon has $C_{n-2} = \frac{1}{n-1}\binom{2n-4}{n-2}$ [triangulations](/catalan-triangulation-theorem/), and a point set has at most $O(30^n)$. The [interval dynamic program](/polygon-triangulation-dp/) finds the cheapest triangulation of a polygon in $\Theta(n^3)$ time and $\Theta(n^2)$ space, but for a point set [minimum weight](/min-weight-triangulation/) is NP-hard.
- An [edge flip](/edge-flip/) is possible exactly when the two triangles form a strictly convex quadrilateral. Flipping to raise the smallest angle ends at the [max-min angle triangulation](/max-min-angle-triangulation/), which is the Delaunay triangulation, after $O(n^2)$ flips.
- The [flip graph](/flip-graph/) is connected. For a convex $n$-gon it has diameter $2n - 10$ when $n \ge 13$; for point sets the diameter is $\Theta(n^2)$ and the [flip distance](/flip-distance/) is NP-complete.
- Good angles need [Steiner points](/steiner-points/). [Ruppert's algorithm](/ruppert-algorithm/) guarantees angles of about $20.7°$ and [Chew's second algorithm](/chew-second-algorithm/) about $26.57°$, with meshes whose size is within a constant factor of the smallest possible.

## The main algorithms side by side

| Algorithm | Input | Time | Space | Output |
|---|---|---|---|---|
| [Ear clipping](/ear-clipping/) | simple polygon | $\Theta(n^2)$ | $\Theta(n)$ | some triangulation |
| [Monotone pieces and stack](/monotone-polygon-triangulation/) | polygon, holes allowed | $\Theta(n \log n)$ | $\Theta(n)$ | some triangulation |
| [Seidel](/seidel-polygon-triangulation/) | simple polygon | $O(n \log^* n)$ expected | $O(n)$ expected | some triangulation |
| [Tarjan and Van Wyk](/tarjan-van-wyk-triangulation/) | simple polygon | $O(n \log \log n)$ | $O(n)$ | some triangulation |
| [Chazelle](/chazelle-polygon-triangulation/) | simple polygon | $\Theta(n)$ | $\Theta(n)$ | some triangulation |
| [Interval dynamic program](/polygon-triangulation-dp/) | polygon | $\Theta(n^3)$ | $\Theta(n^2)$ | cheapest for a sum of costs |
| [Point-set triangulation](/triangulation-of-point-set/) by sorting | point set | $\Theta(n \log n)$ | $\Theta(n)$ | some triangulation |
| [Greedy triangulation](/greedy-triangulation/) | point set | $O(n^3)$ directly | $\Theta(n^2)$ | shortest edges first |
| [Max-min angle](/max-min-angle-triangulation/) by flips | point set | $O(n^2)$ flips | $\Theta(n)$ | largest smallest angle |
| [Ruppert](/ruppert-algorithm/) | segments and points | $O(m^2)$ | $O(m)$ | angles $\ge 20.7°$ |
| [Chew's second](/chew-second-algorithm/) | segments and points | $O(m^2)$ | $O(m)$ | angles $\ge 26.57°$ |

: Triangulation algorithms. Here $n$ is the input size and $m$ the number of output vertices of a mesh. The greedy triangulation also takes $O(n \log n)$ time when computed from the Delaunay triangulation, and the max-min angle triangulation takes $\Theta(n \log n)$ by any Delaunay algorithm. The angle bounds of the two mesh algorithms assume that the input has no small angles.

## Choosing a method

- For a polygon of a few hundred vertices, or one that is drawn once, use [ear clipping](/ear-clipping/). It is short, needs only the [orientation test](/orientation-test/), and is easy to make exact.
- For large polygons, or for polygons with holes, use the [monotone partition and stack](/monotone-polygon-triangulation/), or [Seidel's algorithm](/seidel-polygon-triangulation/) when expected time is enough. Do not implement Chazelle's algorithm.
- When the triangles must be well shaped, as for interpolation or for a finite element method, triangulate the points by the max-min angle rule, that is, compute the Delaunay triangulation. When some edges are prescribed, use a [constrained triangulation](/constrained-triangulation/).
- When the angles must be bounded below, add Steiner points with [Delaunay refinement](/delaunay-refinement/): [Ruppert's algorithm](/ruppert-algorithm/) is the usual choice, and [Chew's second algorithm](/chew-second-algorithm/) gives a better angle bound on a constrained triangulation.
- For the cheapest triangulation of a polygon under a cost such as total diagonal length, use the [dynamic program](/polygon-triangulation-dp/). For a point set, accept an approximation such as the [greedy triangulation](/greedy-triangulation/); the exact problem is NP-hard.
- To store a triangulation that will be changed by flips and insertions, use the [quad-edge structure](/quad-edge-data-structure/) or a half-edge structure.
