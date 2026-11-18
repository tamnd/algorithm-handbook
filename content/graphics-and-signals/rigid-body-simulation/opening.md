A box falls onto a table, bounces once, slides a little and comes to rest. A game shows hundreds of such boxes, crates stacked into walls and barrels knocked down by a ball, at sixty frames a second. Each frame a rigid body simulator must find which of the bodies touch, how deep they overlap and where, and what impulses or forces keep them apart without adding energy. The same machinery moves parts in assembly planning, robots in their simulators and debris in film.

The work splits into two halves that use very different mathematics. Collision detection is geometry: it prunes the pairs of bodies, then finds the distance, the closest features or the penetration depth of each close pair. For convex shapes these answers are exact. Contact response is mechanics and numerics: it turns the contacts into impulses or forces under laws of restitution and friction, and for many contacts at once it solves a complementarity problem, usually by iteration. Those solvers are approximations, and their entries say which properties are proved and which are only measured.

## What the chapter covers

1. **The problem and the contact laws.** The [rigid body simulation problem](/rigid-body-simulation-problem/) states the state, the time step and the contact conditions. The [coefficient of restitution](/coefficient-of-restitution/) fixes how much of the approach speed comes back, and the [Coulomb friction law](/coulomb-friction-law/) bounds the tangential force by $\mu$ times the normal force.
2. **Broad and middle phase.** [Sweep and prune](/sweep-and-prune/) finds overlapping boxes by sorting interval ends along an axis. Bounding volume trees prune the pairs inside two bodies: the [OBB tree](/obb-tree/), the [k-DOP tree](/k-dop-tree/) and the [sphere tree](/sphere-tree/). [Approximate convex decomposition](/approximate-convex-decomposition/) splits a concave body into a few nearly convex pieces for the next phase.
3. **Distance and depth of convex shapes.** [Lin-Canny](/lin-canny-closest-features/) and [V-Clip](/v-clip/) walk the features of two convex polyhedra to the closest pair, and use the pair found at the last frame as a start. When the shapes overlap, [penetration depth](/penetration-depth/) asks for the shortest move that separates them, and the [expanding polytope algorithm](/expanding-polytope-algorithm/) computes it.
4. **Continuous collision detection.** A fast body can pass through a thin one between two frames. [Continuous collision detection](/continuous-collision-detection/) finds the first time of contact along the motion. [Conservative advancement](/conservative-advancement/) steps toward it without passing it, and the [elementary tests](/elementary-ccd-tests/) solve a cubic in time for a moving vertex and face or two moving edges.
5. **Contact and collision response.** The [contact manifold](/contact-manifold/) is the set of contact points of two bodies. The [collision impulse](/collision-impulse/) resolves one contact in closed form, [penalty contact](/penalty-contact/) pushes with a stiff spring, and [impulse-based simulation](/impulse-based-simulation/) models resting contact as a stream of small collisions.
6. **Solving many contacts at once.** [Projected Gauss-Seidel](/projected-gauss-seidel/) solves all contacts by sweeps of one-contact updates, and [Baumgarte stabilization](/baumgarte-stabilization/) feeds the position error back into the velocity constraint. [Shock propagation](/shock-propagation/) solves a stack from the bottom up, and the [Baraff contact force algorithm](/baraff-contact-force-algorithm/) pivots to exact contact forces.

## A first reading

For a first pass, read these entries in this order:

1. [Rigid body simulation problem](/rigid-body-simulation-problem/)
2. [Coefficient of restitution](/coefficient-of-restitution/)
3. [Coulomb friction law](/coulomb-friction-law/)
4. [Sweep and prune](/sweep-and-prune/)
5. [OBB tree](/obb-tree/)
6. [V-Clip](/v-clip/)
7. [Penetration depth](/penetration-depth/)
8. [Continuous collision detection](/continuous-collision-detection/)
9. [Contact manifold](/contact-manifold/)
10. [Collision impulse](/collision-impulse/)
11. [Projected Gauss-Seidel](/projected-gauss-seidel/)
12. [Baumgarte stabilization](/baumgarte-stabilization/)

These cover one full step of a simulator: prune the pairs, measure each pair, catch fast bodies, and respond to the contacts. The k-DOP and sphere trees are variants of the OBB tree, and Lin-Canny is the older form of V-Clip. The expanding polytope algorithm and approximate convex decomposition can wait until the depth and the shapes matter. Conservative advancement and the elementary tests refine continuous detection. Penalty contact, impulse-based simulation, shock propagation and the Baraff algorithm are other ways to respond, and read best after projected Gauss-Seidel.

## Before you start

The narrow phase is computational geometry from Volume 13. Read the [convex collision detection](/convex-collision-detection/) problem, the [GJK algorithm](/gjk-algorithm/), which the expanding polytope algorithm continues, the [Minkowski sum](/minkowski-sum/), the [support function](/support-function/) and the [separating axis theorem](/separating-axis-theorem/), which the OBB test uses. The broad phase builds on [collision detection](/collision-detection/) and the [uniform grid](/uniform-grid/) from Volume 3, and on the [bounding volume hierarchy](/bounding-volume-hierarchy/) and the [axis-aligned bounding box](/axis-aligned-bounding-box/) from the ray tracing chapter of this volume.

The equations of motion are the [Newton-Euler equations](/newton-euler-equations/) of Volume 37, with orientation as a [unit quaternion](/unit-quaternion-rotation/); the same volume gives the [friction cone](/friction-cone/), [rigid contact complementarity](/rigid-contact-complementarity/) and the [Painlevé paradox](/painleve-paradox/). From Volume 12 come the [symplectic Euler method](/symplectic-euler-method/) for the time step, the [Gauss-Seidel method](/gauss-seidel-method/) behind projected Gauss-Seidel, [positive definite matrices](/positive-definite-matrix/), [differential-algebraic equations](/differential-algebraic-equations/) for Baumgarte stabilization and [polynomial root finding](/polynomial-root-finding/) for the cubic of the elementary tests. [Quadratic programming](/quadratic-programming/) and the [KKT conditions](/kkt-conditions/) of Volume 15 explain the contact problem as an optimization. Vectors, the [cross product](/cross-product/) and the inertia tensor are assumed.
