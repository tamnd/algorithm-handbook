A drone circles a church and takes 100 photographs. Matching gives tracks of 50000 scene points, each seen in a few images. The task is to find the 100 camera poses and the 50000 points: $100 \cdot 6 + 50000 \cdot 3 = 150600$ unknowns, tied by the reprojection error of every observation. A dense Cholesky factorization of a matrix of that size would cost about $150600^3/3 \approx 1.1 \times 10^{15}$ operations. But each observation involves one camera and one point, so the points can be eliminated point by point, and what is left is a $600 \times 600$ system for the cameras, which costs about $7.2 \times 10^7$ operations to factor. That one fact, the sparsity of the problem, is what makes bundle adjustment of thousands of images possible.

The chapter covers the two ways of using it. Structure from motion works on a set of photographs, in any order, and can take its time: it builds the reconstruction one image at a time, or it averages all the pairwise rotations and directions at once. Visual odometry works on a video, as it arrives, and must keep up with the camera: it keeps a few keyframes and refines a window of them. Both end in nonlinear least squares, and the solvers of the chapter find a local minimum, which is the right one only if the start is good. With one camera, nothing fixes the scale of the scene, and in visual odometry the scale drifts as the errors of the steps multiply: a bias of 1 percent per step gives a factor of $1.01^{100} = 2.70$ after 100 steps.

## What the chapter covers

1. **Tracks and the reconstruction problem.** [Feature tracks](/feature-track/) built by union-find, and the [structure from motion problem](/structure-from-motion-problem/).
2. **Nonlinear least squares.** The [problem](/nonlinear-least-squares/), the [Gauss-Newton algorithm](/gauss-newton-algorithm/), [Levenberg-Marquardt](/levenberg-marquardt/) and [Powell's dog leg](/powell-dogleg/).
3. **Bundle adjustment.** [Bundle adjustment](/bundle-adjustment/), [gauge freedom](/gauge-freedom/), the [reduced camera system](/reduced-camera-system/), [sparse bundle adjustment](/sparse-bundle-adjustment/) and [inexact Newton bundle adjustment](/inexact-newton-bundle-adjustment/).
4. **Factorization.** The [Tomasi-Kanade](/tomasi-kanade-factorization/) and [Sturm-Triggs](/sturm-triggs-factorization/) methods.
5. **Incremental and global reconstruction.** [Incremental SfM](/incremental-structure-from-motion/), the [view graph](/view-graph/), [rotation averaging](/rotation-averaging/) and its [Lie-algebraic form](/lie-algebraic-rotation-averaging/), [translation averaging](/translation-averaging/) and [global SfM](/global-structure-from-motion/).
6. **Visual odometry.** [Visual odometry](/visual-odometry/), [keyframe selection](/keyframe-selection/), [scale drift](/scale-drift/), [sliding-window bundle adjustment](/sliding-window-bundle-adjustment/) and [Nistér's visual odometry](/nister-visual-odometry/).
7. **Direct methods.** The [photometric error](/photometric-error/), [direct image alignment](/direct-image-alignment/), [DSO](/direct-sparse-odometry/) and [SVO](/semi-direct-visual-odometry/).

## A first reading

Read these 10 entries in order:

1. feature track;
2. structure from motion problem;
3. nonlinear least squares;
4. Gauss-Newton algorithm;
5. Levenberg-Marquardt;
6. bundle adjustment;
7. reduced camera system;
8. incremental structure from motion;
9. Tomasi-Kanade factorization;
10. visual odometry.

Skip at first the dog leg, the inexact Newton method, the Sturm-Triggs method, the averaging entries and the direct methods. Come back to gauge freedom when you need the uncertainty of a reconstruction, to rotation and translation averaging when incremental SfM is too slow for your collection, and to the direct methods when the images have little texture for features.

## Before you start

The chapter uses most of Chapter 38.3: the [reprojection error](/reprojection-error/), [perspective-n-point](/perspective-n-point/), [point triangulation](/point-triangulation/), the [relative pose problem](/relative-pose-problem/), [RANSAC](/ransac/) and the [five-point algorithm](/five-point-algorithm/). Matches come from [feature matching](/feature-matching/) in Chapter 38.1. From Volume 12 you need the [normal equations](/normal-equations/), the [Cholesky decomposition](/cholesky-decomposition/), the [Schur complement](/schur-complement/), the [conjugate gradient method](/conjugate-gradient-method/) with [preconditioning](/preconditioning/), and [bilinear interpolation](/bilinear-interpolation/). Tracks use [union-find](/union-find-connectivity/) and rotation averaging uses the [graph Laplacian](/laplacian-matrix/) (Volume 7). Rotations come from Volume 37, with the [special orthogonal group](/special-orthogonal-group/) and the [logarithm map](/so3-logarithm-map/), and direct alignment from the [Lucas-Kanade method](/lucas-kanade-method/) of Volume 28.

The roadmap below lists every entry of the chapter with its kind and level, and the figure after it shows which entries lean on which.
