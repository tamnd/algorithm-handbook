## What to remember

- A trace is modelled as $d = w * r + n$, with the reflection coefficient $r_j = (Z_{j+1} - Z_j)/(Z_{j+1} + Z_j)$ at the two-way time of interface $j$. Second-order statistics do not see the phase of $w$. The normal equations of predictive deconvolution are Toeplitz, and Levinson solves them in $O(p^2)$.
- Normal moveout follows $t = \sqrt{t_0^2 + x^2/v^2}$. The correction stretches the wavelet by $t/t_0$. Stacking $F$ traces with independent noise lowers the noise by $\sqrt F$.
- Semblance lies in $[0, 1]$ and has the noise floor $1/m$ for $m$ traces. The Dix formula $v_n^2 = (V_n^2 t_n - V_{n-1}^2 t_{n-1})/(t_n - t_{n-1})$ is exact for flat layers with rms velocities, but it amplifies errors in thin layers and can give $v_n^2 < 0$ from noisy picks.
- Migration applies the adjoint $L^{\mathsf T}$ of the Born forward operator, not its inverse. Only wavenumbers on the circle $k_x^2 + k_z^2 = (2\omega/v)^2$ of the data band can appear in the image. Least-squares migration iterates toward the least-squares image and semi-converges on noisy data.
- Phase-shift migration is exact for $v(z)$ at all dips. The 15-degree finite-difference equation has a relative error of $6.0 \times 10^{-4}$ at 15° and $0.061$ at 45°. The split-step error per step is about $\Delta z\,\frac{k_x^2}{2\omega}(1/s - 1/s_0)$.
- Reverse time migration stores or recomputes the source wavefield: $O(sg)$ memory for $s$ steps on $g$ points, or $O(\sqrt s\, g)$ with checkpoints. Its explicit scheme in 2D is stable for a Courant number up to $1/\sqrt2$.
- The adjoint-state method gives the gradient of a misfit with one forward and one adjoint solve, whatever the number of parameters. Full waveform inversion is a nonconvex least-squares problem; for a shifted sinusoid the basin is $|\tau| < T/2$, and for a Ricker wavelet the misfit is largest at $|\tau| = 0.4315/f_0$.
- Surface-related multiple elimination is exact under its model, $P_0 = P(I + aP)^{-1}$; its iteration is a Neumann series that converges only when $\rho(aP) < 1$.
- Traveltime tomography linearizes $\delta T = \int \delta s\, dl$, since a change of the ray path changes the time only to second order. Its matrices have null spaces, such as the checkerboard on a $2 \times 2$ grid.

| Method | Velocity | Time | Status |
|---|---|---|---|
| [Kirchhoff migration](/kirchhoff-migration/) | any, with traveltimes | $O(n_x n_t\log n_t + n_z n_x a)$ | high-frequency approximation |
| [Phase-shift migration](/phase-shift-migration/) | $v(z)$ | $O(n_z n_t n_x + n_t n_x \log(n_t n_x))$ | exact for $v(z)$ |
| [Finite-difference migration](/finite-difference-migration/) | $v(x, z)$ | $O(n_z n_t n_x + n_x n_t\log n_t)$ | about 15 degrees |
| [Split-step Fourier migration](/split-step-fourier-migration/) | $v(x, z)$, moderate contrast | $O(n_z n_t n_x \log n_x + n_x n_t \log n_t)$ | exact for $v(z)$, angle error otherwise |
| [Stolt migration](/stolt-migration/) | constant | $O(p\,n_t n_x\log(p\,n_t n_x) + n_z n_x \log(n_z n_x))$ | exact up to interpolation |
| [Reverse time migration](/reverse-time-migration/) | $v(x, z)$ | $O(sg)$ per shot | exact adjoint of discrete Born modelling |
| [Least-squares migration](/least-squares-migration/) | as its adjoint | about $k$ times two migrations | converges to the least-squares image |
| [Full waveform inversion](/full-waveform-inversion/) | $v(x, z)$, estimated | $O(kesg)$ | local minima, needs a good start |

: Migration and inversion methods, 2D zero-offset costs from the entries: $n_t$, $n_x$, $n_z$ samples in time, traces and depth, $a$ aperture traces, $p$ padding, $s$ steps on $g$ grid points, $e$ shots, $k$ iterations.

## Choosing a method

Deconvolve with a predictive filter when the wavelet is close to minimum phase, and remove surface multiples with SRME when sources and receivers are dense, near offsets included; use the parabolic Radon transform when primaries and multiples differ clearly in moveout. Pick velocities with semblance, and use the Dix formula only on layers thick enough for the error amplification to stay small.

For migration, the velocity model decides. With a constant velocity, Stolt migration is the fastest. With velocity that varies only with depth, use phase shift. With moderate lateral changes, split-step Fourier or finite differences are cheap, at the price of errors at steep dips. Kirchhoff migration handles any velocity with computable traveltimes and can image one target region alone, but it is a high-frequency method. Reverse time migration, the most expensive, is the choice for steep dips and strong contrasts, such as below salt. When the amplitudes matter, run a few iterations of least-squares migration and stop before the noise grows.

To improve the velocity model itself, start with traveltime tomography, which is close to linear, and then run full waveform inversion from low frequencies upward. Check the starting model against the half-period rule at the lowest usable frequency.
