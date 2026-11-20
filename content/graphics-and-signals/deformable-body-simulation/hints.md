1. The rest edge matrix is $D_m = I$, so $F = D_s = \begin{pmatrix} 1.2 & 0.3 \\ 0 & 0.9 \end{pmatrix}$ and $J = 1.08$. Then $C = \begin{pmatrix} 1.44 & 0.36 \\ 0.36 & 0.9 \end{pmatrix}$ and $E = \begin{pmatrix} 0.22 & 0.18 \\ 0.18 & -0.05 \end{pmatrix}$. $J > 0$, so the triangle is not inverted; it is stretched along $x$, squeezed along $y$ and sheared.

2. With $\mu = E/(2(1 + \nu))$ and $\lambda = E\nu/((1 + \nu)(1 - 2\nu))$: for $\nu = 0.3$, $\mu = 38\,462$ Pa and $\lambda = 57\,692$ Pa; for $0.45$, $\mu = 34\,483$ Pa and $\lambda = 310\,345$ Pa; for $0.49$, $\mu = 33\,557$ Pa and $\lambda = 1\,644\,295$ Pa. $\lambda$ blows up, because $1 - 2\nu \to 0$: the material becomes incompressible, and the volume term makes the equations much stiffer.

3. $\omega = \sqrt{50/0.002} = 158.1$ rad/s, so $\Delta t < 2/\omega = 12.6$ ms. A frame of 16.7 ms needs at least 2 substeps. A cloth mesh has a larger $\omega_{\max}$ than one spring, so the real limit is smaller.

4. The inverse masses are $w_1 = 0.5$ and $w_2 = 1$, and $C = 2 - 1.2 = 0.8$, so $s = 0.8/1.5 = 8/15$. The first particle moves up by $s w_1 = 4/15$ and the second down by $s w_2 = 8/15$, to $(0, 4/15)$ and $(0, 22/15)$, at the distance 1.2. The center of mass stays at $y = 2/3$. Then $k' = 1 - 0.5^{1/4} = 0.159$.

5. $\tilde\alpha = 10^{-3}/0.02^2 = 2.5$ and $w = 0.5$, so $\Delta\lambda = -0.3/(0.5 + 2.5) = -0.1$ and the particle moves by $w\,\Delta\lambda = -0.05$ to $1.25$. Backward Euler with $k = 1000$ gives $(2 \cdot 1.3 + 0.0004 \cdot 1000 \cdot 1)/(2 + 0.4) = 1.25$, the same. PBD with stiffness 1 puts the particle at 1, the rest length, whatever the step.

6. $1/(1 + 4) = 1/5$ per step, and $5^{-10} \approx 1.0 \times 10^{-7}$ after 10 steps: the motion is gone. Symplectic Euler is stable only for $\omega\Delta t < 2$. At exactly 2 its matrix has the double eigenvalue $-1$ and the stretch alternates in sign and grows linearly: $1, -3, 5, -7, \dots$

7. By Little's law the count is the rate times the mean lifetime, $200 \cdot 2 = 400$ particles.

8. $A_{pq} = \sum \mathbf p_i\mathbf q_i^T = \begin{pmatrix} 0 & -4 \\ 8 & 0 \end{pmatrix}$ and $\theta = \operatorname{atan2}(8 + 4, 0) = 90$ degrees. The particle that rests at $(1, 1)$ is at $(-1, 2)$ and its goal is $R(1, 1) = (-1, 1)$. Its velocity becomes $0.5\,((-1, 1) - (-1, 2))/0.1 = (0, -5)$, and it moves to $(-1, 1.5)$. The fit removes the turn and pulls only against the stretch.

9. After the sweeps the positions are $(0, 1.3, 2.4)$, $(0, 1.2, 2.3)$, $(0, 1.15, 2.25)$ and $(0, 1.125, 2.225)$. From the second sweep on, the pinned spring is set to 1.1 by moving the middle particle left by its excess $e$. The second spring, which was at 1.1, is now too long by $e$, and its correction moves the middle particle back by $e/2$. So each sweep halves the excess of the first spring and leaves the second at exactly 1.1. A slack $\sigma > 0$ ends the loop.

11. $P_{xx} = \mu(s - 1/s) + \lambda\ln(s)/s$ for neo-Hookean and $(2\mu + \lambda)(s^3 - s)/2$ for St. Venant-Kirchhoff, with $\mu = 0.384615$ and $\lambda = 0.576923$. At $s = 0.5$, $0.2$ and $0.1$ the neo-Hookean values are $-1.377$, $-6.489$ and $-17.092$, the St. Venant-Kirchhoff values $-0.252$, $-0.129$ and $-0.067$. The St. Venant-Kirchhoff stress peaks at $s = 1/\sqrt3$ and then falls toward zero, so it barely resists a flattening bar.

19. The three lengths add up to 3.9, so one of them is at least 1.3, a strain of 30%, while the limit is 1.1. Equal spacing reaches 30%. The sweeps do not approach it: after the second sweep the end state is $(0, 1.4, 2.8, 3.9)$ with the strains 40%, 40% and 10%, and every later sweep moves the particles inside the sweep and returns to the same state. The cloth jitters and ends worse than the even split.

20. Write $k = 1/\alpha = 1000$ and the prediction $\tilde y = (-1.0981, -2.0981)$. Backward Euler solves $(1 + 2k\Delta t^2)y_1 - k\Delta t^2 y_2 = \tilde y_1$ and $-k\Delta t^2 y_1 + (1 + k\Delta t^2)y_2 = \tilde y_2 - k\Delta t^2$, so $y = (-1.015726, -2.023215)$. The multiplier system is $\begin{pmatrix} 1 + \tilde\alpha & -1 \\ -1 & 2 + \tilde\alpha \end{pmatrix}$ with $\tilde\alpha = 0.1$. Gauss-Seidel on a $2 \times 2$ system contracts by $a_{12}a_{21}/(a_{11}a_{22}) = 1/((1 + \tilde\alpha)(2 + \tilde\alpha)) = 0.4329$ per sweep, and the script sees exactly that ratio from the second sweep on.

21. Each bottom vertex carries $4.905$ N, so solve $b'(d) = -4.905\,\Delta t^2/\kappa$ with $b'(d) = -2(d - \hat d)\ln(d/\hat d) - (d - \hat d)^2/d$ by bisection on $(0, \hat d)$. The gaps are $2.1 \times 10^{-4}$, $6.5 \times 10^{-4}$ and $8.7 \times 10^{-4}$ m for the three steps, and $2.3 \times 10^{-5}$ and $9.6 \times 10^{-4}$ m for the two values of $\kappa$, the values the entry measures.

22. In any $3 \times 3$ block, the center and the four middles of the sides are pairwise joined: by structural, shear or bending springs. That is a clique of 5, so at least 5 colors. The color $(i + 2j) \bmod 5$ works, because the offsets $(1, 0)$, $(0, 1)$, $(1, 1)$, $(1, -1)$, $(2, 0)$ and $(0, 2)$ change $i + 2j$ by $1, 2, 3, -1, 2, 4$, none a multiple of 5.

23. $AA^T - I = ((1 + \varepsilon)^2 - 1)I$, so $V_\perp = 2\kappa_o\,\mathrm{vol}\,(2\varepsilon + \varepsilon^2)^2 \approx 8\kappa_o\,\mathrm{vol}\,\varepsilon^2$. One joule needs $\varepsilon \approx 1/\sqrt{8 \cdot 10^7 \cdot 0.08} = 4.0 \times 10^{-4}$; for a fixed energy $\varepsilon$ falls like $\kappa_o^{-1/2}$, ten times for a factor 100. The entry's table has a fixed impact instead of a fixed energy: the force $\partial V_\perp/\partial\varepsilon \approx 16\kappa_o\,\mathrm{vol}\,\varepsilon$ is linear, so $\varepsilon$ falls like $1/\kappa_o$, about 100 times, as measured from $10^7$ to $10^9$.
