## What to remember

- [Triangle mesh slicing](/triangle-mesh-slicing/) of $n$ triangles by $k$ planes with $m$ output segments takes $O(n \log k + k + m)$ expected time, matching the lower bound, with exact topology from exact $z$ comparisons. [Direct slicing](/direct-slicing/) of a CSG solid of quadrics gives exact conics, since the section commutes with the Booleans; NURBS sections are only computed to a tolerance.
- A layer of thickness $t$ leaves a cusp of height $t |\cos \theta|$ ([staircase effect](/staircase-effect/)). [Adaptive slicing](/adaptive-slicing/) bounds it, not always with the fewest layers, and [curved layers](/curved-layer-printing/) of thickness $\Delta c / |\nabla \phi|$ avoid it on the surface they follow; their gains are measured.
- A ball of radius $r$ with passes $w$ apart leaves a [scallop](/scallop-height/) of about $w^2/(8r)$. [Gouge detection](/gouge-detection/) needs a local curvature test and a global distance test.
- In a [pocket](/pocket-machining/) the tool clears only the opening; [contour-parallel](/contour-parallel-toolpath/) loops leave islands in a corner of angle $\alpha$ when $s > r(1 + \sin(\alpha/2))$. A straight cut of depth $a$ engages $\arccos(1 - a/R)$; [trochoidal](/trochoidal-milling/) and [constant engagement](/constant-engagement-toolpath/) paths bound it, exactly per step, with measured gains per path.
- A flat end of radius $R$ at lead $\lambda$ cuts like a ball of radius $R/\sin\lambda$ ([five-axis orientation](/five-axis-tool-orientation/)). The [principal axis method](/principal-axis-method/) is exact on a concave cylinder, [collision-free orientation](/collision-free-tool-orientation/) is optimal over its sampled candidates only, and [flank milling](/flank-milling/) is exact on developable surfaces.
- A [z-map](/z-map-model/) cannot show undercuts; a [dexel](/dexel-representation/) Boolean is exact on rational endpoints. Sampled simulation cannot prove a path free of gouges.
- With $b = v^2$ the speed and acceleration limits are linear, and the forward and backward scan of [feedrate scheduling](/feedrate-scheduling/) is time optimal in $O(n)$; jerk limits break convexity. A second order [interpolator](/parametric-cnc-interpolator/) step errs by $O(L^3)$.
- A direction that sees a set of faces exists exactly when 0 is not in the convex hull of their normals ([accessibility cone](/accessibility-cone/)). [Nesting](/nesting-problem/) is strongly NP-hard; a convex [no-fit polygon](/no-fit-polygon/) has at most $n + m$ edges.
- 0/1 [topology optimization](/topology-optimization/) is ill-posed. [Homogenization](/homogenization-method/) relaxes it and leaves gray designs, [SIMP](/simp-method/) and [level sets](/level-set-topology-optimization/) find local optima, and a [density filter](/density-filtering/) puts $W^{\mathsf T}$ in the chain rule. [BESO](/beso-method/) is optimal for parallel bars of equal area, arbitrarily worse otherwise, with no convergence proof.

| Method | Model | Time | Guarantee |
|---|---|---|---|
| Triangle mesh slicing | exact $z$ comparisons | $O(n \log k + k + m)$ expected | exact topology |
| Direct slicing, quadrics | exact rationals | $O(tn)$ | exact conics; polygon within tol |
| Multi-axis decomposition | voxels | $O(mwhn \log n)$ | plans print; search heuristic |
| Contour-parallel pocket | real | $O(Kn^2)$, convex pocket | clears the opening for $s \le r$ |
| Direction-parallel pocket | real | $O(Kn \log n + In^3)$ | retractions $\le 5\,\mathrm{OPT} + 6h$ |
| Collision-free orientation | exact box test | $O(mkn + mk^2)$ | optimal on the candidates |
| Z-map | floating point | $O(c)$ per move | three axes |
| Dexel | rational endpoints | $O(m_1 + m_2)$ per ray | exact per ray |
| Feedrate scan | speed, acceleration | $O(n)$ | time optimal |
| SIMP | finite elements | $O(kn(h^2 + r^2))$ | local optimum |
| BESO | finite elements | $O(k(s + n \log n))$ | 0/1; no convergence proof |

: The main methods. $t$ counts CSG leaves; for pockets $n$ counts edges, $K$ loops, $I$ islands, $h$ holes; for orientation $m$ counts points, $k$ candidates, $n$ obstacles; for decomposition $m$ rounds, $w$ beam width, $h$ layers; for optimizers $k$ iterations, $n$ elements, $h$ elements across, $r$ filter radius, $s$ a solve.

## Choosing a method

For printing, slice with the sweep, or slice the CAD model when the mesh error matters. Use adaptive slicing when sloped walls matter more than build time, and curved layers for thin shells on a printer that can tilt. Fix the orientation before the supports; on a robot arm, try a support-free decomposition.

For milling, rough with contour-parallel loops, or trochoidal or constant engagement paths when corners would overload the tool. Finish with iso-parametric passes on even parametrizations and iso-planar or iso-scallop passes otherwise, then pencil-cut concave edges. On five axes, tilt by the principal axis rule and check collisions over candidate tilts; flank-mill nearly developable ruled surfaces. Schedule the feed by the forward and backward scan, and simulate every program: a z-map for three axes, dexels when the tool tilts.

For nesting, compute no-fit polygons once and run bottom-left fill inside a search over piece orders. In topology optimization, SIMP with a density filter is the usual default; BESO gives 0/1 designs, level sets a sharp boundary, and homogenization graded lattices.
