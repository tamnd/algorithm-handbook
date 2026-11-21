In these exercises $\bar\gamma = 42.577$ MHz per tesla for hydrogen. A Cartesian line of $n$ samples has the frequencies $-n/2, \ldots, n/2 - 1$ times $\Delta k$, so $k_{\max} = n\Delta k/2$, as in the [k-space](/k-space/) entry. In the SENSE exercises the noise covariance is $\Psi = I$ unless stated otherwise, and the g-factor of pixel $p$ is $g_p = \sqrt{[M^{-1}]_{pp}[M]_{pp}}$ with $M = E^H \Psi^{-1} E$, as in the [g-factor](/g-factor/) entry.

1. ◦ Compute the Larmor frequency of hydrogen at 7 T.

2. ◦ A Cartesian scan has a field of view of 240 mm and a $192 \times 192$ matrix. Find $\Delta k$ and $k_{\max}$ in cycles per meter and the pixel size in mm.

3. ◦ The scan of exercise 2 keeps every third phase encoding line, $R = 3$, and the full field of view is $[-120, 120)$ mm. What is the reduced field of view, and which positions fold onto the pixel at $y = 10$ mm?

4. ◦ After an inversion pulse, $M_z(t) = M_0(1 - 2e^{-t/T_1})$. At what time is the signal of fat with $T_1 = 250$ ms zero?

5. ◦ A radial scan has $n = 320$ samples on each spoke over the diameter. How many spokes over 180 degrees does the rule of the [trajectory](/k-space-trajectory/) entry ask for? With one spoke per 5 ms, compare the scan time with that of 320 Cartesian lines at the same rate.

6. ◦ The [root sum of squares](/root-sum-of-squares-coil-combination/) entry gives the noise-only mean $\Gamma(c + \frac12)/\Gamma(c)$. Compute it for $c = 8$ and $c = 32$ and compare each with $\sqrt c$.

7. ◦ A [GRAPPA](/grappa/) reconstruction has $c = 8$ coils and $R = 3$. Its kernel uses 2 acquired source lines and 3 columns per coil. How many source values does one kernel have, and how many complex weights are fitted in all?

8. ◦ For a real image with a constant phase, the error of [POCS partial Fourier](/pocs-partial-fourier/) halves at each iteration. How many iterations reduce it by a factor of at least $10^6$?

9. ◦ In [QSM](/quantitative-susceptibility-mapping/), compute the fraction of directions where the dipole kernel has $|D| < 0.02$, and compare it with the small-$\varepsilon$ value $\sqrt3\,\varepsilon$.

10. • SENSE with $R = 2$ and two coils folds the pixels $p$ and $q$ together. Coil 1 has the sensitivities $1$ at $p$ and $1/4$ at $q$; coil 2 has $1/2$ at $p$ and $1$ at $q$. The folded values are $3/2$ in coil 1 and $5/2$ in coil 2. Unfold them, and compute the g-factor of both pixels.

11. • In the setting of exercise 10, replace the sensitivities by $(1, 1)$ for coil 1 and $(1, -1)$ for coil 2. Compute the g-factor, and say what property of $E$ gives this value.

12. • A [partial Fourier](/partial-fourier-reconstruction/) line has $n = 128$ and $k_0 = 16$. What fraction of the line is acquired? With the true constant phase, give the least squares noise variance per pixel and the factor by which the noise standard deviation grows against the full line.

13. • Find the Ernst angle of the [Bloch equations](/bloch-equations/) entry for $T_1 = 1$ s with $T_R = 10$ ms and with $T_R = 100$ ms.

14. • A spiral scan has a field of view of 240 mm, a $192 \times 192$ matrix and $N_i = 8$ interleaves. How many turns does each interleaf make?

15. • A dynamic scan has $128 \times 128$ voxels and $T = 200$ frames. How many degrees of freedom does the [partial separability model](/partial-separability-model/) of rank $L = 8$ have, and how does that compare with the number of values in the series?

16. • Form the $8 \times 8$ Casorati matrix $X_{xt} = \cos(2\pi(x + t)/8)$ for $x, t = 0, \ldots, 7$. Find its rank, and the rank after adding the constant 1 to every entry.

17. • In [variable density sampling](/variable-density-sampling/), let $n = 4$ with $\mu_k^2 = (1/2, 1/4, 1/8, 1/8)$, and ask for 3 samples in expectation, with inclusion probabilities $p_k \le 1$. Scaling $p_k = c\,\mu_k^2$ gives $p_1 > 1$, so cap it at 1 and scale the others to keep the expected count. Find the $p_k$ and $K^2 = \max_k \mu_k^2/p_k$, and compare with uniform sampling at the same expected count and with the value $\sum_k \mu_k^2/3$ that the uncapped rule would give.

18. • In [compressed sensing MRI](/compressed-sensing-mri/), the [proximal gradient method](/proximal-gradient-method/) has the bound $L R^2/(2k)$ and [FISTA](/fista/) the bound $2LR^2/(k+1)^2$. With $LR^2 = 1$, how many iterations does each bound need for an accuracy of $10^{-4}$?

19. • Tikhonov dipole inversion with $\alpha = 10^{-3}$ multiplies the noise at a frequency by $|D|/(D^2 + \alpha)$. Find the largest gain and the value of $|D|$ where it occurs, and the fraction of directions where $|D|$ is below that value.

20. ★ In SENSE with $R = 2$, let coil 1 have the sensitivities $(1, a)$ at the pixels $(p, q)$ and coil 2 have $(a, 1)$, with $0 \le a < 1$. Find the g-factor as a function of $a$, and the value of $a$ at which it reaches 2.

21. ★ Two coils each see only one of two folded pixels, $E = I$, but their noise is correlated, $\Psi = \begin{pmatrix} 1 & \rho \\ \rho & 1 \end{pmatrix}$. Compute the g-factor of each pixel, and its value for $\rho = 0.5$.

22. ★ [CG-SENSE](/cg-sense/) runs the conjugate gradient method on $E^H D E x = E^H D y$ from $x_0 = 0$, with $A = E^H D E$ positive definite and the solution $x^\star$. Show that $\lVert D^{1/2}(E x - y)\rVert^2 = \lVert D^{1/2}(E x^\star - y)\rVert^2 + \lVert x - x^\star\rVert_A^2$ for every $x$, and conclude that the weighted data residual does not increase from step to step. When is the plain residual $\lVert E x - y\rVert$ covered?

23. ★ Run the [density compensation](/density-compensation/) iteration $w \leftarrow w/(Cw)$ with $C = \begin{pmatrix} 1 & 1/2 & 0 \\ 1/2 & 1 & 1/2 \\ 0 & 1/2 & 1 \end{pmatrix}$ from $w = (1, 1, 1)$. Give the first two iterates exactly, find the only solution of $Cw = \mathbf{1}$, and find how fast the middle weight goes to it.

24. ★ Show that the signal at the Ernst angle is $M_0\sqrt{(1 - E_1)/(1 + E_1)}$, and that it is about $M_0\sqrt{T_R/(2T_1)}$ when $T_R \ll T_1$. Compare both with the signal at $90°$ for $T_R/T_1 = 0.01$.
