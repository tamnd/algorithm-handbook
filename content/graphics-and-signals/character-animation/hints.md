1. The elbow is at $(\cos 30°, \sin 30°) = (0.86603, 0.5)$. The forearm points at $30° + 60° = 90°$, so the wrist is at $(0.86603, 1.5)$. $B^{-1}$ takes the vertex to $(0.5, 0)$ in the forearm frame, and $M$ turns that by 90° and adds the elbow: $(0.86603, 1.0)$.

2. At $w = 1/2$ the factor is $|\cos(\theta/2)|$: 0.70711, 0.5 and 0. At $w = 1/4$ and 180°, $s = |1 - 2w| = 0.5$. At 360° the factor is 1, because a full turn is the identity matrix.

4. $\cos\alpha = (0.2025 + 0.64 - 0.25)/0.72 = 0.82292$, so $\alpha = 34.62°$. $\cos\beta = (0.2025 + 0.25 - 0.64)/0.45 = -0.41667$, so $\beta = 114.62°$ and the knee bends 65.38° from straight. The target is in reach for $0.05 \le d \le 0.95$ m.

6. $f = 28\,800$ frames and $f^2 = 8.29 \cdot 10^8$ entries, about 3.3 GB. The weights are $112/125$, $81/125$, $44/125$, $13/125$ and 0, that is 0.896, 0.648, 0.352, 0.104 and 0.

7. The frames become $(0.4, 1.0)$, $(-0.4, -1.0)$ and $(1.0, 0.5)$, and the query becomes $(0.2, 0.2)$. The costs are 0.68, 1.8 and 0.73, so frame 0 wins. With turn weight 4 the costs are 2.6, 6.12 and 1.0, and frame 2 wins. The weights are tuning, and they decide the match.

8. The driving force is $80 \cdot 1.5/0.5 = 240$ N, and $d^* = 0.6 + 0.08 \ln(1000/120) = 0.770$ m, against 0.802 m at 1 m/s: the faster walker stands closer. The relaxation converges for $0 < \Delta t < 2\tau = 1$ s and does not overshoot for $\Delta t \le \tau = 0.5$ s.

11. $r = (0.70711, 0, 0, 0.70711)$ and $d = \tfrac12 t r = (0, 0.35355, -0.35355, 0)$, and $r \cdot d = 0$. The blend has a rotation of 45° and sends the origin to $(0.5, -0.20711, 0)$. The linear blend sends it to $(0.5, 0, 0)$. The motion is a rotation by 90° about the fixed point $(0.5, 0.5)$, and the dual quaternion blend turns by half the angle about the same point.

12. The two rigid copies are $(1, 0.2, 0)$ and $(0.82679, -0.1, 0)$. Their average, the linear blend, is $(0.91340, 0.05, 0)$, at distance 0.1 from the elbow, half of the rest distance. Dual quaternion skinning rotates the vertex by 60° about the elbow, to $(0.82679, 0.1, 0)$, and keeps the distance 0.2.

15. The basis values at $u = 1/2$ are $1/48$, $23/48$, $23/48$ and $1/48$. Their squares sum to $265/576 = 0.46007$. The control points are $-0.2$ times the basis values divided by that sum: $(-0.00906, -0.20830, -0.20830, -0.00906)$. The change is $-0.17509$ at frames 8 and 10, $-0.04075$ at frames 6 and 12, and $-0.00151$ at frames 4 and 14. It is 0 from frame 16 and up to frame 2.

18. $(x - 1)^2 + (x - 1.5)^2 = 1$ gives $x = (5 + \sqrt 7)/4 = 1.9114$, which is above both neighbors, as causality needs. With 1 and 2.5 the discriminant is negative, and the one-term value $1 + 1 = 2$ is below 2.5. So the larger neighbor would not be accepted before this cell, and it plays no part.

22. Write the blend as $\begin{pmatrix} a & -b \\ b & a \end{pmatrix}$ with $a = 1 - w + w\cos\theta$ and $b = w\sin\theta$. A matrix of this form is $\sqrt{a^2 + b^2}$ times a rotation. Expand $a^2 + b^2$. The smallest value is at $\theta = \pi$, where $s = |1 - 2w|$. For $w = 1/2$, $s^2 = \cos^2(\theta/2)$ is the determinant.

23. $|b_0| \ge b_0 \cdot q_p = \sum_i w_i\, q_i \cdot q_p \ge w_p\, q_p \cdot q_p = w_p$, and the largest of $k$ weights that sum to 1 is at least $1/k$. Without the alignment, $q$ and $-q$ with weights $1/2$ give $b_0 = 0$.

24. The goal asks for $w_L + w_B = 1$ and $w_R + w_B = 1$, a line of solutions. The regularized solve gives $(10/31, 10/31, 20/31) = (0.32258, 0.32258, 0.64516)$, with both vertices at $30/31$. As $\alpha \to 0$ the weights tend to the least norm solution $(1/3, 1/3, 2/3)$, which shares the motion among the dependent targets.

25. Take $n \le m$. The path needs $m - n$ more steps along $j$ than along $i$. Runs along $j$ have at most $L$ steps and must be separated by diagonal steps or steps along $i$. An $i$ step costs one more $j$ step, so it never helps. With $n - 1$ diagonals there are at most $n$ runs, which gives $m - n \le Ln$. For the walks, $46 \le 3 \cdot 31 = 93$.
