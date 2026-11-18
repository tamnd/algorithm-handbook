1. ◦ A [differential drive](/differential-drive-model/) robot has wheel radius $r = 0.04$ m and track width $2d = 0.36$ m. Its wheels turn at $\omega_R = 10$ and $\omega_L = 6$ rad/s. Find $v$, $\omega$ and the radius of the circle it drives on, and its pose after $2$ s from $(0, 0, 0)$.

2. ◦ A car of wheelbase $L = 2.5$ m has a largest steering angle of $30°$. In the [kinematic bicycle model](/kinematic-bicycle-model/), find the smallest turning radius of the rear axle center and of the front axle center. At $v = 8$ m/s and $\delta = 0.04$ rad, find the yaw rate and the lateral acceleration.

3. ◦ A robot has four mecanum wheels of radius $r = 0.05$ m at $(\pm 0.2, \pm 0.15)$ m, in the layout of the [omnidirectional kinematics](/omnidirectional-robot-kinematics/) entry, so $c = 0.35$ m. Find the wheel speeds for the twists $(v_x, v_y, \omega) = (0.4, 0, 0.5)$, $(0, 0.3, 0)$ and $(0.2, -0.2, 0)$, and check the consistency condition for each.

4. ◦ In the vehicle frame of a car with wheelbase $L = 2.7$ m, the [pure pursuit](/pure-pursuit/) goal point is $(4, 1)$ m. Find the look-ahead distance, the curvature of the arc, its radius and the steering angle.

5. ◦ A hexapod stands on three feet at $(0.25, 0.15)$, $(0.25, -0.15)$ and $(-0.25, 0)$ m, with mass $12$ kg and its center of mass above $(0.05, 0.02)$. Find the three normal forces and the static stability margin of its [support polygon](/support-polygon/).

6. ◦ The center of mass of a robot is at constant height $0.85$ m, above the ankle. The heel is $0.06$ m behind the ankle and the toe $0.14$ m ahead. Using the point-mass formula of the [zero moment point](/zero-moment-point/), find the largest forward acceleration and the largest braking the foot allows without tipping, and the ZMP for a forward acceleration of $0.5$ m/s².

7. ◦ A robot modeled by the LIPM has $z_0 = 0.9$ m, and its sole reaches $0.12$ m ahead of the center of mass. A push gives it a forward speed of $0.3$ m/s; a second push gives $0.45$ m/s. For each, find the [capture point](/capture-point/) and say whether the ankle can stop the robot or it must step.

8. ◦ A quadrotor in the "+" layout of the [quadrotor dynamics](/quadrotor-dynamics/) entry has $m = 0.8$ kg, $l = 0.2$ m and $c = 0.02$ m. Find the rotor thrusts at hover, the total thrust needed to hold the height at a tilt of $15°$ and the horizontal acceleration that tilt gives. Then find the four thrusts for $f = mg$, $M_1 = 0.06$ N m, $M_2 = 0$ and $M_3 = -0.004$ N m.

9. ◦ A $12 \times 6$ room has two disjoint convex obstacles in general position. In layout (a), obstacle $A$ spans $x$ from $2$ to $5$ and $B$ spans $x$ from $7$ to $9$. In layout (b), $B$ spans $x$ from $4$ to $8$ and lies above $A$. For each layout, list the cells of the [boustrophedon cell decomposition](/boustrophedon-cell-decomposition/) with their $x$ ranges, and count the lanes for a tool of width $w = 1$ in layout (a).

10. ◦ A rectangle $[0, 6] \times [0, 2]$ is to be milled by an axis-parallel unit square tool that stays inside it. Use the length bound of [coverage path planning](/coverage-path-planning/) to give the shortest possible length, and compare a path with lanes along the long side with one with lanes along the short side.

11. ◦ Three candidate views $A$, $B$ and $C$ in [next-best-view planning](/next-best-view-planning/) would see $15$, $24$ and $40$ unknown cells, at travel costs of $2$, $4$ and $9$ m. Which view wins with the score $G - \lambda c$ for $\lambda = 0$, $2$ and $5$, and which with $G/c$?

12. • Decide which of these [Pfaffian constraints](/pfaffian-constraint/) in $(x, y, z)$ are holonomic, and give the integral of each holonomic one: (a) $y\dot x + x\dot y = 0$; (b) $\dot z - y\dot x = 0$; (c) $\dot z - y\dot x - x\dot y = 0$.

13. • A car runs the [Stanley controller](/stanley-controller/) on a straight path with $k = 2$ and $u = 4$ m/s, starting with a cross-track error of $3$ m and no heading error. Using the closed-loop equation $\dot e = -ke/\sqrt{1 + (ke/u)^2}$, find the time until the error is $0.5$ m, and compare it with the time the linear law $\dot e = -ke$ would need.

14. • With $\rho = 1$, compute the six [Dubins](/dubins-path/) words from $(0, 0, 0)$ to $(3, 0, \pi)$. Which words exist, which one is shortest, and why can the CCC words exist here?

15. • Find a [Reeds-Shepp](/reeds-shepp-path/) path of length $\pi$ with three arcs of radius $1$ that takes the car from $(0, 0, 0)$ to $(0, 0, \pi)$, and check its end pose.

16. • A [DWA](/dynamic-window-approach/) robot drives straight at $v_0 = 0.7$ m/s with $a_v = 0.4$ m/s² and $\Delta t = 0.2$ s, and an obstacle leaves a free distance of $0.6$ m ahead. Find the window of speeds, the stopping distance of the straight pairs $v = 0.62, 0.66, 0.70, 0.74, 0.78$, and which are admissible. What does the continuous test $v \le \sqrt{2\,\mathrm{dist}\,a_v}$ accept?

17. • A robot at the origin and a static obstacle at $(4, 0)$ have radii that add up to $r = 1$. Find the half-angle of the [velocity obstacle](/velocity-obstacle/). Which of $(1, 0.2)$, $(1, 0.26)$ and $(1, 0.3)$ lie in it, and when does the first one touch? Is it in $VO^\tau$ for $\tau = 3$ s?

18. • In the [LIPM](/linear-inverted-pendulum-model/) with $z_0 = 0.8$ m and the foot at $p = 0$, the center of mass is at $x_0 = -0.1$ m. Find the orbital energy and the outcome for $\dot x_0 = 0.3$ and for $\dot x_0 = 0.4$ m/s, and the smallest speed that brings the mass over the foot.

19. • A rectangular foot has $X = 0.12$ m, $Y = 0.06$ m and $\mu = 0.6$. Using the closed form of the [contact wrench cone](/contact-wrench-cone/), find the bounds on $\tau_x$, $\tau_y$ and $\tau_z$ for $f = (0, 0, 600)$ N with $\tau_x = \tau_y = 0$, and the yaw bounds for $f = (60, 30, 600)$ N with $\tau = (6, -12, \tau_z)$ N m. Where is the center of pressure in the second case?

20. • For the cart-table model of [ZMP preview control](/zmp-preview-control/), $p = c - h\ddot c$ with $h = z_c/g$, find the transfer function from $c$ to $p$ and its zeros for $z_c = 0.8$ m. Explain why the ZMP must first move the wrong way when the center of mass starts to move.

21. • A rimless wheel of [passive dynamic walking](/passive-dynamic-walking/) has $10$ spokes of length $l = 1$ m and rolls down a slope of $\gamma = 0.1$ rad. Find the fixed point $\omega^-$ of its stride map, the speed $\omega^+$ after impact, the factor by which the error in $u = (\omega^-)^2$ shrinks per step, and check that the hub passes over each spoke.

22. • Solve by [hierarchical quadratic programming](/hierarchical-quadratic-programming/), with $x = (x_1, x_2)$: level 1, $x_2 \le 0.5$; level 2, $x_1 + 2x_2 = 2$; level 3, $x_1 = 0$ and $x_2 = 0$. Give $x$ and the residual of each level.

23. • A quadrotor of mass $1$ kg flies on the circle $x(t) = (2\cos t, 2\sin t, h)$. Using [differential flatness](/quadrotor-differential-flatness/), find the thrust and the tilt of $b_3$ from the vertical. For which paths does condition (C1) fail?

24. • In [geometric tracking control](/geometric-tracking-control-se3/), let $R_d = I$ and let $R$ be a rotation by $\varphi$ about $b_2$. Compute $e_R$ and $\Psi$. How does the size of the proportional moment $k_R|e_R|$ change from $0$ to $180$ degrees, and what does this say about the 90-degree and 180-degree conditions of the theorem?

25. ★ Show that for the differential drive with wheel angles $\varphi_R$ and $\varphi_L$ in the configuration $(x, y, \theta, \varphi_R, \varphi_L)$, the quantity $\theta - r(\varphi_R - \varphi_L)/(2d)$ is constant, and that the reachable set from a configuration is the four-dimensional level set of this quantity.

26. ★ With the steering angle as a state and its rate as an input, the [kinematic bicycle](/kinematic-bicycle-model/) is $\dot q = v\,g_1(q) + u\,g_2(q)$ with $q = (x, y, \theta, \delta)$, $g_1 = (\cos\theta, \sin\theta, \tan\delta/L, 0)$ and $g_2 = (0, 0, 0, 1)$. Compute $[g_1, g_2]$ and $[g_1, [g_1, g_2]]$, show that the four fields span $\mathbb{R}^4$ for $|\delta| < \pi/2$, and say what this gives when the car may reverse and when it may not.

27. ★ Show that the Dubins length is not symmetric by computing it from $(0, 0, 0)$ to $(1, 0, 0)$ and back, with $\rho = 1$. Then show that the Reeds-Shepp length is symmetric.

28. ★ A symmetric LIPM gait with $z_0 = 0.8$ m has step length $s = 0.3$ m and step time $T = 0.5$ s: each step starts with the center of mass at $-s/2$ from the new foot and ends at $+s/2$ with the same speed. Show that the speed at the step change is $v_0 = \omega (s/2)\coth(\omega T/2)$, compute it, and find the speed over the foot.

29. ★ For a vertical hop of the [spring-loaded inverted pendulum](/spring-loaded-inverted-pendulum/) with touchdown speed $v$, derive the stance time $t_s = (2\pi - 2\beta)/\omega_s$ with $\beta = \operatorname{atan2}(v/\omega_s, mg/k)$. Evaluate it, the largest compression and the peak force for $m = 70$ kg, $k = 15000$ N/m, $\ell_0 = 1$ m and a drop from an apex of $1.05$ m.
