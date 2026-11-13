The outline of a letter in a font, the body of a car in a design program and the face of a character in an animated film are smooth shapes stored as a few numbers. A designer moves a handful of control points, and an algorithm turns them into a curve or surface that can be drawn, milled or split into triangles. The reverse tasks matter as much: build a surface from scanned points or from a medical volume, and make a mesh or a polyline smaller without changing its shape much.

The central objects are polynomial pieces. A Bézier curve of degree $n$ has $n + 1$ control points; it passes through the first and the last and stays in the convex hull of all of them. The de Casteljau algorithm evaluates it by $n(n+1)/2$ linear interpolations, and the same steps split the curve in two. B-splines join such pieces with smoothness built in, so that moving one control point of a degree-$k$ spline changes the curve on at most $k + 1$ knot intervals. Rational forms (NURBS) represent circles exactly, which polynomials cannot.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Parametric curves.** Continuity at joints, arc length, the Frenet frame, offset curves and curve intersection.
2. **Bézier and B-spline curves.** Bernstein polynomials, the de Casteljau algorithm and Bézier clipping, knot vectors and the Cox-de Boor recursion, de Boor's algorithm, knot insertion by Boehm's and the Oslo algorithm, and NURBS.
3. **Interpolating splines.** Hermite, natural cubic, Catmull-Rom and Kochanek-Bartels splines, and least-squares B-spline fitting.
4. **Surfaces.** Tensor-product, Bézier, triangular and Coons patches, ruled, swept and implicit surfaces, curvature, and tessellation.
5. **Subdivision.** Chaikin's corner cutting, the four-point scheme, and the Catmull-Clark, Doo-Sabin, Loop, butterfly and $\sqrt{3}$ surface schemes.
6. **Meshes from data.** Marching squares, marching cubes and dual contouring; reconstruction by ball pivoting and the Poisson method; mesh simplification by quadric error metrics; and polyline simplification by Ramer-Douglas-Peucker and Visvalingam-Whyatt.

## What to read meanwhile

Chapter 12.5 has the spline theory: [cubic spline interpolation](/cubic-spline-interpolation/), the [cubic Hermite spline](/cubic-hermite-spline/), [smoothing splines](/smoothing-spline/) and [spline evaluation](/spline-evaluation/), which treats de Boor's algorithm. The [Weierstrass approximation theorem](/weierstrass-approximation-theorem/) is proved there with Bernstein polynomials, and [tensor-product interpolation](/tensor-product-interpolation/) is the scheme behind tensor-product patches.

Volume 13 has the discrete side. [Polygon simplification](/polygon-simplification/) states the problem that Ramer-Douglas-Peucker attacks greedily, with error measured by the [Hausdorff](/hausdorff-distance/) or [Fréchet distance](/frechet-distance/). The [alpha shape](/alpha-shape/) and the [Delaunay triangulation](/delaunay-triangulation/) underlie many reconstruction methods. Meshes are stored in a [quad-edge structure](/quad-edge-data-structure/) or in the [doubly connected edge list](/doubly-connected-edge-list/) of Volume 7. Chapter 28.1 turns the finished triangles into pixels by [triangle rasterization](/triangle-rasterization/).
