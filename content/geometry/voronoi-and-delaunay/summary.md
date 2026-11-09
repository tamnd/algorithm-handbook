## What to remember

- The [Voronoi cell](/voronoi-cell/) of a site is the intersection of $n - 1$ half-planes, so it is convex with at most $n - 1$ edges. It is unbounded exactly when its site lies on the boundary of the convex hull.
- For $n \ge 3$ sites not all on a line, with $h$ on the hull boundary and no four on an empty circle, the [Voronoi diagram](/voronoi-complexity-theorem/) has $2n - 2 - h$ vertices and $3n - 3 - h$ edges, at most $2n - 5$ and $3n - 6$. The [Delaunay triangulation](/delaunay-triangulation/) has $2n - 2 - h$ triangles and $3n - 3 - h$ edges, because it is the [dual](/voronoi-delaunay-duality/) of the diagram: one triangle per Voronoi vertex, one edge per Voronoi edge.
- A triangle is Delaunay when its circumcircle holds no site strictly inside. The [in-circle test](/in-circle-test/) decides this with a $3 \times 3$ determinant $I = D(a, b, c)(R^2 - |d - o|^2)$, of degree 4 in the coordinates and exact on integers.
- A triangulation of a point set is Delaunay if and only if every interior edge is [locally Delaunay](/local-delaunay-criterion/). It exists when the points are not all on a line, and it is [unique](/delaunay-triangulation-uniqueness/) when no four are cocircular. Among all triangulations it [maximizes the smallest angle](/delaunay-max-min-angle/), but it does not minimize the largest angle or the total edge length.
- The [lifting map](/paraboloid-lifting-map/) $p \mapsto (x, y, x^2 + y^2)$ turns the in-circle test into an orientation test in space. The Delaunay triangulation is the projection of the lower hull of the lifted points, and lifting to height $|p|^2 - w_p$ gives the [regular triangulation](/regular-triangulation/) dual to the [power diagram](/power-diagram/).
- Both construction problems take $\Theta(n \log n)$ time in the worst case. The [lower bound](/voronoi-construction-lower-bound/) puts the numbers $x_i > 0$ on the parabola $y = x^2$, where the triangulation reveals their sorted order.
- The proximity graphs nest, $\mathrm{EMST} \subseteq \mathrm{RNG} \subseteq \mathrm{GG} \subseteq \mathrm{DT}$, so the closest pair, all nearest neighbours and the minimum spanning tree come from the Delaunay edges.
- Changing the distance changes the diagram. The [farthest-point diagram](/farthest-point-voronoi-diagram/) is a tree on the hull sites, the [order-$k$ diagram](/order-k-voronoi-diagram/) has size $O(k(n - k))$, and the [multiplicatively weighted diagram](/weighted-voronoi-diagram/) can have size $\Theta(n^2)$.

## The main algorithms side by side

| Algorithm | Time | Space | Builds | Dimensions |
|---|---|---|---|---|
| [Lawson's flips](/lawson-flip-algorithm/) | $O(n^2)$, at most $\binom{n}{2}$ flips | $O(n)$ | triangulation, from any starting one | plane only |
| [Bowyer-Watson](/bowyer-watson-algorithm/) | $\Theta(n^2)$ worst; $O(n \log n)$ expected in random order with a history DAG | $\Theta(n)$ | triangulation, one point at a time | any $d$ |
| [Guibas-Stolfi](/guibas-stolfi-algorithm/) | $O(n \log n)$ worst | $O(n)$ | triangulation, by divide and conquer | plane |
| [Dwyer](/dwyer-algorithm/) | $O(n \log \log n)$ expected for uniform points, $O(n \log n)$ worst | $O(n)$ | triangulation, by strips | plane |
| [Fortune](/fortunes-algorithm/) | $O(n \log n)$ worst | $O(n)$ | diagram, by a sweep | plane |
| [Lifting and a hull](/paraboloid-lifting-map/) | $O(n \log n)$ worst in the plane | $O(n)$ | either | any $d$, with a hull in $d + 1$ |

: Delaunay and Voronoi algorithms for $n$ points. Any of them gives the other structure in $O(n)$ more time by duality. The expected bound of Bowyer-Watson is that of the randomized incremental method of Guibas, Knuth and Sharir, which inserts in random order and locates each point in a history DAG.

## Choosing a method

- For a few thousand points, or for a first program, use [Bowyer-Watson](/bowyer-watson-algorithm/) with a large starting triangle or ghost triangles. Insert the points in random order and find each one by a [walk](/triangle-walk-point-location/) from the last triangle. It is short and works in any dimension.
- If a triangulation already exists, for example from a sweep or from a mesh that moved a little, repair it with [Lawson's flips](/lawson-flip-algorithm/). Flip only on a strictly positive in-circle test, or the loop may not stop on cocircular points.
- For a guaranteed $O(n \log n)$ bound in the plane, use [Guibas-Stolfi](/guibas-stolfi-algorithm/) on a [quad-edge structure](/quad-edge-data-structure/), with [Dwyer's](/dwyer-algorithm/) strips when the points are spread out evenly. Use [Fortune's sweep](/fortunes-algorithm/) when the diagram itself is the output.
- In three or more dimensions, use Bowyer-Watson or a convex hull of the lifted points. Flips alone do not reach the Delaunay triangulation there.
- When points arrive and leave over time, keep a [dynamic triangulation](/dynamic-delaunay-triangulation/). When segments must appear as edges, use the [constrained](/constrained-delaunay-triangulation/) version.
- Compute every predicate exactly, with integers or adaptive arithmetic. Rounding errors in the in-circle test make flip loops cycle and cavities lose their shape.
