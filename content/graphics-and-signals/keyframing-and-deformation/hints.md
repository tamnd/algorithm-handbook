1. The tangents are $m_1 = (3 - 0)/2 = 3/2$ and $m_2 = (1 - 2)/2 = -1/2$. The Hermite basis at $s = 1/2$ gives $\tfrac12 \cdot 2 + \tfrac18 \cdot \tfrac32 + \tfrac12 \cdot 3 - \tfrac18 \cdot (-\tfrac12) = 11/4$. That is above the average $5/2$.

2. At $t = 0.6$ s, $u = 0.3$ and $e(0.3) = 0.27 - 0.054 = 0.216$, so the door is at $2.16$ m. The speed is $5e'(u) = 30u(1 - u)$, largest at $u = 1/2$: $7.5$ m/s, which is $1.5$ times the average speed of 5 m/s.

4. With degree 1 the deformation is trilinear. The moved corner has the weight $(1/2)^3 = 1/8$ at the centre, so the centre goes to $(1/2, 1/2, 5/8)$.

6. The length $1.2$ lies between $0.97473$ and $1.47894$, so linear interpolation gives $u = 0.75 + 0.25 \cdot (1.2 - 0.97473)/(1.47894 - 0.97473) = 0.86169$. Newton's step $u - (s(u) - 1.2)/\sqrt{1 + 4u^2}$ gives $0.86841$, within $2 \cdot 10^{-5}$ of the true value.

7. The speed is $\sqrt 2$, so one turn has length $2\pi\sqrt 2$. The Frenet frame turns by $\tfrac12 \cdot 2\pi\sqrt 2 = \pi\sqrt 2 \approx 4.443$ radians, about $254.6°$, per turn of the helix.

8. $u = (1, 2) \cdot (4, 0)/16 = 1/4$ and $v = (1, 2) \cdot (0, 4)/4 = 2$. The source line has direction $(0, 8)$ and unit perpendicular $(-1, 0)$, so $X' = (1, 1) + \tfrac14 (0, 8) + 2(-1, 0) = (-1, 3)$.

11. The Jacobian is $\begin{pmatrix} r & 0 & x r' \\ 0 & r & y r' \\ 0 & 0 & 1 \end{pmatrix}$ with $r = 3/2$ and $r' = 1/2$, and the point goes to $(3/2, 0, 1)$. The inverse transpose sends $(1, 0, 0)$ to a multiple of $(1, 0, -x r') = (1, 0, -1/2)$, whose unit vector is $(0.8944, 0, -0.4472)$. The tapered surface is $x^2 + y^2 = r(z)^2$, with gradient $(3, 0, -3/2)$ there, which agrees. The Jacobian itself gives $(3/2, 0, 0)$, which is not normal to that surface.

14. The closest point on the reference curve is $(1, 0, 0)$ at distance 1, so $x = 1/2$ and $F = (3/4)^2 = 9/16$. With $s = 1$ the point moves by $F(0, 0, 2)$ to $(1, 1, 1.125)$. With $s = 3$ the offset $(0, 1, 0)$ is also scaled by $1 + (s - 1)F = 2.125$, giving $(1, 2.125, 1.125)$.

16. A turn is a similarity, and both kinds of coordinates reproduce similarities, so both give $(1 - 0.3, 0.25) = (0.7, 0.25)$. Mean value coordinates have linear precision and partition of unity, so they reproduce every affine map and send the point to $(0.4, 0.3)$. A shear is not conformal, and Green coordinates give a conformal map in 2D, so they cannot reproduce it.

19. With $B(s) = 2s(1 - s)$, the height is $z' = z + h B(x) B(y) B(z)$ and $\partial z'/\partial z = 1 + h B(x) B(y) \cdot 2(1 - 2z)$. Its minimum on the closed cube is at $x = y = 1/2$, $z = 1$, where it equals $1 - h/2$. The determinant stays positive exactly when $h < 2$; at $h = 2$ it reaches 0 on the top face, and for $h > 2$ the cube folds.

20. The derivative is $(1 - u^2, 2u)$, and $(1 - u^2)^2 + 4u^2 = (1 + u^2)^2$, so the speed is $1 + u^2$ and the length is $4/3$. Five-point Gauss-Legendre is exact for degree up to 9, so every table entry is exact. Newton on $u + u^3/3 = 1$ from $u = 1$ gives $0.833333$, $0.817851$, $0.817732$.

21. Rotations about one axis commute and multiply by adding angles, so each factor $\exp(\tilde B_j(u) \log(q_{j-1}^{-1} q_j))$ adds $\tilde B_j(u)(\theta_j - \theta_{j-1})$. The sum is the cumulative form of the uniform cubic B-spline. At the joints the angles are $(0 + 4 \cdot 90 + 90)/6 = 75°$ and $(90 + 4 \cdot 90 + 0)/6 = 75°$. The middle of the segment reaches $86.25°$, so the curve never meets the $90°$ controls.

22. The chord $v_1 = x_1 - x_0$ is perpendicular to the bisector of the two radii, so the first reflection maps the inward normal at $x_0$, $(-1, 0, 0)$ to $x_1$'s inward normal $(-1/2, -\sqrt 3/2, 0)$ and the tangent $t_0$ to $-t_1$. The second reflection, in the plane normal to $t_1 - (-t_1)$, fixes vectors normal to $t_1$, so the normal stays. The binormal $(0, 0, 1)$ is fixed by both. On any plane curve the rotation minimizing frame is the planar normal frame, and both reflections keep it exactly.
