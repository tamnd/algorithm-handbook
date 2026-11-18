Move one robot joint by 1 rad, from rest to rest, with its speed at most 1 rad/s and its acceleration at most 2 rad/s². A trapezoidal velocity profile does it in 1.5 s, and no motion under these two limits is faster. A cubic polynomial in time needs $\sqrt 3 \approx 1.732$ s and a quintic 1.875 s, because their shapes are fixed and they reach a limit only at one instant. In exchange the quintic starts and stops with zero acceleration, while the trapezoid switches its acceleration on and off at four instants and shakes the arm. Now give a two-link arm a fixed path in joint space and limits on its two motor torques. The limits now depend on where the arm is along the path, and the fastest timing touches one limit or another at every instant. For one such arm it takes 1.5106 s, found by integrating curves in a plane of path position and path speed, or by a sequence of tiny linear programs on a grid.

A trajectory says where the robot is at every instant: positions, velocities and accelerations as functions of time. A planner gives a path, a list of waypoints or only a start and a goal. Trajectory generation turns that into something the controller can follow within the limits of the motors. The chapter starts with closed forms, polynomials and limit-based profiles that cost a few operations per joint. It goes on to the exact fastest timing along a fixed path, where the entries prove optimality and say on which grid. It ends with trajectory optimization, which chooses the path and the timing together. Those methods are local: CHOMP, STOMP, TrajOpt, GPMP2 and DDP find a local solution near their start, and the pages say so.

## What the chapter covers

1. **Paths, timings and the problem.** A [time scaling](/time-scaling/) turns a path into a trajectory, and the chain rule turns joint limits into limits on the path speed. The [trajectory generation problem](/trajectory-generation-problem/) compares the standard profiles on one move.
2. **Smooth point-to-point motions.** The [cubic](/cubic-polynomial-trajectory/) and [quintic](/quintic-polynomial-trajectory/) polynomials meet end conditions in closed form. The [minimum-jerk trajectory](/minimum-jerk-trajectory/) is the rest-to-rest quintic, and the [minimum-snap trajectory](/minimum-snap-trajectory/) passes through waypoints. [Dynamic movement primitives](/dynamic-movement-primitives/) encode a demonstrated motion as a stable differential equation.
3. **Profiles from limits.** The [trapezoidal velocity profile](/trapezoidal-velocity-profile/) is time-optimal for one axis under velocity and acceleration limits. The [double S profile](/double-s-velocity-profile/) adds a jerk limit, and [online trajectory generation](/online-trajectory-generation/) starts from any state in every control cycle.
4. **The fastest timing along a fixed path.** [Time-optimal path parameterization](/time-optimal-path-parameterization/) works under the [maximum velocity curve](/maximum-velocity-curve/). [Bobrow's algorithm](/bobrow-time-optimal-algorithm/) integrates the phase plane, [TOPP-RA](/topp-reachability-analysis/) solves small linear programs, and the [convex formulation](/convex-time-optimal-path-parameterization/) solves one convex program.
5. **Working with a planned path.** [Random shortcuts](/random-shortcut-path-smoothing/) shorten a planner's path, [elastic bands](/elastic-bands/) deform it as obstacles move, and the [path-velocity decomposition](/path-velocity-decomposition/) plans the speed along it past moving obstacles.
6. **Trajectory optimization.** The [trajectory optimization problem](/trajectory-optimization/) is solved locally by [CHOMP](/chomp/), [STOMP](/stomp/), [TrajOpt](/sequential-convex-trajectory-optimization/) and [GPMP2](/gaussian-process-motion-planning/). [Control-limited DDP](/control-limited-ddp/) adds dynamics with torque bounds, and [contact-implicit optimization](/contact-implicit-trajectory-optimization/) lets the optimizer choose when contacts happen.

## A first reading

Read these thirteen entries in order:

1. [Time scaling](/time-scaling/)
2. [Trajectory generation problem](/trajectory-generation-problem/)
3. [Cubic polynomial trajectory](/cubic-polynomial-trajectory/)
4. [Quintic polynomial trajectory](/quintic-polynomial-trajectory/)
5. [Trapezoidal velocity profile](/trapezoidal-velocity-profile/)
6. [Double S velocity profile](/double-s-velocity-profile/)
7. [Minimum-jerk trajectory](/minimum-jerk-trajectory/)
8. [Time-optimal path parameterization](/time-optimal-path-parameterization/)
9. [Maximum velocity curve](/maximum-velocity-curve/)
10. [Time-optimal path parameterization by reachability analysis](/topp-reachability-analysis/)
11. [Random shortcut path smoothing](/random-shortcut-path-smoothing/)
12. [Trajectory optimization](/trajectory-optimization/)
13. [CHOMP](/chomp/)

Bobrow's algorithm can wait until the phase plane is familiar; its switch points are where implementations fail, and TOPP-RA avoids them. Skip at first the convex formulation, minimum snap, movement primitives and the whole second half of the optimization group. Contact-implicit optimization needs the contact models of the previous chapter and comes last.

## Before you start

The chapter needs the [configuration space](/configuration-space/) and the [motion planning problem](/motion-planning/) from Volume 29, and the [manipulator equation](/manipulator-equation/) from the previous chapter, which gives the joint torques along a path. From Volume 12 it uses [polynomial interpolation](/polynomial-interpolation/) and the [initial value problem](/ode-initial-value-problem/). The optimization entries use [linear programming](/linear-programming-problem/), [quadratic programming](/quadratic-programming/), [convex functions](/convex-function/) and [gradient descent](/gradient-descent/), all in Volume 15. The [optimal control problem](/optimal-control-problem/) and [bang-bang control](/bang-bang-control/) in Volume 36 explain why the fastest profiles switch between limits. Calculus is assumed: the chain rule, integrals of polynomials, and the Euler-Lagrange equation of the calculus of variations.
