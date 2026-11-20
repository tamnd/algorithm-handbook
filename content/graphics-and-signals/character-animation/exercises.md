1. ◦ A planar arm has the shoulder at the origin, an upper arm of length 1 and a forearm of length 1. In the [bind pose](/bind-pose/) the arm lies straight along $x$, so the elbow is at $(1, 0)$. A pose turns the shoulder by 30° and the elbow by 60° in its parent's frame. Give the elbow and wrist positions. A vertex at $(1.5, 0)$ in the bind pose is weighted fully to the forearm. Where does $C = M B^{-1}$ put it?

2. ◦ A forearm twists by $\theta$ about its own axis, and a ring of vertices sits halfway between the two joints with weights $1/2$. Use the [candy wrapper](/candy-wrapper-artifact/) formula to find the factor by which [linear blend skinning](/linear-blend-skinning/) shrinks the ring at $\theta = 90°$, 120° and 180°. Do the same for a ring with weight $1/4$ at 180°, and for weight $1/2$ at 360°.

3. ◦ A [blendshape](/blendshape-model/) face has one vertex with the neutral position $(0, 0)$, a "smile" target at $(1, 0)$ and an "open" target at $(0, 2)$. Find the vertex for the delta weights $w = (0.5, 0.25)$, and the coefficients of the same shape in the whole-face form, which sum to 1. With $0 \le w \le 1$, which positions can the vertex reach? Can it reach $(1.2, 0.5)$?

4. ◦ A leg has a thigh of 0.45 m and a shin of 0.50 m, and the ankle target is 0.8 m from the hip. Use [two-bone inverse kinematics](/two-bone-inverse-kinematics/) to find the angle at the hip between the thigh and the line to the target, and the inner angle at the knee. For which distances is the target reachable?

5. ◦ In [motion warping](/motion-warping/), a channel gets the keys $(0, v_0)$ and $(40, v_1)$, with the offsets 0.2 and $-0.2$. There is no scale curve. What offset is added at frame 10, and at frame 60? A time warp has the pairs $(0, 0)$, $(30, 60)$ and $(90, 120)$. Which original times do new frames 15, 60 and 100 read?

6. ◦ A [motion graph](/motion-graph/) is built from 4 minutes of capture at 120 frames per second. How many entries does the frame distance matrix have, and how much memory does it need at 4 bytes per entry? With the window $k = 5$, list the blend weights $\alpha(p)$ of a transition for $p = 0, \dots, 4$.

7. ◦ A [motion matching](/motion-matching/) database has two features: speed, with mean 1 m/s, standard deviation 0.5 and weight 1; and turn rate, with mean 0, standard deviation 2 and weight 2. The playable frames have $(1.2, 1.0)$, $(0.8, -1.0)$ and $(1.5, 0.5)$, and the query is $(1.1, 0.2)$. Normalize everything, give the three costs and the chosen frame. Which frame wins if the turn weight is 4?

8. ◦ In the [social force model](/social-force-model/) with the constants of Helbing, Farkas and Vicsek, find the standing distance between a person pushing at $v^0 = 1.5$ m/s and a fixed person, with $r_{ij} = 0.6$ m. Compare it with the value for $v^0 = 1$ m/s. For which steps $\Delta t$ does the relaxation of a lone walker converge under symplectic Euler, and for which does it not overshoot?

9. ◦ In [DeepMimic](/deepmimic/), a step has the summed squared pose error 0.1, velocity error 1.0, end effector error 0.01 m² and center of mass error 0.01 m². Compute the four terms and $r^I$, then $r$ with a task reward of 0.5. What is the largest return of an episode of 300 steps with $\gamma = 0.99$?

10. ◦ In the weight step of [skinning decomposition](/skinning-decomposition/), one vertex has the candidate positions $(1, 0)$ under bone 1 and $(0, 1)$ under bone 2. Find the best convex weights and the squared error for the targets $(0.8, 0.6)$ and $(-1, 0.5)$.

11. • Write the unit dual quaternion of the motion "rotate by 90° about $z$, then translate by $(1, 0, 0)$". Check that the real and dual parts are orthogonal. Blend it with the identity at weights $1/2$ by [dual quaternion skinning](/dual-quaternion-skinning/). Give the rotation angle of the result and the image of the origin. Compare it with the linear blend of the two transforms, and explain the difference through the fixed point of the motion.

12. • An elbow sits at $(1, 0, 0)$. The forearm joint rotates by 120° about $z$ through the elbow, and a vertex at $(1, 0.2, 0)$ has weights $1/2$ on the upper arm and $1/2$ on the forearm. Find the vertex under linear blend skinning and under dual quaternion skinning, and the distance of each from the elbow.

13. • Take the [pose space deformation](/pose-space-deformation/) example of its entry: poses 0 and $\pi/2$, corrections 0 and 0.1, and the Gaussian $\varphi(r) = \exp(-r^2/(2\sigma^2))$. Use $\sigma = 1$ instead of 0.5. Find $\varphi_{12}$, the two coefficients and the correction at $\pi/4$, and compare it with 0.028913 for $\sigma = 0.5$ and with the linear value 0.05.

14. • In [verbs and adverbs](/verbs-and-adverbs/), four examples have the adverbs $p = 0, 1, 2, 3$ and the values $y = 1, 2, 2, 4$. Find the least squares linear part and the residuals, and check that the residuals are orthogonal to the constant and to $p$. With the radius rule of the entry, every $\alpha_i = 2$. What does the interpolant give at $p = 10$?

15. • In [motion retargeting](/motion-retargeting/), the root height has a displacement made of uniform cubic B-splines. The control point $c_j$ sits at the knot frame $2j$. One constraint asks for the change $-0.2$ at frame 9, halfway between two knots, and only the root may move. Find the four basis values at frame 9, the least norm control points, and the change at the knot frames 4 to 14.

16. • In [footskate cleanup](/footskate-cleanup/), a planar leg has $l_1 = 0.45$ and $l_2 = 0.50$, the hip is at $(0, 0.94)$ and the planted ankle target is at $(0.3, 0)$. Is the target in reach? With the stretch limit $\epsilon = 0.05$, what stretch factor does the leg get, and does the root move? If no stretch were allowed, how far would the hip have to drop straight down?

17. • In the toy problem of [spacetime constraints](/spacetime-constraints/), a unit mass moves a distance $D$ in time $T$, at rest at both ends. Show by a change of variables that the least effort is $12 D^2 / T^3$, and give it for $D = 2$, $T = 2$. By what factor does the effort fall when the time doubles?

18. • A cell of [continuum crowds](/continuum-crowds/) has the known neighbors $\phi = 1$ on one axis and $\phi = 1.5$ on the other, with $C\,\Delta x = 1$. Solve the two-term update. Then solve it with the neighbors 1 and 2.5, and say why the answer comes from one neighbor only.

19. • Redo the square example of [automatic rigging](/automatic-rigging/) with $c = 0.5$ instead of 1. Find the weight of bone A at the lower corners, and say whether more or less heat leaks to the far side.

20. • In [direct manipulation](/blendshape-direct-manipulation/), one vertex has the deltas $d_1 = (1, 0, 0)$ and $d_2 = (0, 1, 0)$, with $\alpha = 0.5$, $\mu = 0$ and $w_0 = 0$. The animator drags the vertex to $(1, 1, 0)$ and keeps the mouse there, so each solve starts from the last weights. Give the weights after one, two, three and four solves, and the factor by which the error falls per solve.

21. • A [registration curve](/registration-curves/) uses the slope limit $L = 1$ and the frame distances below, with rows $i = 0, 1, 2$ and columns $j = 0, \dots, 3$. Find the cheapest admissible path and its cost.

| | $j=0$ | $j=1$ | $j=2$ | $j=3$ |
|---|---|---|---|---|
| $i=0$ | 0 | 2 | 5 | 9 |
| $i=1$ | 4 | 1 | 1 | 6 |
| $i=2$ | 8 | 5 | 2 | 0 |

22. ★ Show that the planar blend $(1 - w) I + w R_\theta$ of the identity and a rotation is a rotation times a scale $s$ with $s^2 = 1 - 2w(1 - w)(1 - \cos\theta)$. Find the smallest $s$ over all $\theta$ for a fixed $w$. Show that the determinant of $(I + R_\theta)/2$ is $\cos^2(\theta/2)$.

23. ★ In dual quaternion skinning, the signs are aligned to the pivot $p$, the joint of largest weight, so that every $q_i \cdot q_p \ge 0$. Prove that the real part $b_0$ of the blend then has $|b_0| \ge w_p \ge 1/k$ for $k$ influences, so the normalization never divides by zero. Give two inputs whose blend has $b_0 = 0$ without the alignment.

24. ★ A face has the targets L $= (1, 0)$ and R $= (0, 1)$ at two scalar vertices, and a third target B $= (1, 1)$ for both sides. Show that the least squares weights for the goal $(1, 1)$ are not unique. Then solve the problem of direct manipulation with $w_0 = 0$, $\mu = 0$ and $\alpha = 0.1$, and find the limit as $\alpha \to 0$.

25. ★ Prove that registration curves admit a path between motions of $n$ and $m$ frames under the slope limit $L$ if and only if $\max(n, m) \le (L + 1)\min(n, m)$. Check it on the two walks of 31 and 46 frames with $L = 2$ from the entry.

26. ★ In a directed graph of frames, show that a walk of any length can start at a frame exactly when that frame reaches a cycle. A motion graph keeps a stronger property: it prunes to the largest strongly connected component. Give a small graph where a frame can play forever but is still pruned, and explain why the motion graph wants the stronger property.
