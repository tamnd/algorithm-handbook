A welding robot has six motors, one per joint, and a torch at the end of its arm. The program says where the torch must be and how it must point, a position and an orientation in space. The motors only understand angles. Kinematics is the geometry that links the two: given the angles, where is the torch, and given a pose of the torch, which angles put it there. It also links velocities, forces and errors: how fast the torch moves when the joints turn, what torques hold a load at the tip, and how far off the torch ends up when the link lengths in the model are slightly wrong.

The same questions come up wherever a chain of rigid bodies has to reach somewhere. A surgical arm moves an instrument through a small opening. A character in an animation reaches for a cup, and the software has to bend the shoulder, elbow and wrist in a believable way. A flight simulator rides on six legs whose lengths set the pose of the cabin. The geometry is the same; what changes is the shape of the chain and how fast and how exactly the answer must come.

The direct question is easy. [Forward kinematics](/forward-kinematics/) multiplies one rigid transformation per joint, and the cost is linear in the number of joints. The inverse question is hard. [Inverse kinematics](/inverse-kinematics/) is a system of nonlinear equations: a target can have no solution, a finite number of solutions or infinitely many. A general arm with six revolute joints has at most 16 solutions, which are counted over the complex numbers, and arms exist with 16 real ones. Iterative methods find one solution near a starting guess, and they converge only locally, from a good start and away from singularities.

## What the chapter covers

1. **Joints, chains and mobility.** The [kinematic pair](/kinematic-pair/) and the [kinematic chain](/kinematic-chain/), and [Grübler's formula](/grubler-formula/), which counts the degrees of freedom of a mechanism when its joint constraints are independent.
2. **Forward kinematics.** The [Denavit-Hartenberg convention](/denavit-hartenberg-convention/) and the [product of exponentials](/product-of-exponentials-formula/), two ways to write the same map, and the [workspace](/robot-workspace/) that the map reaches.
3. **Inverse kinematics in closed form.** [Kinematic decoupling](/kinematic-decoupling/) of an arm with a spherical wrist, the [Paden-Kahan subproblems](/paden-kahan-subproblems/), the [Pieper criterion](/pieper-criterion/), and, for the general 6R arm, the [Raghavan-Roth method](/raghavan-roth-method/) and the [bound of 16 solutions](/six-r-inverse-kinematics-sixteen-solutions/).
4. **Velocity kinematics and statics.** The [geometric Jacobian](/geometric-jacobian/), the [analytic Jacobian](/analytic-jacobian/), the [space and body Jacobians](/space-and-body-jacobian/), and the [duality](/jacobian-statics-duality/) $\tau = J^{\mathsf T}F$ between velocities and forces.
5. **Singularities and manipulability.** [Kinematic singularities](/kinematic-singularity/), where the Jacobian loses rank, and the [manipulability ellipsoid](/manipulability-ellipsoid/) and [Yoshikawa's measure](/yoshikawa-manipulability-measure/), which say how far an arm is from one.
6. **Numerical inverse kinematics.** The [pseudoinverse method](/jacobian-pseudoinverse-method/) and [Newton-Raphson](/newton-raphson-inverse-kinematics/) on poses, [damped least squares](/damped-least-squares-inverse-kinematics/), the [Jacobian transpose](/jacobian-transpose-method/), [resolved-rate control](/resolved-rate-motion-control/), and two methods without a Jacobian, [cyclic coordinate descent](/cyclic-coordinate-descent-inverse-kinematics/) and [FABRIK](/fabrik/).
7. **Redundancy.** [Kinematic redundancy](/kinematic-redundancy/), [null-space projection](/null-space-projection/) and the [task-priority method](/task-priority-inverse-kinematics/).
8. **Parallel robots and calibration.** The [parallel manipulator](/parallel-manipulator/), the [forward kinematics of the Stewart-Gough platform](/stewart-gough-forward-kinematics/), with at most 40 complex solutions, all 40 of which can be real, and [kinematic calibration](/kinematic-calibration/).

## A first reading

For a first pass, read these entries in order:

1. [Kinematic chain](/kinematic-chain/)
2. [Grübler's formula](/grubler-formula/)
3. [Forward kinematics](/forward-kinematics/)
4. [Denavit-Hartenberg convention](/denavit-hartenberg-convention/)
5. [Product of exponentials formula](/product-of-exponentials-formula/)
6. [Inverse kinematics](/inverse-kinematics/)
7. [Kinematic decoupling](/kinematic-decoupling/)
8. [Geometric Jacobian](/geometric-jacobian/)
9. [Kinematic singularity](/kinematic-singularity/)
10. [Manipulability ellipsoid](/manipulability-ellipsoid/)
11. [Jacobian pseudoinverse method](/jacobian-pseudoinverse-method/)
12. [Damped least squares](/damped-least-squares-inverse-kinematics/)
13. [Kinematic redundancy](/kinematic-redundancy/)
14. [Parallel manipulator](/parallel-manipulator/)

That path gives the maps, the Jacobian, the singularities and the numerical method most used in practice. Skip at first the algebra of the general 6R arm ([Raghavan-Roth](/raghavan-roth-method/) and the 16 solutions), the Paden-Kahan subproblems, task priority, the Stewart-Gough forward kinematics and calibration. They matter when you build a solver or a real robot, not to follow the rest.

## Before you start

The chapter uses the rigid-body motion of Chapter 37.1 throughout: the [homogeneous transformation matrix](/homogeneous-transformation-matrix/), [Euler angles](/euler-angles/), [angular velocity](/angular-velocity/), the [twist](/rigid-body-twist/), the [exponential map of SE(3)](/se3-exponential-map/), the [adjoint map](/adjoint-map-se3/), the [wrench](/wrench/) and [Rodrigues' formula](/rodrigues-rotation-formula/).

From linear algebra you need the [singular value decomposition](/singular-value-decomposition/) and the [pseudoinverse](/pseudoinverse/) (Volume 12), and from numerical methods [Newton's method for systems](/newton-method-for-systems/) (Volume 12). The iterative methods are relatives of [gradient descent](/gradient-descent/) and [coordinate descent](/coordinate-descent/) (Volume 15). Calibration is [nonlinear least squares](/nonlinear-least-squares/) (Volume 38), the elimination of the 6R arm uses the [resultant](/resultant/) (Volume 11), and [configuration space](/configuration-space/) (Volume 29) is the space where the joint values live.
