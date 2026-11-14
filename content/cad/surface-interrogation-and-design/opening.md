A car door is built from a dozen patches. Before tooling, someone must find the point of the surface closest to a measured point, find where two panels meet, and check that a reflected light line crosses each patch boundary without a kink. Interrogation answers such questions about an existing surface. Design builds surfaces with control over how they join: patches through a network of curves, smooth fillings of holes with three or five sides, fair shapes that minimize an energy, and curves with polynomial arc length and rational offsets.

The methods are of different kinds, and the entries will keep them apart. Implicitization by resultants is exact algebra. Point projection by Newton steps converges only from a good start. Lattice evaluation can miss a small closed loop of an intersection, while the loop test of Sederberg and Meyers is a proved condition under which none can be missed. Isophotes and reflection lines show defects to the eye but do not measure them.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Points and distances.** Point projection onto a curve or surface, Newton point inversion from a coarse grid, the minimum distance between two surfaces, and geodesics on parametric surfaces.
2. **Intersections.** Curve-surface intersection, algebraic surface intersection and implicitization, Levin's method for two quadrics, lattice evaluation, the interval projected polyhedron solver, Sederberg-Meyers loop detection, and tangential intersections, where marching fails.
3. **Shape inspection.** Lines of curvature and umbilic points, silhouette curves, curvature combs, isophotes and reflection lines.
4. **Patches and their joins.** Tangent plane continuity, twist compatibility, Gregory patches, n-sided and generalized Bézier patches, vertex blends, Gordon surfaces and surface skinning.
5. **Fairing and special shapes.** Energy-based fairing, fairing by knot removal and reinsertion, minimum variation surfaces, developable surfaces and their approximation, offset trimming, and Pythagorean hodograph curves with PH quintic Hermite interpolation.

## What to read meanwhile

The differential geometry is in Volume 28: the [parametric surface](/parametric-surface/), the [fundamental forms](/fundamental-forms/) and [surface curvature](/surface-curvature/), with the [Bézier patch](/bezier-patch/), the [Bézier triangle](/bezier-triangle/), the [Coons patch](/coons-patch/) and the [ruled surface](/ruled-surface/), whose entry tests developability. Plane versions of two problems are there too: [curve intersection](/curve-intersection/), [Bézier clipping](/bezier-clipping/), the [offset curve](/offset-curve/) and [curve offsetting](/curve-offsetting/).

In the chapter on solid modeling, [surface-surface intersection](/surface-surface-intersection/) states the problem and the loop test; [marching surface intersection](/marching-surface-intersection/) traces one branch by Newton corrections and misses a loop that has no start point; [subdivision surface intersection](/subdivision-surface-intersection/) loses no intersection point but stops at a flatness tolerance. The [offset surface](/offset-surface/) and the [rolling-ball blend](/rolling-ball-blend/) are there as well. The numerical tools are [Newton's method for systems](/newton-method-for-systems/) and the [interval Newton method](/interval-newton-method/) (Volume 12) and the [resultant](/resultant/) (Volume 11). On meshes, see [discrete Gaussian curvature](/discrete-gaussian-curvature/) and the [discrete geodesic problem](/discrete-geodesic-problem/).
