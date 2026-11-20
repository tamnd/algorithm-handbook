1. $u = \pi\sin\pi x\cos\pi y$ and $v = -\pi\cos\pi x\sin\pi y$, so $\omega = 2\pi^2\sin\pi x\sin\pi y = 2\pi^2\psi$. Since $\psi = 0$ on the boundary, the normal velocity vanishes on all four sides. The tangential velocity does not; on $y = 0$ it is $u = \pi\sin\pi x$. So the field satisfies no penetration but not no slip.

2. $L/\eta = 10^{6 \cdot 3/4} \approx 31\,600$, the time ratio is $Re^{1/2} = 1000$, and $(L/\eta)^3 \approx 3.2 \times 10^{13}$ points.

6. $\nu = (0.8 - 0.5)/3 = 0.1$; $\tau = 0.5 + 3 \cdot 0.05 = 0.65$; $\mathrm{Ma} = 0.1\sqrt3 \approx 0.173$. The physical viscosity is $\nu\,\Delta x^2/\Delta t$, so $\Delta t = 0.1 \cdot (10^{-3})^2/10^{-6} = 0.1$ s.

7. For $\beta \le 1$ the liquid is a triangle with legs $\beta$ and $\beta/3$, of area $\beta^2/6$, so $f = 0.1$ gives $\beta = \sqrt{0.6} \approx 0.775$. For $1 \le \beta \le 3$ it is a trapezoid of area $(\beta - \frac12)/3$, so $f = 0.4$ gives $\beta = 1.7$, and the line meets $x = 0$ at $y \approx 0.567$ and $x = 1$ at $y \approx 0.233$.

8. The offsets $(X - x_k)/h$ are $1.3$, $0.3$, $-0.7$ and $-1.7$, and the weights are about $0.13044$, $0.46956$, $0.36956$ and $0.03044$. The first moment is $-1.3(0.13044) - 0.3(0.46956) + 0.7(0.36956) + 1.7(0.03044) = 0$ to rounding. On a node the weights are $\frac14, \frac12, \frac14$ and 0, with squares summing to $\frac1{16} + \frac14 + \frac1{16} = \frac38$.

9. $W(0) = \frac23$, $W(1) = \frac16$ and $W(2) = 0$. The end particle has density $\frac23 + \frac16 = \frac56$; the particle at $x = 1$ has $\frac23 + 2 \cdot \frac16 = 1$, the bulk value. Only the neighbor at $x = 1$ contributes to the derivative, with $\partial_xW = \frac12$, so the estimate is $\frac12$ instead of 1. SPH is not even exact for constants and linear fields near a free surface.

10. The divergence of $u^*$ is $(1, -1, 0, 0)$ in cells $(00, 10, 01, 11)$. The solution is $p = (0, \frac34, \frac14, \frac12)$, and $Gp = (\frac34, \frac14, \frac14, -\frac14)$ on $(u_{10}, u_{11}, v_{01}, v_{11})$. The projected velocity $(\frac14, -\frac14, -\frac14, \frac14)$ circulates around the box with zero divergence in every cell, and the energy falls from 1 to $\frac14$.

13. $\mu_{\max} = 400 + 400 = 800$. The condition $800\Delta\tau^2 + 16\Delta\tau < 4$ gives $\Delta\tau < 0.0614$, smaller than the acoustic limit $2/\sqrt{800} \approx 0.0707$ and far below the viscous limit $0.25$.

15. $2\nu C\varepsilon^{2/3} \cdot \frac34 k_d^{4/3} = \varepsilon$ gives $k_d^{4/3} = \frac{2}{3C}\,\varepsilon^{1/3}\nu^{-1}$, which is $\frac{2}{3C}\eta^{-4/3}$. So $k_d\eta = (2/(3C))^{3/4} \approx 0.544$ for $C = 1.5$.

18. Start from $u_\tau = 0.1$ and iterate $u_\tau \leftarrow U/(\ln(yu_\tau/\nu)/\kappa + B)$. It converges to $u_\tau \approx 0.0984$ m/s, so $y^+ \approx 492$ and $\tau_w = \rho u_\tau^2 \approx 9.69$ Pa. The usual range is $30 \lesssim y^+ \lesssim 300$, so the first cell is too far from the wall.

19. After the first step the node to the right holds only a right-moving population of $\frac16$. Collision with $1/\tau = \frac43$ overshoots its equilibrium $\frac1{36}$. The condition $\tau > \frac12$ is what makes the diffusivity positive; it does not keep every population nonnegative.

21. Along $x$, the rest population and the two with $c_i$ perpendicular to $u$ are proportional to $1 - \frac32|u|^2$; they reach zero at $|u| = \sqrt{2/3} \approx 0.816$, and the others stay positive. Along the diagonal, write $u = (a, a)$; the populations with $c_i = (-1, 0)$ and $(0, -1)$ are proportional to $1 - 3a + \frac32a^2$, which vanishes at $a = 1 - 1/\sqrt3 \approx 0.423$, that is $|u| \approx 0.598$.

22. For bilinear $u$, $\int_K\partial_xu\,dx$ over a square equals $\frac h2$ times the sum of the two right-corner values minus the two left-corner values. An interior node is a right corner of two squares and a left corner of the two others, and the checkerboard signs of these four squares cancel. The same holds for $\partial_yv$, so $p$ lies in the kernel of $B^{\mathsf T}$ and the discrete inf-sup constant is 0.

23. Differentiate both forms: $y\,dU/dy = u_\tau y^+f'(y^+) = -u_\tau\eta g'(\eta)$ with $\eta = y/\delta = y^+/Re_\tau$. For fixed $y^+$ and varying $Re_\tau$ the left side is fixed while $\eta$ moves, so both sides equal a constant, written $u_\tau/\kappa$. Integrating gives the log law; the argument fixes its form but not the values of $\kappa$ and $B$, which come from measurement.

24. Only four sums are distinct: $w_0 + 4w_1 + 4w_2 = 1$, $\sum w_ic_{ix}^2 = 2w_1 + 4w_2 = c_s^2$, $\sum w_ic_{ix}^4 = 2w_1 + 4w_2 = 3c_s^4$ and $\sum w_ic_{ix}^2c_{iy}^2 = 4w_2 = c_s^4$. Then $c_s^2 = \frac13$, $w_2 = \frac1{36}$, $w_1 = \frac19$ and $w_0 = \frac49$, uniquely. The fourth moments enter the momentum flux of the first-order term, and isotropy there makes the viscous stress that of an isotropic Newtonian fluid.

25. Let $j = f_+ - f_-$. Collision keeps $\rho$ and multiplies $j$ by $1 - 1/\tau$; streaming then moves $f_\pm$ by $\pm1$. The Chapman-Enskog argument, as in the entry for D1Q3, gives $D = (\tau - \frac12)c_s^2$ with $c_s^2 = \sum_iw_ic_i^2 = 1$. At $\tau = 1$ every population is reset to $\rho/2$, so each unit of mass takes an independent step of $\pm1$, and the variance grows by 1 $= 2D$ per step.

26. The force on $i$ from $j$ is $-m_im_j\bigl(p_i/\rho_i^2 + p_j/\rho_j^2\bigr)F_{ij}(x_i - x_j)$, which changes sign when $i$ and $j$ swap, so the pair forces cancel in $\sum m_i\dot v_i$. For angular momentum, $\frac{d}{dt}\sum m_ix_i \times v_i = \sum m_ix_i \times \dot v_i$; pair the terms $(i, j)$ and $(j, i)$ to get $(x_i - x_j) \times (\text{a multiple of } x_i - x_j) = 0$.
