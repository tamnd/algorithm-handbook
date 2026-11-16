## What to remember

- The [maximum principle](/pontryagin-maximum-principle/) is a necessary condition: an optimal input minimizes the Hamiltonian $H = \lambda_0 L + \lambda^T f$ at almost every time, along a state and costate that solve the canonical equations. The [Hamilton-Jacobi-Bellman equation](/hamilton-jacobi-bellman-equation/) gives a sufficient one: a $C^1$ solution is the value function. In general the value function is not smooth and solves the equation only in the viscosity sense.
- For a linear model and a quadratic cost with $R > 0$, the optimal input is $u = -Kx$, with $K = R^{-1} B^T P$ in continuous time and $K = (R + B^T P B)^{-1} B^T P A$ in discrete time. When $(A, B)$ is stabilizable and $(Q^{1/2}, A)$ is detectable, the Riccati equation has exactly one stabilizing solution $P$, and the optimal cost is $x_0^T P x_0$.
- On a finite horizon the gains come from the Riccati recursion run backward, in $O(N(n^3 + m^3))$ time. Under the same conditions the recursion from $P = 0$ converges to the stabilizing solution.
- The continuous-time single-input LQR loop has $|1 + L(j\omega)| \ge 1$, so it stays stable for every gain factor above $1/2$ and has a phase margin of at least 60 degrees. Discrete-time LQR has no such guarantee, and [LQG](/lqg-control/) has no guaranteed margins at all ([Doyle 1978](/lqg-guaranteed-margins-counterexample/)).
- LQG puts a [Kalman-Bucy filter](/kalman-bucy-filter/) in front of the LQR gain. It is optimal for a linear model with Gaussian white noise, and under the standard assumptions it is also the [H2 optimal controller](/h2-optimal-control/).
- [Linear MPC](/linear-mpc/) solves a convex quadratic program in the $Nm$ future inputs at each sample. With no active constraint and the DARE solution as terminal cost, it gives the LQR law for every $N \ge 1$. With constraints the law is continuous and piecewise affine, which [explicit MPC](/explicit-mpc/) stores region by region.
- The [MPC stability theorem](/mpc-stability-theorem/) needs a terminal set that a local law keeps invariant inside the constraints, and a terminal cost that falls by at least the stage cost under that law. Then the nominal loop is recursively feasible and asymptotically stable on the feasible set. Without them a short horizon can fail: on $x^+ = 2x + u$ with no terminal cost, horizon 1 gives an unstable loop and horizon 2 one that is not asymptotically stable.
- [Tube MPC](/tube-mpc/) meets the constraints for every disturbance in a bounded set, [min-max MPC](/min-max-mpc/) plans for the worst case, and [stochastic MPC](/stochastic-mpc/) makes each predicted constraint hold with a given probability.

| Method | Cost | What is guaranteed |
|---|---|---|
| Finite-horizon LQR | $O(N(n^3 + m^3))$ | optimal for the model and cost |
| Schur method | $O(n^3)$ typical | stabilizing solution, no starting gain needed |
| Kleinman iteration | $O(k(n^3 + m^3))$ | needs a stabilizing $K_0$; monotone, quadratic convergence |
| LQG | $O(in^3 + n^2(m + p))$ | optimal for linear Gaussian models; no margins |
| Dynamic matrix control | $O(PL)$ per sample | integral action; no stability guarantee |
| Linear MPC | $O(t(cNm + N^2m^2))$ per sample | stable and feasible with terminal ingredients |
| Explicit MPC | $O(M(c + n)n)$ online | same law as online MPC; $M$ can be exponential in $c$ |
| Tube MPC | $O(IL^2)$ per sample | constraints met for every disturbance in the set |

: The main methods of the chapter, with the worst-case costs of their entries. Here $k$ counts Newton steps, $i$ sign function iterations, $t$ QP iterations, $I$ simplex pivots, $c$ constraint rows and $M$ regions; $P$ is the prediction horizon and $L$ the length of the step response or the size of the LP. Iteration counts and solve times are measurements.

## Choosing a method

With a linear model, no hard limits and the full state, use infinite-horizon LQR, with the [Schur method](/schur-method-riccati/) or with the [Kleinman iteration](/kleinman-iteration/) from a known stabilizing gain. If only outputs are measured, design LQG and check the margins of the loop you get, or use [loop transfer recovery](/loop-transfer-recovery/) for a square minimum-phase plant.

With limits on inputs or states, use linear MPC with the DARE terminal cost and a terminal set such as the [maximal positively invariant set](/maximal-positively-invariant-set/) of the LQR loop. Add [offset-free MPC](/offset-free-mpc/) when constant setpoints must be reached with an imperfect model. Explicit MPC suits small systems with short sample times. A [reference governor](/reference-governor/) protects an existing loop from its limits at a lower cost than MPC.

For nonlinear models, use [nonlinear MPC](/nonlinear-mpc/), with the [real-time iteration](/real-time-iteration/) when the sample time is short, and accept that each solve finds a local optimum.
