Hold a two-link arm out straight and level. With links of 1 m and a mass of 1 kg at the end of each link, the shoulder must supply 29.43 N m and the elbow 9.81 N m just to keep it still. Now bend the elbow to a right angle and swing both joints at 1 rad/s without any acceleration. Without gravity, the shoulder still needs $-3$ N m and the elbow $1$ N m, because a turning arm pushes on its own joints. The manipulator equation
$$M(q)\ddot q + C(q, \dot q)\dot q + g(q) = \tau$$
collects these effects: the inertia matrix $M$, the velocity terms $C\dot q$ and the gravity torques $g$.

Robot dynamics is the study of this equation: how to derive it, what structure it has, and how to evaluate it fast. A torque controller of an arm evaluates it about a thousand times a second. A simulator of a humanoid robot with dozens of joints solves it for the accelerations at every time step, often with contact forces from the ground. An optimizer that plans a jump asks for its derivatives too. The chapter gives the equations, the recursive algorithms that evaluate them in time linear in the number of joints, and the models for contact and for flexible gears.

## What the chapter covers

1. **The equations of motion.** The [Newton-Euler equations](/newton-euler-equations/) govern one rigid body. The [joint-space inertia matrix](/joint-space-inertia-matrix/) gives the kinetic energy of a chain, and [Euler-Lagrange manipulator dynamics](/euler-lagrange-manipulator-dynamics/) turns it into the [manipulator equation](/manipulator-equation/). The [skew symmetry](/skew-symmetry-of-manipulator-dynamics/) of $\dot M - 2C$ and the [linearity in the dynamic parameters](/linearity-in-dynamic-parameters/) are the two properties that control uses most. [Kane's method](/kanes-method/) is a second derivation.
2. **Inverse and forward dynamics.** [Inverse dynamics](/inverse-dynamics/) finds the torques for a motion and [forward dynamics](/forward-dynamics/) the accelerations for the torques. [Floating-base dynamics](/floating-base-dynamics/) covers robots whose base is not bolted down.
3. **Spatial vectors.** [Spatial vector algebra](/spatial-vector-algebra/) writes velocities and forces as 6-vectors, and the [spatial inertia](/spatial-inertia/) of a body is a $6 \times 6$ matrix with ten parameters.
4. **Recursive algorithms.** The [recursive Newton-Euler algorithm](/recursive-newton-euler-algorithm/) solves inverse dynamics in $O(n)$ time. The [composite rigid body algorithm](/composite-rigid-body-algorithm/) forms $M(q)$ in $O(nd)$ time, which is $O(n^2)$ for a chain. The [articulated-body inertia](/articulated-body-inertia/) leads to the [articulated-body algorithm](/articulated-body-algorithm/), which solves forward dynamics in $O(n)$ time. [Rigid body dynamics derivatives](/rigid-body-dynamics-derivatives/) differentiate these maps. All of them are exact for the rigid-body model.
5. **Matching the model to the robot.** The [base inertial parameters](/base-inertial-parameters/) are the combinations of masses and inertias that torque data can fix, and [dynamic parameter identification](/dynamic-parameter-identification/) estimates them by least squares. The [flexible joint model](/flexible-joint-model/) adds a spring between each motor and its link.
6. **Task space and momentum.** The [operational space formulation](/operational-space-formulation/) writes the dynamics in task coordinates, and the [dynamically consistent generalized inverse](/dynamically-consistent-generalized-inverse/) separates the task from the rest of a redundant arm. The [centroidal momentum matrix](/centroidal-momentum-matrix/) and [centroidal dynamics](/centroidal-dynamics/) describe the total momentum of a legged robot.
7. **Constraints and contact.** The [Gauss principle of least constraint](/gauss-principle-of-least-constraint/) makes constrained motion a quadratic program. [Rigid contact complementarity](/rigid-contact-complementarity/) models one-sided contact with friction. The [Painlevé paradox](/painleve-paradox/) shows that the force form can have no solution or several, and [Stewart-Trinkle time stepping](/stewart-trinkle-time-stepping/) solves one linear complementarity problem in impulses per step instead.

## A first reading

Read these twelve entries in order:

1. [Newton-Euler equations](/newton-euler-equations/)
2. [Joint-space inertia matrix](/joint-space-inertia-matrix/)
3. [Euler-Lagrange manipulator dynamics](/euler-lagrange-manipulator-dynamics/)
4. [Manipulator equation](/manipulator-equation/)
5. [Skew symmetry of manipulator dynamics](/skew-symmetry-of-manipulator-dynamics/)
6. [Linearity in dynamic parameters](/linearity-in-dynamic-parameters/)
7. [Inverse dynamics](/inverse-dynamics/)
8. [Forward dynamics](/forward-dynamics/)
9. [Spatial vector algebra](/spatial-vector-algebra/)
10. [Spatial inertia](/spatial-inertia/)
11. [Recursive Newton-Euler algorithm](/recursive-newton-euler-algorithm/)
12. [Composite rigid body algorithm](/composite-rigid-body-algorithm/)

The two-link planar arm with point masses runs through most of these entries, so its numbers can be checked from one page to the next. Kane's method can wait. The articulated-body algorithm and the derivatives are worth reading only after the recursive Newton-Euler algorithm feels routine. The groups on task space, momentum and contact are for readers who work on redundant arms, legged robots or simulators, and they use everything before them.

## Before you start

The chapter builds on the rigid body motion of Chapter 37.1: [angular velocity](/angular-velocity/), the [twist](/rigid-body-twist/), the [wrench](/wrench/) and the [adjoint map](/adjoint-map-se3/). From Chapter 37.2 it needs [forward kinematics](/forward-kinematics/), the [kinematic chain](/kinematic-chain/) and the [geometric Jacobian](/geometric-jacobian/). From Volume 12 it uses [positive definite matrices](/positive-definite-matrix/), the [Cholesky decomposition](/cholesky-decomposition/), the [Schur complement](/schur-complement/), the [least squares problem](/least-squares-problem/), the [pseudoinverse](/pseudoinverse/) and the [initial value problem](/ode-initial-value-problem/). The [Euler-Lagrange equation](/euler-lagrange-equation/) and [passivity](/passivity/) are in Volume 36, and [quadratic programming](/quadratic-programming/) and the [Lagrange multiplier](/lagrange-multiplier/) are in Volume 15. The contact group uses the [friction cone](/friction-cone/) and the [polyhedral friction cone](/polyhedral-friction-cone/), and the operational space formulation uses [computed-torque control](/computed-torque-control/); all three are in Chapter 37.6.
