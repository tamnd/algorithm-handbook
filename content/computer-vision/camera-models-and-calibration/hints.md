1. The line is $(1, 2, 1) \times (3, 5, 1) = (-3, 2, -1)$, that is $3x - 2y + 1 = 0$; both points satisfy it. The lines $(1, 0, -1)$ and $(1, 0, -2)$ meet at $(0, 1, 0)$, a point at infinity in the direction of the $y$ axis.

2. $X_c = (1, 0.5, 10)$, so the pixel is $(320 + 800 \cdot 0.1, 240 + 800 \cdot 0.05) = (400, 280)$. The centre is $C = -R^{\mathsf T} t = (0, 0, -5)$.

4. $r^2 = 0.25$ and the radial factor is $1 - 0.05 + 0.003125 = 0.953125$, which gives $(0.2859375, 0.38125)$. The tangential terms add $(0.0011, 0.00105)$, giving $(0.2870375, 0.3823)$.

5. $P$ has 11 degrees of freedom and each point gives 2 equations, so 5.5 points; round up to 6, and use only one equation of the sixth point if you want a minimal set. Ten points give a $20 \times 12$ system.

7. $K$ has the rows $(500, 0, 250)$, $(0, 500, 200)$ and $(0, 0, 1)$, and $R$ is the turn by $90°$ about the $z$ axis, with the rows $(0, -1, 0)$, $(1, 0, 0)$ and $(0, 0, 1)$. Then $t = K^{-1} p_4 = (1, 2, 10)$ and $C = -R^{\mathsf T} t = (-2, 1, -10)$. Each row of $P$ gives 0 at $(C, 1)$.

8. $r_u = 1/(1 - 0.1) = 1.1111$. For $r_u = 1$, solve $\lambda r_u r_d^2 - r_d + r_u = 0$, here $0.1 r_d^2 + r_d - 1 = 0$, whose positive root is $r_d = 0.91608$.

11. The vanishing points are $(-591.88, 458.38)$, $(320.00, -1408.49)$ and $(767.09, 458.38)$. The altitude from the second point is the vertical line $x = 320$, and the altitude from the first meets it at $y = 240$, so the orthocenter is $(320, 240)$. Then $f^2 = -(v_1 - c) \cdot (v_3 - c) = 360000$, so $f = 600$.

13. $R = R_2 R_1^{\mathsf T} = R_y(10°)$ and $t = t_2 - R t_1 = (-0.6488, 0, 0.1130)$, so the baseline is 0.6586.

15. With the principal point at the origin, distortion and focal length scale $(x_c, y_c)$ by one positive factor, so $(u, v) \times (x_c, y_c) = 0$, that is $u\, y_c - v\, x_c = 0$. Divide by $T_y$: the equation is linear in the seven unknowns $r_{11}/T_y$, $r_{12}/T_y$, $r_{13}/T_y$, $T_x/T_y$, $r_{21}/T_y$, $r_{22}/T_y$, $r_{23}/T_y$ (with the scale $s_x$ folded in), and $f$, $T_z$ and $\kappa_1$ do not appear.

16. Three views give three pairs and 6 equations for 5 unknowns. The equations of the three pairs need not be independent, the equations are quadratic and may have several real solutions, and critical motions such as rotations about parallel axes leave a family of solutions.

17. The constraints say that $[h_1, h_2]^{\mathsf T} B [h_1, h_2]$ is a multiple of the identity. For the turned board this matrix becomes $Q^{\mathsf T} (\cdot) Q$, which is a multiple of the identity exactly when the first one is. So the new rows of $V$ express the same two conditions and the rank stays 2.

18. The infinite homography is $H_\infty = K R K^{-1}$, which is $I$ when $R = I$. The constraint becomes $\omega = \omega$.
