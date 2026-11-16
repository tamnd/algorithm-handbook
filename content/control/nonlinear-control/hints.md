2. $\mathrm{ad}_f g = (-2 x_2, 0)$. For $n = 2$ the only condition is that $g$ and $\mathrm{ad}_f g$ are
independent, which holds exactly when $x_2 \ne 0$. So the system is feedback linearizable near every point
with $x_2 \ne 0$ but not near the origin. The linearization has $A = \operatorname{diag}(-1, 0)$ and
$B = (0, 1)^T$, so $[B \ AB]$ has rank 1: not controllable.

3. For $y = x_1$: $L_g h = L_g L_f h = 0$ and $L_g L_f^2 h = 1 + x_1^2 \ne 0$, so $r = 3$. For
$y = x_1 + x_2$: $L_f h = x_2 - x_1 + x_3$ and $L_g L_f h = 1 + x_1^2$, so $r = 2$. For $y = x_2$:
$L_f h = -x_1 + x_3$, again $r = 2$.

5. $L_f V = x^4$ and $L_g V = x$, so $u = -(x^4 + \sqrt{x^8 + x^4}) / x = -x^3 - x \sqrt{1 + x^4}$, with
$u(0) = 0$. The closed loop is $\dot x = -x \sqrt{1 + x^4}$, and $u(1) = -1 - \sqrt 2 \approx -2.414$.

6. $\dot s = \dot x_2 + 2 \dot x_1 = -\operatorname{sign}(s) + d$, so $s \dot s \le -(1 - 0.3)|s|$. With
$s(0) = 1.4$ the reaching time is at most $1.4 / 0.7 = 2$. On $s = 0$, $\dot x_1 = -2 x_1$, so $x_1$ decays
like $e^{-2t}$ whatever $d$ does. With Euler steps each step changes $s$ by at most $(k + D) h$, so
$|s| \le 1.3 \times 10^{-3}$ after reaching.

7. $k_2 > 2 + 8/9 = 26/9 \approx 2.889$. The rule of thumb gives $k_1 \approx 2.121$, $k_1^2 = 4.5$ and
the bound $2 + 8/4.5 \approx 3.78$, which $k_2 = 2.2$ does not exceed; the certificate is only sufficient,
so the gains may still work. With $k_2 = 1.5 < L$ no $k_1$ works: holding $s = 0$ against $\dot d = L$
needs $\dot v \ge L - k_2 > 0$ at the same time as $v = 0$.

11. For $y = x_1 + x_2$, $y \equiv 0$ forces $x_2 = -x_1$ and $x_3 = x_1 - x_2 = 2 x_1$, and what remains is
$\dot x_1 = -x_1$: minimum phase. For $y = x_2$, $y \equiv 0$ forces $x_3 = x_1$ and leaves $\dot x_1 = 0$,
which is stable but not asymptotically stable. The linear part from $(1 + x_1^2) u$ to $x_1$ is
$1 / ((s + 1)(s^2 + 1))$; the two outputs multiply it by $s + 1$ and by $s$, so the zeros are $-1$ and $0$.

12. $g = e_3$, $\mathrm{ad}_f g = -e_2$ and $\mathrm{ad}_f^2 g = (1 + 2 x_2) e_1$. They are independent
when $x_2 \ne -1/2$, and the span of $e_3$ and $e_2$ is involutive because the fields are constant. Use
$h = x_1$: $z = (x_1,\ x_2 + x_2^2,\ (1 + 2 x_2) x_3)$, $L_f^3 h = 2 x_3^2$, and
$u = (v - 2 x_3^2) / (1 + 2 x_2)$. Since $z_2 = x_2 + x_2^2$ is increasing for $x_2 > -1/2$, the change of
coordinates is one-to-one there, and $c = -1/2$.

14. $L_f V = (2 x_1 + x_2) x_2$ and $L_g V = x_1 + 2 x_2$. Where $L_g V = 0$ and $x \ne 0$, $x_1 = -2 x_2$
with $x_2 \ne 0$, and $L_f V = -3 x_2^2 < 0$. At $(1, 0)$: $a = 0$, $b = 1$, $u = -1$, $\dot V = -1$. At
$(0, 1)$: $a = 1$, $b = 2$, $u = -(1 + \sqrt{17}) / 2 \approx -2.562$, $\dot V = -\sqrt{17}$.

17. On the negative real axis $G(j\omega)$ has $\omega^2 = 2$ and $|G(j\sqrt 2)| = 1/6$. The balance
$N(A) G(j\omega) = -1$ gives $\omega = \sqrt 2 \approx 1.414$ and $A = 4 / (6 \pi) = 2 / (3 \pi) \approx
0.212$. A fourth order Runge-Kutta simulation with step $10^{-3}$ and the relay output held over each step
gives a period of $4.552$, so $\omega \approx 1.380$, and an amplitude of $0.2201$; the step $2.5 \times
10^{-4}$ gives the same digits. The prediction is off by about 2.4 percent in frequency and 3.7 percent in
amplitude, because the relay output is a square wave, not a sine.

20. On the axis with $0 \le x_1 < 1$, $a = (2(x_1 - 2), 0)$, $b = (x_1 - 2)^2 - 1$, and
$a \cdot u_{\text{nom}} + b = (x_1 - 2)(6 - x_1) - 1 \le -6$, so the filter acts. The second component of
the correction is a multiple of $2 x_2 = 0$. The first component is $-b / a_1$, which gives the formula; at
$x_1 = 0$ it is $0.75$. Near $x_1 = 1$ it behaves like $1 - x_1$, so the robot approaches the point
$(1, 0)$ on the obstacle and stops there: an equilibrium created by the filter.

23. The map $(x, u) \mapsto (u_1, u_2, x_2 u_1)$ never takes the value $(0, 0, \varepsilon)$ with
$\varepsilon \ne 0$, since $u_1 = 0$ forces the third component to be 0. So the image of no neighborhood
contains a neighborhood of 0. Steering: $u = (0, -1)$, then $(1, 0)$, then $(0, 1)$, then $(-1, 0)$, each
for one time unit. The second piece changes $x_3$ by $x_2 \cdot \Delta x_1 = -1$.

24. Try $V = \frac12 x_1^2 + \frac14 x_2^4$. Then
$\dot V = -x_1^2 + x_1 x_2^2 - x_2^4$, a quadratic form in $(x_1, x_2^2)$ with eigenvalues $1/2$ and
$3/2$, so $\dot V \le -\frac12 (x_1^2 + x_2^4)$. $V$ is radially unbounded.

25. With $w = x^2$ and $e = \theta - \hat\theta - c$, $\dot w = 2 e w$ and $\dot e = -\gamma w$, so
$\frac{d}{dt}(\gamma w / 2 + e^2 / 2) = 0$. Since $x \to 0$ and $e$ decreases, the limit is
$e_\infty = -\sqrt{\gamma x(0)^2 + e(0)^2}$, so
$\hat\theta_\infty = \theta - c + \sqrt{\gamma x(0)^2 + (\theta - \hat\theta(0) - c)^2}$. For the numbers
given this is $\sqrt 2 - 1 \approx 0.41421$, not $\theta = 1$; a fourth order Runge-Kutta simulation with
step $10^{-3}$ gives the same value to 13 digits.

26. Eliminate $u$ and $z_2$ with $b_0 u = -k_p z_1 - z_2$ and set $r = 0$. The result is
$s^3 + (k_p + 2 \omega_o) s^2 + \beta (\omega_o^2 + 2 \omega_o k_p) s + \beta k_p \omega_o^2$. The Hurwitz
condition $(k_p + 2 \omega_o)(\omega_o^2 + 2 \omega_o k_p) > k_p \omega_o^2$ does not depend on $\beta$
and always holds, so the loop is stable exactly when $\beta > 0$. The second order loop of the entry has a
finite range of $b / b_0$.

27. Between samples $\dot x$ is constant. When the filter acts, $u = \gamma (1 - x_k)$ and
$1 - x_{k+1} = (1 - \gamma T)(1 - x_k)$; when it does not, $u_{\text{nom}} \le \gamma (1 - x_k)$ and the
same expression is a lower bound. So $\gamma T \le 1$ keeps $h \ge 0$. If $\gamma T > 1$, start with
$0 < 1 - x_0 < 1/\gamma$. For the numbers given, $x$ rises by $0.15$ per step to $0.9$, the next input is
still $1$, and the seventh sample has $x = 1.05$, $h = -0.05$.
