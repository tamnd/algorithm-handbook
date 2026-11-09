## What to remember

- The [cross product](/cross-product/) $u \times v = u_x v_y - u_y v_x = |u||v|\sin\theta$ and the [dot product](/dot-product/) $u \cdot v = u_x v_x + u_y v_y = |u||v|\cos\theta$ are the two formulas behind nearly every test in the volume. Both have degree 2, so with integer coordinates below $2^{30}$ in absolute value, every difference-based value fits in a signed 64-bit integer.
- The [orientation test](/orientation-test/) is the sign of $(q - p) \times (r - p)$, twice the [signed area](/oriented-triangle-area/) of the triangle $pqr$. Use it, not angles or slopes, to decide turns, sides and crossings.
- The [shoelace formula](/shoelace-formula/) gives twice the signed area, $2A = \sum_i v_i \times v_{i+1}$, in $\Theta(n)$ time. Its sign is the [orientation](/polygon-orientation/) of a simple polygon: positive when counterclockwise.
- For a simple lattice polygon, [Pick's theorem](/picks-theorem/) says $A = I + B/2 - 1$, where $B$ is a sum of one gcd per edge.
- [Point in polygon](/point-in-polygon/) takes $\Theta(n)$ time per query without preprocessing, by the [crossing number](/crossing-number-algorithm/) with the half-open rule or by the [winding number](/winding-number-algorithm/). A [convex polygon](/point-in-convex-polygon/) answers in $\Theta(\log n)$ time with no preprocessing.
- A simple polygon with $n$ vertices has interior angles summing to $(n - 2)\pi$ and at most $n - 3$ reflex vertices; a rectilinear one has exactly $(n - 4)/2$.
- $\lfloor n/3 \rfloor$ guards always suffice for a simple polygon and are sometimes needed, but the fewest guards for a given polygon is NP-hard to find. [Hertel-Mehlhorn](/hertel-mehlhorn/) cuts a triangulated polygon into fewer than four times the fewest convex pieces in $\Theta(n)$ time.
- The [Minkowski sum](/minkowski-sum-convex-polygons/) of two convex polygons has at most $n + m$ vertices and takes $\Theta(n + m)$ time. Clipping two general polygons can produce $\Theta(nm)$ vertices.

## The main algorithms side by side

| Algorithm | Input | Time | Note |
|---|---|---|---|
| [Shoelace formula](/shoelace-formula/) | polygon | $\Theta(n)$ | signed area, exact on integers |
| [Crossing number](/crossing-number-algorithm/) | polygon, query point | $\Theta(n)$ | even-odd rule |
| [Winding number](/winding-number-algorithm/) | polygon, query point | $\Theta(n)$ | nonzero rule |
| [Point in convex polygon](/point-in-convex-polygon/) | convex polygon, query point | $\Theta(\log n)$ | binary search on a fan |
| [Simplicity test](/polygon-simplicity-test/) | polygon | $O(n \log n)$ | sweep line |
| [Monotone partition](/monotone-polygon-partition/) | polygon, holes allowed | $O(n \log n)$ | sweep with helpers |
| [Hertel-Mehlhorn](/hertel-mehlhorn/) | triangulated polygon | $\Theta(n)$ | fewer than $4\times$ the fewest convex pieces |
| [Sutherland-Hodgman](/sutherland-hodgman/) | polygon, convex window | $O(nm^2)$ worst | one output list |
| [Weiler-Atherton](/weiler-atherton-algorithm/), [Greiner-Hormann](/greiner-hormann-algorithm/) | two polygons | $O(nm + k \log k)$ | trace boundaries through $k$ crossings |
| [Vatti](/vatti-clipping/) | any polygons | sweep over edges and crossings | holes, self-intersections, fill rules |
| [Convex Minkowski sum](/minkowski-sum-convex-polygons/) | two convex polygons | $\Theta(n + m)$ | merge of edge directions |
| [Polygon kernel](/polygon-kernel/) | simple polygon | $O(n)$ | $O(n \log n)$ by general half-plane intersection |
| [Funnel algorithm](/funnel-algorithm/) | triangulated simple polygon | $\Theta(n)$ | shortest path with a deque |

: Polygon algorithms. Here $n$ and $m$ are the numbers of vertices of the two inputs and $k$ the number of boundary crossings. The bounds for the funnel algorithm and Hertel-Mehlhorn exclude the triangulation, which takes $O(n \log n)$ time in practice.

## Choosing a method

- Keep coordinates as integers or exact fractions when you can, and write every test with the cross and dot products. Check the extreme case of each predicate against the 64-bit bound.
- For one point-in-polygon query, use the crossing number with the half-open rule and an explicit boundary test. For a self-intersecting polygon under the nonzero rule, use the winding number. For many queries on one polygon, triangulate it and use point location; for a convex polygon, use the binary search.
- Test simplicity before calling an algorithm that requires it; the all-pairs test is fine for a few hundred edges.
- To clip against a rectangle or other convex window, use Sutherland-Hodgman. For two general polygons use Greiner-Hormann when the input is in general position, and a Vatti-style sweep, as in the libraries built on it, when it has holes, overlaps or touching edges.
- For convex pieces, triangulate and run Hertel-Mehlhorn unless the exact minimum matters.
- For collision tests and robot motion with convex shapes, compute Minkowski sums by merging edge sequences.
