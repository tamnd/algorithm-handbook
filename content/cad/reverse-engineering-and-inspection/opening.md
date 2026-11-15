A pump housing made forty years ago has no drawing, and a spare must be machined. A laser scanner returns two million points on its surface, but a designer needs a solid with planes, cylinders and exact hole sizes, not a cloud of points. A new batch of the same housing comes off the machine, and a coordinate measuring machine touches 40 points on one face to decide whether the face is flat to within 0.05 mm. The drawing says how far each face may vary, and an engineer must know whether ten parts, each within its limits, still fit together. This chapter is about the algorithms behind these three tasks: reverse engineering, inspection and tolerancing.

The same few problems recur, and the pages keep their guarantees apart. A least-squares fit is exact for its own objective, the sum of squared distances. An algebraic fit minimizes the value of an equation instead of the distance and is biased under noise: on a short arc the simplest algebraic circle fit returns a radius that is too small. Form error, as the standards define it, is a minimax quantity, the width of the thinnest zone that holds the points, and a least-squares fit only bounds it from above. Registration of points to a model by iterative closest points converges to a local minimum, and segmentation by random sampling succeeds with a probability that the method states. In tolerance analysis a worst-case sum bounds every assembly, while root sum of squares and Monte Carlo estimate the fraction of assemblies that fail.

## What the chapter covers

The chapter is in seven groups, read in order.

1. **Fitting primitives to points.** The problem of [reverse engineering](/reverse-engineering-of-geometric-models/) and the fits of one region: [algebraic distance fitting](/algebraic-distance-fitting/), [circle fitting](/circle-fitting/), [Taubin fitting](/taubin-fitting/), [geometric primitive fitting](/geometric-primitive-fitting/) of spheres, cylinders, cones and tori, and [constrained primitive fitting](/constrained-primitive-fitting/), which keeps faces parallel and radii equal.
2. **Fitting free-form curves and surfaces.** [Parameter correction](/parameter-correction/) and [squared distance minimization](/squared-distance-minimization/) for B-spline curves and surfaces.
3. **Segmentation and B-rep reconstruction.** [Segmentation into primitives](/primitive-segmentation/), the [variable-order surface fitting](/variable-order-surface-fitting/) of Besl and Jain, [slippage analysis](/slippage-analysis/), and [B-rep reconstruction](/brep-reconstruction-from-scans/), which closes the fitted faces into a solid.
4. **Specifying tolerances.** [Geometric dimensioning and tolerancing](/geometric-dimensioning-and-tolerancing/), the [datum reference frame](/datum-reference-frame/), [Requicha's tolerance zones](/requicha-tolerance-zone-theory/), the [small displacement torsor](/small-displacement-torsor/) and the [Tolerance-Map](/tolerance-map/).
5. **Measuring a part against its model.** [CAD-based inspection](/cad-based-inspection/), the [localization](/inspection-localization/) of measured points in the model frame, [Hammersley sampling](/hammersley-sampling-for-cmm/) and [CMM probe path planning](/cmm-probe-path-planning/).
6. **Form error.** [Form error evaluation](/form-error-evaluation/), the [least-squares reference feature](/least-squares-reference-feature/), [minimum-zone flatness](/minimum-zone-flatness/) and [minimum-zone cylindricity](/minimum-zone-cylindricity/).
7. **Tolerance analysis and allocation.** The [direct linearization method](/direct-linearization-method/), the [Jacobian-torsor model](/jacobian-torsor-model/), [Monte Carlo tolerance analysis](/monte-carlo-tolerance-analysis/) and [tolerance allocation](/tolerance-allocation/).

Some neighbors live in other chapters. The worst-case and root-sum-of-squares rules for a chain of dimensions are in [tolerance stack-up](/tolerance-stack-up/), in chapter 31.8 on CAM and additive manufacturing, and the [3-2-1 locating principle](/three-two-one-locating-principle/) is in chapter 31.9 on process planning. [Mesh segmentation](/mesh-segmentation/) and the [Metro mesh comparison](/metro-mesh-comparison/) are in chapter 31.5 on mesh processing. Registration by iterative closest points, RANSAC, normal estimation and outlier removal belong to the computer vision volume, which has only short stub pages so far; the entries here state what they use of them.

## A first reading

Read these in order:

1. Reverse engineering of geometric models
2. Algebraic distance fitting and circle fitting
3. Geometric primitive fitting
4. Segmentation into primitives
5. B-rep reconstruction from scans
6. Geometric dimensioning and tolerancing
7. The datum reference frame
8. Inspection localization
9. Form error evaluation and the least-squares reference feature
10. Minimum-zone flatness
11. Monte Carlo tolerance analysis
12. Tolerance allocation

Skip at first Taubin fitting, squared distance minimization, variable-order surface fitting, slippage analysis, the Tolerance-Map, the Jacobian-torsor model and minimum-zone cylindricity. Each refines a method of the first reading, and each reads more easily once the plain least-squares fit, the minimax zone and the worst-case sum are clear. Read the small displacement torsor before the Tolerance-Map and the Jacobian-torsor model, since both are built on it.

## Before you start

The fits rest on Volume 12: the [least-squares problem](/least-squares-problem/), the [singular value decomposition](/singular-value-decomposition/), the [generalized eigenvalue problem](/generalized-eigenvalue-problem/), [Newton's method for systems](/newton-method-for-systems/) and [interval arithmetic](/interval-arithmetic/). Monte Carlo tolerance analysis uses [Monte Carlo integration](/monte-carlo-integration/), and Hammersley points are a finite form of the [Halton sequence](/halton-sequence/), both also in Volume 12. A line or plane fitted by orthogonal distance is [errors-in-variables regression](/errors-in-variables-regression/), and [least median of squares](/least-median-of-squares/) is a fit that tolerates outliers (Volume 33). The orthogonal fit is also [principal component analysis](/principal-component-analysis/) in Volume 25, and the best rotation between matched points is the [Kabsch algorithm](/kabsch-algorithm/) in Volume 27.

Form error is computational geometry from Volume 13: the [3D convex hull](/convex-hull-3d/), the [width](/polygon-width/) of a point set by [rotating calipers](/rotating-calipers/), the [minimum-width annulus](/minimum-width-annulus/) for roundness and the [Minkowski sum](/minkowski-sum/) for Tolerance-Maps. Minimax fits and allocation use [linear programming](/linear-programming-problem/) and [Lagrange multipliers](/lagrange-multiplier/), and probe paths use the [traveling salesman problem](/traveling-salesman-problem/), all in Volume 15. Free-form fitting needs [B-spline fitting](/b-spline-fitting/) and [surface curvature](/surface-curvature/) from Volume 28. Within Volume 31 the chapter assumes the [boundary representation](/boundary-representation/), [r-sets](/r-set/) and [solid offsetting](/solid-offsetting/) of chapter 31.1, [point projection onto a surface](/point-projection-onto-a-surface/) from chapter 31.2, and [vector loop closure](/vector-loop-closure/) from chapter 31.4.
