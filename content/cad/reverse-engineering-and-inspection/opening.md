An old casting with no drawings is scanned, and a CAD model must be rebuilt from millions of points: that is reverse engineering. A machined part is probed on a coordinate measuring machine, and the points must be compared with the CAD model to decide whether a hole lies within its tolerance zone: that is inspection. Tolerancing says how far each feature may vary and how the variations of many parts add up in an assembly.

The fitting problems differ in what distance they minimize. Algebraic distance fitting is a linear least squares problem but is biased for points far from the curve. Geometric fitting minimizes true distances, which is nonlinear and solved by iterations that need a good start. Form error is defined by the minimum zone, the thinnest zone of the ideal form that holds the points, so a least-squares reference feature gives a zone at least as wide. Tolerance analysis can be worst case, statistical or by Monte Carlo sampling, which has sampling error. Scan segmentation is judged by measured results.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Fitting.** Algebraic distance fitting, Taubin's gradient-weighted fitting, circle fitting, least-squares fitting of spheres, cylinders, cones and tori, constrained fitting, parameter correction and squared distance minimization.
2. **From scans to CAD models.** Reverse engineering of geometric models, segmentation into surface primitives, variable-order surface fitting, slippage analysis and B-rep reconstruction from segmented scans.
3. **Inspection.** CAD-based inspection, localization of measured points to the model, CMM probe path planning and Hammersley sampling.
4. **Form error.** Form error evaluation, minimum zone flatness and cylindricity, and the least-squares reference feature.
5. **Tolerance specification.** Geometric dimensioning and tolerancing, the datum reference frame, Requicha's tolerance zone theory, the small displacement torsor and tolerance maps.
6. **Tolerance analysis and allocation.** The direct linearization method, the Jacobian-torsor model, Monte Carlo tolerance analysis and tolerance allocation.

## What to read meanwhile

The fitting tools are in Volume 12: the [least squares problem](/least-squares-problem/), the [singular value decomposition](/singular-value-decomposition/) and the [eigenvalue problem](/eigenvalue-problem/); the normal of the best-fit plane is the direction of least variance in [principal component analysis](/principal-component-analysis/) (Volume 25). The [Kabsch algorithm](/kabsch-algorithm/) (Volume 27) gives the best rotation between matched point sets, a step of localization. Volume 13 solves the form-error problems in the plane: the [minimum-width annulus](/minimum-width-annulus/) measures roundness, and the [width](/polygon-width/) of a point set, found with [rotating calipers](/rotating-calipers/), measures straightness; the [Hausdorff distance](/hausdorff-distance/) compares shapes.

For surfaces, read [B-spline fitting](/b-spline-fitting/) and [surface reconstruction](/surface-reconstruction/) in Volume 28, and [mesh segmentation](/mesh-segmentation/) and [Metro mesh comparison](/metro-mesh-comparison/) in the chapter on mesh processing. [Tolerance stack-up analysis](/tolerance-stack-up/), in the chapter on CAM and additive manufacturing, gives the worst-case and root-sum-of-squares rules. Hammersley points are a finite form of the [Halton sequence](/halton-sequence/), and [Monte Carlo integration](/monte-carlo-integration/) explains the error of sampling (both Volume 12).
