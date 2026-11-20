## What to remember

- Direct summation visits $N(N-1)/2$ pairs, so it costs $\Theta(N^2)$ per step. Its forces are exact up to rounding, and they are antisymmetric in each pair, so the total momentum is conserved.
- Plummer softening caps the pair force at $\frac{2}{3\sqrt3}\, G m_i m_j / \epsilon^2$, reached at $r = \epsilon/\sqrt2$, and changes it by about $\frac32 \epsilon^2 / r^2$ far away. It changes the physics at short range; it is a choice of model.
- A multipole expansion of degree $p$ about a ball of radius $a$ has error at most $\frac{GM}{r-a} (a/r)^{p+1}$ at distance $r$. In 3D it has $(p+1)^2$ coefficients, in 2D $p+1$. Well-separated boxes give the ratio $\sqrt3/3$ in 3D and $\sqrt2/3$ in 2D.
- Barnes-Hut accepts a cell when $s/d < \theta$. It takes $\Theta(N \log N)$ time on typical distributions and $\Theta(N^2)$ in the worst case. With $\theta > 1/\sqrt3$ it can accept a cell that contains the target. Its forces are not symmetric, so momentum drifts.
- The fast multipole method costs $O(N)$ for a fixed order $p$, and $p = O(\log(1/\varepsilon))$ for an accuracy $\varepsilon$; in 2D the count is about $40 N p$. A uniform tree degrades to $\Theta(N^2)$ when the bodies cluster, and the adaptive tree fixes this.
- Particle-mesh codes cost $\Theta(N + M \log M)$ with $M$ mesh points. NGP, CIC and TSC are B-splines of orders 1, 2 and 3; using the same weights to assign and to interpolate gives zero self-force and conserves momentum, but not energy. The force is smoothed over about one cell, and P3M or TreePM restore it at short range.
- Particle-in-cell plasma codes need $\omega_p h < 2$ for the leapfrog and $\Delta x \lesssim \lambda_D$ on the mesh. The Boris rotation turns the velocity by $2\arctan(\Omega h/2)$, keeps the speed exactly in a pure magnetic field, and is time reversible and volume preserving, but not symplectic.
- The Hermite scheme is fourth order with one force evaluation per step and is not symplectic; block steps $h_0/2^k$ cut the work further and give up momentum conservation. Wisdom-Holman is symplectic and second order, with error $O(\varepsilon h^2)$ for a perturbation of relative size $\varepsilon$, and exact for one planet.

| Method | Cost of one force evaluation | Accuracy in the entries' tests | Exact conservation |
|---|---|---|---|
| [Direct summation](/direct-n-body-summation/) | $\Theta(N^2)$ | rounding only | momentum |
| [Barnes-Hut](/barnes-hut-algorithm/) | $\Theta(N \log N)$ typical, $\Theta(N^2)$ worst | median $5.7 \times 10^{-3}$ at $\theta = 0.5$, $9.7 \times 10^{-4}$ at $\theta = 0.3$ | none |
| [Fast multipole method](/fast-multipole-method/) | $O(N)$ for fixed $p$, about $40 N p$ in 2D | falls geometrically in $p$ | none |
| [Black-box FMM](/black-box-fast-multipole-method/) | $\Theta(N n^2)$ best | $9.5 \times 10^{-5}$ with $n = 4$, $5.8 \times 10^{-8}$ with $n = 8$ | none |
| [Particle-mesh](/particle-mesh-method/) | $\Theta(N + M \log M)$ | force smoothed over about one cell | momentum |
| [P3M](/p3m-method/) | mesh plus short-range pairs, $\Theta(N^2)$ worst | $4.4 \times 10^{-4}$ on a $32^2$ mesh with TSC | none |
| [TreePM](/treepm-method/) | tree plus mesh, $\Theta(N \log N)$ on top of the FFT | $7.6 \times 10^{-4}$ at $\theta = 0$, $r_s = 1.25$ cells | none for $\theta > 0$ |

: Force methods of the chapter. Barnes-Hut: 300 random bodies in 3D. Black-box FMM: 400 points in the plane, logarithmic kernel. P3M (optimal influence function) and TreePM: 200 particles in 2D.

## Choosing a method

When every close encounter matters, as in a star cluster, use direct summation with Hermite steps and block time steps, and regularize close binaries. For a planetary system, use Wisdom-Holman: its error scales with the planetary masses, and it keeps a nearby modified energy bounded for a fixed step.

For a large collisionless system, such as a galaxy or a cosmological box, use a tree, a mesh or both. Barnes-Hut is simple and adapts to any clustering; choose $\theta$ by measuring the force error on the actual distribution. A periodic box with mild clustering suits particle-mesh; strong clustering calls for P3M or TreePM, and TreePM keeps its cost when P3M's pair sum grows. Soften in all of them, and choose $\epsilon$ as part of the model.

For many digits, or kernels other than gravity, use the fast multipole method: the classical one for the Laplace kernel, the adaptive one for clustered points, the kernel-independent or black-box ones when no analytic expansion is at hand, and the fast Gauss transform for Gaussian sums. For plasmas, use particle-in-cell with the Boris pusher, and resolve the Debye length and the plasma frequency.
