1. ◦ A three-joint arm moves on the straight joint-space line from $q_0$ to $q_0 + \Delta$ with $\Delta = (2, 1, 0.5)$ rad. The limits are $V = (1.2, 0.8, 0.25)$ rad/s and $A = (4, 3, 1.5)$ rad/s². Use the [time scaling](/time-scaling/) $q = q_0 + s\Delta$ to find the bounds on $\dot s$ and $|\ddot s|$, say which joint sets each, and give the shortest trapezoidal time scaling. Then give the time each joint would need alone.

2. ◦ A [cubic polynomial trajectory](/cubic-polynomial-trajectory/) moves a joint from rest at $0.2$ rad to rest at $1.0$ rad. With $V = 0.5$ rad/s and $A = 1$ rad/s², find the smallest duration $T$, the limit that binds, and the coefficients $a_2$ and $a_3$ for that $T$.

3. ◦ Find the [quintic](/quintic-polynomial-trajectory/) on $[0, 1]$ with $q(0) = 0$, $\dot q(0) = 3$, $\ddot q(0) = 0$ and $q(1) = 1$, $\dot q(1) = \ddot q(1) = 0$. Does it stay below its target? Do the same with $\dot q(0) = 2$.

4. ◦ For one axis with $V = 1$ and $A = 2$, give the [trapezoidal velocity profile](/trapezoidal-velocity-profile/) for $D = 0.4$ and for $D = 3$: the shape, the duration and the peak speed.

5. ◦ Give the duration of the [double S profile](/double-s-velocity-profile/) for $D = 2$, $V = 1$, $A = 2$ and $J = 8$, after checking that both $V$ and $A$ are reached. How much slower is it than the trapezoid with the same $V$ and $A$?

6. ◦ A hand moves from $(0, 0)$ to $(0.6, 0.8)$ m in $T = 2$ s along the [minimum-jerk trajectory](/minimum-jerk-trajectory/). Give the peak speed, the peak acceleration, the jerk at the start and the value of $\int_0^T \|\dddot x\|^2\,dt$.

7. ◦ A planner returns the path $(0,0) \to (0,4) \to (4,4) \to (4,0)$ in the half-plane $y \ge 0$, around the rectangular obstacle $[1, 3] \times [0, 3]$, which stands on the edge $y = 0$. [Random shortcut path smoothing](/random-shortcut-path-smoothing/) draws three pairs of points, at arc lengths $(2, 10)$, $(1, 6)$ and $(3.5, 8.5)$. Which shortcuts are accepted, and what is the length after each? What is the length of the shortest free path?

8. ◦ In the [path-velocity decomposition](/path-velocity-decomposition/), a path is 12 m long and the speed is at most 3 m/s. A moving obstacle occupies $s \in [5, 7]$ during $t \in [1, 3]$. Find the least time to the end, and a speed profile that reaches it. Then answer the same question when the obstacle occupies $[5, 7]$ during $t \in [3, 5]$.

9. ◦ The transformation system of a [dynamic movement primitive](/dynamic-movement-primitives/) with $f = 0$ is linear in $(y, z)$. Find its eigenvalues for $\alpha_z = 25$, $\beta_z = \alpha_z/4$ and $\tau = 1$, and for $\tau = 2$. What are they for $\beta_z = \alpha_z/2$, and what does the motion then do near the goal?

10. ◦ In [Gaussian process motion planning](/gaussian-process-motion-planning/) with $Q_c = 1$, the prior cost between two rest states is the least value of $\tfrac12 \int_0^T \|\ddot p\|^2\,dt$. Compute it for a straight move of length $2$ in $T = 1$ and in $T = 2$, and name the curve that attains it.

11. • Cubic segments pass through $0$, $2$ and $1$ at times $0$, $1$ and $3$, from rest to rest. Find the velocity $v$ at the via point that makes the acceleration continuous, and the acceleration there. Compare with the heuristic that sets $v = 0$ when the two neighboring slopes have opposite signs. Does the trajectory with continuous acceleration stay below $2$?

12. • Two axes move $D_1 = 1$ and $D_2 = 0.3$ with $V = 1$ and $A = 2$ each. Synchronize axis 2 to the duration of axis 1 in two ways: keep $A = 2$ and lower the cruise speed, or use the same phase durations as axis 1. Give the cruise speed of axis 2 in each case, and say which one keeps the joint-space path straight.

13. • Find the double S profile for $D = 0.1$, $V = 1$, $A = 2$ and $J = 8$. Show that neither $V$ nor $A$ is reached, and give $T_j$, the peak acceleration, the peak speed and the duration. Compare with the trapezoid.

14. • For $D = 0.5$, $V = 1$ and $A = 4$, find the smallest rest-to-rest duration of the cubic, the quintic and the trapezoid, and the limit that binds each. Explain why the cubic is faster than the quintic here.

15. • A [minimum-snap trajectory](/minimum-snap-trajectory/) from rest at $0$ to rest at $2$ passes through $1$ at $t = 1$, with segment times $1$ and $1$. Show that it is a single degree-7 polynomial, and give its velocity at the via point and its cost $\int (q^{(4)})^2\,dt$.

16. • Run [TOPP-RA](/topp-reachability-analysis/) by hand on the path $q(s) = s$ with $|\dot q| \le 1$ and $|\ddot q| \le 1$, on the grid $s_i = i/4$, from rest to rest. Give the sets $K_i$, the greedy profile $x_i$ and $u_i$, and the time. Compare with the continuous optimum.

17. • One axis has $-4 \le \ddot s \le 1$ on $s \in [0, 1]$, from rest to rest. Find the switch point and the time of [Bobrow's algorithm](/bobrow-time-optimal-algorithm/) without a velocity limit. Then add $\dot s \le 1$: describe the profile in the phase plane and give the new time.

18. • In [online trajectory generation](/online-trajectory-generation/), an axis is at $p_0 = 0$ moving away from its target at $v_0 = -0.5$, with $p_T = 1$, $v_T = 0$, $V = 1$ and $A = 2$. Find the time-optimal profile and its duration.

19. • In [CHOMP](/chomp/), take $n = 3$ waypoints and $\Delta t = 1$, so that $A$ is the tridiagonal matrix with $2$ on the diagonal and $-1$ next to it. Compute $A^{-1}$, the covariant step for a gradient that is $1$ at the middle waypoint and $0$ elsewhere, and the smallest eigenvalue of $A$. Check the eigenvalue against the formula $4\sin^2(\pi/(2(n+1)))/\Delta t^2$.

20. • At one waypoint, the four samples of [STOMP](/stomp/) have costs $1, 2, 3, 6$ and noise values $0.1, -0.2, 0.05, 0.3$. Compute the weights for $\lambda = 1$, $0.5$ and $10$, and the update at that waypoint for $\lambda = 1$. Show that adding $5$ to every cost changes nothing.

21. • For $x_{k+1} = x_k + u_k$, $x_0 = 1$ and the cost $x_0^2 + u_0^2 + x_1^2 + u_1^2 + x_2^2$, find the optimal feedback by the Riccati recursion and the optimal cost. Then add the box $|u_k| \le 0.4$ of [control-limited DDP](/control-limited-ddp/). Find the optimum, check the first-order condition at the clamped control, and say why it is global.

22. • A point follows the circle $q(s) = R(\cos 2\pi s, \sin 2\pi s)$ with $R = 0.5$ and each coordinate of $\ddot q$ bounded by $2$ in absolute value. Find the [maximum velocity curve](/maximum-velocity-curve/) as a function of the angle $\varphi = 2\pi s$, and give its values at $\varphi = 0$ and $\varphi = \pi/4$.

23. ★ The [path-velocity decomposition](/path-velocity-decomposition/) entry times a path of 10 m with the speed at most 2 m/s past an obstacle on $s \in [4, 6]$ during $t \in [2, 4]$, and finds 7 s. Add the acceleration limit $|\ddot s| \le 1$, from rest to rest. Find the least time, give a profile that reaches it, and prove that no motion is faster.

24. ★ Consider the out-and-back motion through $0$, $1$, $0$ at times $0$, $1$, $2$, from rest to rest. Show by symmetry that the optimal velocity at the via point is $0$ for any cost $\int (q^{(k)})^2\,dt$. Then show that stopping is optimal for $k = 2$, and that for $k = 3$ the best via acceleration is not zero: find it and the cost against stopping. The [minimum-snap](/minimum-snap-trajectory/) entry gives the case $k = 4$.

25. ★ In the [convex formulation](/convex-time-optimal-path-parameterization/), prove that $2\Delta/(\sqrt{b_k} + \sqrt{b_{k+1}})$ is convex for $b_k, b_{k+1} > 0$. Then write the same discretized problem in the path speed $v = \dot s$ and explain why it is not a convex program, although its objective is convex in $v$.

26. ★ For the path $q(s) = s$ with $|\dot q| \le 0.8$ and $|\ddot q| \le 2$, the continuous optimum is $1.65$. Compute the discretized optimum on 2, 4 and 10 equal intervals. Prove that on this path every discretized profile is admissible in continuous time, so the grid can only be pessimistic. Then explain why the grid for the two-link arm of the [TOPP-RA](/topp-reachability-analysis/) entry is optimistic instead.

27. ★ An online generator replans in every cycle of length $\Delta t$ toward a fixed target, with fixed limits, and follows the first cycle of each plan. Prove that it reaches the target after $\lceil T^*/\Delta t\rceil$ cycles, where $T^*$ is the optimal time from the start. Which step of the proof fails when the target moves?
