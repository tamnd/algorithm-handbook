## What to remember

- An explicit step of a spring or element with frequency $\omega$ is stable only for $\omega\Delta t < 2$, and refining a cloth mesh raises $\omega_{\max}$, so the step shrinks with the spacing. The chapter's methods are ways around this limit.
- [Backward Euler](/backward-euler-method/) multiplies the energy of a linear oscillator by $1/(1 + (\omega\Delta t)^2)$ per step. It allows large steps and damps the motion; stable is not accurate.
- The [deformation gradient](/deformation-gradient/) $F = D_sD_m^{-1}$ is the input of every element model. Green strain does not see inversion. [St. Venant-Kirchhoff](/st-venant-kirchhoff-model/) softens under compression and its stress reverses past the flat state, [neo-Hookean](/neo-hookean-model/) is undefined for $J \le 0$, and [stable neo-Hookean](/stable-neo-hookean/) is finite and smooth for every $F$. No objective energy is both convex and unbounded as $J \to 0$.
- [Corotational](/corotational-fem/) elements remove the forces that a linear model gives under rotation. [Invertible elements](/invertible-finite-elements/) push inverted elements back, but their extended force is not the gradient of an energy below the threshold.
- [Position based dynamics](/position-based-dynamics/) is not physically exact: its stiffness depends on the sweep count and the step. [XPBD](/extended-position-based-dynamics/) gives the stiffness $1/\alpha$ when its sweeps converge, and converges to backward Euler for affine constraints with $\alpha > 0$; with turning gradients a gap remains. The gain of [small steps](/small-steps-physics/) is a measurement on chains and cloth.
- [Fast mass-spring](/fast-mass-spring/) and [projective dynamics](/projective-dynamics/) never raise the step objective and use one prefactored matrix, but converge only linearly. [Vertex block descent](/vertex-block-descent/) descends only with a line search, which its paper leaves out by default.
- [Robust cloth collision](/robust-cloth-collision/) ends with no intersection in exact arithmetic when no cubic of its test vanishes, with [impact zones](/impact-zones/) as the failsafe. [Incremental potential contact](/incremental-potential-contact/) keeps every iterate free of intersection only if its collision check is conservative. The speedups of [affine body dynamics](/affine-body-dynamics/) are measurements on its paper's scenes.

## The main methods compared

| Method | Step | Stiffness set by | Guarantee stated in the entry |
|---|---|---|---|
| [Mass-spring](/mass-spring-system/), explicit | symplectic Euler | $k$, but depends on the mesh | stable iff $\omega\Delta t < 2$ |
| [Provot strain limiting](/provot-strain-limiting/) | explicit plus projection | $\tau$ | sweeps converge if the limits are feasible |
| [Baraff-Witkin cloth](/baraff-witkin-cloth/) | one linearized backward Euler step | $k$ per condition | none; large steps measured |
| [Corotational FEM](/corotational-fem/) | implicit, approximate Newton | $\mu$, $\lambda$ | zero force under rotation |
| [PBD](/position-based-dynamics/) | projection, $n_s$ sweeps | $k$, $n_s$ and $\Delta t$ | linear momentum kept |
| [XPBD](/extended-position-based-dynamics/) | Gauss-Seidel on simplified Newton | compliance $\alpha$ | backward Euler for affine constraints, $\alpha > 0$ |
| [Shape matching](/meshless-shape-matching/) | pull toward a rigid fit | $\alpha$ and $\Delta t$ | bounded in the fixed goal model only |
| [Optimization integrator](/optimization-time-integration/) | Newton, line search | the energy | objective never rises |
| [Projective dynamics](/projective-dynamics/) | local and global | weights | objective never rises; linear rate measured |
| [Vertex block descent](/vertex-block-descent/) | vertex Newton steps | the energy | descent only with a line search |
| [IPC](/incremental-potential-contact/) | projected Newton, barrier | the energy and $\kappa$ | no intersection if the check is conservative |

: Methods of the chapter for the time step. A sweep of the local methods costs $\Theta(n + c)$ for $n$ particles and $c$ constraints or springs; Newton methods solve a sparse system per iteration.

For one particle of mass 1 at $x = 1.5$ on a spring of rest length 1 and stiffness 100 to a pin, with $\Delta t = 0.1$, fast mass-spring, projective dynamics, vertex block descent, XPBD with $\alpha = 0.01$ and the optimization integrator all give the backward Euler value $x = 1.25$ in one iteration, so the hand examples of the entries agree.

## Choosing a method

For games with a fixed budget per frame, use XPBD with substeps, or plain PBD when the stiffness only has to look right. Shape matching suits squishy objects without a mesh. For cloth in film, an implicit step with a hyperelastic or spring energy is the usual base: Baraff-Witkin, projective dynamics or vertex block descent for speed, the optimization integrator when the solver must not fail at large steps. Add strain limiting when the cloth must hardly stretch, and use discrete shells or the quadratic bending model for bending, discrete elastic rods for hair.

For solids, the corotated or stable neo-Hookean energy with finite elements handles large rotations and inversion; modal reduction fits bodies that only wobble near their rest shape. For cloth contact, use robust cloth collision with impact zones. When every state must be free of intersection, use incremental potential contact, and affine body dynamics for many stiff objects.
