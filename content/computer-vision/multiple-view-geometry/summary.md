## What to remember

- The planar maps form a hierarchy with 3, 4, 6 and 8 degrees of freedom: Euclidean, similarity, affine and projective. A [homography](/homography/) is fixed by four matches with no three points on a line, and it keeps the [cross-ratio](/cross-ratio/) of four points on a line.
- The [DLT](/dlt-homography/) solves a $2n \times 9$ system by the SVD. It is exact on noise-free data and otherwise minimizes an algebraic error, which depends on the frame; [Hartley normalization](/hartley-normalization/) moves the centroid to the origin and scales the mean distance to $\sqrt 2$ in each image first.
- The [reprojection error](/reprojection-error/) is the maximum likelihood cost under independent Gaussian noise in the image. The [Sampson distance](/sampson-distance/) is its first-order approximation for a single constraint, $(x_2^{\mathsf T} F x_1)^2$ divided by the squared norm of the gradient.
- The [fundamental matrix](/fundamental-matrix/) satisfies $x_2^{\mathsf T} F x_1 = 0$, has rank 2 and 7 degrees of freedom, and cannot be found from points on one plane: then $F = [v]_\times H$ for any $v$. The [essential matrix](/essential-matrix/) $E = [t]_\times R$ has 5 degrees of freedom and singular values $(s, s, 0)$, equivalently $2EE^{\mathsf T}E - \operatorname{tr}(EE^{\mathsf T})E = 0$.
- [Decomposing $E$](/essential-matrix-decomposition/) gives four poses, two rotations times two signs of $t$; [cheirality](/cheirality/) keeps the one with the points in front of both cameras. The length of $t$ is never found from images alone.
- The eight-point algorithm needs 8 matches and enforces rank 2 after the linear solve. The [seven-point algorithm](/seven-point-algorithm/) has one or three real solutions, the [five-point algorithm](/five-point-algorithm/) at most 10 and also works for planar scenes, and [P3P](/p3p/) at most 4; [EPnP](/epnp/) handles $n$ points in $O(n)$ time.
- Linear [triangulation](/linear-triangulation/) is exact on noise-free data but not invariant to projective maps, the midpoint method is invariant only to similarities, and the [optimal method](/optimal-triangulation/) finds the global minimum of the two-view reprojection error from a polynomial of degree 6.
- [RANSAC](/ransac/) draws $k = \lceil \log(1 - p)/\log(1 - w^s) \rceil$ samples to get a clean one with probability $p$: 72 for $w = 0.5$, $s = 4$, $p = 0.99$. Success is probable, not certain, and maximizing the consensus exactly is NP-hard.
- The [trifocal tensor](/trifocal-tensor/) has 27 entries and 18 degrees of freedom. Matches alone fix a scene up to a projective map ([projective reconstruction theorem](/projective-reconstruction-theorem/)), except in [critical configurations](/critical-configurations/), such as points and centres on a ruled quadric for two views.

| Model | Degrees of freedom | Minimal sample | Solutions from it | Linear method |
|---|---|---|---|---|
| Homography $H$ | 8 | 4 matches | 1 | DLT, 4 or more matches |
| Fundamental matrix $F$ | 7 | 7 matches | 1 or 3 | eight-point, 8 or more |
| Essential matrix $E$ | 5 | 5 matches | up to 10 | eight-point on normalized points |
| Calibrated pose (PnP) | 6 | 3 points | up to 4 | DLT on 6 points, EPnP |
| Camera matrix $P$ | 11 | 5.5 points (6) | 1 | DLT resectioning |
| Trifocal tensor | 18 | 6 points in 3 views | 1 or 3 | linear, 7 points |

: The geometric models of the chapter with their minimal samples. The number of RANSAC samples grows fast with the sample size.

## Choosing a method

For two views, decide first what is known. If the camera turned about its centre, or the scene is a plane, fit a homography with the normalized DLT inside RANSAC with four-point samples. If the cameras are calibrated, fit $E$ with the five-point algorithm, which also survives planar scenes, and decompose it with the cheirality test. If they are not calibrated, fit $F$ with the seven-point algorithm and check that the scene is not nearly planar. To find a camera against a known 3D model, use P3P inside RANSAC and refine the pose with EPnP or a nonlinear fit.

Always finish with a cost in pixels: refine the best model on its inliers by the reprojection error or the Sampson distance, and triangulate with the optimal method or with a few Gauss-Newton steps from the linear answer. Among the RANSAC variants, [LO-RANSAC](/lo-ransac/) and [MSAC](/msac/) scoring improve the answer at little cost, [PROSAC](/prosac/) saves time when the matches have quality scores, and [MAGSAC](/magsac/) removes the need to pick an inlier threshold.
