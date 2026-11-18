## What to remember

- A [feature track](/feature-track/) is a connected component of the match graph, found by union-find; a component with two features of one image is inconsistent and must be split or dropped. Two calibrated views need $n \ge 5$ points by counting ($4n \ge 3n + 5$), and two uncalibrated views need $n \ge 7$.
- The [Gauss-Newton step](/gauss-newton-algorithm/) solves $J^{\mathsf T} J\, h = -J^{\mathsf T} r$. Its local rate is quadratic for zero-residual problems, linear for small residuals, and it may diverge for large ones; a full step can raise the cost.
- [Levenberg-Marquardt](/levenberg-marquardt/) solves $(J^{\mathsf T} J + \mu D)h = -J^{\mathsf T} r$, accepts only steps that lower the cost, and is defined even when the gauge makes $J^{\mathsf T} J$ singular. [Powell's dog leg](/powell-dogleg/) moves on the path from the steepest descent point to the Gauss-Newton point inside a trust region, and a rejected step costs no new factorization.
- [Bundle adjustment](/bundle-adjustment/) is the maximum likelihood estimate under Gaussian image noise, and every solver finds a local minimum. Its cost does not change under a [gauge](/gauge-freedom/) of 7 dimensions for calibrated cameras and 15 for projective ones.
- Eliminating the points leaves the [reduced camera system](/reduced-camera-system/) with $S = U - W V^{-1} W^{\mathsf T}$, of size $6m$ for $m$ cameras, because no residual involves two points. [Sparse bundle adjustment](/sparse-bundle-adjustment/) gives exactly the dense step at far lower cost; the inexact Newton form solves $S$ by conjugate gradients with a block Jacobi preconditioner.
- Under an affine camera the centred $2F \times P$ measurement matrix has rank 3, and [Tomasi-Kanade](/tomasi-kanade-factorization/) splits it by the SVD in closed form, with a metric upgrade from the orthogonality of the camera rows. The projective [Sturm-Triggs](/sturm-triggs-factorization/) matrix has rank 4 once the depths are known.
- [Rotation averaging](/rotation-averaging/) finds all rotations from the relative ones on the view graph; the [Lie-algebraic method](/lie-algebraic-rotation-averaging/) converges to a stationary point near its start, not to a global minimum. [Translation averaging](/translation-averaging/) needs a parallel rigid view graph, or the positions are not fixed up to scale and shift.
- With one camera the scale of [visual odometry](/visual-odometry/) is never observed, so it drifts: a relative error of 1 percent per step gives $1.01^{100} = 2.70$ after 100 steps. [Scale drift](/scale-drift/) stays unless a loop closure, a stereo baseline or an inertial sensor fixes it.

| Method | Data | Solves for | Result |
|---|---|---|---|
| Tomasi-Kanade | complete tracks, affine camera | all cameras and points | closed form, rank 3 |
| Incremental SfM | image collection | cameras one at a time | bundle adjusted after each step |
| Global SfM | view graph | all rotations, then all centres | bundle adjusted at the end |
| Sparse bundle adjustment | tracks and a start | all cameras and points | a local minimum |
| Nistér's visual odometry | video | pose of each frame | five-point and P3P in preemptive RANSAC |
| DSO | video | keyframe poses and sparse depths | photometric window optimization |
| SVO | video | frame poses and a feature map | direct motion, feature refinement |

: Reconstruction and odometry methods of the chapter. All the iterative ones end in a local minimum.

## Choosing a method

For a collection of photographs, incremental SfM is the robust default: it rejects bad images and tracks as it grows, at the price of repeated bundle adjustments. When the collection has many thousands of images, a global method with robust rotation averaging and then translation averaging is faster, and a final bundle adjustment fixes what the averages leave. Factorization is useful for a quick start on short sequences with a narrow field of view and complete tracks.

For a moving camera, use visual odometry with keyframes and a sliding window. A feature method such as Nistér's or one built on ORB features copes with large motions and changes of light; direct methods such as DSO use more of the image and do well in scenes with little texture but need good photometric calibration and small motions between frames. In bundle adjustment, use sparse Levenberg-Marquardt with a Cholesky factorization of $S$ while $S$ fits in memory, and the inexact Newton form for very large problems.
