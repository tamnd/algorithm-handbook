## What to remember

- **Homogenization.** For $-\nabla\cdot(A(x/\varepsilon)\nabla u_\varepsilon) = f$ with $A$ periodic, $u_\varepsilon \to u_0$, which solves the same equation with a constant $A^*$ from cell problems. Then $\langle A^{-1}\rangle^{-1} \le A^* \le \langle A\rangle$, in one dimension $a^*$ is the harmonic mean, and $\|u_\varepsilon - u_0\|_{L^2} \le C\varepsilon$; in $H^1$ a corrector is needed, and the error with it is $O(\varepsilon^{1/2})$.
- **Coarse bases.** The [multiscale finite element method](/multiscale-finite-element-method/) is exact at the nodes in one dimension but has a resonance error in two and three dimensions. [Localized orthogonal decomposition](/localized-orthogonal-decomposition/) has an error of order $H/\sqrt{\alpha}$ that does not depend on how fast the coefficient oscillates, with patches of $k \sim \log(1/H)$ layers.
- **Heterogeneous multiscale method.** The macro solver approximates the homogenized solution $u_0$, not $u_\varepsilon$. Its cost does not depend on $\varepsilon$; in one dimension the estimated coefficient has an error of order $\varepsilon/\delta$ for a micro domain of size $\delta$.
- **Atoms and continua.** The [Cauchy-Born rule](/cauchy-born-rule/) is proved to be accurate under a phonon stability condition and can fail without it. Energy-based coupling, as in the [quasicontinuum method](/quasicontinuum-method/), creates ghost forces at the interface when the potential reaches beyond nearest neighbours; force-based coupling removes them but has no energy.
- **Saddles.** At a fixed point of the [nudged elastic band](/nudged-elastic-band/), the climbing image is a stationary point of the energy; convergence is not proved, nor that the saddle is the lowest one. The same holds for the string and dimer methods.
- **Rates.** [Harmonic transition state theory](/harmonic-transition-state-theory/) gives $k = \frac{\prod_i \nu_i^{\min}}{\prod_j \nu_j^{\text{saddle}}} e^{-\Delta E/k_BT}$, equal to the TST rate when the potential is harmonic and to $k_{\mathrm{TST}}(1 + O(1/\beta))$ otherwise. TST itself overestimates the true rate. [Kinetic Monte Carlo](/kinetic-monte-carlo/) samples the jump process of a given rate catalogue exactly; its results are only as good as the catalogue.
- **Accelerated dynamics.** Hyperdynamics is exact for TST rates, parallel replica dynamics is exact when the replicas start in the quasi-stationary distribution, and temperature-accelerated dynamics misses an event with probability below $\delta$ per event if every prefactor is at least $\nu_{\min}$. In all three the boost is measured, not guaranteed.
- **Coarse-graining.** The [Mori-Zwanzig formalism](/mori-zwanzig-formalism/) is exact but has a memory term; dropping it is a theorem only under scale separation. Force matching projects the mean force onto a basis and adds no friction or noise.

## The methods side by side

| Method | Cost | What is proved |
|---|---|---|
| [Periodic homogenization](/periodic-homogenization/) | one cell problem per direction | $O(\varepsilon)$ error in $L^2$ for periodic coefficients |
| [FE²](/fe2-method/) | $\Theta(p\,q\,M\,n)$ | exact tangent and unique solution in 1D for convex cell energies |
| [Multiscale FEM](/multiscale-finite-element-method/) | $\Theta(N)$ | nodally exact in 1D; resonance error in 2D and 3D |
| [Heterogeneous multiscale method](/heterogeneous-multiscale-method/) | $\Theta(M\,n)$, independent of $\varepsilon$ | error in $A_K$ of order $\varepsilon/\delta$ in 1D |
| [Coarse projective integration](/coarse-projective-integration/) | $\Theta(n(k+1)s)$ | stability lemma for linear fast modes |
| [Quasicontinuum](/quasicontinuum-method/) | $O(I(N + n^3))$ | ghost forces with second neighbours; no error bound against atomistics |
| [Nudged elastic band](/nudged-elastic-band/) | $O(I\,N(G+d))$ | climbing image is stationary at a fixed point; convergence not proved |
| [Kinetic Monte Carlo](/kinetic-monte-carlo/) | $O(M)$ per event, $O(\log M)$ with a sum tree | exact sample for the rate catalogue |
| [Parallel replica dynamics](/parallel-replica-dynamics/) | work $O((mc+s)G)$ | exact from the quasi-stationary distribution; speedup at most $m$ |
| [Temperature-accelerated dynamics](/temperature-accelerated-dynamics/) | $O(n\,S)$ | an event is missed with probability at most $\delta$ if all prefactors are at least $\nu_{\min}$ |

: Costs as the entries state them, in each entry's own symbols.

## Choosing a method

For a periodic or statistically uniform microstructure with a linear law, compute the effective coefficient once, by homogenization or from a representative volume element, and run an ordinary finite element model. Use FE² or the heterogeneous multiscale method when the micro law is nonlinear or depends on the macro state, and the multiscale finite element method or localized orthogonal decomposition when the coefficient has no scale separation at all. Keep atoms only near a crack tip, a dislocation core or a reacting site, with the quasicontinuum or QM/MM method.

For rare events in a crystal, find saddles with the nudged elastic band or the dimer method, compute rates by harmonic transition state theory, and run kinetic Monte Carlo on the catalogue. If the catalogue is unknown, use accelerated molecular dynamics: parallel replica dynamics when many processors are free, hyperdynamics when a bias can be built that vanishes at every saddle, and temperature-accelerated dynamics when the harmonic approximation holds. With no clear saddle, as in soft matter, use transition path sampling or forward flux sampling.
