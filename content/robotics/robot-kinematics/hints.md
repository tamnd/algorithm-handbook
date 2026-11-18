1. (a) $N = 8$ links (base, platform and six leg links), $J = 9$ revolute joints, $m = 3$: $3(8 - 1 - 9) + 9 = 3$. (b) $N = 8$, $J = 9$ with $f = 1, 1, 3$ in each leg, $m = 6$: $6(8 - 1 - 9) + 15 = 3$.

2. The reachable set is the annulus $1 \le r \le 3$. The points $(0, 0)$ and $(0, 4)$ are out of reach, $(1, 0)$ and $(3, 0)$ lie on the boundary with one solution each, and $(2, 1)$, with $r = \sqrt5$, is inside with two.

3. $\cos\theta_2 = (r^2 - L_1^2 - L_2^2)/(2L_1L_2) = 0$, so $\theta_2 = \pm\pi/2$. With $\theta_2 = \pi/2$ the solution is $\theta_1 = 0$. With $\theta_2 = -\pi/2$, $\cos\theta_1 = 3/5$ and $\sin\theta_1 = 4/5$, so $\theta_1 \approx 53.13^\circ$.

4. $p = (\cos\theta_1\cos\theta_2, \sin\theta_1\cos\theta_2, 1 + \sin\theta_2)$. At $(0, 0)$ it is $(1, 0, 1)$; at $(90^\circ, 30^\circ)$ it is $(0, \sqrt3/2, 3/2)$.

6. The end is at $(2, 1)$ and $J = \begin{bmatrix} -1 & -1 \\ 2 & 0 \end{bmatrix}$, with $\det J = 2$. $JJ^{\mathsf T}$ has eigenvalues $3 \pm \sqrt5$, so $\sigma_1 \approx 2.2882$ and $\sigma_2 \approx 0.8740$; $w = \sigma_1\sigma_2 = 2 = L_1L_2|\sin\theta_2|$, and $\sigma_1/\sigma_2 = (3 + \sqrt5)/2 \approx 2.618$.

7. $\tau = J^{\mathsf T}F = (20, 0)$ N m. The second link points straight up, along the force, so the force has no moment about joint 2; about joint 1 its lever arm is $2$ m.

12. $J = \begin{bmatrix} -2 & -2 & -1 \\ 1 & 0 & 0 \end{bmatrix}$, $JJ^{\mathsf T} = \begin{bmatrix} 9 & -2 \\ -2 & 1 \end{bmatrix}$ with determinant $5$, and $J^{+}v = (1, -\tfrac45, -\tfrac25)$. The null space is spanned by $(0, 1, -2)/\sqrt5$, and its dot product with $J^{+}v$ is $-\tfrac45 + \tfrac45 = 0$.

13. With $J = \begin{bmatrix} -1 & -1 \\ 1 & 0 \end{bmatrix}$: the exact step is $(0, -\tfrac1{10})$, residual $0$; the damped step is $(-\tfrac2{145}, -\tfrac2{29})$, residual about $0.0221$; the transpose gain is $\alpha = \tfrac25$, the step $(-\tfrac1{25}, -\tfrac1{25})$ and the residual $\sqrt5/50 \approx 0.0447$.

15. Cyclic coordinate descent turns joint 2 by about $123.69^\circ$ and then joint 1 by about $28.15^\circ$; the end is at $(0, 0.9437)$, at distance $0.5563$ from the target. One FABRIK iteration leaves the end at distance about $0.0294$.

17. With $N = 4$ and $J = 4$ joints of freedoms $1, 3, 3, 1$: $6(4 - 1 - 4) + 8 = 2$. The coupler can spin about the line through its two ball joints without moving anything else, so the useful count is $1$.

19. Set the gradient to zero: $(J^{\mathsf T}J + \lambda^2 I)\Delta\theta = J^{\mathsf T}e$, and $J^{\mathsf T}(JJ^{\mathsf T} + \lambda^2 I)^{-1} = (J^{\mathsf T}J + \lambda^2 I)^{-1}J^{\mathsf T}$. In the singular value basis each component of the step is $\sigma e_i/(\sigma^2 + \lambda^2)$, and $\sigma/(\sigma^2 + \lambda^2) \le 1/(2\lambda)$ with equality at $\sigma = \lambda$. Equality holds when $e$ lies along left singular vectors whose singular value equals $\lambda$.

20. The rank drops exactly when the three vectors from the joints to the end are parallel. The vector from joint 3 is link 3, of length $1$, so link 2 must be parallel to link 3 and then link 1 to both. The singular set is $\theta_2, \theta_3 \in \{0, \pi\}$, with any $\theta_1$: four families.

21. Near the solution the error map is $e \mapsto (I - \alpha JJ^{\mathsf T})e$, and $JJ^{\mathsf T}$ has eigenvalues $(3 \pm \sqrt5)/2$. Local convergence needs $0 < \alpha < 2/\lambda_{\max} = 3 - \sqrt5 \approx 0.764$; the best gain is $2/(\lambda_{\max} + \lambda_{\min}) = 2/3$, with rate $(\lambda_{\max} - \lambda_{\min})/(\lambda_{\max} + \lambda_{\min}) = \sqrt5/3 \approx 0.745$.

22. In the frame of link 1, $JJ^{\mathsf T}$ is a multiple of $I$ exactly when the two columns are orthogonal and of equal length. This gives $L_2/L_1 = 1/\sqrt2$ and $\theta_2 = \pm 3\pi/4$, and then $w = L_1L_2\sin(3\pi/4) = L_1^2/2$.

23. With $\theta_2$ fixed, $p = R(\theta_1)p_0$ where $p_0$ depends only on the four parameters; every such pose measures the same two numbers $p_0$, so the stacked identification Jacobian has rank $2$. The poses $(0, 0)$ and $(0, \pi/2)$ give a $4 \times 4$ Jacobian of rank $4$.

24. Write the wrist center as $p = R_1(\theta_1)(a + R_2(\theta_2) f(\theta_3))$ in Denavit-Hartenberg form, where $f$ is linear in $\cos\theta_3$ and $\sin\theta_3$. The squared distance $|p|^2$ and the component of $p$ along axis 1 do not depend on $\theta_1$. For a general arm ($a_1 \ne 0$, $\sin\alpha_1 \ne 0$) they give $f_x\cos\theta_2 - f_y\sin\theta_2 = g_1$ and $f_x\sin\theta_2 + f_y\cos\theta_2 = g_2$, with $g_1, g_2$ also linear in $\cos\theta_3, \sin\theta_3$. Squaring and adding removes $\theta_2$: $f_x^2 + f_y^2 = g_1^2 + g_2^2$ is quadratic in $\cos\theta_3, \sin\theta_3$, so of degree at most $4$ in $t$ after multiplying by $(1 + t^2)^2$. Each root then gives one $\theta_2$ from the two linear equations and one $\theta_1$.
