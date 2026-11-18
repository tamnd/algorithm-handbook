1. ◦ Write the [skew-symmetric matrix](/skew-symmetric-matrix-of-a-vector/) $[\omega]$ of $\omega = (1, 0, 2)$ and compute $[\omega]x$ for $x = (3, 1, -1)$. Check that the result is $\omega \times x$, and that $[\omega]\omega = 0$.

2. ◦ A rotation matrix has trace $2$. What is its angle? What are the angles for trace $-1$ and trace $3$? Can a rotation matrix have trace $3.5$?

3. ◦ A [rigid body transformation](/rigid-body-transformation/) turns the plane $z = 0$ by $90^\circ$ about the vertical line through $q = (1, 2, 0)$. Write it as $x \mapsto R x + p$: give $R$ and $p$.

4. ◦ A robot in the plane has the [pose](/robot-pose/) $(1, 2, \pi)$. Its laser sees a landmark at $(2, 1)$ in the robot's own frame. Where is the landmark in the world frame?

5. ◦ Use the vector form of the [Rodrigues formula](/rodrigues-rotation-formula/) to rotate $x = (1, 0, 0)$ by $90^\circ$ about the unit axis $(0, 1, 1)/\sqrt2$.

6. ◦ Let $q_z$ and $q_x$ be the [unit quaternions](/unit-quaternion-rotation/) of the quarter turns about $z$ and about $x$. Compute the Hamilton product $q_z q_x$ and read off the axis and the angle of the rotation it stands for.

7. ◦ Show that with pitch $\theta = 90^\circ$ the [roll-pitch-yaw](/roll-pitch-yaw-angles/) matrix $R_z(\psi) R_y(\theta) R_x(\phi)$ depends on $\psi$ and $\phi$ only through $\psi - \phi$. Write the matrix in terms of $\psi - \phi$.

8. ◦ Write the [screw axis](/screw-motion/) $\mathcal S = (\omega, v)$ of a revolute joint that turns about the $z$ direction through the point $(0, 2, 0)$, and of a prismatic joint that slides along the $y$ axis.

9. ◦ Compute $x_1 \oplus x_2$ and $x_2 \oplus x_1$ for the planar poses $x_1 = (1, 0, \pi/2)$ and $x_2 = (0, 1, 0)$ with the [pose compounding operators](/pose-compounding-operators/). Describe each result in words.

10. • Prove that $[\omega]^3 = -|\omega|^2 [\omega]$ for every $\omega \in \mathbb{R}^3$. Use it to sum the series of $e^{[\hat\omega]\theta}$ for a unit vector $\hat\omega$ and obtain the Rodrigues formula.

11. • Compute $R_x(\pi/2) R_z(\pi/2)$ and use the [SO(3) logarithm](/so3-logarithm-map/) to find its axis and angle. Compare with $R_z(\pi/2) R_x(\pi/2)$, the rotation by $120^\circ$ about $(1, 1, 1)/\sqrt3$, and explain why the angles agree while the axes differ.

12. • A screw has its axis along the $z$ direction through the point $(1, 0, 0)$ and pitch $h = 1/2$. Write its screw axis $\mathcal S$ and compute $e^{[\mathcal S]\pi}$ with the [SE(3) exponential map](/se3-exponential-map/). Check the translation against the geometry: a half turn about the axis and a slide of $h\pi$ along it.

13. • A frame $\{b\}$ sits at $T_{sb}$ with $R = R_z(\pi/2)$ and $p = (1, 0, 0)$. A body moves with the body [twist](/rigid-body-twist/) $\mathcal V_b = (0, 0, 1, 1, 0, 0)$. Compute the space twist $\mathcal V_s = \operatorname{Ad}_{T_{sb}} \mathcal V_b$ with the [adjoint map](/adjoint-map-se3/), and describe the motion in words.

14. • By [Chasles' theorem](/chasles-theorem/), the motion with $R = R_z(\pi/2)$ and $p = (1, 1, 1)$ is a screw motion. Find the angle, the direction of the axis, a point on the axis, the slide along it and the pitch. Check your answer by computing $e^{[\mathcal S]\theta}$.

15. • Interpolate from the identity to the rotation by $120^\circ$ about $z$. Give the rotation angle at $t = 1/4$ and at $t = 1/2$ for [slerp](/spherical-linear-interpolation/) and for normalized linear interpolation of the quaternions. Which method keeps a constant angular rate?

16. • The rotation by $120^\circ$ about $z$ is stored as $q_1 = (-\tfrac12, 0, 0, -\tfrac{\sqrt3}{2})$. Slerp from $q_0 = (1, 0, 0, 0)$ to $q_1$ without the sign check. What rotation does the midpoint give, and through what total angle does the interpolation turn? What does the midpoint become with the sign check?

17. • Build the rotation by $150^\circ$ about the unit axis $(6, 2, 3)/7$ with the Rodrigues formula, then run [Shepperd's method](/shepperd-method/) on the matrix. Which of the four candidates is largest, and which quaternion results? Compare with $(\cos 75^\circ, \sin 75^\circ\,\hat\omega)$.

18. • Integrate the [quaternion kinematic equation](/quaternion-kinematic-equation/) $\dot q = \tfrac12 q\,(0, \omega_b)$ with constant $\omega_b = (0, 0, 1)$ rad/s by the explicit Euler method with step $h = 0.1$ s, from $q = (1, 0, 0, 0)$. Give the norm after one step and the angle after one step and normalization, against the exact $0.1$ rad. Show that each step multiplies the norm by $\sqrt{1 + h^2 |\omega_b|^2 / 4}$, and give the norm after $100$ steps without normalization.

19. • An aircraft has roll $\phi = 0$, pitch $\theta = 60^\circ$ and body rates $(p, q, r) = (0, 0, 1)$ rad/s, a pure turn about its own $z$ axis. Compute the roll, pitch and yaw rates. What happens to them as $\theta \to 90^\circ$, and why is this not a property of the motion?

20. • A robot drives $d = 10$ m straight ahead with a heading error $\theta \sim N(0, \sigma^2)$, $\sigma = 0.5$ rad, so that it ends at $(d\cos\theta, d\sin\theta)$. Compute the exact mean and variance of the $x$ coordinate and compare them with the first-order prediction of the [pose compounding operators](/pose-compounding-operators/). Check by a seeded simulation.

21. ★ Prove that there is no continuous map $s$ from SO(3) to the unit quaternions with $R(s(R)) = R$ for all $R$: the sign of a quaternion cannot be chosen continuously on the whole group. Use the loop $t \mapsto R_z(t)$, $t \in [0, 2\pi]$.

22. ★ Prove the closed form of the [SE(3) exponential map](/se3-exponential-map/): for $|\omega| = 1$ the translation is $G(\theta) v$ with $G(\theta) = I\theta + (1 - \cos\theta)[\omega] + (\theta - \sin\theta)[\omega]^2$. Then check that $G(\theta)^{-1} = I/\theta - \tfrac12 [\omega] + (1/\theta - \tfrac12 \cot(\theta/2))[\omega]^2$ for $0 < \theta < 2\pi$.

23. ★ Show that the map $c \mapsto R = (I - [c])^{-1}(I + [c])$ of the [Cayley parameters](/cayley-rotation-parameters/) is a bijection from $\mathbb{R}^3$ onto the rotations whose angle is less than $\pi$, with $c = \tan(\theta/2)\,\hat\omega$, and that its inverse is $c = \operatorname{vee}(R - R^{\mathsf T}) / (1 + \operatorname{tr} R)$.

24. ★ Prove that $T \operatorname{Exp}(\xi) T^{-1} = \operatorname{Exp}(\operatorname{Ad}_T \xi)$ for $T \in$ SE(3) and a twist $\xi$. Deduce that if $T = \bar T \operatorname{Exp}(\xi)$ with $\xi \sim N(0, \Sigma)$, as in [uncertainty on Lie groups](/uncertainty-on-lie-groups/), then $T = \operatorname{Exp}(\xi') \bar T$ with $\xi' \sim N(0, \operatorname{Ad}_{\bar T} \Sigma \operatorname{Ad}_{\bar T}^{\mathsf T})$.
