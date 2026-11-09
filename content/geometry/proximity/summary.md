## What to remember

- Compare [squared distances](/euclidean-distance/): they are exact on integer input and order pairs the same way. The distance from $p$ to the line through $a$ and $b$ is $|u \times w| / \|u\|$ with $u = b - a$ and $w = p - a$, and the distance to the [segment](/point-to-segment-distance/) uses the sign of $w \cdot u$ to pick the foot or an endpoint.
- The [closest pair](/closest-pair-of-points/) takes $\Theta(n \log n)$ time by [divide and conquer](/closest-pair-divide-and-conquer/), which compares each strip point with at most 7 others, or by a [sweep](/closest-pair-sweep-line/). The [lower bound](/closest-pair-lower-bound/) of $\Omega(n \log n)$ holds for algebraic computation trees, by a reduction from element distinctness. With the floor function a [random grid](/randomized-closest-pair/) takes $O(n)$ expected time.
- The [farthest pair](/farthest-pair/) lies on the convex hull and is an antipodal pair, so the hull and rotating calipers give it in $O(n \log n)$ time. Any point and its farthest point give a 2-approximation in $O(n)$.
- [Collinear points](/collinear-points/) take $O(n^2)$ time and are 3SUM-hard, a different kind of hardness.
- With distinct distances, the [nearest neighbor graph](/nearest-neighbor-graph/) is a forest in which every point has in-degree at most 5 in the plane. It lies in every minimum spanning tree.
- The [proximity graphs](/proximity-graphs/) nest: $\text{NNG} \subseteq \text{MST} \subseteq \text{RNG} \subseteq \text{GG} \subseteq \text{DT}$. All are planar with at most $3n - 6$ edges, and each is cut from the Delaunay triangulation in $O(n \log n)$ time.
- A [Yao graph](/yao-graph/) with cone angle $\theta < \pi/3$ is a $t$-spanner with $t = 1/(1 - 2\sin(\theta/2))$. A [well-separated pair decomposition](/well-separated-pair-decomposition/) with separation $s > 4$ gives one with $t = (s+4)/(s-4)$ and $O(s^d n)$ edges.
- The [Fréchet distance](/frechet-distance/) of curves with $m$ and $n$ segments is decided in $\Theta(mn)$ time by [Alt and Godau](/alt-godau-algorithm/). Under SETH no $O(n^{2-\delta})$ algorithm exists. It is at least the [Hausdorff distance](/hausdorff-distance/).

## The main algorithms side by side

| Problem and method | Time | Space | Remark |
|---|---|---|---|
| Closest pair, all pairs | $\Theta(n^2)$ | $O(1)$ | any dimension |
| Closest pair, divide and conquer | $\Theta(n \log n)$ | $\Theta(n)$ | at most 7 comparisons per strip point |
| Closest pair, sweep line | $\Theta(n \log n)$ | $\Theta(n)$ | balanced tree on $y$ |
| Closest pair, random grid | $O(n)$ expected, $O(n^2)$ worst | $O(n)$ | needs floor and hashing |
| Farthest pair, hull and calipers | $O(n \log n)$ | $O(n)$ | $O(h)$ once the hull is known |
| Collinear points, dual arrangement | $O(n^2)$ | $O(n)$ with topological sweep | 3SUM-hard |
| Nearest neighbor query, [k-d tree](/kd-tree-nearest-neighbor-search/) | $O(\log n)$ expected, $O(n)$ worst | $O(\log n)$ stack | exact |
| [All nearest neighbors](/all-nearest-neighbors/) | $O(n \log n)$ | $O(n)$ | from the Delaunay triangulation |
| [Euclidean MST](/euclidean-minimum-spanning-tree/), Delaunay and Kruskal | $O(n \log n)$ | $O(n)$ | Prim on all pairs: $\Theta(n^2)$ |
| [Gabriel graph](/gabriel-graph/) from Delaunay | $O(n \log n)$ | $O(n)$ | $O(n)$ after triangulation |
| Yao graph, $k$ cones | $O(n^2)$ directly | $O(kn)$ | spanner for $k \ge 7$ |
| Fréchet decision, Alt and Godau | $\Theta(mn)$ | $O(mn)$ | optimization $O(mn \log mn)$ |

: Proximity algorithms in the plane. Here $h$ is the number of hull vertices, and $m$ and $n$ are the segment counts of the two curves in the last row. Theta-graphs take $O(n \log n)$ time for a fixed number of cones.

## Choosing a method

- For a few thousand points, checking all pairs is fast enough. Beyond that, use divide and conquer when you need a worst-case bound, and the random grid when integer coordinates and hashing are available.
- For many nearest neighbor queries on a fixed set in low dimension, build a k-d tree. In high dimension, accept an [approximate answer](/approximate-nearest-neighbor/) and use locality-sensitive hashing.
- When you need several of the nearest neighbor graph, the MST, the RNG and the Gabriel graph, build the Delaunay triangulation once and filter its edges. The [Urquhart graph](/urquhart-graph/) is a cheaper filter, but it can keep edges that the [relative neighborhood graph](/relative-neighborhood-graph/) drops.
- For a sparse graph with short paths, use the Delaunay triangulation when the graph must be planar, and a Yao or Theta graph when edges may cross and each point should choose its own links. For stretch close to 1, use the well-separated pair decomposition or the greedy [spanner](/geometric-spanner/).
- To compare curves, use the discrete Fréchet distance when the vertices are dense samples, and the continuous one by Alt and Godau when the segments are long.
- Keep every predicate exact: squared distances, cross products and dot products of integers need no square roots.
