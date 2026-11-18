1. ◦ In [homogeneous coordinates](/homogeneous-coordinates/), find the line through the points $(1, 2)$ and $(3, 5)$ as a cross product, and the point where the lines $x = 1$ and $x = 2$ meet. What kind of point is the second one?

2. ◦ A camera has $K$ with $f = 800$ and the principal point $(320, 240)$, $R = I$ and $t = (0, 0, 5)$. Project the world point $(1, 0.5, 5)$ with the [projection matrix](/camera-projection-matrix/), and give the camera centre from the [extrinsic parameters](/camera-extrinsic-parameters/).

3. ◦ Count the degrees of freedom of a finite projection matrix $P$, of a general [intrinsic matrix](/camera-intrinsic-matrix/) $K$, of $K$ with zero skew and square pixels, and of an [affine camera](/affine-camera-model/).

4. ◦ Apply the [Brown-Conrady model](/brown-conrady-distortion-model/) with $k_1 = -0.2$ and $k_2 = 0.05$ to the normalized point $(0.3, 0.4)$, first with no tangential terms and then with $p_1 = 0.001$ and $p_2 = 0.002$, using $\delta x = 2p_1 xy + p_2(r^2 + 2x^2)$ and $\delta y = p_1(r^2 + 2y^2) + 2p_2 xy$.

5. ◦ How many points does [DLT resectioning](/dlt-camera-resectioning/) need, and why is the answer not a whole number before rounding? What is the size of the linear system for 10 points?

6. ◦ How many views of a flat pattern does [Zhang's method](/zhang-calibration-method/) need for a general $K$, and how many if the skew is known to be zero?

7. • Decompose $P$ with the rows $(0, -500, 250, 3000)$, $(500, 0, 200, 3000)$ and $(0, 0, 1, 10)$ by [camera matrix decomposition](/camera-matrix-decomposition/). Give $K$, $R$, $t$ and the centre $C$, and check that $PC = 0$.

8. • In the [division model](/division-distortion-model/) with $\lambda = -0.1$, a distorted point at radius $r_d = 1$ is undistorted to what radius? Which distorted radius gives the undistorted radius $r_u = 1$? Write the quadratic equation you solve.

9. • A fisheye lens has $f = 300$ pixels. Compare the image radius of a ray at $60°$ under the pinhole model and under the equidistant [Kannala-Brandt model](/kannala-brandt-fisheye-model/), and give the radius at $90°$ for the equidistant model and for $k_1 = 300$, $k_2 = -15$.

10. • For the [unified omnidirectional model](/unified-omnidirectional-camera-model/), show that a ray at angle $\theta$ from the axis lands at the normalized radius $\sin\theta/(\cos\theta + \xi)$. Evaluate it at $30°$, $60°$ and $90°$ for $\xi = 0$, $0.5$ and $1$, give the field of view for each $\xi$, and show that $\xi = 1$ gives $\tan(\theta/2)$.

11. • A camera with $f = 600$, principal point $(320, 240)$ and $R = R_x(-20°) R_y(35°)$ sees a building whose edges run along the three world axes. Compute the three vanishing points $v_i \sim K r_i$, where $r_i$ is column $i$ of $R$. Then do [vanishing point calibration](/vanishing-point-calibration/) backward: find the orthocenter of their triangle and recover $f$ from two of them.

12. • A [rolling shutter](/rolling-shutter-camera-model/) reads 1000 rows in 30 ms. What is the time between two rows? The camera pans at 1 rad/s with $f = 1000$ pixels. By how many pixels does a vertical edge shift from one row to the next, and from the top to the bottom of the frame?

13. • In [stereo calibration](/stereo-camera-calibration/), one view of the pattern gives $R_1 = I$, $t_1 = (-0.1, 0, 2)$ for camera 1 and $R_2 = R_y(10°)$, $t_2 = (-0.4, 0, 2.1)$ for camera 2. Find the relative pose $(R, t)$ with $X_{c2} = R X_{c1} + t$ and the baseline $\|t\|$.

14. • Using the [image of the absolute conic](/image-of-the-absolute-conic/), show that the back-projected rays of two image points $x_1$ and $x_2$ are orthogonal exactly when $x_1^{\mathsf T} \omega x_2 = 0$, with $\omega = K^{-\mathsf T} K^{-1}$.

15. ★ Prove the radial alignment constraint of [Tsai's method](/tsai-calibration-method/): radial distortion and the focal length change only the distance of a point from the principal point, so the direction from the principal point to the image point is parallel to $(x_c, y_c)$, and this gives one equation per point that does not involve $f$, $T_z$ or $\kappa_1$.

16. ★ The [Kruppa equations](/kruppa-equations/) give two independent equations for each pair of views. With a constant $K$ of 5 unknowns, how many views are needed by counting, using all pairs? Why does counting only give a necessary condition?

17. ★ In Zhang's method, a second view of the board is made by turning the board in its own plane, about its normal, so that $[h_1, h_2]$ becomes $[h_1, h_2]Q$ for a $2 \times 2$ rotation $Q$. Show that the two equations it gives on $B$ are combinations of the equations of the first view, so the system does not gain rank.

18. ★ Show that for a camera that only translates, the homography of the plane at infinity between two views is the identity, so the constraint $\omega = H_\infty^{-\mathsf T} \omega H_\infty^{-1}$ of [self-calibration](/self-calibration/) says nothing about $K$.
