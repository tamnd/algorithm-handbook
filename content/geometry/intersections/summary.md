## What to remember

- **Two objects** meet in a constant number of steps. Write lines as $Ax + By + C = 0$ with integer coefficients, decide with [orientation tests](/orientation-test/) and exact integers, and divide only at the end, if at all. A [segment pair](/segment-intersection-point/) needs four orientation tests and a separate rule for collinear segments.
- **Neighbors in a sweep.** The leftmost crossing of a set of segments is between two segments that are adjacent in the sweep status just before it. That one fact is why the [Shamos-Hoey](/shamos-hoey-algorithm/) and [Bentley-Ottmann](/bentley-ottmann-algorithm/) sweeps need only $O(1)$ new tests per event.
- **Detection costs $\Theta(n \log n)$.** The [lower bound](/segment-intersection-lower-bound/) comes from element distinctness: $n$ vertical unit segments at $x_1, \ldots, x_n$ meet exactly when two of the $x_i$ are equal.
- **Reporting costs $\Theta(n \log n + k)$**, but Bentley-Ottmann pays $O((n + k) \log n)$, which is worse when $k$ is large. With $k = \Theta(n^2)$ crossings, a plain pairwise test is as fast. The optimal method of [Chazelle and Edelsbrunner](/chazelle-edelsbrunner-algorithm/) is long and rarely implemented.
- **Axis-parallel input is easier.** [Horizontal against vertical](/orthogonal-segment-intersection-sweep/) segments reduces to one-dimensional range queries on the sweep line, in $O(n \log n + k)$ time with simple structures.
- **Convexity makes intersection linear.** [Half-planes](/half-plane-intersection-deque/) take $O(n \log n)$ for the sort and $O(n)$ after it. Two [convex polygons](/convex-polygon-intersection/) meet in a convex polygon with at most $p + q$ vertices, found in $O(p + q)$ time.
- **Collision is cheaper than intersection.** Deciding whether two convex polygons overlap needs only one separating axis or one point in common. The [separating axis theorem](/separating-axis-theorem/) checks a finite list of directions, and [GJK](/gjk-algorithm/) measures the distance from the origin to the Minkowski difference.
- **Arrangements are quadratic.** $n$ lines in general position make $\binom{n}{2}$ vertices, $n^2$ edges and $\binom{n}{2} + n + 1$ faces, and the [zone theorem](/edelsbrunner-o-rourke-seidel-algorithm/) lets an incremental construction build them in $\Theta(n^2)$ time.

## The main methods side by side

| Problem | Method | Time | Space |
|---|---|---|---|
| Any two of $n$ segments cross? | [Shamos-Hoey](/shamos-hoey-algorithm/) | $\Theta(n \log n)$ | $O(n)$ |
| All $k$ crossings of $n$ segments | [Bentley-Ottmann](/bentley-ottmann-algorithm/) | $O((n + k) \log n)$ | $O(n)$ with deletions |
| All $k$ crossings of $n$ segments | [Chazelle-Edelsbrunner](/chazelle-edelsbrunner-algorithm/) | $O(n \log n + k)$ | $O(n + k)$ |
| Horizontal against vertical | [orthogonal sweep](/orthogonal-segment-intersection-sweep/) | $O(n \log n + k)$ | $O(n)$ |
| Pairs of $n$ rectangles | [interval tree sweep](/rectangle-intersection-reporting/) | $O(n \log n + k)$ | $O(n)$ |
| Area of a union of $n$ rectangles | [sweep with a segment tree](/klee-measure-problem/) | $\Theta(n \log n)$ | $O(n)$ |
| Volume of a union of $n$ boxes in $d \ge 3$ | [Overmars-Yap](/overmars-yap-algorithm/) | $O(n^{d/2} \log n)$ | $O(n)$ |
| Intersection of $n$ half-planes | [sort and deque](/half-plane-intersection-deque/) | $\Theta(n \log n)$ | $O(n)$ |
| Two convex polygons, intersection | [edge chasing](/convex-polygon-intersection/) | $\Theta(p + q)$ | $O(p + q)$ |
| Two convex polygons, overlap test | [Chazelle-Dobkin](/chazelle-dobkin-algorithm/) | $O(\log p + \log q)$ | $O(1)$ extra |
| Arrangement of $n$ lines | [incremental, zone theorem](/edelsbrunner-o-rourke-seidel-algorithm/) | $\Theta(n^2)$ | $\Theta(n^2)$ |

: The main intersection methods. All times are worst case on the real RAM. $n$ is the input size, $k$ the number of reported pairs or points, and $p$, $q$ the vertex counts of two convex polygons. The overlap test of Chazelle and Dobkin needs the polygons as arrays in boundary order.

## Choosing a method

- For a few hundred segments, test every pair with [segment intersection point](/segment-intersection-point/). It is short, has no ordering subtleties, and is fast enough.
- To check that a polygon or a wire layout has no crossing, use the Shamos-Hoey sweep. It stops at the first crossing and never stores crossing events.
- To report crossings when $k$ is small compared with $n^2 / \log n$, use Bentley-Ottmann. Keep only the crossings of current neighbors in the queue so the space stays $O(n)$.
- When every segment is horizontal or vertical, or every object is an axis-parallel box, use the orthogonal sweeps. They are simpler, and each reported pair costs $O(1)$ instead of $O(\log n)$.
- For half-planes, sort by angle and run the deque pass. Add a large bounding box first if the result may be unbounded.
- For collision tests between convex shapes in a game or simulation, use the separating axis test for boxes and small polygons, and GJK for general convex shapes given by a support function.
