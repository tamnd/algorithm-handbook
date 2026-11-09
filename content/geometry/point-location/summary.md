## What to remember

- **The target is $O(\log n)$ query time in $O(n)$ space.** It is optimal: a subdivision with $N$ possible answers needs $\lceil \log_3 N \rceil$ orientation tests in the worst case, since each test has three outcomes.
- **Most methods shoot a vertical ray.** Find the edge directly above the query point, and the face is the one below that edge. Points with the $x$-coordinate of a vertex are handled by a symbolic shear, which orders points lexicographically.
- **Slabs are simple but quadratic.** Inside a slab between consecutive vertex $x$-coordinates the edges are totally ordered, so two binary searches answer a query; the slab lists can hold $\Theta(n^2)$ entries.
- **Persistence removes the quadratic space.** Consecutive slab lists differ by a few insertions and deletions, $2n$ in all. [Sarnak and Tarjan](/sarnak-tarjan-point-location/) keep every version in one persistent tree in $O(n)$ space.
- **The trapezoidal map is the practical choice.** It has at most $3n + 1$ trapezoids, and the history of a random-order construction answers queries in $O(\log n)$ expected time. A bad insertion order gives $\Theta(n)$ query paths; a random one makes that unlikely.
- **Triangulations allow a hierarchy or a walk.** [Kirkpatrick's hierarchy](/kirkpatrick-point-location/) is optimal in the worst case but has large constants. A [walk](/triangle-walk-point-location/) costs $O(n)$ in the worst case, yet it needs no extra memory and is fast when the start is close to the query.
- **A convex polygon needs no preprocessing.** [Binary search over the wedges](/convex-polygon-point-location/) around an interior point takes $O(\log n)$ time on the vertex array.

## The methods side by side

| Method | Preprocessing | Space | Query |
|---|---|---|---|
| Linear scan | none | $O(n)$ | $O(n)$ |
| [Slab method](/slab-method-point-location/) | $O(n^2)$ | $\Theta(n^2)$ | $O(\log n)$ |
| [Sarnak-Tarjan](/sarnak-tarjan-point-location/) | $O(n \log n)$ | $O(n)$ | $O(\log n)$ |
| [Trapezoidal map](/seidel-point-location/), random order | $O(n \log n)$ expected | $O(n)$ expected | $O(\log n)$ expected |
| [Kirkpatrick](/kirkpatrick-point-location/) | $O(n)$ from a triangulation | $O(n)$ | $O(\log n)$ |
| [Chain method](/chazelle-monotone-point-location/), cascading | $O(n \log n)$ | $O(n)$ | $O(\log n)$ |
| [Triangle walk](/triangle-walk-point-location/) | none | $O(n)$ | $O(n)$ |
| [Convex polygon wedges](/convex-polygon-point-location/) | none | $O(n)$ | $O(\log n)$ |

: Methods for planar point location in a subdivision with $n$ edges. Bounds are worst case unless marked expected. The trapezoidal map reaches $O(\log n)$ worst-case query time by rebuilding when its search structure is too deep, with the same expected preprocessing time.

## Choosing a method

- For a handful of queries, scan the faces or edges. Preprocessing pays only when queries are many.
- For a static subdivision and many queries, build a trapezoidal map in random order. It handles any set of non-crossing segments, needs no triangulation, and its code is moderate in length.
- When the worst case must be guaranteed and a persistent tree is at hand, use Sarnak and Tarjan; it is also the natural choice if the subdivision is already processed by a sweep.
- In a mesh with neighbor pointers, where consecutive queries are close together, walk from the triangle of the previous answer. Use the stochastic walk, or the visibility walk only on a Delaunay triangulation, since it can loop on others.
- For a single convex polygon, use the wedge search on the vertex array.
