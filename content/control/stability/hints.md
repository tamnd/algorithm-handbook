1. The rows are $1, 3, 5$; $2, 4$; $1, 5$; $-6$; $5$. The first column $1, 2, 1, -6, 5$ changes sign twice, so two roots lie in the right half plane. They are about $0.288 \pm 1.416j$.

2. The first matrix has trace $-1$ and determinant $4$, so it is Hurwitz; its eigenvalues are $-\tfrac12 \pm j\sqrt{15}/2$. The second has determinant $-5 < 0$, so its eigenvalues $-1 \pm \sqrt6$ have opposite signs: a saddle, and the origin is unstable. The third has trace $0$ and eigenvalues $\pm j$, which are simple, so the origin is Lyapunov stable but not asymptotically stable.

3. The first column is $1, \tfrac34, \tfrac{27}{100}$, all positive, so both roots lie inside the unit circle; they are $\tfrac35 \pm \tfrac{j}{5}\sqrt{\tfrac72}$, of modulus $1/\sqrt2$. For the second polynomial, $1 - a_1 + a_0 = 1 - \tfrac85 + \tfrac12 = -\tfrac1{10} < 0$, so it fails the triangle: one root, about $-1.174$, lies outside.

4. (a) Locally exponentially stable, with region of attraction $(-1, 1)$; not global, since $\pm 1$ are equilibria. (b) Globally asymptotically stable, but not exponentially stable: $x(t)$ decays like $t^{-1/4}$. (c) Lyapunov stable, not asymptotically stable. (d) Unstable: $\dot x = x^2(1 - x^2) > 0$ for small $x > 0$.

5. Write $P = \begin{bmatrix} p & q \\ q & r \end{bmatrix}$. The three entries of the equation give $-2p = -1$, $p - 3q = 0$ and $2q - 4r = -1$, so $p = \tfrac12$, $q = \tfrac16$, $r = \tfrac13$. Then $p > 0$ and $\det P = \tfrac{5}{36} > 0$.

7. With $f(r) = r(1 - r^2)(4 - r^2)$, the circles $r = 1$ and $r = 2$ are periodic orbits of period $2\pi$. Since $f'(1) = -6$ and $f'(2) = 24$, the circle $r = 1$ attracts, with multiplier $e^{-12\pi}$, and $r = 2$ repels, with multiplier $e^{48\pi}$. The origin is an unstable focus.

9. $\mu_1(J) = \max(-3 + 2, -4 + 1) = -1$, $\mu_\infty(J) = \max(-3 + 1, -4 + 2) = -2$, and $\mu_2(J)$ is the largest eigenvalue of $(J + J^T)/2$, which is $(-7 + \sqrt{10})/2 \approx -1.919$. The rates are $1$, about $1.919$ and $2$, each in its own norm.

10. $p = (x+1)^4 + 4 = \big((x+1)^2\big)^2 + 2^2$. Its minimum is $4$, at $x = -1$, and $p - 4 = (x+1)^4$ is a square, so the largest $\gamma$ is $4$.

12. The rows are $1, 2, 1$; $1, 2$; $\varepsilon, 1$; $2 - 1/\varepsilon$; $1$. For small $\varepsilon > 0$ the column has signs $+, +, +, -, +$: two changes. The count is exact because no root lies on the imaginary axis: $p(j\omega) = (\omega^2 - 1)^2 + j\omega(2 - \omega^2)$, whose two parts never vanish together. The roots are about $0.122 \pm 1.307j$ and $-0.622 \pm 0.441j$.

16. $V = \tfrac12(x^2 + \dot x^2)$ gives $\dot V = -\dot x^4 \le 0$, and $V$ is radially unbounded. A solution that stays in $\{\dot x = 0\}$ has $\ddot x = 0$, so $x = 0$. For the second part, the Jacobian at the origin has eigenvalues $\pm j$; exponential stability would force it to be Hurwitz.

17. $\dot V = -4x_1^2(1 - x_2) - 2x_2^2$, which can be positive only where $x_2 > 1$. On the curve $\dot V = 0$ with $x_2 > 1$, $V = x_2^2 + x_2^2/(2(x_2 - 1))$; this is smallest at $x_2 = (7 + \sqrt{17})/8$, where $c^* \approx 4.409$. The disc has radius about $2.100$; the other equilibria $(\pm\sqrt2, 2)$ lie at distance $\sqrt6 \approx 2.449$.

22. $\operatorname{Re} G(j\omega) = (2 - t)/(t^2 + 5t + 4)$ with $t = \omega^2$. Its minimum is at $t = 2 + 3\sqrt2$ and equals $-\sqrt2/(12 + 9\sqrt2)$, so the circle criterion gives $k < 9 + 6\sqrt2 \approx 17.49$. With $\eta = \tfrac13$, $\operatorname{Re}[(1 + j\eta\omega)G(j\omega)] = 2/|(j\omega + 1)(j\omega + 2)|^2 > 0$ at every $\omega$.

24. Use $V = x^T P x$ for $\dot x = (A + \Delta)x$: $\dot V = x^T(-I + \Delta^T P + P\Delta)x \le -(1 - 2\|P\|_2\|\Delta\|_2)|x|^2$. For the matrix of exercise 5, $\lambda_{\max}(P) = (5 + \sqrt5)/12$, so the bound is $3(5 - \sqrt5)/10 \approx 0.829$. The smallest $\Delta$ that makes $A + \Delta$ singular has norm $\sigma_{\min}(A) = \sqrt{3 - \sqrt5} \approx 0.874$, so the Lyapunov bound is not far from tight here.

25. Put $w = 1/x_1$. Then $\dot w = w - x_2(0)e^{-t}$, which is linear, and $w(t) = e^t\big(w(0) - \tfrac12 x_2(0)(1 - e^{-2t})\big)$. It reaches $0$ in finite time exactly when $x_1(0)x_2(0) > 2$, at $t = \tfrac12 \ln\big(x_1 x_2/(x_1 x_2 - 2)\big)$ with the initial values; from $(2, 2)$ this is $\tfrac12 \ln 2 \approx 0.347$. So the first system is not input-to-state stable with respect to $x_2$, and a cascade of globally asymptotically stable systems need not be globally asymptotically stable.

26. $x_1\dot x_1 + x_2\dot x_2 = r^2 - (x_1^4 + x_2^4)$, and $r^4/2 \le x_1^4 + x_2^4 \le r^4$. So $r$ grows on $r = 0.9$ and shrinks on $r = 1.5$. For the angle, $r^2\dot\theta = r^2 + \tfrac14 r^4 \sin 4\theta \ge r^2(1 - r^2/4)$, which is positive for $0 < r < 2$, while any equilibrium has $r \le \sqrt2$; so the origin is the only one. The divergence is $2 - 3r^2 > 0$ on the disc $r < \sqrt{2/3}$. A simulation shows the orbit between $r \approx 1.07$ and $r \approx 1.25$.

27. The output is a pulse of height $1$ while $a\sin\theta > \tfrac12$. Its first harmonic gives $N(a) = \frac{4}{\pi a}\sqrt{1 - \frac{1}{4a^2}}$ for $a > \tfrac12$, largest at $a = 1/\sqrt2$, where $N = 4/\pi$. Since $G(j\sqrt2) = -K/6$, a cycle needs $N(a) = 6/K$, which has solutions exactly when $K > 3\pi/2 \approx 4.71$. For $K = 10$, $N(a) = 0.6$ at $a \approx 0.515$ and $a \approx 2.059$; the larger cycle attracts, and a simulation gives amplitude about $2.10$ and period about $4.50$, against the predicted $2\pi/\sqrt2 \approx 4.44$.

28. The loop has a pole at $j\omega_0$ when $\Delta(j\omega_0) = -1/G(j\omega_0)$. Take $\omega_0 = 1/\sqrt2$, where $|G|$ peaks: $-1/G(j\omega_0) = -\tfrac12 - j/\sqrt2$ has modulus $\sqrt3/2$, so $c = \sqrt3/2$. The all-pass factor has phase $-2\arctan(\omega_0/a)$, and matching the phase gives $a = (\sqrt3 - 1)/2$. The closed loop polynomial is $s^3 + \tfrac{1 + \sqrt3}{2}s^2 + \tfrac12 s + \tfrac{1 + \sqrt3}{4}$, with roots $\pm j/\sqrt2$.
