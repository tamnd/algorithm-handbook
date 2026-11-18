## What to remember

- A rolling wheel gives a Pfaffian constraint $A(q)\dot q = 0$, nonholonomic when the brackets of the allowed motions leave the allowed directions. The unicycle is controllable, its linearization at rest is not, and by Brockett's condition no continuous time-invariant feedback stabilizes a pose.
- The differential drive has $v = r(\omega_R + \omega_L)/2$ and $\omega = r(\omega_R - \omega_L)/(2d)$. The kinematic bicycle has $\dot\theta = v\tan\delta/L$ at the rear axle. Mecanum and omni wheels in a good layout give a map of rank 3.
- Pure pursuit steers with curvature $2\sin\alpha/\ell_d$; its linearized error on a straight path has damping ratio $1/\sqrt2$ for every speed. The Stanley law converges globally on a straight path without saturation. Pure pursuit has no global guarantee.
- Dubins and Reeds-Shepp paths are shortest paths in closed form, found in $O(1)$ time by checking a fixed list of words. The Reeds-Shepp distance is symmetric; the Dubins length is not and is not continuous. Hybrid A* is neither complete nor optimal; a state lattice is complete and optimal with respect to the lattice only.
- DWA is safe by a theorem (static known obstacles, exact model, start at rest) and has no guarantee of reaching the goal. VFH is a heuristic with no collision guarantee. A velocity obstacle is exact only while every obstacle keeps a constant velocity.
- A robot at rest on flat ground balances exactly when its center of mass projects into the support polygon. In motion, the ZMP equals the center of pressure while the foot stays flat, and the ZMP criterion is a condition at one instant: a robot can satisfy it and still fall.
- In the LIPM, $\ddot x = \omega^2(x - p)$ with $\omega = \sqrt{g/z_0}$, and only $\xi = x + \dot x/\omega$ is unstable. Holding $p = \xi$ brings the robot to rest. This capture point is exact for the LIPM only.
- Many legged results are computations, not theorems: the stable SLIP gaits, the stable passive gaits and the Raibert controller are found or checked by simulation. HZD reduces stability to a scalar map, under its conditions.
- The quadrotor's position and yaw are flat outputs while the thrust is not zero. The geometric controller is exponentially stable for attitude errors below 90 degrees and attractive from almost every error below 180 degrees, for the continuous-time law.

| Method | Problem | Kind of result | Cost |
|---|---|---|---|
| [Dubins path](/dubins-path/) | shortest forward path, bounded curvature | exact, closed form | $O(1)$ |
| [Reeds-Shepp path](/reeds-shepp-path/) | shortest path with reverse | exact, closed form | $O(1)$ |
| [State lattice planning](/state-lattice-planning/) | car planning on a lattice | complete and optimal for the lattice | $O(N(\log N + bc))$ |
| [Hybrid A*](/hybrid-a-star/) | car planning in continuous poses | not complete, not optimal | $O(B(\log B + s))$ |
| [Dynamic window approach](/dynamic-window-approach/) | local avoidance with acceleration limits | safe under its assumptions, goal not guaranteed | $O(ck)$ per cycle |
| [Boustrophedon decomposition](/boustrophedon-cell-decomposition/) | coverage of a known map | complete, no length bound | $O(n \log^2 n + m \log n)$ |
| [Frontier-based exploration](/frontier-based-exploration/) | mapping an unknown grid | maps every reachable free cell | $O(c^2 r^2)$ |
| [ZMP preview control](/zmp-preview-control/) | CoM motion from a ZMP plan | optimal for the cart-table model | $O(N)$ per step |
| [Convex MPC](/convex-mpc-legged-locomotion/) | ground forces over a horizon | each QP exact, closed loop not proved | one QP per cycle |
| [Hierarchical QP](/hierarchical-quadratic-programming/) | tasks in strict priority | lexicographic optimum in exact arithmetic | one QP per level |
| [Geometric tracking on SE(3)](/geometric-tracking-control-se3/) | quadrotor tracking | exponentially stable below 90 degrees | $O(1)$ per step |

: The main planners and controllers of the chapter. The symbols in the costs are those of each entry.

## Choosing a method

In open space, Dubins and Reeds-Shepp paths give a car the exact distance. Among obstacles, use a state lattice for a guarantee relative to its motions, and Hybrid A* when continuous poses matter more than completeness. Track the plan with pure pursuit or the Stanley law, with DWA or velocity obstacles below for obstacles that appear on the way.

For walking with flat feet on flat ground, plan the footsteps, then the CoM by ZMP preview control, and track it with whole-body control. On uneven ground, test balance with the contact wrench cone. For a push, use the capture point to decide between the ankle and a step. For running, start from the SLIP model; for bipeds with point feet, use HZD. For a quadrotor, compute the feedforward from flatness and close the loop with the geometric controller.
