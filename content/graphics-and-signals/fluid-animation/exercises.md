1. ◦ A smoke density sits at the centers of five cells, $q = (0, 0, 4, 0, 0)$, and the velocity is constant and to the right, with $u\,\Delta t/\Delta x = 1/4$. Run two semi-Lagrangian steps of [stable fluids](/stable-fluids/) with linear interpolation, taking values outside the five cells as 0. Give the field after each step, its sum and its peak.

2. ◦ On a [MAC grid](/mac-grid/) with $\Delta x = 0.5$ m, one cell has the face velocities $u_{\text{left}} = 1$, $u_{\text{right}} = 3$, $v_{\text{bottom}} = 2$ and $v_{\text{top}} = 1$, all in m/s. What is its divergence? How many velocity faces does a grid of $4 \times 3$ cells have?

3. ◦ After the grid update of one step, a particle has the velocity $v_p = 2.0$ m/s, the old grid velocity interpolated at the particle is $1.5$ m/s and the new one is $1.8$ m/s. What velocity does the particle get under [PIC](/particle-in-cell/), under [FLIP](/fluid-implicit-particle/), and under the blend with $\alpha = 0.95$?

4. ◦ A dam break starts from a water column of height $H = 0.5$ m with $\rho_0 = 1000$ kg/m³ and $g = 9.81$ m/s². Follow the rules of [weakly compressible SPH](/weakly-compressible-sph/): $v_{\max} = (2gH)^{1/2}$, $c = 10\,v_{\max}$, $B = \rho_0 c^2/7$. Find $c$, the pressure at 1% compression, and the largest step for $h = 0.02$ m with $\lambda = 0.4$. Compare the pressure with the hydrostatic pressure $\rho_0 g H$ at the bottom of the column.

5. ◦ With [Boussinesq buoyancy](/boussinesq-buoyancy/), $T_{amb} = 300$ K, $\beta = g/T_{amb}$ and $\alpha = g/\rho_0$ for $\rho_0 = 1.2$ kg/m³, find the vertical force per unit mass on a cell at 330 K with soot density $s = 0.1$ kg/m³. For what $s$ would the cell at 330 K neither rise nor sink? By what factor does the linear law overstate the ideal gas lift at 330 K?

6. ◦ In the [fire model](/fire-simulation/), take $\rho_f = 1$ kg/m³, $\rho_h = 0.25$ kg/m³ and the flame speed $S = 0.2$ m/s. Find the jump $J$ of the normal velocity across the core, the pressure drop $P$, and the factor by which the products fill more volume than the fuel they replace.

7. ◦ A single [Gerstner wave](/gerstner-waves/) in deep water has wavelength 20 m and amplitude $A = 1.5$ m. Find $k$, $\omega$, the period, the phase speed and the steepness $kA$. Where is the mean level, and how far above it is the crest and below it the trough? What is the largest amplitude without a cusp? A sum of three waves has $k_iA_i = 0.5, 0.4, 0.3$; which choppiness values $Q$ satisfy the no-loop condition?

8. ◦ For [FFT ocean synthesis](/fft-ocean-synthesis/) with the Phillips spectrum and wind speed $V = 20$ m/s, find $\ell$ and the peak wavelength along the wind. Is the peak on a patch of side $L = 200$ m? For $N = 256$, by what factor does one FFT frame beat the direct sum of $N^2$ waves at $N^2$ points, counting $N^2\log_2 N$ against $N^4$?

9. • In 1D, grid nodes sit at $x = 0$ and $x = 1$ and two particles of unit mass sit at $x = 0.25$ with $v = 2$ and at $x = 0.75$ with $v = 0$. With linear weights, transfer the velocity to the grid and back as PIC does. Give the grid velocities, the particle velocities, the momentum and the kinetic energy at each stage. What does FLIP return if the grid velocity does not change in between?

10. • Use the setting of exercise 9, but give the particles the velocities of the field $v(x) = 1 + 2x$ and, for [APIC](/affine-particle-in-cell/), the affine term $C_p = 2$. Show that the APIC round trip returns $v_p$ and $C_p$ exactly, while the PIC round trip returns $(1.875, 2.125)$. Then prove that APIC reproduces every linear field in 1D with linear weights.

11. • In the setting of exercise 9, put three particles of unit mass at $x = 0.25$, $0.5$ and $0.75$. Find a nonzero change of their velocities that gives zero momentum at both grid nodes. What happens to such a change under one PIC step and under one FLIP step? Explain what this has to do with the noise of FLIP.

12. • Run one semi-Lagrangian step of stable fluids on a periodic grid of six cells with $q = (0, 0, 1, 0, 0, 0)$, a constant velocity to the right and $u\,\Delta t/\Delta x = 2.3$. Then prove that for any velocity and any $\Delta t$ the step with linear interpolation never raises the maximum of $q$ or lowers its minimum.

13. • Apply [BFECC](/bfecc/) at $u\,\Delta t/\Delta x = 1/2$ to the periodic step $q = (0, 0, 0, 1, 1, 1, 1, 0, 0, 0)$, moving to the right. Give $\hat q$, the corrected field $\bar q$ and the new field. Which new values leave the range of the two old values that the plain step mixes, and what does the clamp limiter give?

14. • The density error of weakly compressible SPH is of order $(v/c)^2$. By what factor must $c$ grow to cut the error from 1% to 0.1%, and by what factor does the number of steps per second grow? In 2D at fixed $c$, by what factor does the cost of one simulated second grow when $h$ is halved and the particle spacing with it?

15. • A FULL cell of [Foster-Metaxas](/foster-metaxas-fluids/) lies against a wall, so it has $n_c = 3$ open faces, with $\Delta x = 0.1$ m and divergence 3 per second. Which $\beta_0$ makes one update balance the cell exactly? With $\beta_0 = 1.5$, what is the divergence after the update, and how much does the kinetic energy $\sum \tfrac12 v^2$ over the faces drop?

16. • The blobby field of [surface reconstruction from particles](/particle-fluid-surfacing/) is $\phi = T - \sum_i e^{-a|x - x_i|^2}$ with $T = 0.5$ and $a = \ln 2/0.25$. For two particles at distance $d$, find the radius of the neck at the midpoint as a function of $d$, and the largest $d$ at which the two blobs are joined.

17. • In stable fluids the diffusion step solves $(I - \alpha L)q' = q$, where $L$ is the 1D Laplacian with closed ends and $\alpha = \nu\,\Delta t/\Delta x^2$. Solve it for three cells with $q = (0, 3, 0)$ and $\alpha = 1$. Then take one explicit step $q' = (I + \alpha L)q$ with the same $\alpha$, and explain the difference.

18. ★ Let $A = 1 - c + c\,e^{-i\theta}$ be the amplification factor of the plain semi-Lagrangian step with linear interpolation, and let the backward step have the factor $\bar A$. Derive the factors $G = A(3 - |A|^2)/2$ of BFECC and $G = A + \tfrac12(1 - |A|^2)$ of the [MacCormack method](/unconditionally-stable-maccormack/), and show that both satisfy $|G| \le 1$. Evaluate $|A|$ and both $|G|$ at $c = 1/2$ for $\theta = \pi$ and for $\theta = \pi/2$.

19. ★ Show that for a constant velocity $u > 0$ and $0 < c = u\,\Delta t/\Delta x < 1$, the semi-Lagrangian step with linear interpolation is the first order upwind scheme, and that to leading order it solves the advection equation with an added diffusion $\nu_{num} = u\,\Delta x\,(1 - c)/2$. Evaluate $\nu_{num}$ for $u = 1$ m/s, $\Delta x = 1$ cm and $c = 1/4$, and compare it with the viscosity of water, $10^{-6}$ m²/s.

20. ★ [IISPH](/implicit-incompressible-sph/) solves its pressure system with relaxed Jacobi, $\omega = 1/2$. Take the symmetric positive definite matrix with ones on the diagonal and $0.7$ everywhere else, of size $3 \times 3$. Find the spectral radius of the Jacobi iteration matrix $I - \omega D^{-1}A$ for $\omega = 1$ and $\omega = 1/2$, and the largest $\omega$ for which the iteration converges. Why can plain Jacobi fail on a matrix like this when the diagonal is not dominant?

21. ★ On a MAC grid with closed walls, let $D$ be the discrete divergence and $G$ the discrete gradient. Show that $D = -G^{\mathsf T}$ (with $\Delta x = 1$), and use it to prove that the projection $u' = u - Gp$ with $DGp = Du$ satisfies $|u|^2 = |u'|^2 + |Gp|^2$. Then show that the checkerboard $p_{ij} = (-1)^{i+j}$ has a zero gradient under central differences on cell centers, but a nonzero gradient on the MAC faces.
