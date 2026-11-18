1. The impact speed is $\sqrt{2gh} = \sqrt{39.24} \approx 6.264$ m/s. The rebound speed is $e$ times that, so the height is $e^2 h = 0.72$ m. Each bounce adds $2e^{2i}h$, so the total is $h(1 + e^2)/(1 - e^2) = 2 \cdot 1.36/0.64 = 4.25$ m.

3. With $k = 1/2$, the impulse is $j = -(1 + e)v_n/k = 1.5 \cdot 4 \cdot 2 = 12$ along $(0, 1)$. The velocity becomes $(3, -4 + 12/2) = (3, 2)$. The kinetic energy falls from 25 to 13.

4. The pairs $\{0,1\}$, $\{0,2\}$, $\{0,3\}$ and $\{2,3\}$ overlap on one axis, $\{1,3\}$ on none and $\{1,2\}$ on both. Only $\{1, 2\}$ is reported. The pair $\{2, 3\}$ touches at $y = 1$ but is separated in $x$.

6. The triangle has $x \in [1, 5]$, $y \in [0, 4]$, $x + y \in [1, 5]$ and $x - y \in [-3, 5]$. The square has $x + y \in [7, 11]$, which is disjoint from $[1, 5]$, so the 8-DOPs are separated. The axis-aligned boxes $[1, 5] \times [0, 4]$ and $[4, 6] \times [3, 5]$ overlap, so that test reports a false pair.

8. The error is $0.02 \cdot 0.8^5 = 0.0065536$ m after 5 steps. It drops below $0.001$ m when $0.8^n < 0.05$, at $n = 14$. The contact gets the speed $(\beta/\Delta t)C = 0.2 \cdot 60 \cdot 0.02 = 0.24$ m/s, which adds $0.0288$ J.

9. $k = 1/m + (r \times n)^2/I = 1 + 3 = 4$, and $j = 1/4$. The centre moves at $(0, -3/4)$ and $\omega = -3/4$. The struck end stops; the far end moves at $(0, -3/2)$. The energy goes from $1/2$ to $3/8$, a loss of $1/8 = 1/(2 \cdot 4)$.

13. The centres are at distance $3/2$ when $(5 - 8t)^2 + 1 = 9/4$, so $t = (5 - \sqrt{5}/2)/8 \approx 0.4852$. At $t = 1$ the distance of the centres is $\sqrt{10} \approx 3.162 > 3/2$, so both end tests miss.

14. A point of the square is at most $\sqrt 2$ from its centre, so $\mu = 4 + 2\sqrt 2 \approx 6.828$. The first gap is 4, and the step is $4/\mu = 2 - \sqrt 2 \approx 0.586$. Since no point approaches faster than $\mu$, the gap cannot close before that time; the true contact is near $t \approx 0.966$.

18. For $\tau = -5$, $b = (5, -25)$ and both contacts push, with $f = (5/2, 15/2)$. For $\tau = -10$, $f = (0, 10)$. For $\tau = -15$ the two-contact solution gives $f_1 = -5/2 < 0$, so contact 1 leaves: $f_2 = 55/4$ and $a_1 = 15/2 > 0$. The plank tips when $\tau < -10$.

19. Gauss-Seidel sets $x_1 = (c_1 - A_{12}x_2)/A_{11}$ and then $x_2 = (c_2 - A_{21}x_1)/A_{22}$. Subtract the fixed point to get $e_2' = A_{21}A_{12}e_2/(A_{11}A_{22})$. In exercise 10 the factor is $4/16 = 1/4$, and the error of $\lambda_2$ after $n$ sweeps is $-2^{-(2n + 1)}$, below $10^{-6}$ at $n = 10$.

20. The step is $v' = v - \omega^2 h x$, $x' = x + h v'$, with the matrix $\begin{pmatrix} 1 - \omega^2 h^2 & h \\ -\omega^2 h & 1 \end{pmatrix}$ on $(x, v)$. The eigenvalues have product 1 and sum $2 - \omega^2 h^2$. They are complex conjugates of modulus 1 exactly when $|2 - \omega^2 h^2| < 2$, that is $0 < \omega h < 2$. At $\omega h = 2$ both equal $-1$ and the matrix is a Jordan block, so the error grows linearly. For $\omega h > 2$ they are real with product 1, and one has modulus above 1.

21. $A_{ij} = 1 + 3x_ix_j$ gives the rows $(4, 1, -2)$, $(1, 1, 1)$ and $(-2, 1, 4)$, and the first plus the third is twice the second. Force and torque balance give $f_1 + f_2 + f_3 = 10$ and $f_1 = f_3$, so $f = (t, 10 - 2t, t)$ for $0 \le t \le 5$. Every one of them gives $Af + b = 0$, so all accelerations are 0.

22. Without friction the normal velocity is linear in the impulse, $v(p) = v^- + kp$. It is 0 at $p_{mc} = -v^-/k$. Poisson's law sets the total to $(1 + e)p_{mc}$, which gives $v^+ = -ev^-$, Newton's law. The work in compression is $-(v^-)^2/(2k)$ and in restitution $(v^+)^2/(2k) = e^2(v^-)^2/(2k)$, so Stronge's energy ratio $e^2$ gives the same impulse.
