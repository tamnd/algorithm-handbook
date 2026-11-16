Take a cart on a frictionless track, pushed by a force $u$: its position $x_1$ and speed $x_2$ obey $\dot x_1 = x_2$, $\dot x_2 = u$. The task is to bring it back to the origin. A designer can pick feedback gains by hand and look at the response, or can state what a good response is and let mathematics find the input. Asking for the least value of $\int_0^\infty (x_1^2 + x_2^2 + u^2)\, dt$ gives the feedback $u = -x_1 - \sqrt 3\, x_2$, with closed-loop polynomial $s^2 + \sqrt 3\, s + 1$. Asking instead for the shortest time with $|u| \le 1$ gives an input that sits at $+1$ or $-1$ and switches at most once, on a parabola in the plane. The first is the [linear quadratic regulator](/lqr-problem/), the second [time-optimal control](/time-optimal-control/). Both are answers to one question: which input minimizes a cost along the solution of a model.

This chapter treats that question in three layers. The first is the theory: what an optimal input must satisfy and what makes an input optimal. The second is the linear quadratic case, where the answer is a linear feedback computed from a Riccati equation, with filters and margins around it. The third is [model predictive control](/model-predictive-control/) (MPC), which solves a finite-horizon problem again at every sample and so handles limits on inputs and states. MPC has run refineries and chemical plants since the late 1970s, and fast solvers now put it in vehicles, engines and other machines with short sample times. Every result below holds for a stated model: linear or nonlinear, continuous or discrete time, known plant or bounded or random disturbances. The entries keep these conditions, and so should you.

## What the chapter covers

1. **The optimal control problem and its conditions.** The [optimal control problem](/optimal-control-problem/), the [Euler-Lagrange equation](/euler-lagrange-equation/), the [Hamiltonian](/control-hamiltonian/) and [costate](/costate/), the [maximum principle](/pontryagin-maximum-principle/) as a necessary condition, the [Hamilton-Jacobi-Bellman equation](/hamilton-jacobi-bellman-equation/) as a sufficient one, and the [indirect method](/indirect-method-optimal-control/) that solves the resulting boundary value problem by shooting.
2. **Minimum energy and minimum time.** [Minimum-energy control](/minimum-energy-control/) through the controllability Gramian, time-optimal control, the [bang-bang principle](/bang-bang-control/) and [singular arcs](/singular-arc/).
3. **The linear quadratic regulator.** [Finite-horizon LQR](/finite-horizon-lqr/) by a backward Riccati recursion, the [continuous](/continuous-algebraic-riccati-equation/) and [discrete](/discrete-algebraic-riccati-equation/) algebraic Riccati equations, [infinite-horizon LQR](/infinite-horizon-lqr/), and the [stability margins](/lqr-stability-margins/) of the continuous-time loop.
4. **Solving the Riccati equation.** The [Hamiltonian matrix](/hamiltonian-matrix/), the [stabilizing solution theorem](/stabilizing-riccati-solution-theorem/), the [Schur method](/schur-method-riccati/) and the [Kleinman iteration](/kleinman-iteration/).
5. **Output feedback, LQG and H2.** The [Kalman-Bucy filter](/kalman-bucy-filter/), [LQG control](/lqg-control/), [H2 optimal control](/h2-optimal-control/), [Doyle's counterexample](/lqg-guaranteed-margins-counterexample/) on LQG margins, and [loop transfer recovery](/loop-transfer-recovery/).
6. **Model predictive control.** The receding-horizon template, the industrial [dynamic matrix control](/dynamic-matrix-control/) and [generalized predictive control](/generalized-predictive-control/), [linear MPC as a quadratic program](/linear-mpc/), [offset-free MPC](/offset-free-mpc/), and [explicit MPC](/explicit-mpc/) through [multiparametric quadratic programming](/multiparametric-quadratic-programming/).
7. **Invariant sets, feasibility and stability.** [Positively invariant](/positively-invariant-set/) and [control invariant](/control-invariant-set/) sets, the [maximal positively invariant set](/maximal-positively-invariant-set/), [recursive feasibility](/recursive-feasibility/), the [stability theorem with terminal ingredients](/mpc-stability-theorem/), and the [reference governor](/reference-governor/).
8. **Nonlinear and economic MPC.** [Nonlinear MPC](/nonlinear-mpc/), the [real-time iteration](/real-time-iteration/) and [economic MPC](/economic-mpc/).
9. **MPC under uncertainty.** [Min-max MPC](/min-max-mpc/), [tube MPC](/tube-mpc/) and [stochastic MPC](/stochastic-mpc/).

## A first reading

Read these first, in this order:

1. [Optimal control problem](/optimal-control-problem/)
2. [Hamiltonian of an optimal control problem](/control-hamiltonian/)
3. [Pontryagin maximum principle](/pontryagin-maximum-principle/)
4. [Hamilton-Jacobi-Bellman equation](/hamilton-jacobi-bellman-equation/)
5. [Linear quadratic regulator problem](/lqr-problem/)
6. [Finite-horizon LQR](/finite-horizon-lqr/)
7. [Discrete algebraic Riccati equation](/discrete-algebraic-riccati-equation/)
8. [Infinite-horizon LQR](/infinite-horizon-lqr/)
9. [LQR stability margins](/lqr-stability-margins/)
10. [LQG control](/lqg-control/)
11. [Model predictive control](/model-predictive-control/)
12. [Linear MPC as a quadratic program](/linear-mpc/)
13. [Control invariant set](/control-invariant-set/)
14. [Recursive feasibility](/recursive-feasibility/)
15. [Stability of MPC with terminal ingredients](/mpc-stability-theorem/)

That path goes from the problem to its two kinds of conditions, through the linear quadratic case to its receding-horizon form with constraints, and ends with the theorem that makes MPC safe to use. Skip at first the transversality conditions, singular arcs, the Riccati solvers, H2 control, loop transfer recovery, explicit MPC and the last two groups. Read the [continuous algebraic Riccati equation](/continuous-algebraic-riccati-equation/) next to the discrete one if you work in continuous time.

## Before you start

The models come from the [state-space representation](/state-space-representation/) and [zero-order hold discretization](/zero-order-hold-discretization/) of the modeling chapter. The LQR results need [stabilizability](/stabilizability/), [detectability](/detectability/) and the [controllability Gramian](/controllability-gramian/) from the state space control chapter, and the stability results need [Lyapunov functions](/lyapunov-function/). Dynamic programming enters through the [principle of optimality](/principle-of-optimality/) of Volume 2 and the [Bellman equation](/bellman-equation/) of Volume 29. The matrix work uses [positive definite matrices](/positive-definite-matrix/), the [Lyapunov equation](/lyapunov-equation/), the [Schur decomposition](/schur-decomposition/) and [Newton's method for systems](/newton-method-for-systems/) from Volume 12. MPC is built on [quadratic programming](/quadratic-programming/), the [KKT conditions](/kkt-conditions/) and [linear programming](/linear-programming-problem/) of Volume 15. The discrete-time [Kalman filter](/kalman-filter/) is in Volume 28; this chapter gives only its continuous-time form. You should be at ease with matrix algebra, eigenvalues and linear differential equations.
