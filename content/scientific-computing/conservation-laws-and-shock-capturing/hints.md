1. The first crossing time is $1/\max(-u_0')$, and $-u_0' = 2x/(1 + x^2)^2$ is largest at $x_0 = 1/\sqrt3$, where it equals $9/(8\sqrt3)$. So $t^* = 8\sqrt3/9 \approx 1.540$, and the shock appears at $x_0 + u_0(x_0)t^* = 1/\sqrt3 + \frac34 \cdot 8\sqrt3/9 = \sqrt3 \approx 1.732$.

2. The shocks move at $(2 + 1)/2 = 1.5$ and $(1 + 0)/2 = 0.5$. They meet when $1.5t = 1 + 0.5t$, at $t = 1$ and $x = 1.5$. After that a single shock joins 2 to 0 and moves at speed 1.

3. $s = (f(0.8) - f(0.2))/0.6 = (0.16 - 0.16)/0.6 = 0$: the jump stands still. $f'(0.2) = 0.6 > 0 > f'(0.8) = -0.6$, so it is admissible. For a concave flux the admissible jumps have $\rho_L < \rho_R$: cars run into denser traffic.

4. The density ratio is $27/7 \approx 3.857$ and the pressure ratio $31/3 \approx 10.33$. $M_2^2 = 2.8/12.4$, so $M_2 \approx 0.475$. As $M \to \infty$ the density ratio tends to $(\gamma + 1)/(\gamma - 1) = 6$: a shock can compress air at most sixfold.

5. $Fr_1 = 5/\sqrt{9.81 \cdot 0.5} \approx 2.258$. The depth ratio is $\frac12(\sqrt{1 + 8Fr_1^2} - 1) \approx 2.732$, so $h_2 \approx 1.366$ m, $u_2 \approx 1.830$ m/s and $Fr_2 \approx 0.500$. The head loss is about 0.238 m.

6. $\Delta^- = 1$ and $\Delta^+ = 2$. Minmod gives slope 1 and face values 1.5 and 2.5; van Leer gives $2 \cdot 1 \cdot 2/3 = 4/3$ and faces $4/3$, $8/3$; MC gives $\operatorname{minmod}(2, 1.5, 4) = 1.5$ and faces 1.25, 2.75, the steepest. In the fourth cell $\Delta^+ = 0$, so all three give slope 0.

8. $\Delta t \le \Delta x/(c\sqrt3) \approx 1.93$ ps. A wave crosses 30 cm in 1 ns, about 520 steps at the largest time step.

9. $\sigma_{\max} = 4\ln(10^8)/20 \approx 3.68$. The reflection is $R^{\cos\theta}$: about $2.2 \cdot 10^{-6}$ at $45°$ and $10^{-4}$ at $60°$.

11. The coefficients are $c_{-2} = -\frac18$, $c_{-1} = \frac34$, $c_0 = \frac38$; one is negative, so the scheme is not monotone, as the barrier requires of a second-order linear scheme. The step gives $(\dots, 0, \frac38, \frac98, 1, 1)$: the overshoot $\frac98$ appears ahead of the moving jump, on the side it has not reached yet. Lax-Wendroff, by contrast, oscillates behind the jump.

13. With $s = (u_L + u_R)/2$, factor out $u_R - u_L$: the rate is $(u_R - u_L)\big[(u_L + u_R)^2/4 - (u_L^2 + u_Lu_R + u_R^2)/3\big] = -(u_R - u_L)^3/12$. It is nonnegative exactly when $u_L \ge u_R$, which for Burgers is the Lax condition.

15. Rusanov $-\frac74$, Roe $\frac12$, HLL $-1$, Godunov 0 (the fan contains the sonic point $u = 0$). An E-flux must satisfy $\operatorname{sgn}(u_R - u_L)(F - f(u)) \le 0$ for $u$ between the states, here $F \le 0$. Rusanov and HLL do, and Roe does not: it keeps an expansion shock.

16. $\bar u = 0$, $\bar c = \sqrt{1.5} \approx 1.2247$, and both wave strengths are $-\frac12$. The Roe flux is $(\bar c/2, 1.25) \approx (0.6124, 1.25)$, the exact flux about $(0.6061, 1.3095)$. The Rusanov mass flux is $\frac12\sqrt2 \approx 0.7071$, the largest of the three.

19. $k\Delta x = 2\pi/10$. The phase speeds are $0.98759c$, $0.99966c$ and exactly $c$. At 20 cells per wavelength and $S = 0.5$ the error is 0.31% instead of 1.24%, four times smaller, as for a second-order scheme.

20. $Du = (\frac14, \frac12, 1, \frac32, \frac74)$ against $2x = (0, \frac12, 1, \frac32, 2)$: the interior is exact and the boundary rows err by $\frac14$. Then $\mathbf 1^THDu = 1$ and $u^THDu = \frac12$, as the identities require.

22. For $k$ outside $[u_R, u_L]$ both sides are equal. For $u_R < k < u_L$, use $f_L - su_L = f_R - su_R$ to reduce the inequality to $f(k) \le f_R + s(k - u_R)$, the chord. A convex $f$ lies below every chord, and for $u_L > u_R$ this is $f'(u_L) > s > f'(u_R)$.

23. For $u_L \le u_R$ the solution is a rarefaction, and the value at $x = 0$ is $u_L$ if $f'(u_L) \ge 0$, $u_R$ if $f'(u_R) \le 0$, and the sonic point otherwise; each is the minimum of the convex $f$ on the interval. For $u_L > u_R$ the shock gives $f_L$ or $f_R$ by the sign of $s$, and this is the larger of the two since $f_L - f_R = s(u_L - u_R)$. In Exercise 15 the minimum of $u^2/2$ on $[-1, 2]$ is 0.

24. With $v = u$ and $q' = uf'$, integration by parts gives $\psi(u) = \int_0^u f(w)\,dw$, so $\psi_R - \psi_L = \int_{u_L}^{u_R} f$, which is $(u_R - u_L)F^*$. For $f = u^3/3$, $F^* = (u_L^3 + u_L^2u_R + u_Lu_R^2 + u_R^3)/12$, which is $u^3/3$ when the states agree.

25. The Jacobian is $\begin{pmatrix} 0 & 1 \\ gh - u^2 & 2u \end{pmatrix}$. The first row is immediate. In the second, $\frac g2\Delta(h^2) = g\bar h\Delta h$, and $\Delta(hu^2) = 2\bar u\Delta(hu) - \bar u^2\Delta h$ holds for the $\sqrt h$-weighted $\bar u$; check it by writing $a = \sqrt{h_L}$, $b = \sqrt{h_R}$.

26. Second order needs $\beta_{21}\beta_{10} = \frac12$ and $\beta_{20} + \alpha_{21}\beta_{10} + \beta_{21} = 1$. If the coefficient is $C$, then $\beta_{10} \le 1/C$ and $\beta_{21} \le \alpha_{21}/C$, so $\alpha_{21} \ge C/(2\beta_{10})$. Put this into $\alpha_{21}\beta_{10} + \beta_{21} \le 1$ to get $C/2 + 1/(2\beta_{10}) \le 1$, so $C \le 2 - 1/\beta_{10} \le 2 - C$, which gives $C \le 1$.
