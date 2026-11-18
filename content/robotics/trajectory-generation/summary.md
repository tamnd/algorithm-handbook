## What to remember

- A trajectory is a path composed with a time scaling, $q(t) = \theta(s(t))$. Then $\dot q = \theta' \dot s$ and $\ddot q = \theta' \ddot s + \theta'' \dot s^2$, so joint limits become limits on $\dot s$ and $\ddot s$. On a straight line with box limits, $\dot s \le \min_i V_i/|\Delta_i|$ and $|\ddot s| \le \min_i A_i/|\Delta_i|$.
- For a rest-to-rest move of length $D$ in time $T$, the cubic peaks at speed $1.5D/T$ and the quintic at $1.875D/T$. They are the unique minimizers of $\int \ddot q^{\,2}$ and $\int \dddot q^{\,2}$, with costs $12D^2/T^3$ and $720D^2/T^5$. Neither is time-optimal: the duration is an input.
- The trapezoid is time-optimal for one axis from rest to rest under $V$ and $A$, a theorem: $T = D/V + V/A$, or $2\sqrt{D/A}$ when $D < V^2/A$. The double S adds a jerk limit; when $V$ and $A$ are both reached, $T = D/V + V/A + A/J$. Its entry does not prove it the fastest motion under three limits.
- Minimum snap is optimal for its cost with fixed segment times, but it ignores the limits; check them afterward.
- Along a fixed path, the variable $x = \dot s^2$ makes every torque limit linear in $(\ddot s, x)$, and $dx/ds = 2\ddot s$. The maximum velocity curve is the ceiling of the phase plane. Bobrow's integration is time-optimal only under its regularity conditions, with exact switch points, up to integrator error.
- TOPP-RA finds an admissible profile of the discretized problem whenever one exists, and is optimal for it on a fine enough grid without zero-inertia points. The convex formulation gives the global optimum of the discretized problem, to tolerance. Both check limits only at grid points.
- CHOMP, STOMP, TrajOpt, GPMP2 and control-limited DDP are local. They can stop at a poor stationary point or in collision, and none can report that no solution exists.
- Shortcutting keeps a path free and never lengthens it, a theorem; how close it gets to the shortest path is only measured.

| Method | Input | Result | Guarantee | Cost |
|---|---|---|---|---|
| [Cubic](/cubic-polynomial-trajectory/), [quintic](/quintic-polynomial-trajectory/) | end states, duration | polynomial per segment | exact fit | $\Theta(nm)$ |
| [Trapezoid](/trapezoidal-velocity-profile/) | $D$, $V$, $A$ per axis | piecewise quadratic | time-optimal | $\Theta(n)$ |
| [Double S](/double-s-velocity-profile/) | $D$, $V$, $A$, $J$ per axis | up to seven jerk segments | meets the limits | $\Theta(n)$ |
| [Online generation](/online-trajectory-generation/) | current and target states | profile from any state | time-optimal for one axis, Type II | $\Theta(n)$ per cycle |
| [Minimum snap](/minimum-snap-trajectory/) | waypoints, segment times | degree-7 spline | optimal for its cost | $\Theta(dm^3)$ dense |
| [Bobrow](/bobrow-time-optimal-algorithm/) | path, limit rows | phase-plane curves | optimal under conditions | $O(kbm^2/h)$ |
| [TOPP-RA](/topp-reachability-analysis/) | path, rows, grid of $N$ | greedy profile | complete; optimal on a fine grid | $O(Nm^2)$ |
| [Convex TOPP](/convex-time-optimal-path-parameterization/) | path, rows, grid of $N$ | squared speeds | global for the grid | Newton steps of $O(Nm)$ |
| [CHOMP](/chomp/) | start line, distance field | waypoints | cost decreases | $O(n(d+m))$ per iteration |
| [STOMP](/stomp/) | start line, cost values | waypoints | best iterate kept | $O(Kn(d+C) + n^2d)$ per iteration |
| [TrajOpt](/sequential-convex-trajectory-optimization/) | start, signed distances | waypoints | stationary point of the penalty | one convex program per step |
| [Control-limited DDP](/control-limited-ddp/) | dynamics, costs, box | controls and gains | first-order point | $O(N(n^3 + pm^3 + F))$ per iteration |

: The main methods of the chapter. Here $n$ counts joints, axes or waypoints, $m$ segments or constraint rows, $N$ grid intervals or time steps, and $h$ is the integration step; the entries define the other symbols.

## Choosing a method

For a point-to-point move with known limits, use the trapezoid when acceleration jumps are acceptable and the double S when they are not. Use online generation when the target can change or the robot is already moving. For a smooth move of a given duration, use the quintic; through waypoints, use minimum snap and check the limits.

For a fixed path with torque limits, use TOPP-RA and check the result on a finer grid. Use the convex formulation when the cost includes energy or smoothness. Use Bobrow's method when the switch points are wanted and the path has no singular arcs.

For a path from a sampling planner, shortcut it, then time it. When the path itself should change, use CHOMP with a distance field, STOMP when the cost has no gradient, TrajOpt for collision as a constraint, and DDP for dynamics with torque bounds. Start from several guesses and check the result for collisions.
