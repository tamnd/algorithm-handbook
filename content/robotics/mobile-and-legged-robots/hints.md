1. $v = 0.04 \cdot 16/2 = 0.32$ m/s and $\omega = 0.04 \cdot 4/0.36 = 0.4444$ rad/s, so the radius is $v/\omega = 0.72$ m. After $2$ s the heading is $0.8889$ rad, and the exact arc gives $x = 0.72\sin 0.8889 = 0.5590$ m and $y = 0.72(1 - \cos 0.8889) = 0.2662$ m.

2. The rear axle center turns on $L/\tan 30° = 4.330$ m and the front axle center on $L/\sin 30° = 5.000$ m. At $v = 8$ m/s and $\delta = 0.04$ rad, the yaw rate is $8\tan 0.04/2.5 = 0.1281$ rad/s, the radius is $62.47$ m and the lateral acceleration is $v\dot\theta = 1.025$ m/s².

3. In the order FL, FR, RL, RR: $(4.5, 11.5, 4.5, 11.5)$, $(-6, 6, 6, -6)$ and $(8, 0, 0, 8)$ rad/s. In each case $u_{FL} + u_{FR} - u_{RL} - u_{RR} = 0$. The diagonal motion uses only two wheels.

5. The center of mass is the convex combination with weights $11/30$, $7/30$ and $2/5$ of the three feet, so the normal forces are $43.16$, $27.47$ and $47.09$ N. The distances to the three edges are $0.2$, $0.1054$ and $0.0670$ m, so the margin is $0.067$ m, set by the edge from $(-0.25, 0)$ to $(0.25, 0.15)$.

7. $\omega = \sqrt{9.81/0.9} = 3.3015$ 1/s. For $0.3$ m/s, $\xi = 0.0909$ m, inside the sole, so the ankle can stop the robot. For $0.45$ m/s, $\xi = 0.1363$ m, beyond the toe, so the robot must step.

9. Layout (a) has seven cells: $[0, 2]$; below and above $A$ on $[2, 5]$; $[5, 7]$; below and above $B$ on $[7, 9]$; $[9, 12]$. With $w = 1$ they take $2 + 3 + 3 + 2 + 2 + 2 + 3 = 17$ lanes. Layout (b) also has seven cells: $[0, 2]$; below $A$ on $[2, 5]$; above $A$ on $[2, 4]$; between $A$ and $B$ on $[4, 5]$; above $B$ on $[4, 8]$; below $B$ on $[5, 8]$; $[8, 12]$. The count $1 + 3k$ does not depend on whether the $x$ ranges overlap.

11. With $\lambda = 0$ the scores are $15, 24, 40$ and $C$ wins; with $\lambda = 2$ they are $11, 16, 22$ and $C$ still wins; with $\lambda = 5$ they are $5, 4, -5$ and $A$ wins. The ratios are $7.5$, $6$ and $4.44$, so $G/c$ picks $A$.

12. In three variables, a constraint $a \cdot \dot q = 0$ is integrable exactly when $a \cdot (\nabla \times a) = 0$. (a) Holonomic: it says $\frac{d}{dt}(xy) = 0$. (b) $a = (-y, 0, 1)$ has curl $(0, 0, 1)$ and $a \cdot \nabla \times a = 1$, so it is nonholonomic. (c) Holonomic: $z - xy$ is constant.

13. Put $s = ke/u$. Then $dt = -\sqrt{1 + s^2}\,ds/(ks)$, which integrates with the function $F$ of the Stanley entry; from $s = 1.5$ to $s = 0.25$ it gives $1.121$ s. The linear law needs $\ln 6/2 = 0.896$ s; the arctangent saturates the steering when the error is large.

14. Here $d = 3 < 4$, so all six words exist. LSR and RSL tie at $6.837$, with pieces $0.730$, $2.236$ and $3.871$. RLR and LRL have $11.216$, and LSL and RSR have $13.030$. The ties come from the mirror symmetry of the goal about the $x$ axis.

16. The window is $[0.62, 0.78]$ m/s. The braking cycles are $8, 9, 9, 10, 10$, and the stopping distances are $0.558$, $0.660$, $0.700$, $0.814$ and $0.858$ m, so only $0.62$ is admissible. The continuous test accepts $v \le 0.693$, so it also accepts $0.66$, which needs $0.66$ m.

18. $\omega = 3.5018$ 1/s and $E = \dot x_0^2/2 - \omega^2 x_0^2/2$. For $0.3$ m/s, $E = -0.0163$: the mass stops at $x = -0.0516$ m and falls back. For $0.4$ m/s, $E = 0.0187$: it passes over the foot at $\sqrt{2E} = 0.193$ m/s. The threshold is $E = 0$, at $\dot x_0 = 0.350$ m/s.

21. Take $\alpha = \pi/10$. The fixed point of $u' = \cos^2(2\alpha)u + (4g/l)\sin\alpha\sin\gamma$ gives $\omega^- = 1.8719$ rad/s and $\omega^+ = \cos(2\alpha)\omega^- = 1.5144$ rad/s. The error in $u$ shrinks by $\cos^2(\pi/5) = 0.6545$ per step. The hub passes, since $(\omega^+)^2 = 2.293$ exceeds $(2g/l)(1 - \cos(\alpha - \gamma)) = 0.448$.

25. The heading equation $\dot\theta = r(\dot\varphi_R - \dot\varphi_L)/(2d)$ is the derivative of a function of the configuration, so it integrates. On a level set, use $(x, y, \theta, \varphi_R)$ as coordinates; the two wheel motions and their brackets span all four directions, and the Chow-Rashevskii theorem gives the whole level set.

26. With $[f, g] = Dg\,f - Df\,g$, $[g_1, g_2] = (0, 0, -\sec^2\delta/L, 0)$ and $[g_1, [g_1, g_2]] = (-\sin\theta\sec^2\delta/L, \cos\theta\sec^2\delta/L, 0, 0)$. The determinant of the four fields has absolute value $\sec^4\delta/L^2 \neq 0$. With reverse the system is driftless with $v$ of both signs, and the rank condition gives small-time local controllability. With $v \ge 0$ only, the rank test does not give it, and the entry states that it fails.

28. Solve $x(T) = s/2$ from $x(0) = -s/2$ with the closed form of the LIPM; symmetry then gives $\dot x(T) = v_0$. With $\omega = 3.5018$ 1/s, $v_0 = 0.746$ m/s. The orbital energy is $0.1403$ m²/s², so the speed over the foot is $0.530$ m/s.
