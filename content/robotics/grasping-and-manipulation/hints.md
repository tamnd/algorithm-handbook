1. The block stays put up to $\arctan 0.3 = 16.70°$. The force has tangential size $\sqrt{1 + 1} = 1.414$, and the cone allows $\mu f_n = 1.2$. Since $1.414 > 1.2$, the force lies outside the cone and the contact slips.

5. The two springs act in series, so the rest force is $k_e K_d / (k_e + K_d) \cdot 0.01 = 4.545$ N. As $k_e \to \infty$ the force tends to $K_d \cdot 0.01 = 5$ N.

7. For $x = 0.3$ the edge moments are $0.8$ and $-0.2$, so the edges disagree and the pushing direction decides. The direction $(0, 1)$ has moment $0.3$, so the object turns counterclockwise; $(-1, 1)$ has moment $-0.7$, so it turns clockwise. For $x = 0.6$ both edges give positive moments ($1.1$ and $0.1$), so the object turns counterclockwise for every push.

8. Here $\lambda = l/(2\mu r) = 0.75$. The peg slides while $M < r F_z(\lambda + \mu(1 + \lambda) u)$ with $u = F_x / F_z$. This gives 75, 80.25 and 69.75 N·mm. Wedging needs $l \le 2\mu r = 2$ mm, so it is possible at this depth.

10. At rest the controller torque equals the gravity torque, so $-K_p q = 9.81 \cos q$. Solve by fixed-point iteration. The rest angles are $-0.1926$ rad for $K_p = 50$ and $-0.0490$ rad for $K_p = 200$. The error shrinks like $1/K_p$ but never vanishes. With gravity compensation it is zero for every $K_p > 0$.

13. The line between the fingers has slope $(y_2 - y_1)/4$, and it lies inside both cones when this is below $\mu = 1/2$ in size. So the pair is in closure exactly when $\lvert y_1 - y_2\rvert < 2$. The largest difference within two copies of $[a, a + L]$ is $L$, so every $L < 2$ works and $L = 2$ does not.

14. At $t = 0$: $\tilde q = 0.2$, $\dot q_r = 0.5 - 1 = -0.5$, $\ddot q_r = 0 - 5(0 - 0.5) = 2.5$ and $s = 0.5$. Then $Y = (2.5, 0.98007)$, so $\tau = 1.25 + 4.807 - 10 = -3.943$, and $\dot{\hat\pi} = -(1 \cdot 2.5 \cdot 0.5,\ 20 \cdot 0.98007 \cdot 0.5) = (-1.25, -9.80)$.

17. Put $u = \pi/2 - q$. The equilibria satisfy $K_p u = 9.81 \sin u$. For $u \ne 0$, $\lvert\sin u\rvert < \lvert u\rvert$, so there is no other root when $K_p \ge 9.81$. For $K_p = 5$ the roots are $u = 0$ and $u = \pm 1.8731$, that is $q = \pi/2$, $-0.3023$ and $3.4439$. An equilibrium is stable when $K_p - 9.81 \sin q > 0$. This fails at $q = \pi/2$, so the goal is unstable, and holds at the other two, where $\sin q < 0$.

18. A breadth-first search over subsets of states finds the word $baaabaaab$, of length $9 = (4 - 1)^2$. This is the Černý bound, and it shows that a reset word can be quadratic in the number of states.

19. One squeeze leaves two states, $0$ and $\pi/2$, since both have basins of positive measure. A second squeeze at angle $\varphi$ sends both states to the same orientation when $\lvert\varphi\rvert < 1.2490$ and $\lvert\pi/2 - \varphi\rvert < 1.2490$, that is $0.3218 < \varphi < 1.2490$. The middle choice $\varphi = \pi/4$ leaves a margin of $0.4636$ rad, about $26.6°$, on each side.

20. Use $a \dot s = \tau - a \ddot q_r - b \cos q = Y\tilde\pi - K_D s$. Then $\dot V = s(Y\tilde\pi - K_D s) + \tilde\pi^\top \Gamma^{-1} \dot{\hat\pi} = -K_D s^2$. Barbalat's lemma gives $s \to 0$, and then $\tilde q \to 0$. The parameters converge only if the trajectory is persistently exciting.
