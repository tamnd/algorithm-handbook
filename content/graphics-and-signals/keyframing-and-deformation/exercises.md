1. ◦ One channel has the keys $(0, 0)$, $(1, 2)$, $(2, 3)$ and $(3, 1)$. Find the [Catmull-Rom](/catmull-rom-spline/) tangents at the keys $t = 1$ and $t = 2$, and the value of the [keyframe interpolation](/keyframe-interpolation/) at $t = 1.5$. Is the value above or below the average of the two keys around it?

2. ◦ A door slides 10 m in 2 s with the position $x(t) = 10\,e(t/2)$, where $e(u) = 3u^2 - 2u^3$ is the cubic [ease curve](/ease-in-ease-out/). Where is the door at $t = 0.6$ s, and what is its largest speed?

3. ◦ A [Barr taper](/barr-global-deformations/) along the $z$ axis maps $(x, y, z)$ to $(r(z)x, r(z)y, z)$ with $r(z) = 1 - z/4$. Where does it send $(2, 1, 2)$? What is the Jacobian determinant there, and what does it say about the volume near that point?

4. ◦ A [free-form deformation](/free-form-deformation/) of degree 1 in each direction has the eight corners of the unit cube as its control points. The corner $(1, 1, 1)$ moves to $(1, 1, 2)$ and the others stay. Where does the centre $(1/2, 1/2, 1/2)$ go?

5. ◦ Find the [barycentric coordinates](/barycentric-interpolation/) of $(1, 1)$ in the triangle $(0, 0)$, $(4, 0)$, $(0, 4)$. Explain with the dimension count of [generalized barycentric coordinates](/generalized-barycentric-coordinates/) why no other weights with partition of unity and linear precision exist for a triangle.

6. ◦ An [arc length table](/arc-length-table/) for the curve $(u, u^2)$, $0 \le u \le 1$, stores the exact lengths at $u = 0, 1/4, 1/2, 3/4, 1$: $0$, $0.26006$, $0.57390$, $0.97473$, $1.47894$. Find the parameter that the table gives for the length $1.2$ by binary search and linear interpolation, and then the result of one Newton step from it. The true answer is $0.868391$.

7. ◦ The helix $(\cos s, \sin s, s)$ has curvature $1/2$ and torsion $1/2$. Its [Frenet frame](/frenet-frame/) turns about the tangent, relative to a [rotation minimizing frame](/rotation-minimizing-frame/), at the rate of the torsion per unit of arc length. By what angle in radians and in degrees does it turn in one full turn of the helix? Note that $s$ is not arc length.

8. ◦ In [Beier-Neely morphing](/beier-neely-morphing/) with one line pair, the line runs from $P = (0, 0)$ to $Q = (4, 0)$ in the destination and from $P' = (1, 1)$ to $Q' = (1, 9)$ in the source, with $\operatorname{perp}(d_x, d_y) = (-d_y, d_x)$. Compute $u$, $v$ and the source point $X'$ for the destination pixel $X = (1, 2)$.

9. • A [Kochanek-Bartels spline](/kochanek-bartels-spline/) with continuity and bias 0 scales the Catmull-Rom tangents by $1 - \tau$, where $\tau$ is the tension. For the keys of exercise 1, write the value at $t = 1.5$ as a function of $\tau$ and evaluate it at $\tau = 1/5$. For which $\tau$ does the curve at $t = 1.5$ fall to the average of the two keys?

10. • The quintic ease curve is $q(u) = 6u^5 - 15u^4 + 10u^3$. Show that $q(0) = 0$, $q(1) = 1$, and that its first and second derivatives vanish at both ends. Compute $q(1/4)$ and the peak of $q'$, and compare with the cubic of exercise 2.

11. • Taper the unit cylinder $x^2 + y^2 = 1$ by $r(z) = 1 + z/2$. At the point $(1, 0, 1)$ the outward normal is $(1, 0, 0)$. Find the image point and the unit normal there by the inverse transpose of the Jacobian. Show that moving the normal by the Jacobian itself gives a vector that is not normal to the tapered surface.

12. • A free-form deformation of degree 2 in each direction has its 27 control points on the regular grid of the unit cube. Only the centre control point moves, by $h = 2$ in $z$. Find the new $z$ of the centre of the cube and of the point $(1/4, 1/4, 1/4)$.

13. • Apply a twist about the $z$ axis by the angle $\pi z/2$ and the Barr bend with rate $k = 1/2$, centre $y_0 = 0$ and region $-2 \le y \le 2$ to the point $(0, 1, 0)$, first twist then bend, and then bend then twist. Give both results to four places and explain why they differ.

14. • A [wire](/wire-deformation/) has the reference curve from $(0, 0, 0)$ to $(4, 0, 0)$, the same wire moved by $(0, 0, 2)$, radius $r = 2$ and falloff $f(x) = (1 - x^2)^2$. Where does $P = (1, 1, 0)$ go with scale $s = 1$, and with scale $s = 3$?

15. • Compute the [mean value coordinates](/floater-mean-value-coordinates/) of $(1/4, 1/4)$ in the unit square with the vertices $(0, 0)$, $(1, 0)$, $(1, 1)$, $(0, 1)$, to four places. Check that they reproduce the point, and compare them with the bilinear weights of the same point.

16. • In [cage-based deformation](/cage-based-deformation/), turn the unit-square cage by 90 degrees counterclockwise about its centre. Where do mean value coordinates and [Green coordinates](/green-coordinates/) send $(0.25, 0.3)$? Then shear the cage by $(x, y) \mapsto (x + y/2, y)$. Which of the two sends the point to $(0.4, 0.3)$, and why can the other not?

17. • The triangle $(0, 0)$, $(1, 0)$, $(0, 1)$ is to turn into $(0, 0)$, $(0, 1)$, $(-1, 0)$, with the vertex at the origin held. At $t = 1/2$, find the position of the second vertex and the area under linear interpolation of the vertices and under [as-rigid-as-possible interpolation](/as-rigid-as-possible-shape-interpolation/).

18. • Unit quaternion keys $q_i = q_0 \exp(i\theta u)$, for a fixed pure unit quaternion $u$, lie evenly spaced on one great circle. Show that the inner control points of [squad](/squad/) equal the keys, so that squad reduces to [slerp](/spherical-linear-interpolation/) on every segment.

19. ★ In the lattice of exercise 12, let the centre control point move by $h > 0$ in $z$. Only the height changes, to $z'(x, y, z)$. Show that the Jacobian determinant of the deformation is $\partial z'/\partial z$, find its minimum over the closed cube, and find the values of $h$ for which the deformation does not fold the cube.

20. ★ The curve $(u - u^3/3, u^2)$, $0 \le u \le 1$, has polynomial speed. Find the speed and the length. Show that [Gauss-Legendre quadrature](/gauss-legendre-quadrature/) with 5 points gives the arc length table without error, and find the parameter of length 1 by Newton's method from $u = 1$, to six places.

21. ★ All control rotations of a [cumulative B-spline quaternion curve](/cumulative-b-spline-quaternion-curve/) turn about one fixed axis, by the angles $\theta_i$. Show that the curve turns about that axis by the uniform cubic [B-spline](/b-spline/) of the $\theta_i$. For the angles $0°, 90°, 90°, 0°$, find the angle at the two inner joints of the segment, and say whether the curve meets the $90°$ control rotations.

22. ★ Run one step of the [double reflection method](/double-reflection-method/) on the unit circle in the $xy$ plane from angle $0$ to angle $\pi/3$, with the start frame vector $r_0 = (-1, 0, 0)$, and then with $r_0 = (0, 0, 1)$. Show that the method is exact on a plane curve, and that the reflected tangent is $-t_1$ before the second reflection.
