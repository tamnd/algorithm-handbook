## What to remember

- In a slab with one speed and isotropic scattering, the transport equation is $\mu\,\partial_x\psi + \Sigma_t\psi = (\Sigma_s\phi + Q)/2$ with $\phi = \int_{-1}^{1}\psi\,d\mu$. In an infinite medium $\phi = Q/\Sigma_a$, and a particle has $1/(1 - c)$ collisions on average, where $c = \Sigma_s/\Sigma_t$.
- A free flight in a uniform medium has length $s = -\ln\xi/\Sigma_t$. In a medium made of regions, one sampled optical depth $-\ln\xi$ is spent region by region. The collision estimator scores $w/\Sigma_t$ at each collision and the track-length estimator scores $w\ell$ for each track of length $\ell$; both are unbiased for the volume integral of the flux.
- Implicit capture, splitting, roulette and weight windows keep every tally unbiased when they are played as their entries state. They do not always lower the variance: that depends on how well the game fits the problem. The exponential transform with $\Sigma^* = \Sigma_t(1 - p\mu)$ gives the collision tally of an infinite medium with isotropic scattering an infinite variance once $c \ge p/\operatorname{artanh} p$.
- The adjoint flux $\phi^+$ is the expected score of a particle. CADIS samples the source from $q\phi^+/R$ and centres the weight window on $\bar w = R/\phi^+$, so particles are born with the weight that the window expects.
- Diffusion theory uses $J = -D\nabla\phi$ with $D = 1/(3\Sigma_{tr})$. It holds where scattering dominates and the flux is nearly isotropic. In an infinite medium the flux far from a plane source decays like $e^{-\kappa\Sigma_t x}$ with $\kappa^2 = 3(1 - c)$ in diffusion and $c\operatorname{artanh}(\kappa)/\kappa = 1$ in transport.
- Source iteration reduces the error by about $c$ per sweep in a thick medium. Diffusion synthetic acceleration lowers the factor to $0.2247c$ in the Fourier analysis, provided the diffusion solve is discretized consistently with the transport sweep; an inconsistent one can diverge on thick cells.
- Discrete ordinates has ray effects and, with diamond differences, a negative cell flux when $\Sigma_t\Delta x > 2|\mu|$. The $P_N$ method has no ray effects, can also go negative, and for $N = 1$ is diffusion theory.
- Power iteration for $k_{\mathrm{eff}}$ removes the higher modes by the dominance ratio per generation, which tends to 1 for large reactors. Monte Carlo cycles are correlated, so the naive error bars of local tallies are too small, and a flat fission source entropy is necessary for source convergence but not sufficient.

| Method | Cost | Error | Main weakness |
|---|---|---|---|
| [Analog Monte Carlo](/analog-monte-carlo-transport/) | $O(NK)$ for $N$ histories of $K$ events | statistical, $\propto N^{-1/2}$ | rare events need very many histories |
| Monte Carlo with [weight windows](/weight-window/) | as analog, plus the window checks | statistical, smaller when the windows fit | needs an importance map |
| [Discrete ordinates](/discrete-ordinates-method/) with [source iteration](/source-iteration/) | $O(INM)$ | quadrature and mesh | ray effects; $I$ large when $c \to 1$ |
| Discrete ordinates with [DSA](/diffusion-synthetic-acceleration/) | $O(INM)$ with small $I$ | as above | the diffusion solve must be consistent |
| [Spherical harmonics](/spherical-harmonics-method/) $P_N$ | $O(MN^3)$ | truncation in angle | oscillations and negative fluxes |
| [Method of characteristics](/method-of-characteristics-transport/) | $O(ITP)$ | track spacing and angles | many long tracks |
| [Diffusion](/diffusion-approximation-of-transport/) | one elliptic solve | model error | wrong near boundaries, sources and strong absorbers |

: Main methods of the chapter. $N$ is the number of histories or of directions, $M$ the number of cells, $I$ the number of iterations, $T$ the number of tracks and $P$ the number of segments per track; the costs are the ones in the entries.

## Choosing a method

- When the geometry is complex and the answer is a few integrated quantities, use Monte Carlo with continuous energy. It has no discretization error in space, angle or energy, only statistics.
- When the answer is a rare event in a thick shield, analog Monte Carlo is hopeless. Run a cheap deterministic adjoint and use CADIS, or FW-CADIS for a map of the whole problem.
- When you need the flux everywhere, or many runs of a lattice, use discrete ordinates or the method of characteristics, always with an acceleration when $c$ is near 1.
- Use diffusion for whole-core reactor calculations with homogenized, multigroup data, and check it against transport near boundaries and absorbers.
- In criticality runs, discard enough inactive cycles, watch the source entropy, and do not trust the naive error bars of local tallies.
