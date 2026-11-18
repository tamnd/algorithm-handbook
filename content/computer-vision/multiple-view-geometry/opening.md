Two photographs of a courtyard give a thousand matched features, and about half of the matches are wrong. If the camera only turned between the shots, or if the matches lie on one flat wall, the true matches obey a [homography](/homography/), a $3 \times 3$ matrix that four matches fix. If the camera also moved, they obey the [fundamental matrix](/fundamental-matrix/), which seven matches fix up to three choices, or the [essential matrix](/essential-matrix/) when the camera is calibrated, which five matches fix up to ten. To find the model among the wrong matches, [RANSAC](/ransac/) fits it to random minimal samples and counts the matches that agree. With half the matches wrong, getting at least one clean sample with probability 0.99 takes 72 samples of four, 146 samples of five, 588 samples of seven and 1177 samples of eight. Small samples pay off.

The chapter is about the algebra of points, lines and cameras in projective space, and about the estimators built on it. Most of the estimators are linear: they are exact for noise-free data, and with noise they minimize an algebraic error that has no direct meaning in pixels. The costs with a meaning are the reprojection error, which is the maximum likelihood cost under Gaussian noise, and its first-order approximation, the Sampson distance. Some configurations are degenerate for a method, and no amount of data fixes the answer: points on one plane for the fundamental matrix, and points and cameras on a ruled quadric for any reconstruction from two views. Each entry says which error it minimizes and when it fails.

## What the chapter covers

1. **The projective plane and its maps.** The [projective plane](/projective-plane/), the homography, the [hierarchy of planar transformations](/planar-transformation-hierarchy/) and the [cross-ratio](/cross-ratio/).
2. **Estimating a homography.** The [estimation problem](/homography-estimation/), the [reprojection error](/reprojection-error/), [algebraic and geometric error](/algebraic-and-geometric-error/), the [Sampson distance](/sampson-distance/), the [DLT](/dlt-homography/) and [Hartley normalization](/hartley-normalization/).
3. **Using homographies.** [Image stitching](/image-stitching/), [multi-band blending](/multi-band-blending/) and [homography decomposition](/homography-decomposition/).
4. **Fitting with outliers.** [Robust model fitting](/robust-model-fitting/), RANSAC and the [RANSAC iteration bound](/ransac-iteration-bound/).
5. **Two-view geometry.** [Epipolar geometry](/epipolar-geometry/), the fundamental and essential matrices, the [characterization of essential matrices](/essential-matrix-characterization/), [cheirality](/cheirality/), the [decomposition of $E$](/essential-matrix-decomposition/) and the [relative pose problem](/relative-pose-problem/).
6. **Estimating F and E.** The [eight-point algorithm](/eight-point-algorithm/), its [normalized form](/normalized-eight-point-algorithm/), the [seven-point algorithm](/seven-point-algorithm/), [minimal solvers](/minimal-solver/) and the [five-point algorithm](/five-point-algorithm/).
7. **Pose and triangulation.** [Perspective-n-point](/perspective-n-point/), [P3P](/p3p/), [EPnP](/epnp/), [point triangulation](/point-triangulation/) and its [midpoint](/midpoint-triangulation/), [linear](/linear-triangulation/) and [optimal](/optimal-triangulation/) methods.
8. **Better sample consensus.** [MSAC](/msac/), [MLESAC](/mlesac/), [LO-RANSAC](/lo-ransac/), [PROSAC](/prosac/), [preemptive RANSAC](/preemptive-ransac/), [MAGSAC](/magsac/) and [J-linkage](/j-linkage/).
9. **Projective reconstruction.** The [trifocal tensor](/trifocal-tensor/), the [projective reconstruction theorem](/projective-reconstruction-theorem/), [critical configurations](/critical-configurations/) and [stratified reconstruction](/stratified-reconstruction/).

## A first reading

Read these 14 entries in order:

1. projective plane;
2. homography;
3. planar transformation hierarchy;
4. reprojection error;
5. DLT for homographies;
6. Hartley normalization;
7. RANSAC;
8. RANSAC iteration bound;
9. epipolar geometry;
10. fundamental matrix;
11. essential matrix;
12. normalized eight-point algorithm;
13. essential matrix decomposition;
14. linear triangulation.

Then read perspective-n-point and P3P. Skip at first the trifocal tensor, the projective reconstruction theorem with its critical configurations, the five-point algorithm and the RANSAC variants. Come back to the five-point algorithm and LO-RANSAC when you build a real pipeline, and to the projective theorems before self-calibration in Chapter 38.2.

## Before you start

You need the [camera projection matrix](/camera-projection-matrix/), the [intrinsic matrix](/camera-intrinsic-matrix/) and [homogeneous coordinates](/homogeneous-coordinates/) from Chapter 38.2. From Volume 12 you need the [singular value decomposition](/singular-value-decomposition/), the [condition number](/condition-number/) and [polynomial root finding](/polynomial-root-finding/). The statistics comes from Volume 25, with [maximum likelihood estimation](/maximum-likelihood-estimation/) and [ordinary least squares](/ordinary-least-squares/), and from Volume 33, with the [breakdown point](/breakdown-point/) and [M-estimators](/m-estimator/). The RANSAC bound uses the [geometric distribution](/geometric-distribution/) (Volume 1). Stitching uses [image warping](/image-warping/) and the [Laplacian pyramid](/laplacian-pyramid/) (Volume 28).

The roadmap below lists every entry of the chapter with its kind and level, and the figure after it shows which entries lean on which.
