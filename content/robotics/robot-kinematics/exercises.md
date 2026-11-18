1. ◦ Use [Grübler's formula](/grubler-formula/) to count the degrees of freedom of two parallel robots. (a) The planar 3-RRR robot: a base and a moving platform joined by three legs, each a chain of two links with a revolute joint at the base, one between the links and one at the platform. (b) The spatial 3-RPS robot: three legs, each with a revolute joint at the base, a prismatic joint in the leg and a spherical joint at the platform.

2. ◦ A planar 2R arm has link lengths $L_1 = 2$ and $L_2 = 1$ and no joint limits. How many [inverse kinematics](/inverse-kinematics/) solutions does each of the targets $(0, 0)$, $(1, 0)$, $(2, 1)$, $(3, 0)$ and $(0, 4)$ have?

3. ◦ For the arm of Exercise 2, find both solutions $(\theta_1, \theta_2)$ for the target $(2, 1)$. Give $\cos\theta_1$ and $\sin\theta_1$ exactly.

4. ◦ An arm has two revolute joints with the [Denavit-Hartenberg](/denavit-hartenberg-convention/) rows $(\theta_1, d_1, a_1, \alpha_1) = (\theta_1, 1, 0, 90°)$ and $(\theta_2, d_2, a_2, \alpha_2) = (\theta_2, 0, 1, 0)$, with $A_i = R_z(\theta_i)T_z(d_i)T_x(a_i)R_x(\alpha_i)$. Find the position of the end of the arm, the origin of frame 2, as a function of $\theta_1$ and $\theta_2$, and evaluate it at $\theta = (0, 0)$ and at $\theta = (90°, 30°)$.

5. ◦ Write the planar 2R arm with $L_1 = 2$ and $L_2 = 1$ in the [product of exponentials](/product-of-exponentials-formula/) form. Both joint axes point along $z$; at $\theta = 0$ the arm lies along the $x$ axis. Give the home pose $M$, the space screw axes $\mathcal S_1, \mathcal S_2$ and the body screw axes $\mathcal B_1, \mathcal B_2$, each as $(\omega, v)$ with $v = -\omega \times q$ for a point $q$ on the axis.

6. ◦ For the same arm at $\theta = (0, \pi/2)$, compute the $2 \times 2$ position Jacobian $J$, its determinant, its singular values, the [Yoshikawa measure](/yoshikawa-manipulability-measure/) $w$ and the condition number $\sigma_1/\sigma_2$.

7. ◦ The arm of Exercise 6 holds up a load: its end pushes on the load with the force $F = (0, 10)$ N. Ignore the weight of the links. Which joint torques hold the arm still? Explain from the geometry why one of them is zero.

8. ◦ Give the degree of [redundancy](/kinematic-redundancy/), $n - m$, for each arm and task: (a) a spatial 7R arm, full pose; (b) a planar 5R arm, position of the end only; (c) a planar 3R arm, position and orientation of the end; (d) a spatial 6R arm, position of the end only; (e) a spatial 6R arm, full pose.

9. • Take ZYX angles, $R = R_z(\alpha)R_y(\beta)R_x(\gamma)$. Find the matrix $T(\alpha, \beta)$ with $\omega = T(\alpha, \beta)(\dot\alpha, \dot\beta, \dot\gamma)$, its determinant, and the angles at which the [analytic Jacobian](/analytic-jacobian/) built on these angles fails even though the arm itself is not singular.

10. • For the arm of Exercise 5 at $\theta = (0, \pi/2)$, compute the [space and body Jacobians](/space-and-body-jacobian/) as $6 \times 2$ matrices, with the angular part first. Check that $\dot p = v_s + \omega \times p$, with $p$ the position of the end, gives the linear part of the Jacobian of Exercise 6.

11. • Show that $\det \mathrm{Ad}_T = 1$ for every $T \in SE(3)$. Deduce that a $6 \times n$ space Jacobian and the body Jacobian at the same configuration have the same Yoshikawa measure.

12. • A planar 3R arm has unit links and is at $\theta = (0, \pi/2, 0)$. Compute its $2 \times 3$ position Jacobian, the least-norm joint velocity $J^{+}v$ for $v = (0, 1)$, and a unit vector that spans the null space of $J$. Check that the two vectors are orthogonal. Use exact fractions.

13. • A planar 2R arm with unit links is at $\theta = (0, \pi/2)$, and the error is $e = (0.1, 0)$. Compute three steps: the exact step $J^{-1}e$, the [damped least squares](/damped-least-squares-inverse-kinematics/) step with $\lambda = 0.5$, and the [Jacobian transpose](/jacobian-transpose-method/) step $\alpha J^{\mathsf T}e$ with the gain $\alpha = \langle e, JJ^{\mathsf T}e\rangle / |JJ^{\mathsf T}e|^2$. For each, give the residual $|e - J\Delta\theta|$ of the linear model.

14. • Run [Newton's method](/newton-raphson-inverse-kinematics/) for the position of a planar 2R arm with unit links, from $\theta^0 = (0, \pi/2)$ to the target $(0.9, 1.1)$. Write a short program, print the distance from the end to the target after each step, and say what the numbers show about the rate.

15. • A planar 2R arm with unit links lies stretched along the $x$ axis, $\theta = (0, 0)$, and the target is $(0, 1.5)$. Do one sweep of [cyclic coordinate descent](/cyclic-coordinate-descent-inverse-kinematics/), from the tip joint to the base joint, and one iteration of [FABRIK](/fabrik/): place the end at the target and work back to the base, then put the base back and work out to the end. Give the distance from the end to the target after each.

16. • Solve the second [Paden-Kahan subproblem](/paden-kahan-subproblems/) for $\omega_1 = (0, 0, 1)$ and $\omega_2 = (1, 0, 0)$, both axes through the origin, $p = (1, 1, 0)$ and $q = (1, 1, 0)$: find every $(\theta_1, \theta_2)$ with $e^{[\omega_1]\theta_1}e^{[\omega_2]\theta_2}p = q$.

17. • A spatial four-bar has the joints R, S, S, R in order around the loop: a crank turns about a fixed axis, a coupler with a ball joint at each end, and a rocker on a second fixed axis. Count its degrees of freedom with Grübler's formula. Find a motion that the count includes but that does not move the crank or the rocker, and give the number of useful degrees of freedom.

18. • The planar 3R arm of Exercise 12 has two tasks. Task 1, of higher priority, keeps the end where it is: $e_1 = (0, 0)$. Task 2 turns the end by $e_2 = 0.1$ rad, with $J_2 = (1, 1, 1)$. Compute the [task-priority](/task-priority-inverse-kinematics/) step $\Delta\theta = J_1^{+}e_1 + (J_2P_1)^{+}(e_2 - J_2J_1^{+}e_1)$, with $P_1 = I - J_1^{+}J_1$, and check both tasks.

19. • Prove that the damped least squares step $\Delta\theta = J^{\mathsf T}(JJ^{\mathsf T} + \lambda^2I)^{-1}e$ minimizes $|J\Delta\theta - e|^2 + \lambda^2|\Delta\theta|^2$, and that $|\Delta\theta| \le |e|/(2\lambda)$ for every $J$. When does equality hold?

20. ★ A planar 3R arm has unit links, and the task is the position of the end. Find all configurations at which the $2 \times 3$ Jacobian has rank less than 2, and prove that there are no others.

21. ★ Run the Jacobian transpose iteration $\theta \leftarrow \theta + \alpha J^{\mathsf T}e$ with a fixed gain on the 2R arm with unit links near the solution $(0, \pi/2)$ of the target $(1, 1)$. Find the gains $\alpha$ for which the iteration converges from every start close enough, the gain with the fastest local rate, and that rate.

22. ★ A planar 2R arm has link lengths $L_1$ and $L_2$. Its [manipulability ellipsoid](/manipulability-ellipsoid/) for the position of the end is a circle when $JJ^{\mathsf T}$ is a multiple of $I$. Find the ratio $L_2/L_1$ and the angles $\theta_2$ for which this happens, and the value of $w$ there.

23. ★ The 2R arm of [kinematic calibration](/kinematic-calibration/) gets two more parameters, the joint offsets: $p = (L_1\cos(\theta_1 + \delta_1) + L_2\cos(\theta_1 + \delta_1 + \theta_2 + \delta_2), \ldots)$, with nominal values $L_1 = L_2 = 1$, $\delta_1 = \delta_2 = 0$. The end position is measured at some poses. Show that two poses with the same $\theta_2$ never identify the four parameters, whatever $\theta_1$ they use, and that the poses $(0, 0)$ and $(0, \pi/2)$ do.

24. ★ A general spatial 3R arm places a point, the wrist center, at a target $p$. Show that the position problem reduces to one polynomial equation of degree at most 4 in $\tan(\theta_3/2)$, and conclude that it has at most 4 solutions when the polynomial is not identically zero.
