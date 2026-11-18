1. The half kick gives $v = -0.1$, the drift $x = 1 - 0.2 \cdot 0.1 = 0.98$, the new force is $-0.98$, and the second half kick gives $v = -0.1 - 0.1 \cdot 0.98 = -0.198$. Then $H = 0.499802$, below $\frac12$ by $0.000198 = \frac{h^2}{8}(1 - x^2)$, and $v^2 + 0.99\, x^2 = 0.039204 + 0.950796 = 0.99$, the same value as at the start.

2. $U'(r) = 0$ gives $(\sigma/r)^6 = \frac12$, so $r_m = 2^{1/6}\sigma \approx 1.1225\,\sigma$ and $U(r_m) = 4\epsilon(\frac14 - \frac12) = -\epsilon$. At $r = \sigma$, $U = 0$ and $-U'(\sigma) = 24\epsilon/\sigma > 0$: the force pushes the atoms apart.

5. The conserved quantity $v^2 + (1 - h^2/4) x^2$ equals $15/16$ at the start, so $|v|$ is at most $\sqrt{15}/4 \approx 0.968$, reached on the invariant curve where $x = 0$, with $H = 15/32$.

8. $U''(r_m) = 72 \cdot 2^{-1/3}\epsilon/\sigma^2 \approx 57.15$, so $\omega = \sqrt{2 U''(r_m)} \approx 10.69$ and $h < 2/\omega \approx 0.187$. The tiny start keeps the motion harmonic, so the run with $h = 0.186$ stays within $10^{-4}$ of $r_m$ with an energy error near $3 \times 10^{-7}$, and the run with $h = 0.19$ grows until the run breaks down. With a large start, such as $1.02\, r_m$, the anharmonic potential lowers the frequency and the threshold moves.

9. Write the step as kick, drift, kick with $f$ at the two ends. Apply a step to $(x', -v')$: the first half kick undoes the last half kick of the original step with the sign of $v$ flipped, the drift returns the position to $x$, and the second half kick uses $f(x)$.

10. $M = \begin{pmatrix} 1 - z^2/2 & h \\ -\omega z (1 - z^2/4) & 1 - z^2/2 \end{pmatrix}$ in the variables $(x, v)$. A real $2 \times 2$ matrix with determinant 1 has eigenvalues $e^{\pm i\theta}$ when $|\operatorname{tr} M| < 2$; at $z = 2$ there is a double eigenvalue $-1$ with a Jordan block, and the solution grows linearly. For the last part, $\theta = 2 \arcsin(z/2)$ and $\arcsin y > y$ for $0 < y \le 1$.
