A car with a turning radius of one unit must come back to the point where it stands, facing the other way. It needs a path of length $7\pi/3 \approx 7.33$ if it may only drive forward. If it may also reverse, a path of length $\pi$ does the job, with two changes of direction. Both numbers come from closed forms, the Dubins and the Reeds-Shepp paths, and both rest on one fact: a wheel can roll along its plane but cannot slide along its axle. Now put the robot on legs. A humanoid that speeds up at $1$ m/s² with its center of mass $0.8$ m above the floor needs the ground to push at a point $8.15$ cm behind that center. If the heel is less than that behind the center of mass, the foot tips back onto its heel. The chapter is about such facts: what a wheel, a foot or a rotor allows, and the algorithms that plan and control motion within those limits.

The chapter covers robots that move their whole body: wheeled robots, cars, legged robots and quadrotors. The models are kinematic or rigid-body models, and the results hold for them. Some methods have proofs on their model, such as the closed-form shortest paths, the safety of the dynamic window approach and the stability theorems of geometric quadrotor control. Others are heuristics that work well on real machines but have no proof that the closed loop converges, such as the Raibert hopping controller and convex MPC. Each entry says which kind it is.

## What the chapter covers

1. **Wheels and their constraints.** A [Pfaffian constraint](/pfaffian-constraint/) is a linear condition on the velocities, and a [nonholonomic constraint](/nonholonomic-constraint/) is one that cannot be integrated to a condition on the poses. The [unicycle model](/unicycle-model/), the [differential drive model](/differential-drive-model/) and the [kinematic bicycle model](/kinematic-bicycle-model/) have such constraints; [omnidirectional robot kinematics](/omnidirectional-robot-kinematics/) shows how omni and mecanum wheels avoid them.
2. **Following a path.** [Pure pursuit](/pure-pursuit/) steers on the arc through a point ahead on the path, and the [Stanley controller](/stanley-controller/) adds the cross-track error to the heading error at the front axle.
3. **Paths and planners for cars.** The [Dubins path](/dubins-path/) and the [Reeds-Shepp path](/reeds-shepp-path/) are the shortest paths with a bounded turning radius, forward only and with reverse. [State lattice planning](/state-lattice-planning/) and [Hybrid A*](/hybrid-a-star/) search graphs of feasible motions.
4. **Avoiding obstacles on the way.** The [dynamic window approach](/dynamic-window-approach/), the [vector field histogram](/vector-field-histogram/) and the [velocity obstacle](/velocity-obstacle/) choose the next command from the obstacles near the robot.
5. **Covering and exploring.** [Coverage path planning](/coverage-path-planning/) and the [boustrophedon cell decomposition](/boustrophedon-cell-decomposition/) pass a tool over every free point of a known map. [Frontier-based exploration](/frontier-based-exploration/) and [next-best-view planning](/next-best-view-planning/) build the map first.
6. **Balance on legs.** The [support polygon](/support-polygon/), the [center of pressure](/center-of-pressure/), the [zero moment point](/zero-moment-point/) and the [contact wrench cone](/contact-wrench-cone/) are the balance conditions, from standing still to uneven ground. The [linear inverted pendulum model](/linear-inverted-pendulum-model/) and its [capture point](/capture-point/) say where to step.
7. **Walking, running and hopping.** [Footstep planning](/footstep-planning/) and [ZMP preview control](/zmp-preview-control/) make a walk. The [spring-loaded inverted pendulum](/spring-loaded-inverted-pendulum/) and the [Raibert hopping controller](/raibert-hopping-controller/) model and control running. [Passive dynamic walking](/passive-dynamic-walking/) and [hybrid zero dynamics](/hybrid-zero-dynamics/) analyze gaits as periodic orbits.
8. **Whole-body control.** [Convex MPC for legged locomotion](/convex-mpc-legged-locomotion/) plans ground forces, [whole-body control](/whole-body-control/) tracks tasks with the full model, and [hierarchical quadratic programming](/hierarchical-quadratic-programming/) enforces strict priorities among them.
9. **Quadrotors.** [Quadrotor dynamics](/quadrotor-dynamics/) is the rigid-body model, [quadrotor differential flatness](/quadrotor-differential-flatness/) gives the states and inputs from a path, and [geometric tracking control on SE(3)](/geometric-tracking-control-se3/) follows the path.

## A first reading

Read these twelve entries in order:

1. [Pfaffian constraint](/pfaffian-constraint/)
2. [Unicycle model](/unicycle-model/)
3. [Differential drive model](/differential-drive-model/)
4. [Kinematic bicycle model](/kinematic-bicycle-model/)
5. [Pure pursuit](/pure-pursuit/)
6. [Dubins path](/dubins-path/)
7. [Dynamic window approach](/dynamic-window-approach/)
8. [Coverage path planning](/coverage-path-planning/)
9. [Support polygon](/support-polygon/)
10. [Zero moment point](/zero-moment-point/)
11. [Linear inverted pendulum model](/linear-inverted-pendulum-model/)
12. [Quadrotor dynamics](/quadrotor-dynamics/)

They give one model and one method for each kind of robot. The Lie bracket test of nonholonomic constraints, the Reeds-Shepp word list and the contact wrench cone can wait. Leave for later the groups on gaits as periodic orbits and on whole-body control, which use the balance conditions, quadratic programming and nonlinear control together.

## Before you start

The wheeled models use the [Lie bracket](/lie-bracket/), [controllability](/controllability/) and [Brockett's condition](/brockett-condition/) from Volume 36. The controllers use [exponential stability](/exponential-stability/), the [Lyapunov function](/lyapunov-function/), the [limit cycle](/limit-cycle/), [differential flatness](/differential-flatness/), [zero dynamics](/zero-dynamics/), the [LQR problem](/lqr-problem/) and [model predictive control](/model-predictive-control/), also in Volume 36. The planners rest on the [configuration space](/configuration-space/), [motion planning](/motion-planning/), [A* search](/a-star-search/), [cell decomposition](/cell-decomposition/) and the [potential field method](/potential-field-method/) from Volume 29, and on [breadth-first search](/breadth-first-search/) from Volume 7. The [convex hull](/convex-hull/) and the [Minkowski sum](/minkowski-sum/) are in Volume 13, and [quadratic programming](/quadratic-programming/) and [lexicographic optimization](/lexicographic-optimization/) in Volume 15. From this volume, read [SO(3)](/special-orthogonal-group/), the [Newton-Euler equations](/newton-euler-equations/), [centroidal dynamics](/centroidal-dynamics/), the [friction cone](/friction-cone/) and the [occupancy grid map](/occupancy-grid-map/) first.
