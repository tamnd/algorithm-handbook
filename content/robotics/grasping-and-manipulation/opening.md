Two fingers squeeze a box of 1 kg from the sides, at the points $(\pm 1, 0)$, with friction coefficient $\mu = 0.5$. Gravity pulls the box down with 9.81 N, so each finger must supply 4.905 N of tangential force, and Coulomb's law allows that only if each finger presses with at least $4.905 / 0.5 = 9.81$ N. A squeeze of 10 N holds the box; a squeeze of 9 N lets it slide. Now tilt the fingers so that the line between them is no longer along the normals, and the same squeeze may fail at any force. The question of which contacts can hold a body, and with how much force, has exact answers for a given contact model, and most of the chapter's first half computes them.

Grasping is only part of manipulation. The arm must reach the object, the tool must press on a surface without pushing too hard, a camera may guide the hand, and some objects are pushed or squeezed into place instead of being held. The chapter keeps two kinds of statement apart. Closure tests, the voting theorem and Goldberg's plans are theorems inside their models: rigid bodies, point or soft finger contacts, Coulomb friction, quasi-static motion. How well a grasp score predicts success on a real hand, or how well a learned policy works, is measured.

## What the chapter covers

1. **Contacts and friction.** The [friction cone](/friction-cone/) bounds the force at one contact. The [grasp contact models](/grasp-contact-models/) say what a frictionless point, a hard finger and a soft finger transmit. The [polyhedral friction cone](/polyhedral-friction-cone/) replaces the round cone by a pyramid so that the tests become linear.
2. **Holding an object still.** [Form closure](/form-closure/) holds a body by geometry alone. The [grasp matrix](/grasp-matrix/) maps contact forces to the net wrench, and [force closure](/force-closure/) asks that friction forces balance every wrench. The [antipodal grasp](/antipodal-grasp/) is the two-finger case, the [force-closure test](/force-closure-test/) decides closure by linear feasibility, and the [finger bounds](/finger-bounds-for-form-closure/) count the contacts that form closure needs.
3. **Grasp quality and grasp choice.** The [grasp wrench space](/grasp-wrench-space/) and the [Ferrari-Canny metric](/ferrari-canny-metric/) measure how much a grasp resists per unit of finger force, among other [grasp quality measures](/grasp-quality-measures/). [Grasp synthesis](/grasp-synthesis/) searches for good contacts, [independent contact regions](/independent-contact-regions/) tolerate positioning errors, and [caging](/caging-grasp/) traps an object without holding it.
4. **Moving the arm.** [PD control with gravity compensation](/pd-control-with-gravity-compensation/) reaches set points, [computed-torque control](/computed-torque-control/) tracks paths with a full model, and the [Slotine-Li controller](/slotine-li-adaptive-control/) tracks while it learns the model.
5. **Controlling contact.** [Impedance control](/impedance-control/) and [admittance control](/admittance-control/) make the tool behave as a spring and a damper. [Hybrid position/force control](/hybrid-position-force-control/) splits the directions of the task, and [peg-in-hole insertion](/peg-in-hole/) is the classic test.
6. **Visual servoing.** The [interaction matrix](/interaction-matrix/) links the camera twist to image motion. [Image-based](/image-based-visual-servoing/) and [position-based](/position-based-visual-servoing/) visual servoing are the two basic laws.
7. **Pushing and orienting without sensors.** The [limit surface](/limit-surface/) is the friction law of a sliding object, [quasi-static pushing](/quasi-static-pushing/) predicts its motion, and [Mason's voting theorem](/mason-voting-theorem/) gives its sense of rotation. [Sensorless part orienting](/sensorless-part-orienting/) and [Goldberg's algorithm](/goldberg-part-orienting-algorithm/) orient parts by fixed sequences of actions.
8. **Planning and dexterity.** [Manipulation planning](/manipulation-planning/) and [task and motion planning](/task-and-motion-planning/) plan grasps, transfers and symbolic actions. [Montana's contact kinematics](/montana-contact-kinematics/) describe rolling contacts, the basis of [in-hand manipulation](/in-hand-manipulation/).

## A first reading

Read these twelve entries in order:

1. [Friction cone](/friction-cone/)
2. [Grasp contact models](/grasp-contact-models/)
3. [Form closure](/form-closure/)
4. [Grasp matrix](/grasp-matrix/)
5. [Force closure](/force-closure/)
6. [Antipodal grasp](/antipodal-grasp/)
7. [Polyhedral friction cone](/polyhedral-friction-cone/)
8. [Force-closure test](/force-closure-test/)
9. [Grasp wrench space](/grasp-wrench-space/)
10. [PD control with gravity compensation](/pd-control-with-gravity-compensation/)
11. [Impedance control](/impedance-control/)
12. [Interaction matrix](/interaction-matrix/)

The groups after the second can be read in any order. Skip at first the finger bounds, independent contact regions and caging, the Slotine-Li controller, and the whole pushing group, which has its own friction model. Montana's equations and in-hand manipulation need differential geometry of surfaces and can come last.

## Before you start

From this volume, the chapter needs the [twist](/rigid-body-twist/), the [wrench](/wrench/) and the [adjoint map](/adjoint-map-se3/) of Chapter 37.1, [Jacobian statics duality](/jacobian-statics-duality/) of Chapter 37.2, and the [manipulator equation](/manipulator-equation/), its [skew symmetry](/skew-symmetry-of-manipulator-dynamics/) and its [linearity in the dynamic parameters](/linearity-in-dynamic-parameters/) of Chapter 37.3. The closure tests use the [convex hull](/convex-hull/), the [conic hull](/conic-hull/) and the [support function](/support-function/) of Volume 13, and [linear feasibility](/linear-feasibility/) and the [simplex method](/simplex-method/) of Volume 15. The arm controllers rest on the [Lyapunov function](/lyapunov-function/) and [LaSalle's invariance principle](/lasalle-invariance-principle/) of Volume 36. Visual servoing uses the [pinhole camera model](/pinhole-camera-model/) of Volume 28, the [pseudoinverse](/pseudoinverse/) of Volume 12 and [perspective-n-point](/perspective-n-point/) of Volume 38. The planning group uses the [configuration space](/configuration-space/), [motion planning](/motion-planning/) and [conformant planning](/conformant-planning/) of Volume 29.
