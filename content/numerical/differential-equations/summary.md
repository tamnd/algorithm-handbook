## What to remember

- An initial value problem $y' = f(t, y)$, $y(t_0) = y_0$ has one solution when $f$ is [Lipschitz](/lipschitz-condition/) in $y$. The same constant $L$ bounds how fast errors can grow, by a factor $e^{L(t - t_0)}$ ([Gronwall's inequality](/gronwall-inequality/)).
- A method of order $p$ makes a [local error](/local-truncation-error/) of size $O(h^{p+1})$ per step and a [global error](/global-error/) of $O(h^p)$ on a fixed interval. Halving $h$ divides the error by about $2^p$, which is how order is checked in practice.
- Convergence needs consistency and stability. For multistep methods this is [Dahlquist's theorem](/dahlquist-equivalence-theorem/), with [zero-stability](/zero-stability/) as the stability part; for linear PDE schemes it is the [Lax equivalence theorem](/lax-equivalence-theorem/).
- On $y' = \lambda y$ a one-step method gives $y_{n+1} = R(h\lambda)y_n$, and the step is stable when $|R(h\lambda)| \le 1$. Explicit methods have bounded [stability regions](/stability-region/), so a fast decaying component limits their step even when it no longer affects the solution. That is [stiffness](/stiff-ode-problem/).
- [A-stable](/a-stability/) methods are stable on the whole left half-plane; [L-stable](/l-stability/) ones also damp very stiff components in one step. No A-stable multistep method has order above 2 ([Dahlquist's barrier](/dahlquist-barrier/)), which is why stiff codes use BDF of order up to 5 or implicit Runge-Kutta methods.
- Production codes control the step. An [embedded pair](/embedded-runge-kutta-pairs/) gives an error estimate for free, and when the estimate behaves like $Ch^q$ the next step is $h(\text{tol}/\text{err})^{1/q}$, times a safety factor such as $0.9$.
- Long integrations of Hamiltonian systems need [symplectic](/symplectic-integrators/) methods such as [Verlet](/verlet-integration/): their energy error stays bounded instead of drifting.
- For a time-dependent PDE, explicit schemes have a step limit set by the grid: $\Delta t \le \Delta x^2/(2\kappa)$ for [FTCS](/ftcs-method/) on the heat equation, and the [CFL condition](/courant-friedrichs-lewy-condition/) $|a|\Delta t \le \Delta x$ for advection.
- A linear scheme that never creates new oscillations is at most first order (Godunov). Shock-capturing schemes such as [flux limiters](/flux-limiter-methods/) and [WENO](/weno-scheme/) are nonlinear to get around this.

## Methods side by side

| Method | Type | Order | $f$ evaluations per step | Linear stability |
|---|---|---|---|---|
| [Euler](/euler-method/) | explicit one-step | 1 | 1 | real interval $[-2, 0]$ |
| [Heun](/heuns-method/), [midpoint](/explicit-midpoint-method/) | explicit RK | 2 | 2 | real interval $[-2, 0]$ |
| [RK4](/classical-runge-kutta-4/) | explicit RK | 4 | 4 | real interval $[-2.785, 0]$ |
| [Dormand-Prince](/dormand-prince-method/) 5(4) | explicit embedded pair | 5 | 6 (7 stages, FSAL) | bounded region |
| [Adams-Bashforth](/adams-bashforth-methods/), $k$ steps | explicit multistep | $k$ | 1 | region shrinks as $k$ grows |
| [Adams-Moulton](/adams-moulton-methods/), $k$ steps | implicit multistep | $k + 1$ | Newton iterations | bounded for $k \ge 2$ |
| [Backward Euler](/backward-euler-method/) | implicit one-step | 1 | Newton iterations | A- and L-stable |
| [BDF](/backward-differentiation-formulas/), $k \le 6$ | implicit multistep | $k$ | Newton iterations | A-stable for $k \le 2$, nearly so up to 5 |
| [Gauss](/gauss-legendre-runge-kutta/), $s$ stages | implicit RK | $2s$ | Newton iterations | A-stable, symplectic |
| [Radau IIA](/radau-iia-methods/), $s$ stages | implicit RK | $2s - 1$ | Newton iterations | A- and L-stable |
| [Rosenbrock](/rosenbrock-methods/) | linearly implicit RK | up to 4 in common codes | $s$, plus one Jacobian | A- or L-stable by design |
| [Verlet](/verlet-integration/) | explicit, symplectic | 2 | 1 force | stable for $h\omega < 2$ |

: Methods for $y' = f(t, y)$. Real intervals are the part of the negative real axis inside the stability region; the Verlet bound is for the oscillator $q'' = -\omega^2 q$.

## Choosing a method

Start with an adaptive explicit pair such as Dormand-Prince at a relative tolerance a little tighter than the accuracy you need. If it takes many small steps while the solution changes slowly, or the step count barely changes when the tolerance is loosened, the problem is stiff: switch to a BDF code or a Radau IIA code, and supply the Jacobian if you can. For tolerances near $10^{-10}$ and below on smooth problems, high-order pairs, Adams codes or [Bulirsch-Stoer](/bulirsch-stoer-method/) use fewer evaluations. For long runs of a mechanical system, use Verlet or another symplectic method with a fixed step. Constraints call for a DAE solver such as Radau IIA, after checking the [index](/differentiation-index/).

For PDEs, choose the space discretization first. Finite differences suit simple domains, [finite elements](/finite-element-method/) suit general meshes and elliptic problems, and [spectral methods](/spectral-methods/) suit smooth solutions on simple domains. Then treat time by the [method of lines](/method-of-lines/): diffusion makes the system stiff, so use an implicit or [Crank-Nicolson](/crank-nicolson-method/) step, while advection allows an explicit step under a CFL limit. For conservation laws with shocks, use a [finite volume](/finite-volume-method/) scheme with a [Godunov](/godunov-method/)-type flux and a limiter or WENO reconstruction.
