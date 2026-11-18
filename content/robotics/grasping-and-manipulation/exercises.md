1. ◦ A block rests on a ramp, with $\mu = 0.3$ between them. Up to what tilt does it stay at rest? A contact with the same $\mu$ is asked to transmit the force $(f_{t1}, f_{t2}, f_n) = (1, 1, 4)$ in contact coordinates. Is the force inside the [friction cone](/friction-cone/)?

2. ◦ Two fingers hold a 2 kg box by its vertical sides and carry its weight by friction alone, with $\mu = 0.4$ and $g = 9.81\ \text{m/s}^2$. What is the least squeeze force of each finger?

3. ◦ A parallel-jaw gripper closes on a part whose two sides are each tilted by $15°$ from the closing direction. For which $\mu$ is the grasp [antipodal](/antipodal-grasp/)?

4. ◦ A point feature sits at the normalized image coordinates $(x, y) = (0.2, -0.1)$ at depth $Z = 2$. Use the [interaction matrix](/interaction-matrix/) to find its image velocity $(\dot x, \dot y)$ when the camera moves forward along its optical axis at $v_z = 0.1$, and when it turns about the optical axis at $\omega_z = 0.1$.

5. ◦ An arm under [impedance control](/impedance-control/) with stiffness $K_d = 500$ N/m has its goal 1 cm inside a surface of stiffness $k_e = 5000$ N/m. What force does it press with at rest? What is the limit as the surface becomes rigid?

6. ◦ An [admittance controller](/admittance-control/) runs its virtual dynamics at $\Delta t = 1$ ms with $D_a = 100$ N s/m and $K_a = 1000$ N/m. What is the least virtual mass $M_a$ for which the discrete virtual system does not diverge?

7. ◦ An object slides on a table with its center of friction at the origin. A finger pushes it at the contact point $(x, -1)$, where the normal is $(0, 1)$ and $\mu = 0.5$. Apply [Mason's voting theorem](/mason-voting-theorem/) for $x = 0.3$ with pushing directions $(0, 1)$ and $(-1, 1)$, and for $x = 0.6$ with any pushing direction in the cone.

8. ◦ A peg of radius $r = 5$ mm with $\mu = 0.2$ is in two-point contact at depth $l = 1.5$ mm, and the robot pushes with $F_z = 20$ N. Using the bound of the [peg-in-hole](/peg-in-hole/) entry, find the moment $M$ at which the peg jams for $F_x = 0$, $F_x = 3$ N and $F_x = -3$ N. Is wedging possible at this depth?

9. • The rectangle $[-2, 2] \times [-1, 1]$ is touched by frictionless fingers at $(1, -1)$ with normal $(0, 1)$, at $(0, 1)$ with normal $(0, -1)$, at $(-2, 0)$ with normal $(1, 0)$ and at $(2, -\tfrac12)$ with normal $(-1, 0)$. With wrenches $(p_x n_y - p_y n_x, n_x, n_y)$, show that the grasp is in first-order [form closure](/form-closure/) and give a strictly positive combination that sums to zero.

10. • A one-link arm has gravity torque $9.81 \cos q$, with $q$ measured from the horizontal. It runs plain PD control $\tau = K_p(q_d - q) - K_d \dot q$ with no gravity term, and $q_d = 0$. Find the rest angle for $K_p = 50$ and for $K_p = 200$. What does [gravity compensation](/pd-control-with-gravity-compensation/) change?

11. • A one-link arm of length 1 has a true mass of 1.2 kg at its tip, but [computed-torque control](/computed-torque-control/) uses a model with 1 kg, with $K_p = 100$ and the set point $q_d = 0$ (horizontal). Find the rest error to three significant figures. Which kind of model error gives a constant offset, and which an error that grows with the acceleration?

12. • Four point fingers sit at the corners of a square of side $s$, centerd on a disc of radius $r$ in the plane. For which $s$ do they [cage](/caging-grasp/) the disc without touching it? Is a caged disc in form closure?

13. • A rectangle has the edges $x = 0$ and $x = 4$, both for $0 \le y \le 3$, and $\mu = 1/2$. Two fingers on these edges are in force closure exactly when the line between them lies strictly inside both cones. For which lengths $L$ does every pair of fingers, one in $[a, a + L]$ on each edge, give force closure, in the spirit of [independent contact regions](/independent-contact-regions/).

14. • A one-link arm has $M = a$ and gravity torque $b \cos q$, with true $a = 1$ and $b = 9.81$. The [Slotine-Li controller](/slotine-li-adaptive-control/) uses $\tilde q = q - q_d$, $\dot q_r = \dot q_d - \lambda \tilde q$, $s = \dot q - \dot q_r$, the regressor $Y = (\ddot q_r, \cos q)$, the law $\tau = Y\hat\pi - K_D s$ and the update $\dot{\hat\pi} = -\Gamma Y^\top s$. With $\lambda = 5$, $K_D = 20$, $\Gamma = \operatorname{diag}(1, 20)$ and $\hat\pi = (0.5, 4.905)$, compute $\tau$ and $\dot{\hat\pi}$ at $t = 0$ for $q = 0.2$, $\dot q = 0$, and the desired $q_d(t) = 0.5 \sin t$.

15. • A $1 \times 3$ rectangle has the width $d(\theta) = \lvert\cos\theta\rvert + 3\lvert\sin\theta\rvert$ in the squeeze direction $\theta$. A frictionless parallel-jaw squeeze turns the part to the nearest local minimum of $d$. Find the local maxima, the two stable orientations, and the fraction of uniformly random initial orientations that end with the jaws on the long sides.

16. • [Image-based visual servoing](/image-based-visual-servoing/) uses three points, so that the interaction matrix $L$ is $6 \times 6$, and the law $v = -\lambda L^{-1} e$ with exact depths and $\lambda = 0.5$. Show that the image error decays as $e(t) = e^{-\lambda t} e(0)$ while $L$ stays invertible. How long does it take to reduce the error by a factor of 100?

17. ★ A one-link arm with gravity torque $9.81 \cos q$ uses PD control with a constant gravity term, $\tau = K_p(q_d - q) - K_d \dot q + 9.81 \cos q_d$, and $q_d = \pi/2$ (straight up). Show that $q_d$ is the only equilibrium when $K_p \ge 9.81$. For $K_p = 5$, find all equilibria in $(-\pi, 2\pi)$ and say which are stable.

18. ★ [Sensorless orienting](/sensorless-part-orienting/) is the search for a reset word of an automaton. Take the states $0, 1, 2, 3$ and two actions: $a$ sends $i$ to $i + 1 \bmod 4$, and $b$ sends 0 to 1 and fixes the other states. Find a shortest word that sends every state to one state, and its length.

19. ★ Using exercise 15, design a plan of parallel-jaw squeezes that brings the $1 \times 3$ rectangle from any orientation to one orientation up to the symmetry $\pi$. Show that one squeeze is not enough, and give the angle of the second squeeze relative to the first, with its margin. Compare with what [Goldberg's algorithm](/goldberg-part-orienting-algorithm/) promises.

20. ★ For the one-link arm of exercise 14 with the Slotine-Li law, show that $V = \tfrac12 a s^2 + \tfrac12 \tilde\pi^\top \Gamma^{-1} \tilde\pi$, with $\tilde\pi = \hat\pi - \pi$, has $\dot V = -K_D s^2$. Explain why this gives $\tilde q \to 0$ but not $\hat\pi \to \pi$.
