1. $\nu = (0.8 - 0.5)/3 = 0.1$; $\tau = 0.5 + 3 \cdot 0.05 = 0.65$; $\mathrm{Ma} = 0.1\sqrt3 \approx 0.173$. The physical viscosity is $\nu \Delta x^2 / \Delta t$, so $\Delta t = 0.1 \cdot (10^{-3})^2 / 10^{-6} = 0.1$ s.

3. $f_0 = 397/900 \approx 0.44111$, $f_1 = f_2 = 923/7200 \approx 0.12819$, $f_3 = f_4 = 683/7200 \approx 0.09486$, $f_5 = 107/2880 \approx 0.03715$, $f_6 = f_8 = 397/14400 \approx 0.02757$, $f_7 = 59/2880 \approx 0.02049$. In $x$: $f_1 - f_3 + f_5 - f_6 - f_7 + f_8 = 0.05$.

7. After the first step the node to the right holds only a right-moving population of $\frac16$. Collision with $1/\tau = \frac43$ overshoots its equilibrium $\frac1{36}$. The condition $\tau > \frac12$ is what makes the viscosity, or here the diffusivity, positive; it does not keep every population nonnegative.

9. The rate is $2 \cdot 0.1 \cdot (2\pi/32)^2 \approx 0.0077106$ per step, so the amplitude halves after about 89.9 steps and the energy, which decays at twice the rate, after about 44.9. Over $N^2/8$ steps the exponent is $2 \cdot \frac{1}{10} \cdot \frac{4\pi^2}{N^2} \cdot \frac{N^2}{8} = \frac{\pi^2}{10}$.

10. Along $x$, $f_0$, $f_2$ and $f_4$ are proportional to $1 - \frac32 |u|^2$, and the others stay positive. Along the diagonal, write $u = (a, a)$ and look at the populations with $c_i \cdot u = -a$.

11. Expand with Taylor's theorem and use $u_{tt} = D^2 u_{xxxx}$ for a solution of the heat equation. At $\tau = 1$ the scheme has $\mu = \frac16$, and in diffusive scaling $\Delta t = O(\Delta x^2)$.

12. The kernel is $W(r, h) = B(r/h)/h$, where $B$ is the cubic B-spline with knots at $-2, \ldots, 2$, and integer shifts of $B$ sum to 1. With $h = m \Delta p$, split the index as $k = mj + r$ with $0 \le r < m$.
