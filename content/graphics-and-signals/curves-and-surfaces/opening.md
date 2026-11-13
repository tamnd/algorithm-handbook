A designer shapes the side of a car with a few dozen points on a screen and drags them until the reflection of a light runs smoothly across the panel. A font stores each letter as a chain of quadratic or cubic pieces, each fixed by three or four points. A medical scanner returns a grid of densities, and a laser scanner returns a million points on the surface of a statue. In every case a small amount of data must become a smooth shape that a program can evaluate, cut, offset, intersect and draw. The algorithms of this chapter do that: they turn control points into curves and surfaces, samples into meshes, and large meshes into small ones.

The chapter rests on one idea. A [Bézier curve](/bezier-curve/) or a [B-spline](/b-spline/) curve is a weighted average of its [control points](/control-points/) with weights that are nonnegative and sum to 1. From this come the convex hull property, the variation diminishing property, and the algorithms that evaluate a curve by repeated linear interpolation: [de Casteljau](/de-casteljau-algorithm/) for Bézier curves, [de Boor](/de-boor-algorithm/) for B-splines. The same interpolations split a curve, insert a knot, and drive the subdivision schemes, which refine a control polygon or a control mesh until it converges to a smooth limit.

The guarantees come in four kinds, and the pages keep them apart. Most statements about curves and patches are exact identities in real arithmetic: de Casteljau's points lie on the curve, knot insertion leaves the curve unchanged, a rational quadratic with the right weights is a circle arc. Some are floating-point bounds, such as the rounding error of de Casteljau's algorithm. Subdivision results are limit statements with explicit rates: after $k$ rounds of [Chaikin corner cutting](/chaikin-corner-cutting/) the polygon is within $D / (8 \cdot 4^k)$ of its limit. Some are statements about sampled data: the marching methods work on an interpolant of the samples, not on the unknown field, and only [marching tetrahedra](/marching-tetrahedra/) returns the exact level set of its interpolant. Reconstruction from points has guarantees only under sampling conditions, and the quality of Poisson reconstruction, Visvalingam-Whyatt and quadric error metrics is measured, not proved. Where the smoothness of a subdivision surface at an extraordinary vertex is cited from the literature rather than proved in the entry, the pages say so.

## What the chapter covers

1. **Curves as maps.** The [parametric curve](/parametric-curve/), [parametric continuity](/parametric-continuity/) and geometric continuity, the [arc length parametrization](/arc-length-parametrization/), the [Frenet frame](/frenet-frame/) and the [offset curve](/offset-curve/).
2. **Bézier curves.** [Bernstein polynomials](/bernstein-polynomials/), the [convex hull property](/convex-hull-property/) and the [variation diminishing property](/variation-diminishing-property/), [curve evaluation](/curve-evaluation/), de Casteljau's algorithm, the [rational Bézier curve](/rational-bezier-curve/) and the [Bernstein approximation theorem](/bernstein-approximation-theorem/).
3. **Interpolating splines.** The [Hermite spline](/hermite-spline/), [curve interpolation](/curve-interpolation/), the [Catmull-Rom spline](/catmull-rom-spline/), the [Kochanek-Bartels spline](/kochanek-bartels-spline/) and the [natural cubic spline](/natural-cubic-spline/).
4. **B-splines and NURBS.** The [spline](/spline/), the [knot vector](/knot-vector/), the [Cox-de Boor recursion](/cox-de-boor-recursion/), the [partition of unity](/partition-of-unity/), the [Curry-Schoenberg theorem](/curry-schoenberg-theorem/), the [Schoenberg-Whitney theorem](/schoenberg-whitney-theorem/), de Boor's algorithm and [NURBS](/nurbs/).
5. **Knot insertion and curve subdivision.** The [curve from a control polygon](/curve-from-control-polygon/), [knot refinement](/knot-refinement/), [Boehm's insertion](/boehm-knot-insertion/), the [Oslo algorithm](/oslo-algorithm/), Chaikin, [Lane-Riesenfeld](/lane-riesenfeld-algorithm/) and the [four-point scheme](/four-point-scheme/).
6. **Fitting, intersecting and offsetting curves.** [B-spline fitting](/b-spline-fitting/), [curve intersection](/curve-intersection/), [Bézier clipping](/bezier-clipping/) and [curve offsetting](/curve-offsetting/).
7. **Surfaces and patches.** The [parametric surface](/parametric-surface/), the [fundamental forms](/fundamental-forms/), [surface curvature](/surface-curvature/), surfaces of [revolution](/surface-of-revolution/), [ruled](/ruled-surface/) and [swept](/sweep-surface/) surfaces, the [implicit surface](/implicit-surface/), the [tensor-product surface](/tensor-product-surface/), the [Bézier patch](/bezier-patch/), the [Bézier triangle](/bezier-triangle/), the [Coons patch](/coons-patch/), the [polygon mesh](/polygon-mesh/) and [surface tessellation](/surface-tessellation/).
8. **Subdivision surfaces.** The [surface from a control mesh](/surface-from-control-mesh/), the [subdivision surface](/subdivision-surface/), and the schemes of [Catmull-Clark](/catmull-clark-subdivision/), [Doo-Sabin](/doo-sabin-subdivision/), [Loop](/loop-subdivision/), the [butterfly](/butterfly-subdivision/) and [$\sqrt 3$ subdivision](/sqrt3-subdivision/).
9. **Meshes from data.** [Isosurface extraction](/isosurface-extraction/), [marching squares](/marching-squares/), [marching cubes](/marching-cubes/), marching tetrahedra, [dual contouring](/dual-contouring/), [surface reconstruction](/surface-reconstruction/), the [ball pivoting algorithm](/ball-pivoting-algorithm/) and [Poisson surface reconstruction](/poisson-surface-reconstruction/).
10. **Simplification.** [Curve simplification](/curve-simplification/), [Ramer-Douglas-Peucker](/ramer-douglas-peucker/), [Visvalingam-Whyatt](/visvalingam-whyatt/), [mesh simplification](/mesh-simplification/) and [quadric error metrics](/quadric-error-metrics/).

## A first reading

Read these in order:

1. [Parametric curve](/parametric-curve/) and [parametric continuity](/parametric-continuity/)
2. [Bernstein polynomials](/bernstein-polynomials/)
3. [Bézier curve](/bezier-curve/)
4. [De Casteljau algorithm](/de-casteljau-algorithm/)
5. [Hermite spline](/hermite-spline/) and [Catmull-Rom spline](/catmull-rom-spline/)
6. [Knot vector](/knot-vector/)
7. [B-spline](/b-spline/) and [Cox-de Boor recursion](/cox-de-boor-recursion/)
8. [De Boor algorithm](/de-boor-algorithm/)
9. [Boehm knot insertion](/boehm-knot-insertion/)
10. [Chaikin corner cutting](/chaikin-corner-cutting/)
11. [Bézier patch](/bezier-patch/)
12. [Catmull-Clark subdivision](/catmull-clark-subdivision/)
13. [Marching cubes](/marching-cubes/)
14. [Ramer-Douglas-Peucker](/ramer-douglas-peucker/)

Skip at first the Curry-Schoenberg and Schoenberg-Whitney theorems, the Oslo algorithm, the differential geometry of surfaces beyond the [fundamental forms](/fundamental-forms/), the butterfly and $\sqrt 3$ schemes, and Poisson reconstruction. They refine the core and read more easily after it.

## Before you start

The chapter assumes interpolation from the numerical volume and links there instead of repeating it: [Lagrange interpolation](/lagrange-interpolation/), the [cubic Hermite spline](/cubic-hermite-spline/), [cubic spline interpolation](/cubic-spline-interpolation/) with its tridiagonal system and the [Thomas algorithm](/thomas-algorithm/), [spline evaluation](/spline-evaluation/) and the [Weierstrass approximation theorem](/weierstrass-approximation-theorem/). The same volume gives the [floating-point model](/floating-point-model/), [least squares](/least-squares-problem/) for fitting and the [Poisson equation](/poisson-equation/) behind Poisson reconstruction. From geometry come the [convex hull](/convex-hull/), the [Hausdorff distance](/hausdorff-distance/) and the [Fréchet distance](/frechet-distance/), the [Delaunay triangulation](/delaunay-triangulation/) and the [alpha shape](/alpha-shape/). Meshes are stored in a [doubly connected edge list](/doubly-connected-edge-list/) and counted with [Euler's formula](/euler-formula/); the [octree](/octree/) and the [binary heap](/binary-heap/) come from the volume on data structures. The meshes made here are drawn by [triangle rasterization](/triangle-rasterization/) in the first chapter of this volume.
