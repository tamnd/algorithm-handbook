## What to remember

- A weak solution satisfies the integral form of $U_t + F(U)_x = 0$. Its jumps obey the Rankine-Hugoniot condition $s(U_R - U_L) = F(U_R) - F(U_L)$. Weak solutions are not unique: an expansion shock of Burgers' equation is one. The Lax condition $\lambda_p(U_L) > s > \lambda_p(U_R)$, or an entropy inequality, picks the physical solution; for a scalar law Kruzkov's entropy solution exists and is unique.
- The Lax-Wendroff theorem: if a consistent scheme in conservation form converges boundedly almost everywhere, the limit is a weak solution. It need not be the entropy solution, and a scheme not in conservation form can move shocks at the wrong speed.
- Godunov's barrier: a linear scheme that creates no new extrema is at most first order. Every high-resolution scheme is therefore nonlinear. TVD and MUSCL schemes clip smooth extrema to first order; ENO and WENO do not clip them, but they too lose order at discontinuities. With shocks, every scheme converges at first order or less in $L^1$ in practice.
- A numerical flux approximates the Riemann problem between two cells. Rusanov uses one speed and smears everything; Roe resolves all waves but needs an entropy fix at transonic rarefactions and can give negative pressure; HLL uses two speeds and smears contacts; HLLC adds the contact back.
- The time step obeys the CFL condition $\Delta t \le \nu\Delta x/\max(|u| + c)$. It is necessary, not sufficient: forward Euler with central differences satisfies it and is unstable. SSP Runge-Kutta methods are convex combinations of Euler steps and keep the Euler step's convex bounds under $\Delta t \le C\Delta t_{FE}$, with $C \le s$ for $s$ stages; no SSP method has four stages and order 4, and none has order 5 or more.
- The discontinuous Galerkin method with $P^k$ elements is conservative and observed to converge at order $k + 1$, with a time step near $\Delta x/(2k + 1)$. Shocks need a limiter. The Zhang-Shu limiter keeps density and pressure positive while keeping the order; entropy stable fluxes give $\frac{d}{dt}\sum U\Delta x \le 0$, but only in the semi-discrete scheme.
- Hydrostatic reconstruction keeps the lake at rest to rounding error; Berger-Colella refinement keeps mass only with refluxing; the ghost fluid method keeps a contact clean but is not conservative.
- For linear waves energy is the tool. The Yee scheme conserves a discrete energy and is stable for $c\Delta t \le 1/\sqrt{\sum_d \Delta x_d^{-2}}$. A perfectly matched layer reflects nothing only in the continuous equations. SBP operators with SAT penalties $\tau \ge \frac12$ give a provable energy estimate.

## Numerical fluxes compared

| Flux | Waves used | Stationary contact | Entropy | Sod, $L^1$ error, 100 cells |
|---|---|---|---|---|
| [Rusanov](/rusanov-flux/) | one speed $s$ | smeared | E-scheme; no fix needed | 0.02148 |
| [Roe](/roe-solver/) | all, linearized | exact | needs a fix at sonic points | 0.01319 |
| [HLL](/hll-riemann-solver/) | two speeds | smeared | cell entropy inequality if speeds bound the waves | 0.01505 |
| [HLLC](/hllc-riemann-solver/) | three waves | exact | no inequality proved | 0.01387 |
| [Steger-Warming](/flux-vector-splitting/) | split eigenvalues | smeared | monotone for scalar laws | 0.01881 |
| van Leer splitting | split Mach number | smeared | monotone for scalar laws | 0.01457 |
| [AUSM](/ausm-scheme/) | Mach and pressure split | exact | not proved | 0.01484 (Courant 0.5) |

: First-order fluxes with forward Euler on Sod's shock tube at $t = 0.2$, at Courant number 0.9 unless marked, as measured in the entries. At Courant number 0.5 the AUSM entry gives 0.01626 for Roe.

## Choosing a method

For a first code, use MUSCL with the van Leer or MC limiter, the HLLC flux and third-order SSP Runge-Kutta. The parts can be swapped one at a time. Rusanov's flux is the safe choice when the eigenstructure is unknown or positivity matters more than resolution. Roe's flux needs the Harten-Hyman fix and fails near vacuum, where HLL and HLLC stay positive.

Higher order pays in the smooth regions: use ENO, WENO or DG with a limiter there. Central schemes such as Kurganov-Tadmor need only the largest wave speed, so they apply at once to a new system. For blast waves and low density, add the positivity-preserving limiter rather than lowering the Courant number by trial.

For rivers, lakes and the atmosphere use a well-balanced scheme, or the error in the steady state can exceed the waves you want. Use adaptive refinement, with refluxing, when shocks fill a small part of the domain. For electromagnetics and acoustics use the Yee scheme with a graded PML, and SBP-SAT operators for a high-order finite difference code with provable stability.
