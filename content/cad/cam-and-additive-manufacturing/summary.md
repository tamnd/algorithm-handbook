## What to remember

- [Triangle mesh slicing](/triangle-mesh-slicing/) of $n$ triangles by $k$ planes, with $m$ output segments, takes $O(n \log k + k + m)$ expected time against the lower bound $\Omega(n \log k + k + m)$. The only predicate compares $z$ values, so the contours have the exact topology. A triangle is cut by the plane at $Z$ when $z_{\min} < Z \le z_{\max}$.
- A layer of thickness $t$ leaves a cusp of height $t |\cos \theta|$, where $\theta$ is the angle between the facet normal and the build axis ([staircase effect](/staircase-effect/)). [Adaptive slicing](/adaptive-slicing/) tests $t^2 n_z^2 \le c^2 \|n\|^2$ exactly; its greedy choice does not always give the fewest layers.
- A ball of radius $r$ with passes $w$ apart leaves a [scallop](/scallop-height/) of height $r - \sqrt{r^2 - w^2/4} \approx w^2/(8r)$ on a plane. A ball gouges locally where the part is concave with curvature above $1/r$, but [gouge detection](/gouge-detection/) also needs a global distance test.
- In a [pocket](/pocket-machining/) the tool centre stays in the inward offset $P_r$, so the tool clears only the opening; a convex pocket keeps $r^2 (\sum_i \cot(\alpha_i/2) - \pi)$ uncut in its corners. [Contour-parallel](/contour-parallel-toolpath/) loops with stepover $s \le r$ clear exactly the opening, and a corner of angle $\alpha$ leaves islands when $s > r(1 + \sin(\alpha/2))$.
- A [z-map](/z-map-model/) costs $O(c)$ per move for the $c$ grid lines under the tool and cannot show undercuts. A [dexel](/dexel-representation/) Boolean costs $O(m_1 + m_2)$ per ray and is exact on rational endpoints. A sampled simulation cannot prove a path free of gouges.
- A direction from which a set of faces is visible exists exactly when 0 is not in the convex hull of their normals; a linear program finds it ([accessibility cone](/accessibility-cone/)).
- The [nesting problem](/nesting-problem/) is strongly NP-hard. The [no-fit polygon](/no-fit-polygon/) $A \oplus (-B)$ of two convex polygons has at most $n + m$ edges and takes $O(n + m)$ time.
- 0/1 [topology optimization](/topology-optimization/) is ill-posed; the relaxation with linear stiffness is convex and gives a lower bound. [SIMP](/simp-method/) with $p > 1$ and the [level set method](/level-set-topology-optimization/) find local optima.

| Method | Model | Time | Guarantee |
|---|---|---|---|
| Triangle mesh slicing | exact $z$ comparisons | $O(n \log k + k + m)$ expected | exact topology |
| Adaptive slicing, greedy | exact squared test | $O(Lrn)$ | cusp $\le c$; not fewest layers |
| Tree support | real | $O(n^2 \log n)$ | heuristic; savings measured |
| Contour-parallel pocket | real | $O(Kn^2)$, convex pocket | clears the opening for $s \le r$ |
| Direction-parallel pocket | real | $O(Kn \log n + In^3)$ | retractions $\le 5\,\mathrm{OPT} + 6h$ |
| Voronoi pocket | real | $O(n^2 + Kn \log n)$ | offsets read from the medial axis |
| Inverse tool offset | sampled heights | $O(nk)$ | no gouge at the samples |
| Z-map | floating point | $O(c)$ per move | three axes; no undercuts |
| Dexel | rational endpoints | $O(m_1 + m_2)$ per ray | exact Boolean per ray |
| No-fit polygon, convex | real | $O(n + m)$ | at most $n + m$ edges |
| Bottom-left fill, rectangles | real | $O(n^2)$ | $3\,\mathrm{OPT}$ for decreasing widths |
| Mold, one direction | real | $O(n \log n)$ | exact decision |
| SIMP | finite elements | $O(kn(h^2 + r^2))$ | local optimum |
| Level set | finite elements | $O(kn(h^2 + n))$ | local optimum; not monotone |

: The main methods. For slicing, $L$ counts layers and $r$ allowed thicknesses. For pockets, $n$ counts boundary edges, $K$ offset loops, $I$ islands and $h$ holes. For the optimizers, $k$ counts iterations, $n$ elements, $h$ elements across the short side and $r$ the filter radius.

## Choosing a method

For printing, slice with the sweep. Use adaptive slicing when the finish of sloped walls matters more than build time. Fix the build orientation before the supports, since it decides the overhangs. Tree supports save material over pillars in measurements.

For milling, clear pockets with contour-parallel loops to cut along the walls with few retractions, and with zigzag lines when the pocket is simple. Keep the stepover at most $r$ or check the corners for islands. Finish with iso-parametric passes when the parametrization is even, and with iso-planar or iso-scallop passes when it is not. Simulate every program: a z-map for three axes, dexels when the tool tilts.

For nesting, compute the no-fit polygons once and run bottom-left fill inside a search over piece orders. In topology optimization, SIMP with a filter is the usual default; the level set method keeps a sharp boundary.
