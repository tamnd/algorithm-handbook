## What to remember

- A world point goes to the camera frame by $X_c = R X_w + t$, so the centre is $C = -R^{\mathsf T} t$. The [projection matrix](/camera-projection-matrix/) $P = K[R \mid t]$ is defined up to scale and has 11 degrees of freedom: 5 in $K$, 3 in $R$ and 3 in $t$. With zero skew and square pixels, $K$ has 3.
- [Decomposition](/camera-matrix-decomposition/) factors the left $3 \times 3$ block as $M = KR$ by an RQ factorization, fixes the signs so that $K$ has a positive diagonal and $\det R = +1$, and takes $C$ as the null vector of $P$. It estimates nothing.
- [DLT resectioning](/dlt-camera-resectioning/) needs $n \ge 6$ points, not all on one plane, and solves a $2n \times 12$ system by the SVD. It is exact on noise-free data; with noise it minimizes an algebraic error, so normalize the data first and refine by reprojection error.
- [Zhang's method](/zhang-calibration-method/) gets two linear equations on $B = K^{-\mathsf T} K^{-1}$ from each homography of a flat pattern, so it needs 3 views, or 2 with zero skew. Its final Levenberg-Marquardt fit with distortion finds a local minimum of the reprojection error.
- The [Brown-Conrady model](/brown-conrady-distortion-model/) scales a normalized point by $1 + k_1 r^2 + k_2 r^4 + \cdots$ and adds tangential terms in $p_1, p_2$. The [division model](/division-distortion-model/) undistorts by $x_u = x_d/(1 + \lambda r_d^2)$.
- The [Kannala-Brandt model](/kannala-brandt-fisheye-model/) writes the image radius as $r(\theta) = k_1\theta + k_2\theta^3 + \cdots$ of the angle $\theta$ from the axis; $k_1 = f$ alone is the equidistant fisheye. The [unified model](/unified-omnidirectional-camera-model/) projects the unit sphere point $x_s$ by $x_s/(z_s + \xi)$ and sees a field of $2\arccos(-\xi)$ for $0 \le \xi \le 1$.
- The [image of the absolute conic](/image-of-the-absolute-conic/) $\omega = K^{-\mathsf T} K^{-1}$ depends on $K$ alone; two rays are orthogonal exactly when their image points satisfy $x_1^{\mathsf T} \omega x_2 = 0$. Three [orthogonal vanishing points](/vanishing-point-calibration/) give the principal point as the orthocenter of their triangle when skew is zero and pixels are square.
- The [Kruppa equations](/kruppa-equations/) give two constraints on $K$ for each pair of views, and [self-calibration](/self-calibration/) chooses the metric reconstruction among the projective ones; some motions, such as pure translation, leave it ambiguous.
- A [rolling shutter](/rolling-shutter-camera-model/) with readout time $t_r$ over $H$ rows exposes row $v$ at $v\, t_r/H$ after the first. A [generalized camera](/generalized-camera-model/) has a linear epipolar constraint in 18 unknowns, so 17 matches in general position solve it linearly.

| Method | Input | Minimum data | Output | Error minimized |
|---|---|---|---|---|
| DLT resectioning | known 3D points | 6 points, not coplanar | $P$ | algebraic, then reprojection |
| Tsai's method | known 3D points, one image | 7 points not coplanar, 5 coplanar with known $s_x$ | $R$, $t$, $f$, $\kappa_1$ | linear stages, then nonlinear |
| Zhang's method | a flat pattern | 3 views (2 with zero skew) | $K$, poses, distortion | algebraic, then reprojection |
| Stereo calibration | pattern seen by two cameras | one view pair, more in practice | $K_1$, $K_2$, $R$, $t$ | reprojection in both cameras |
| Vanishing points | one image of orthogonal lines | 3 vanishing points | $f$, principal point, $R$ | none (closed form) |
| Self-calibration | matches of an unknown scene | depends on the assumptions | $K$, metric frame | algebraic, then bundle adjustment |

: Calibration methods of the chapter. Every nonlinear refinement finds a local minimum and needs a good start.

## Choosing a method

When you can put a target in front of the camera, use [Zhang's method](/zhang-calibration-method/) with a checkerboard seen from many angles that fill the image, and check the result by the reprojection error on images not used in the fit. Pick the lens model before you fit: Brown-Conrady with two or three radial terms for ordinary lenses, Kannala-Brandt or the unified model for fisheye and mirror systems, and the division model when a single parameter must be estimated together with geometry, as in minimal solvers.

When no target is possible, as for photos taken by others, use vanishing points for scenes of buildings with three orthogonal directions, or self-calibration over many views with assumptions such as zero skew and a known principal point. Both are fragile: avoid motions that are known to be critical, and finish with [bundle adjustment](/bundle-adjustment/). For phones and fast motion, model the rolling shutter; for rigs of several cameras, the generalized model treats the rig as one camera with a known scale.
