## What to remember

- A Coulomb contact can transmit the forces of its **friction cone**, $\lVert f_t \rVert \le \mu f_n$ with $f_n \ge 0$, a circular cone of half-angle $\arctan \mu$. A pyramid with $k$ edges on the cone keeps a fraction $\cos(\pi/k)$ of the tangential capacity in the worst direction and makes every later test linear.
- The **grasp matrix** $G$ maps the contact forces to the net wrench on the object, and $G^\top$ maps the object twist to the contact velocities. A grasp is in **force closure** when $G$ has full rank and some internal force $G\lambda = 0$ lies strictly inside every cone.
- **Form closure** holds by geometry alone, with frictionless contacts. It needs at least 4 contacts in the plane and 7 in space, and these numbers suffice for every body except a disc or a surface of revolution, which no number of frictionless contacts can hold.
- With friction, two fingers suffice in the plane, exactly when the line between them lies strictly inside both cones: the **antipodal** condition. In space two hard fingers never suffice, because nothing resists a spin about their line; two soft fingers or three non-collinear hard fingers can.
- The **force-closure test** is exact: with linearized cones it is a linear feasibility problem over the $N$ primitive wrenches, and its answer does not depend on the frame or the length unit. The **Ferrari-Canny metric**, the radius of the largest ball about the origin inside the grasp wrench space, does depend on the reference point and on the length $\rho$ that scales moments.
- **PD control with gravity compensation** makes every set point globally asymptotically stable with exact gravity. **Computed-torque control** gives exponential tracking with an exact model. The **Slotine-Li** law tracks with unknown constant parameters, but its estimates need persistent excitation to converge.
- **Impedance control** bounds the rest force on a surface of stiffness $k_e$ at $\frac{k_e K_d}{k_e + K_d}$ times the depth of the goal, at most $K_d$ times it. **Admittance control** needs $2D_a\Delta t + K_a\Delta t^2 < 4M_a$ for its discrete virtual dynamics.
- In quasi-static pushing, **Mason's voting theorem** gives the sense of rotation from three votes, whatever the pressure distribution. A sensorless plan is a reset sequence of a finite automaton, and **Goldberg's algorithm** finds a shortest squeeze plan for a polygon in $O(n^2 \log n)$ time, up to the symmetry of its squeeze function.

## Controllers side by side

| Controller | Needs | Guarantee | Time per step |
|---|---|---|---|
| [PD with gravity compensation](/pd-control-with-gravity-compensation/) | gravity model | global asymptotic, set points | $O(n)$ |
| [Computed torque](/computed-torque-control/) | full dynamic model | exponential tracking, exact model only | $O(n)$ |
| [Slotine-Li adaptive](/slotine-li-adaptive-control/) | regressor $Y$ | tracking error $\to 0$, parameters bounded | $O(n^2)$ |
| [Impedance](/impedance-control/) | torque interface | passive; rest force at most $K_d$ times depth | $O(n^3)$ |
| [Admittance](/admittance-control/) | force sensor, position loop | stable in free space if the step is small | $O(n)$ |
| [Hybrid position/force](/hybrid-position-force-control/) | contact geometry | force set directly in constrained directions | $O(n^3)$ |
| [Image-based visual servoing](/image-based-visual-servoing/) | interaction matrix, depths | local only; image error nonincreasing | $O(k)$ |
| [Position-based visual servoing](/position-based-visual-servoing/) | calibration, target model | global in pose; straight camera path | $O(1)$ |

: Controllers of the chapter for an arm with $n$ joints and, for visual servoing, $k$ point features. The guarantees hold under the assumptions of each entry, such as a rigid arm and exact depths.

## Choosing a method

- To decide whether a grasp holds, run the [force-closure test](/force-closure-test/). To compare grasps that hold, use the [Ferrari-Canny metric](/ferrari-canny-metric/), with the same reference point and $\rho$ for all of them.
- For a parallel-jaw gripper, look for antipodal pairs. If the fingers will land with errors, compute [independent contact regions](/independent-contact-regions/). If the object only needs to stay within reach, a [cage](/caging-grasp/) is enough.
- For free motion to set points, PD with gravity compensation is simple and safe. For fast tracking with a good model, use computed torque; with unknown loads, Slotine-Li.
- When the tool touches the world, use impedance control on a torque-controlled arm and admittance control on a stiff position-controlled one. Use hybrid control only when the contact geometry is known.
- Choose image-based servoing to keep the target in view, and position-based servoing for a predictable camera path.
