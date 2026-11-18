2. From $\operatorname{tr} R = 1 + 2\cos\theta$: trace $2$ gives $\cos\theta = \tfrac12$, so $\theta = 60^\circ$; trace $-1$ gives a half turn, $\theta = 180^\circ$; trace $3$ gives the identity. The trace of a rotation lies in $[-1, 3]$, so $3.5$ is impossible.

3. $R = R_z(\pi/2)$ and $p = (I - R)q$. Since $Rq = (-2, 1, 0)$, $p = (3, 1, 0)$. Check: $Rq + p = q$, so the point $q$ stays where it is.

4. The world point is $(1, 2) + R(\pi)(2, 1) = (1, 2) + (-2, -1) = (-1, 1)$.

6. $q_z = (\tfrac{1}{\sqrt2}, 0, 0, \tfrac{1}{\sqrt2})$ and $q_x = (\tfrac{1}{\sqrt2}, \tfrac{1}{\sqrt2}, 0, 0)$, so $q_z q_x = (\tfrac12, \tfrac12, \tfrac12, \tfrac12)$: $\cos(\theta/2) = \tfrac12$ gives $\theta = 120^\circ$, about the axis $(1, 1, 1)/\sqrt3$.

9. $x_1 \oplus x_2 = (0, 0, \pi/2)$: a step of $1$ along the robot's own $y$ axis, which after the quarter turn points along $-x$ in the world. $x_2 \oplus x_1 = (1, 1, \pi/2)$: the step comes first, in the world $y$ direction. The operator is not commutative.

11. $R_x(\pi/2) R_z(\pi/2)$ has trace $0$, so $\theta = 120^\circ$, and its skew part gives the axis $(1, -1, 1)/\sqrt3$. The two products are conjugate, $R_x R_z = R_x (R_z R_x) R_x^{-1}$, so they have the same angle, and the axis of the first is $R_x(\pi/2)$ applied to the axis of the second.

13. $\omega_s = R\omega_b = (0, 0, 1)$ and $v_s = p \times \omega_s + R v_b = (0, -1, 0) + (0, 1, 0) = 0$. So $\mathcal V_s = (0, 0, 1, 0, 0, 0)$: the body turns about the space $z$ axis through the space origin, and its origin, at distance $1$ from that axis, moves at speed $1$ along its own $x$ axis.

14. The angle is $\pi/2$ about the $z$ direction. The slide is $\hat\omega \cdot p = 1$, so the pitch is $1/(\pi/2) = 2/\pi \approx 0.637$. A point $q$ on the axis solves $(I - R)q = (1, 1, 0)$, which gives $q = (0, 1, 0)$. Then $\mathcal S = (0, 0, 1, 1, 0, 2/\pi)$, and $e^{[\mathcal S]\pi/2}$ returns $p = (1, 1, 1)$.

16. Without the check the angle between $q_0$ and $q_1$ in $\mathbb{R}^4$ is $120^\circ$, and the midpoint is $(q_0 + q_1)/|q_0 + q_1| = (\tfrac12, 0, 0, -\tfrac{\sqrt3}{2})$, the rotation by $120^\circ$ about $-z$. The path turns through $240^\circ$ in all, the long way round. With the check, $q_1$ becomes $-q_1$ and the midpoint is $(\cos 30^\circ, 0, 0, \sin 30^\circ)$, the rotation by $60^\circ$ about $z$.

17. The trace is $1 + 2\cos 150^\circ = 1 - \sqrt3 \approx -0.732$ and the diagonal is about $(0.505, -0.714, -0.523)$, so $r_{11}$ is the largest candidate and the method computes $x$ first: $4x^2 = 1 + 2r_{11} - \operatorname{tr} R \approx 2.742$. The result is $q \approx (0.25882, 0.82794, 0.27598, 0.41397)$, which is $(\cos 75^\circ, \sin 75^\circ\,\hat\omega)$.

18. One step gives $(1, 0, 0, 0.05)$, with norm $\sqrt{1.0025} \approx 1.0012492$; after normalization the angle is $2\arctan 0.05 \approx 0.0999168$ rad. The increment $\tfrac h2 q\,(0, \omega)$ is orthogonal to $q$ in $\mathbb{R}^4$ and has length $\tfrac h2 |q||\omega|$, which gives the factor. After $100$ steps the norm is $1.0025^{50} \approx 1.1330$.

20. $E[\cos\theta] = e^{-\sigma^2/2}$ and $E[\cos^2\theta] = (1 + e^{-2\sigma^2})/2$, so the mean of $x$ is $10 e^{-1/8} \approx 8.825$ and its variance is about $2.446$. To first order $x = 10$ with variance $0$, since $\partial x / \partial\theta = 0$ at $\theta = 0$. A simulation with seed $37$ and $200\,000$ samples gives the mean $8.822$.

21. Suppose $s$ exists. Then $t \mapsto s(R_z(t))$ is a continuous path of quaternions over the loop, closed since $R_z(0) = R_z(2\pi)$. But a continuous path of quaternions over $R_z(t)$ is $\pm(\cos\tfrac t2, 0, 0, \sin\tfrac t2)$ with one sign throughout, so it ends at the negative of its start. This contradicts $s(R_z(2\pi)) = s(R_z(0))$.

22. Expand $e^{[\mathcal S]\theta}$ as a series in the $4 \times 4$ matrix; the upper right block is $\sum_{k \ge 1} \frac{\theta^k}{k!} [\omega]^{k-1} v$. Reduce the powers with $[\omega]^3 = -[\omega]$ and sum the sine and cosine series. For the inverse, multiply the two matrices and use the same identity.

23. Write $C = [c]$. The matrices $I - C$ and $I + C$ commute, $(I - C)$ is invertible since $C$ has eigenvalues $0, \pm i|c|$, and $R^{\mathsf T} R = I$ follows from $C^{\mathsf T} = -C$. On the axis $\hat c$ the map is the identity; on the plane orthogonal to it, $C$ acts as $|c|$ times a quarter turn, and $(1 + i|c|)/(1 - i|c|) = e^{i\theta}$ with $|c| = \tan(\theta/2)$, which covers every $\theta \in (-\pi, \pi)$.

24. $T [\xi] T^{-1} = [\operatorname{Ad}_T \xi]$ is the definition of the adjoint, and $T e^{A} T^{-1} = e^{T A T^{-1}}$ holds for every matrix $A$. Then $\bar T \operatorname{Exp}(\xi) = \operatorname{Exp}(\operatorname{Ad}_{\bar T} \xi) \bar T$, and a linear map of a Gaussian vector is Gaussian with covariance $\operatorname{Ad}_{\bar T} \Sigma \operatorname{Ad}_{\bar T}^{\mathsf T}$.
