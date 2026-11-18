1. The path has the eigenvalues $0$, $2 - \sqrt 2 = 0.586$, $2$ and $2 + \sqrt 2 = 3.414$. The star has $0$, $1$, $1$ and $4$. The star agrees faster, since its $\lambda_2 = 1$ is larger. With $\varepsilon = 1/4$ the factors are $\max(0.854, 0.146) = 0.854$ on the path and $\max(0.75, 0) = 0.75$ on the star; both steps satisfy $\varepsilon < 1/\Delta$.

5. Full window: robot 0 bids 4 on task 0, robot 1 bids 1 on task 1 and robot 2 bids 5 on task 1, so task 0 goes to robot 0 and task 1 to robot 1. In round 2 robot 2 takes task 2 for 8, and the total is 13 s. One task per round: task 0 goes to robot 1 for 3, task 1 to robot 2 for 5 and task 2 to robot 0 for 7, total 15 s. The optimum gives task 0 to robot 0, task 1 to robot 2 and task 2 to robot 1, total 11 s.

9. The rounds give $(0.4, 0.8, 1.6, 2.4, 2.8)$ with diameter 2.4, then $(0.6, 1, 1.6, 2.2, 2.6)$ with diameter 2, then $(1.1, 1.1, 1.6, 2.1, 2.1)$ with diameter 1, and in round 4 every robot sees every other one and all move to 1.6. In each round the target lies within $V/2$ of every midpoint, so no safe disk cuts a step, and the number of links grows from 4 to 10.

11. The closed form is $\tan(e/2) = \tan(e(0)/2)\,e^{-v_L t/d}$. So $t = (d/v_L)\ln(\tan 1/\tan 0.005) = 0.4 \ln 311.5 = 2.30$ s. With $v_L < 0$ the sign flips, $e = 0$ becomes unstable, and the follower turns around.

13. There are $5 \cdot 4 \cdot 3 = 60$ placements. A pebble can never pass another on a cycle, so the cyclic order of the three labels is fixed. Every placement with the same cyclic order can be reached, and three labels have two cyclic orders, so 30 placements are reachable.

14. Take $U = \begin{pmatrix} 1 + \delta & 1 \\ 1 & 0 \end{pmatrix}$ for a small $\delta > 0$. Greedy takes $1 + \delta$ and then must take $0$, while the other matching has value 2. The ratio $(1 + \delta)/2$ tends to $1/2$. CBBA under diminishing marginal gain returns the sequential greedy assignment, so it reaches the same value here.

15. For $\tau = 2$ the relative velocity $(2, 0)$ is outside, since the discs would touch only at $t = 2.5$ s; $A$ keeps $(1, 0)$. For $\tau = 4$ it is inside. With $\sin\alpha = 1/6$, the nearest boundary point lies on a leg, and $u$ has length $2\sin\alpha = 1/3$. On the leg below the axis, $u = (-1/18, -\sqrt{35}/18)$ and $v'_A = v_A + u/2 = (35/36, -\sqrt{35}/36) \approx (0.972, -0.164)$ m/s. The other leg gives the mirror image.

17. The border $b$ is the midpoint of the robots, and each robot sits at the centroid of its cell: $p_1 = 2b/3$ and $p_2 = \tfrac23 (1 + b + b^2)/(1 + b)$. Then $2b = p_1 + p_2$ gives $b^2 + b - 1 = 0$, so $b = 0.618$, $p_1 = 0.412$ and $p_2 = 0.824$. The cost is $0.0155$, against $0.0208$ for $1/4$ and $3/4$.

18. Two agents with $\varepsilon = 1$ swap their values in every round. In general, put $x_i = 1$ on one side and $-1$ on the other. Then $Lx = 2\Delta x$, and since $\lambda_r \le 2\Delta$ for every graph of largest degree $\Delta$, $\lambda_r = 2\Delta$. With $\varepsilon = 1/\Delta$ this mode is multiplied by $-1$ in every round.

19. On the 4-cycle the cyclic order is fixed, so 12 of the 24 placements are reachable. With a chord the graph has a triangle, so it is not bipartite, and the moves around the triangle change the parity of the permutation; all 24 placements are reachable.

20. $VO^\tau$ is the set of $s\,y$ with $y$ in the disc of center $p$ and radius $R$ and $s \ge 1/\tau$, which is convex. Write $w = v_A - v_B$. The two half-planes have the same $u$ with opposite signs, so $(v'_A - v'_B - (w + u)) \cdot n \ge 0$. This is the closed half-plane at the nearest boundary point $w + u$, which supports $VO^\tau$, and it misses the open set.

21. Take a pair $(i, j)$ of an optimal matching. Look at the first greedy pick that uses robot $i$ or task $j$. Just before it, the pair $(i, j)$ was still free, so the greedy pick has utility at least $U_{ij}$. Each greedy pair is the first pick for at most two optimal pairs, one at its robot and one at its task, so twice the greedy total is at least the optimum. For costs, the example of the entry with $1$, $2$, $2$ and $M$ gives the ratio $(1 + M)/4$, which grows without bound.
