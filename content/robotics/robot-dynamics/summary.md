## What to remember

- A rigid robot with a fixed base obeys $M(q)\ddot q + C(q, \dot q)\dot q + g(q) = \tau$, with $M(q) = \sum_i (m_i J_{v_i}^T J_{v_i} + J_{\omega_i}^T I_i J_{\omega_i})$ symmetric positive definite. For the planar arm with two links of 1 m and point masses of 1 kg at the ends, $\det M = 2 - \cos^2 q_2 \ge 1$.
- $\dot M - 2C$ is skew-symmetric for the Christoffel form of $C$, and only for it. Every valid $C$ gives $\dot q^T(\dot M - 2C)\dot q = 0$, the energy balance, and that weaker fact is all PD control with gravity compensation needs. Slotine-Li adaptive control needs the full skew symmetry.
- The torques are linear in the inertial parameters, $\tau = Y(q, \dot q, \ddot q)\,\pi$ with ten numbers per link, but not in the lengths or the angles. Torque data fix only the base parameters, combinations such as $I_1 + m_2 l_1^2$, and only along an exciting motion.
- Inverse dynamics of a fixed-base robot always has exactly one answer, and forward dynamics has one because $M$ is positive definite. With a floating base, the six base rows have no actuator, so inverse dynamics with contact forces can have no solution or many, and is solved as a quadratic program.
- The recursive algorithms are exact for the rigid-body model. The recursive Newton-Euler algorithm solves inverse dynamics in $O(n)$ time, the composite rigid body algorithm forms $M$ in $O(nd)$ time for a tree of depth $d$, $O(n^2)$ for a chain, and the articulated-body algorithm solves forward dynamics in $O(n)$ time, which is optimal.
- The articulated-body inertia of a body is a Schur complement, $I^A_i = I^c_i - F H_s^{-1} F^T$, and it lies between the body and the locked subtree: $I_i \preceq I^A_i \preceq I^c_i$.
- The total momentum about the center of mass changes only by the contact wrenches and gravity: $\dot l = \sum_j f_j + mg$ and $\dot k = \sum_j ((p_j - c) \times f_j + \tau_j)$, six equations for any number of joints.
- Rigid contact is a complementarity: a gap or a force, never both. With Coulomb friction the force form can have no solution or several, the Painlevé paradox; for the sliding rod this needs $\mu > 4/3$. Stewart-Trinkle time stepping solves one LCP in impulses and velocities per step, and impulses restore a solution.

| Method | Computes | Serial chain | Tree of depth $d$ |
|---|---|---|---|
| [Euler-Lagrange](/euler-lagrange-manipulator-dynamics/), direct form | $\tau$ from the closed form | about $n^4$ | not used |
| [Recursive Newton-Euler](/recursive-newton-euler-algorithm/) | $\tau$ for given $\ddot q$ | $\Theta(n)$ | $\Theta(n)$ |
| [Composite rigid body](/composite-rigid-body-algorithm/) | $M(q)$ | $\Theta(n^2)$ | $\Theta(n + \sum_i \mathrm{depth}(i))$, $O(nd)$ |
| CRBA with Cholesky | $\ddot q$ | $O(n^3)$ | follows the tree with the $L^T L$ factorization |
| $n + 1$ calls of the RNEA, then a solve | $\ddot q$ | $O(n^2)$ to form, $O(n^3)$ to solve | same |
| [Articulated-body algorithm](/articulated-body-algorithm/) | $\ddot q$ | $\Theta(n)$ | $\Theta(n)$ |
| [Dynamics derivatives](/rigid-body-dynamics-derivatives/) | $\partial\tau/\partial q$, $\partial\tau/\partial\dot q$ | $\Theta(n^2)$ | $O(nd)$ |
| [Stewart-Trinkle step](/stewart-trinkle-time-stepping/) | $v^+$ with $m$ contact unknowns | $O(n^3 + n^2 m + n m^2)$ to set up, $\Theta(m^2)$ per pivot | same |

: The main computations of the chapter, for $n$ joints in the real RAM. The number of Lemke pivots in the last row is exponential in $m$ in the worst case and small in practice.

## Choosing a method

For the torques of a planned motion, as in the feedforward of a controller, use the recursive Newton-Euler algorithm; it is short and its cost is linear. Keep the closed form with the Christoffel $C$ for analysis and for controllers whose proofs use the skew symmetry.

For simulation of arms, legged robots and humanoids, whose branches are short, forming $M$ with the composite rigid body algorithm and factoring it is often faster than the articulated-body algorithm. For long chains the articulated-body algorithm wins, at about nine bodies or more in Featherstone's counts; the crossover depends on the implementation. A fourth-order Runge-Kutta step calls the forward dynamics four times.

For trajectory optimization and model predictive control, use the analytical derivatives rather than finite differences. For identification, choose base parameters, excite them all, and add physical consistency when the estimates feed a simulator. For legged robots, plan with the centroidal dynamics and the contact wrench cone, and turn the plan into torques with the floating-base equations and a quadratic program. For contact simulation, use a time-stepping method in impulses; use a compliant model when the share of each contact in the load matters, since a rigid model cannot fix it.
