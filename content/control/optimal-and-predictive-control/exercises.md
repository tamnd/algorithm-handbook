1. ◦ For $\dot x = x + u$ with the running cost $L = x^2 + u^2$ and no bound on $u$, write the [Hamiltonian](/control-hamiltonian/) in the normal case $\lambda_0 = 1$. Give the input that minimizes it, the state equation and the [costate](/costate/) equation.

2. ◦ Take the scalar plant $\dot x = 3x + u$ with $q = 16$ and $r = 1$. Solve the [continuous algebraic Riccati equation](/continuous-algebraic-riccati-equation/) for its stabilizing root $p$, and give the gain, the closed-loop pole and the optimal cost from $x_0$. Then find the eigenvalues of the [Hamiltonian matrix](/hamiltonian-matrix/) $\begin{bmatrix} 3 & -1 \\ -16 & -3 \end{bmatrix}$ and read $p$ off its stable eigenvector.

3. ◦ Run [MPC](/model-predictive-control/) on $x_{k+1} = x_k + u_k$ with the stage cost $x^2 + u^2$, no constraints and no terminal cost. For the horizons $N = 1, 2, 3$, find the gain $K_N$ of the law $u = -K_N x$ and the closed-loop factor $1 - K_N$. Which horizon does not give an asymptotically stable loop?

4. ◦ Is the unit box $\{x : |x_1| \le 1, |x_2| \le 1\}$ a [positively invariant set](/positively-invariant-set/) of $x_{k+1} = A x_k$ for $A = \begin{bmatrix} 0.5 & 0.4 \\ -0.3 & 0.6 \end{bmatrix}$? For $A = \begin{bmatrix} 0.6 & 0.5 \\ -0.2 & 0.3 \end{bmatrix}$? For the second matrix, find all $c > 0$ for which the box $|x_1| \le c$, $|x_2| \le 1$ is positively invariant.

5. ◦ The LQR gain for $\dot x = x + u$ with $q = r = 1$ is $K = 1 + \sqrt 2$. For which factors $\beta > 0$ is the loop $\dot x = x - \beta K x$ stable? Compare the answer with the range that the [LQR stability margins](/lqr-stability-margins/) guarantee.

6. ◦ Run the [Kleinman iteration](/kleinman-iteration/) on $\dot x = x + u$ with $q = r = 1$ from $K_0 = 2$. Give $P_0$, $P_1$ and $P_2$ as fractions and their errors against $1 + \sqrt 2$.

7. ◦ For $\dot x = -x + w$ and $y = x + v$, with white noise intensities $W = 3$ and $V = 1$, find the steady-state error variance and the gain of the [Kalman-Bucy filter](/kalman-bucy-filter/), and the pole of the error dynamics. Compare the error variance with the stationary variance of $x$ itself.

8. ◦ A plant at rest has the step response $s = (0.5, 0.8, 0.95, 1)$, and the setpoint jumps to $r = 1$. Compute the first move $\Delta u$ of [dynamic matrix control](/dynamic-matrix-control/) with $M = 1$, $\lambda = 0$ and the prediction horizons $P = 2$ and $P = 3$. Then compute both moves for $M = P = 2$.

9. ◦ Solve the [Euler-Lagrange equation](/euler-lagrange-equation/) for the cost $J(y) = \int_0^2 (y'^2 + 4y)\, dx$ with $y(0) = y(2) = 0$, and give the minimum value of $J$.

10. ◦ MPC on $x_{k+1} = 2x_k + u_k$ with $|u| \le 1$ uses the terminal equality $x_N = 0$. Find its feasible set $\mathcal{X}_N$ for $N = 1, 2, 3$ and in general. What is the limit as $N \to \infty$?

11. ◦ The [bang-bang principle](/bang-bang-control/) bounds the number of switches of a time-optimal scalar input by $n - 1$ when the eigenvalues of $A$ are real. Give the bound for $\ddot y = u$, for $\ddot y = -4\dot y - 3y + u$ and for $\dddot y = u$, each with $|u| \le 1$, and check that each system is controllable.

12. • For $x_{k+1} = x_k + u_k$ with $Q = R = 1$, terminal weight 1 and $N = 2$, write the cost as $U^T H U + 2x F^T U + c x^2$ with $U = (u_0, u_1)$, as in [linear MPC](/linear-mpc/). Find the unconstrained minimizer and its value, and compare with the Riccati recursion. Then add $|u_k| \le 1$, take $x = 2$, and find the constrained optimum and the multiplier of the active bound.

13. • Solve a finite-horizon problem by dynamic programming on a grid. The states are $x \in \{-2, \dots, 2\}$, the inputs $u \in \{-1, 0, 1\}$, the model is $x_{k+1} = x_k + u_k$ (a move must stay on the grid), the stage cost is $x^2 + u^2$, $N = 3$ and the terminal cost is 0. Tabulate $V_1$, $V_2$ and $V_3$ and give the first move from $x = 2$. Compare $V_3(2)$ with the value of the Riccati recursion without the grid.

14. • For the double integrator with $|u| \le 1$, start at $(x_1, x_2) = (0, 2)$. Find the sequence of inputs of the [time-optimal control](/time-optimal-control/), the switching time, the state at the switch and the total time.

15. • For $\dot x = ax + u$, find the least energy $\int_0^{t_1} u^2\, dt$ that moves the state from 0 to 1 in time $t_1$, by [minimum-energy control](/minimum-energy-control/). Evaluate it for $a = 1$ at $t_1 = 1$ and $t_1 = 2$, and find its limit as $t_1 \to \infty$ for $a > 0$ and for $a < 0$.

16. • Compute the [maximal positively invariant set](/maximal-positively-invariant-set/) of $x_{k+1} = A x_k$ with $A = \frac12 \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$ under the limit $|x_1| \le 1$. At which index $t$ does the algorithm stop?

17. • Consider MPC with $N = 1$ on $x_{k+1} = x_k + u_k$, with $|u| \le 1$, stage cost $x^2 + u^2$ and terminal cost $\varphi x^2$, where $\varphi = (1 + \sqrt 5)/2$ solves the DARE. Find the [explicit MPC](/explicit-mpc/) law and its regions, and the value function on each region. Check that the value function is continuous and differentiable at the region boundaries.

18. • For the discrete plant $x_{k+1} = 2x_k + u_k$ with $q = r = 1$, show that the LQR gain is $\varphi = (1 + \sqrt 5)/2$. For which factors $\beta$ is $2 - \beta \varphi$ inside the unit circle? Explain why the result does not contradict the continuous-time margins.

19. • For $\dot x = x + u$ with the LQR gain $K = 1 + \sqrt 2$, the loop gain is $L(s) = K/(s - 1)$. Compute $|1 + L(j\omega)|^2$ and show it is at least 1. Find the crossover frequency and the [phase margin](/phase-margin/).

20. • In [tube MPC](/tube-mpc/) for $x_{k+1} = x_k + u_k + w_k$ with $|w_k| \le 0.1$, the constraints $|x| \le 1$, $|u| \le 1$ and the ancillary law $u = v - 0.5(x - z)$, find the smallest invariant interval for the error $e = x - z$ and the tightened constraints on the nominal $z$ and $v$.

21. • The plant $x_{k+1} = 0.5x_k + u_k + d$ has an unknown constant disturbance $d = 0.1$. Find the steady state under $u = -0.5x$. Then estimate $d$ from the last step as $\hat d_k = x_k - 0.5x_{k-1} - u_{k-1}$ and use $u = -0.5x - \hat d$. What is the steady state now, and after how many steps is it reached? Relate the result to [offset-free MPC](/offset-free-mpc/).

22. • Design [LQG](/lqg-control/) for $\dot x = u + w$, $y = x + v$ with $q = r = 1$ and $W = V = 1$. Give the regulator and filter gains, the controller transfer function from $y$ to $-u$, and the closed-loop characteristic polynomial. Find the gain margin and the phase margin of the loop broken at the plant input.

23. • For the scalar plant $\dot x = ax + bu$ with $b \ne 0$, the LQR closed-loop pole is $-\sqrt{a^2 + b^2 q/r}$. Find the limits of the pole and of the gain as $r \to \infty$, for $a > 0$ and for $a < 0$, and the rate at which the pole moves as $r \to 0$. What does the first limit say about the cheapest way to stabilize an unstable plant?

24. ★ For the double integrator with $|u| \le 1$, the minimum time above the switching curve is $T^*(x) = x_2 + 2\sqrt{x_1 + x_2^2/2}$. Show that it solves the stationary [Hamilton-Jacobi-Bellman equation](/hamilton-jacobi-bellman-equation/) $1 + x_2 \partial_{x_1} T - |\partial_{x_2} T| = 0$ at every point strictly above the curve, and that the input it selects is $u = -1$.

25. ★ Take MPC with $N = 2$ on $x_{k+1} = x_k + u_k$, with $|u| \le 1$, $Q = R = 1$ and the terminal cost $\varphi x^2$. Find all regions of the explicit law and the optimal plan $(u_0, u_1)$ on each. Show that the applied input is $\mathrm{sat}(-x/\varphi)$ for every $x$, and that no region has $u_1$ at a bound while $u_0$ is not.

26. ★ Let $(A, B)$ be stabilizable and $(Q^{1/2}, A)$ detectable, with $R > 0$. Show that unconstrained MPC with no terminal cost gives an asymptotically stable closed loop for every horizon $N$ large enough. Use what the [discrete algebraic Riccati equation](/discrete-algebraic-riccati-equation/) entry proves about the recursion from $P = 0$.

27. ★ For $\dot x = x + u$ and $r = 1$, find all gains $k$ for which $u = -kx$ is the LQR law for some weight $q \ge 0$, and give $q$ as a function of $k$. Compare the set of such $k$ with the gain margin of the LQR loop.

28. ★ For the scalar discrete plant with $a \ne 0$, $b \ne 0$, $q > 0$, $r > 0$, write the Riccati map $g(p) = q + a^2 r p/(r + b^2 p)$. Show that $g$ is increasing and concave on $p \ge 0$ and bounded above, and that the iteration $p_{k+1} = g(p_k)$ from $p_0 = 0$ increases monotonically to the positive fixed point.
