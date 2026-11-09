1. $\|A\|_1 = 6$, $\|A\|_\infty = 7$ and $\|A\|_F = \sqrt{30} \approx 5.48$. All three bound $\|A\|_2 \approx 5.12$, and so does $\sqrt{6 \cdot 7} \approx 6.48$.

3. The first has determinant $-1$, so one eigenvalue is negative; $x = (1, -1)^T$ gives $x^T A x = 0$ only, but $x = (3, -2)^T$ gives $-2$. The second has eigenvalues $1$ and $3$.

5. The determinant is $1/2160$. A small determinant alone proves nothing: $10^{-1} I$ of order 30 has determinant $10^{-30}$ and condition number 1.

7. The spectral radii are $1/2$ and $1/4$, so about 20 Jacobi sweeps and 10 Gauss-Seidel sweeps.

10. The row order is $3, 1, 2$. $L$ has the multipliers $1/4$, $1/2$ and $2/3$ below its unit diagonal, and $U$ has rows $(8, 7, 9)$, $(0, -3/4, -5/4)$ and $(0, 0, -2/3)$.

12. $A^TA = \begin{pmatrix} 3 & 3 \\ 3 & 5 \end{pmatrix}$ and $A^Tb = (5, 6)^T$, so $c_0 = 7/6$ and $c_1 = 1/2$. The residuals are $-1/6, 1/3, -1/6$.

13. Divide $\ln 10^{-6}$ by the logarithm of each spectral radius. Jacobi needs about 28,000 sweeps, Gauss-Seidel half as many, and SOR with $\omega \approx 1.939$ about 220.

14. $\lceil 50 \ln(2 \times 10^6) \rceil = 726$ steps, against $73$ when $\kappa = 100$.

17. Each sweep halves the distance: $(-1/2, 1/2)$, $(-1/4, 1/4)$, $(-1/8, 1/8)$. The lines meet at $45°$ and $\cos^2 45° = 1/2$.

19. Eliminating the first unknown first joins every pair of the others: $(n-1)(n-2)$ fill entries. Taking it last gives no fill at all.

20. Use induction on $k$. The Schur complement after $k$ steps has $2 - k/(k+1) = (k+2)/(k+1)$ in its top corner.

21. Two steps. The eigenvalues are $1$ and $4$, and the polynomial $p(t) = (1 - t)(1 - t/4)$ with $p(0) = 1$ vanishes on both, so the second Krylov space already contains the solution.

23. Classical Gram-Schmidt gives $q_2^Tq_3 \approx 1/2$, while the modified form gives a value near $10^{-16}$ and loses orthogonality only of order $\epsilon$ overall. The classical form projects with coefficients computed from the original column, so the error of $q_2$ enters $q_3$ uncorrected.

24. The Jacobi spectral radius is $\mu = 1/2$, so $\omega_{\mathrm{opt}} = 2/(1 + \sqrt{3}/2) \approx 1.072$ and $\rho = \omega_{\mathrm{opt}} - 1 \approx 0.072$, against $1/4$ for Gauss-Seidel.
