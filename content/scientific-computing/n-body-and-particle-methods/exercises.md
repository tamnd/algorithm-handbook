1. ◦ Three bodies with masses 2, 1 and 1 sit at $(0, 0)$, $(1, 0)$ and $(0, 2)$, with $G = 1$ and no softening. Use [direct summation](/direct-n-body-summation/) to compute the potential energy and the force on each body, and check that the three forces add up to zero.

2. ◦ A grid has spacing 1 and nodes at the integers. A unit mass sits at $x = 3.3$. Give its [cloud-in-cell](/cloud-in-cell-assignment/) weights, and its TSC weights on the nodes 2, 3 and 4. In 2D, give the four CIC weights of a unit mass at $(3.3, 5.75)$.

3. ◦ Eight points on a line are at $0$, $0.15$, $0.32$, $0.9$, $1.05$, $1.5$, $1.62$ and $1.79$. Find the groups of the [friends-of-friends algorithm](/friends-of-friends-algorithm/) with the linking length $0.2$, and again with $0.5$.

4. ◦ In a [hashed oct-tree](/hashed-oct-tree/) the key starts at 1 and each level appends the octal digit $4k_b + 2j_b + i_b$, from the top bit $b$ down. Find the level-3 key of the cell with integer coordinates $(i, j, k) = (3, 5, 6)$, in octal and in decimal. Give the key of its parent, the keys of its children, and read its level from the bit length.

5. ◦ A charge moves in a uniform magnetic field with gyration frequency $\Omega$, and the [Boris pusher](/boris-pusher/) takes steps of size $h$. Find the rotation angle per step for $\Omega h = 1$ and $\Omega h = 0.1$, and its relative error against $\Omega h$. How many steps does one full gyration take at $\Omega h = 1$? What happens to the speed?

6. ◦ Two vortex blobs of circulation $\Gamma = 2\pi$ sit at $(\pm 0.5, 0)$. With the Gaussian blob kernel of the [vortex particle method](/vortex-particle-method/), the induced speed is that of a point vortex times $1 - e^{-r^2/\delta^2}$. Find the angular velocity of the pair for $\delta = 1$ and for $\delta = 0.25$, and compare it with the value 2 for point vortices.

7. ◦ With [block time steps](/block-time-steps/) and $h_0 = 1$, four bodies want the steps $0.3$, $0.07$, $0.6$ and $0.2$. Each gets the largest step $h_0/2^k$ not above its wish. Give the steps, and count the force evaluations over the time interval $[0, 1]$. How many would a shared step equal to the smallest one need?

8. ◦ A [particle-in-cell](/plasma-particle-in-cell/) run uses units with plasma frequency $\omega_p = 1$, thermal speed $0.05$ and a periodic domain of length $4\pi$. The Debye length is the thermal speed over $\omega_p$. Give the largest step for which the leapfrog is stable, the number of steps per plasma period at $h = 0.2$, and the smallest number of cells with $\Delta x \le \lambda_D$.

9. • The 2D [truncation error bound](/multipole-truncation-error-bound/) for well-separated boxes is $\frac{A}{(p+1)(1-q)} q^{p+1}$ with $q = \sqrt2/3$. Find the smallest $p$ for which it is at most $10^{-6} A$.

10. • A cell holds two masses $\frac12$ at $(\pm 0.5, 0, 0)$, so its centre of mass is the origin and $b = 0.5$. The target is at $(2, 0, 0)$ and $G = 1$. Compute the exact potential, the monopole potential and the error, as fractions, and compare the error with the bound $G M b^2 / (d^2 (d - b))$ of the [multipole acceptance criterion](/multipole-acceptance-criterion/). Show that for this cell the bound exceeds the error by the factor $(d + b)/d$ at every $d > b$.

11. • Three unit masses sit at $A = (0, 0)$, $B = (3, 0.5)$ and $C = (3, -0.5)$, with $G = 1$. In the [Barnes-Hut algorithm](/barnes-hut-algorithm/), $A$ sees $B$ and $C$ in one cell of side 1 at distance 3, which $\theta = 0.5$ accepts, while $B$ and $C$ compute all their forces exactly. Find the force on each body and the total force. What happens to the total momentum?

12. • In a uniform 2D quadtree at level 2 there are $4 \times 4$ boxes. The interaction list of a box holds the children of its parent and of the parent's neighbours that are not adjacent to the box. Count the list for a corner box, an edge box and an inner box, and the total number of [multipole-to-local translations](/multipole-to-local-translation/) at this level. How many ordered pairs of adjacent boxes, each box counted as adjacent to itself, are there?

13. • A grid solver of the [Vlasov-Poisson system](/vlasov-poisson-system/) with velocity spacing $\Delta v$ shows a recurrence at $T_R = 2\pi/(k \Delta v)$. For the Landau mode $k = 0.5$, find $T_R$ for $\Delta v = 0.1$, and the number of velocity cells on $[-6, 6]$ needed to push $T_R$ past $t = 100$. The mode damps at the rate $0.1534$; by what factor has it decayed at $T_R$ for $\Delta v = 0.1$?

14. • Take one step of the [Hermite integrator](/hermite-n-body-integrator/) for $\ddot x = -x$, with jerk $-\dot x$, from $x = 1$, $v = 0$ with $h = 0.1$. Give the predicted and the corrected $x$ and $v$, and their errors against $\cos 0.1$ and $-\sin 0.1$.

15. • A bar in the [material point method](/material-point-method/) has $E = 100$ and density 1, so the wave speed is 10. The cells have $\Delta x = 0.05$, the speeds stay below 2, and the step obeys $h \le C \Delta x / (c + |v|)$ with $C = 0.5$. Find the largest step and the number of steps to the time 1.

16. • The [Wisdom-Holman integrator](/wisdom-holman-integrator/) entry measures a position error of $1.17 \times 10^{-5}$ with 20 steps per orbit, at second order. How many steps per orbit give $10^{-8}$? Its energy error with 40 steps per orbit is $1.9 \times 10^{-6}$, against $2.1 \times 10^{-4}$ for leapfrog. If both scale as $h^2$, how many leapfrog steps per orbit match Wisdom-Holman at 40?

17. • In the [P3M method](/p3m-method/), the error of cutting the short-range sum at $r_c$ is of order $e^{-\alpha^2 r_c^2}$. Find the smallest $\alpha r_c$ for an error of $10^{-5}$, and the splitting parameter $\alpha$ when $r_c = 2.5$ cells. What error does the rule $\alpha r_c \ge 3$ give?

18. ★ Show that the total number of M2L translations at level $L \ge 2$ of a uniform 2D quadtree, with $n = 2^L$ boxes per side and no periodic images, is $27 n^2 - 84 n + 60$. Check it at $L = 2$ and $L = 3$, and find the fraction of the interior estimate $27 n^2$ that it reaches at $L = 4$ and $L = 10$.

19. ★ A test body orbits a Plummer-softened point mass $M$ on a circle of radius $r$. Find its circular speed, the radius where that speed is largest and the largest value, and the ratio of the period to the Newtonian period at $r = \epsilon$ and at $r = 10\epsilon$. What does this say about the dynamics of [softened](/gravitational-softening/) systems inside a few $\epsilon$?

20. ★ The Barnes-Hut entry bounds the relative error of the monopole of an accepted cell by $(\sqrt3 \theta)^2 / (1 - \sqrt3\theta)$. Find the $\theta$ at which this bound is $10^{-2}$, and evaluate the bound at $\theta = 0.3$ and $0.5$. The measured median errors are $9.7 \times 10^{-4}$ and $5.7 \times 10^{-3}$. Explain the gap.

21. ★ In the [TreePM method](/treepm-method/) with split scale $r_s$, the tree computes the Newtonian pair force times $f(u) = \operatorname{erfc}(u/2) + \frac{u}{\sqrt\pi} e^{-u^2/4}$, with $u = r/r_s$. Show that $f$ decreases, evaluate it at $u = 1$, $2$ and $4.5$, and find the cutoff $u$ at which $f = 10^{-3}$.
