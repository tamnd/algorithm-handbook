1. $a^* = \bigl(\frac13 \cdot 1 + \frac23 \cdot \frac19\bigr)^{-1} = \frac{27}{11} \approx 2.455$ and $\langle a \rangle = \frac{19}{3}$. From $\chi' = a^*/a - 1$, $\chi' = \frac{16}{11}$ in the soft phase and $-\frac{8}{11}$ in the stiff phase; the mean is $\frac13 \cdot \frac{16}{11} - \frac23 \cdot \frac{8}{11} = 0$, and the flux is $\frac{27}{11}$ in both.

3. $R = 10$ and $u_1 R = 6.5$. The partial sums are 2, 7, 10, and the first one above 6.5 is the second, so event 2 fires. The step is $-\ln(0.5)/10 \approx 0.0693$ s.

4. (a) $V''(-1) = 16$, so $\omega = 4$ and $k = \frac{4}{2\pi} e^{-2\beta} \approx 0.637\, e^{-2\beta}$; in one dimension the curvature at the top does not enter. (b) $\frac{\sqrt4 \sqrt9}{2\pi \sqrt1} = \frac{3}{\pi} \approx 0.955$. (c) $10^{13} e^{-0.8/0.043087} \approx 8.6 \times 10^4$ per second.

6. $C(\theta) = 2\cos^2\theta - \sin^2\theta$, so $C = 0.5$ at 45° and $C = -1$ at 90°. $F = -Hx = (-0.4, 0.3)$; since $C < 0$, $F^\dagger = F - 2(F \cdot N)N = (-0.4, -0.3)$, which points toward the saddle at the origin, uphill along $y$ and downhill along $x$.

7. $\sigma(0.4) = -29.6 \cdot 0.4^k$, and $|\sigma|$ grows on $[0, 0.4]$, so the worst case is $\zeta = 0.4$: $k = 3$ gives $-1.89$ and $k = 4$ gives $-0.758$, so $k = 4$. The sufficient condition $0.4^k \le \frac{1}{101}$ needs $k \ge 5.04$, that is $k = 6$. The saving factor at $k = 4$ is $55/5 = 11$.

9. (a) $\sigma = \frac{2\sqrt2}{3}\varepsilon \approx 0.00943$. (b) $R^2 = R_0^2 - 2t$ for the disk, so $t = 0.125$; $R^2 = R_0^2 - 4t$ for the ball, so $t = 0.0625$. (c) $W''(u_0) = 3u_0^2 - 1$ is $-0.25$ at 0.5 (unstable) and $0.08$ at 0.6 (stable). The fastest mode has $|k|^2 = 0.25/(2\varepsilon^2) = 1250$ and the rate $M W''^2/(4\varepsilon^2) = 156.25\, M$.

12. With $a u_\varepsilon' = C_\varepsilon - x$, integrate over one cell $[s, s + \varepsilon]$: the result is $(C_\varepsilon - s)\varepsilon\langle a^{-1}\rangle$ minus a term $\varepsilon^2 m$ that is the same for every cell. Summing over cells gives $u_\varepsilon(j\varepsilon) = \langle a^{-1}\rangle\bigl(C_\varepsilon x - \frac{x^2}{2}\bigr) + \gamma x$ for some constant $\gamma$, and $u_\varepsilon(1) = 0$ fixes the linear part. Both values at $\frac12$ are $\frac{11}{216} \approx 0.0509$; the arithmetic mean gives $\frac{3}{152} \approx 0.0197$, less than half.

14. $1/k_BT$ is 38.68 at 300 K and 19.34 at 600 K, so $t_{\text{low}} = 1 \text{ ns} \cdot e^{0.6 \cdot 19.34} \approx 1.10 \times 10^{-4}$ s. With $\ln(1/\delta) = 6.908$, $t_{\text{stop}} = \frac{6.908}{10^{12}} \bigl(\frac{10^{12} \cdot 1.10 \times 10^{-4}}{6.908}\bigr)^{1/2} \approx 27.5$ ns, and the boost is about 4000.

16. The rows are $(0.8, 0.2)$, $(0.4, 0.6)$, $(0.2, 0.8)$. The normal equations are $\begin{pmatrix} 21/25 & 14/25 \\ 14/25 & 26/25 \end{pmatrix} c = \begin{pmatrix} 69/50 \\ 31/50 \end{pmatrix}$, with the solution $c = (\frac{68}{35}, -\frac{9}{20}) \approx (1.943, -0.45)$.

19. $Pe = ah/(2\kappa) = 2$ and $\tau = \frac{h}{2a}(\coth 2 - \frac12) \approx 0.0537$. The Galerkin ratio is $(1 + Pe)/(1 - Pe) = -3$, an oscillation. The exact solution gives $e^{ah/\kappa} = e^4 \approx 54.6$, and so does the stabilized scheme, which is nodally exact in one dimension.

21. Over one period $\int 1/(2 + \sin 2\pi y)\, dy = 1/\sqrt3$; the half where $\sin > 0$ gives $1/(3\sqrt3)$, the other half $2/(3\sqrt3)$, and $[\frac14, \frac34]$ gives $1/(2\sqrt3)$. A window of 1.5 periods is one period plus one of these halves, so $A_K = \sqrt3$, $\frac{9\sqrt3}{10} \approx 1.559$ and $\frac{9\sqrt3}{8} \approx 1.949$. The error is of order $\varepsilon/\delta$ and vanishes when $\delta$ is a whole number of periods.

24. In $\int_{-\infty}^1 e^{-\beta V}$, Laplace's method for $f = \alpha u^2 + b u^3 + c u^4$ gives $\sqrt{\pi/(\alpha\beta)}\bigl(1 + \frac1\beta(\frac{15 b^2}{16 \alpha^3} - \frac{3c}{4\alpha^2})\bigr)$. Here $\alpha = \frac12$, $b = -\frac13$, $c = 0$, so the correction is $\frac{5}{6\beta}$. The TST rate divides by this integral, and the end point $x = 1$ adds only an exponentially small term.

26. The function $t \mapsto 1/t$ is convex, so Jensen's inequality applied to the mean $\bar X_m$ of the $1/a_i$ gives $E[1/\bar X_m] \ge 1/E[\bar X_m] = a^*$. For the monotonicity, write $\bar X_{m+1}$ as the average of the $m + 1$ means that leave one cell out, and apply Jensen's inequality again.

27. $C_\varepsilon$ lies in $[0, 1]$, so $|u_\varepsilon'| \le 1/\alpha$ and $|u_0'| \le 1/(2a^*) \le 1/(2\alpha)$. By Exercise 12 the two functions agree at the cell boundaries, and inside a cell each moves by at most $\varepsilon$ times its slope bound, so $C = \frac{3}{2\alpha}$ works.

28. The Markov approximation gives $-1 + \frac13 = -\frac23$, the exact slow eigenvalue is $-2 + \sqrt2 \approx -0.586$. For the expansion, write the slow eigenvalue as $a + \frac{bc}{a - d} + O(d^{-3})$ and expand $\frac{1}{a - d} = -\frac1d\bigl(1 + \frac ad + \dots\bigr)$.
