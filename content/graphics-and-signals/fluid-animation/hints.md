1. Each new value is $\tfrac34 q_i + \tfrac14 q_{i-1}$. After one step $q = (0, 0, 3, 1, 0)$, after two $q = (0, 0, 2.25, 1.5, 0.25)$. The sum stays 4, but the peak falls from 4 to 3 to 2.25: the spike spreads although the exact solution only moves it.

4. $v_{\max} = 3.13$ m/s, $c = 31.3$ m/s, $B = \rho_0 c^2/7 = 140\,143$ Pa, and $p = B(1.01^7 - 1) \approx 10\,100$ Pa. The step is at most $0.4 \cdot 0.02/(31.3 + 3.13) \approx 2.3 \cdot 10^{-4}$ s. The hydrostatic pressure is 4905 Pa, so a compression of 1% already gives about twice the largest pressure the column needs.

7. $k = 0.3142$ rad/m, $\omega = 1.756$ rad/s, period 3.58 s, phase speed 5.59 m/s, $kA = 0.471$. The mean level is $-kA^2/2 = -0.353$ m, so the crest stands 1.853 m above it and the trough 1.147 m below it. A cusp appears at $A = 1/k = 3.18$ m. The sum of $k_iA_i$ is 1.2, so $Q < 1/1.2 \approx 0.83$.

8. $\ell = V^2/g = 40.8$ m and the peak wavelength is $2\pi\sqrt2\,\ell = 362$ m, longer than the patch, so the main waves of the spectrum are missing. The ratio is $N^2/\log_2 N = 65\,536/8 = 8192$.

9. Each node gets mass 1. The grid velocities are $1.5$ and $0.5$, and the particles come back with $1.25$ and $0.75$. The momentum is 2 at every stage. The energy goes from 2 to 1.25 on the grid and to 1.0625 on the particles. FLIP adds a zero change and returns $2$ and $0$.

11. Solve $0.75a + 0.5b + 0.25c = 0$ and $0.25a + 0.5b + 0.75c = 0$: $(a, b, c) = (1, -2, 1)$, up to a factor. PIC replaces the particle velocities by values from the grid, so it removes the change. FLIP adds only the change of the grid velocity, which this mode does not touch, so it stays forever. With more particles than grid values, such invisible modes are what FLIP's noise is made of.

13. $\hat q = (0, 0, 0, 0.5, 1, 1, 1, 0.5, 0, 0)$, $\bar q = (0, 0, -0.125, 1.125, 1, 1, 1.125, -0.125, 0, 0)$ and the new field is $(0, 0, -0.0625, 0.5, 1.0625, 1, 1.0625, 0.5, -0.0625, 0)$. The values $-0.0625$ and $1.0625$ leave their ranges; clamping them gives back $\hat q$, so near this edge the limited step is the plain step.

15. The update multiplies the divergence by $1 - \beta_0 n_c/4$, so $\beta_0 = 4/3$. With $\beta_0 = 1.5$ the factor is $-0.125$ and the divergence becomes $-0.375$ per second. With $F = 0.3$ m/s and $\omega = 1.125$, the energy drops by $\frac{F^2}{2n_c}\omega(2 - \omega) \approx 0.0148$.

18. The backward step after the forward step has the factor $|A|^2$, so the corrected field is $(1 + \tfrac12(1 - |A|^2))q$; one more forward step gives BFECC. For MacCormack, $|G| \le |A| + \tfrac12(1 - |A|^2) = 1 - \tfrac12(1 - |A|)^2$. At $\theta = \pi$, $A = 0$, BFECC gives 0 and MacCormack $0.5$; at $\theta = \pi/2$, $|A| = 0.707$, and the factors are 0.884 and 0.901.

19. Expand $q_{i-1}$ in a Taylor series in the update $q_i' = (1 - c)q_i + c\,q_{i-1}$ and use $q_{tt} = u^2 q_{xx}$. The result is $0.00375$ m²/s, 3750 times the viscosity of water.

20. The eigenvalues of $D^{-1}A$ are $2.4$ and $0.3$ (twice). The spectral radii are 1.4 for $\omega = 1$, so plain Jacobi diverges, and 0.85 for $\omega = 1/2$. The iteration converges for $\omega < 2/2.4 = 5/6$.

21. Each interior face appears in the divergence of its two cells with opposite signs, and in the gradient as the difference of the same two pressures. Then $\langle Gp, u'\rangle = -\langle p, Du'\rangle = 0$. For the checkerboard, $p_{i+1,j} = p_{i-1,j}$, but neighbors across a face differ by 2.
