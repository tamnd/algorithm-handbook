1. ◦ A robot lives on a ring of 5 cells, numbered 0 to 4, with doors at cells 0 and 1. Its sensor says "door" with probability 0.8 at a door and 0.1 elsewhere. Start from a uniform belief, read "door", move one cell forward without error, and read "door" again. Run the [Bayes filter](/bayes-filter/) and give the final belief of each cell as a fraction.

2. ◦ An [occupancy grid](/occupancy-grid-mapping/) starts with prior $p = 0.5$. The inverse sensor model gives $0.8$ for a cell at the end of a beam and $0.3$ for a cell that a beam passes through. One cell is hit by three beams and passed by two. Give its log odds and its probability. Does the answer depend on the order of the five readings?

3. ◦ Four particles have normalized weights $0.5, 0.2, 0.2, 0.1$. Compute the effective sample size $1/\sum_i w_i^2$. Then resample with the low variance sampler of [Monte Carlo localization](/monte-carlo-localization/), with $r = 0.05$ and pointers $r + i/4$. How many copies does each particle get?

4. ◦ A [histogram filter](/histogram-filter/) covers a floor of 50 m by 30 m at 0.1 m and $5°$ in heading. How many cells does the grid have, and how many megabytes do they take as 4-byte floats? Why is the cost per step far below $g^2$ for a real motion model?

5. ◦ The odometry of a robot reports a move from the pose $(0, 0, 0)$ to $(1, 1, \pi/2)$. Give the three parameters $\delta_{\text{rot1}}, \delta_{\text{trans}}, \delta_{\text{rot2}}$ of the [odometry motion model](/odometry-motion-model/).

6. ◦ A robot at $(0, 0, 0)$ sees a landmark at $(3, 4)$. Give the expected range and bearing, and the $2 \times 3$ Jacobian of the [landmark measurement model](/landmark-measurement-model/) with respect to the pose.

7. ◦ A gyro has a constant bias of 0.01 rad/s and white noise with density $0.001\ \text{rad}/\sqrt{\text{s}}$. If you integrate it for 100 s with no correction, what heading error does the bias cause, and what is the standard deviation caused by the noise? Which one dominates, and which grows faster with time?

8. ◦ A reading has innovation $\nu = (0.6, -0.3)$ with covariance $S = \operatorname{diag}(0.09, 0.04)$. Compute the Mahalanobis distance $D^2 = \nu^\top S^{-1} \nu$. Is the pairing inside the gate at $\chi^2_{2,0.95} = 5.991$? At $\chi^2_{2,0.99} = 9.210$? How many joint hypotheses are there for 4 readings and 5 landmarks, if each reading may also be new?

9. ◦ [KLD-sampling](/kld-sampling/) uses $\varepsilon = 0.05$ and $\delta = 0.01$. How many particles does it ask for when $k = 11$ bins are occupied, given $\chi^2_{10, 0.99} = 23.209$? And when $k = 101$, given $\chi^2_{100, 0.99} = 135.807$?

10. • A robot on a line moves one step per time unit with motion noise of variance $q = 1$, and after each step it measures its distance to a landmark at a known position, with noise of variance $r = 2$. Show that the variance of [EKF localization](/ekf-localization/) after each correction tends to a fixed value, and find it, together with the predicted variance and the Kalman gain at that fixed point.

11. • [Global localization](/global-localization/) on a 100 m by 100 m floor uses $N = 10^5$ particles drawn uniformly in position and heading. Call a particle near the true pose if it lies within 0.5 m and within $10°$ of it. Find the probability that no particle is near, and the expected number of near particles.

12. • A 1D [pose graph](/pose-graph/) has $x_0 = 0$ fixed, two odometry edges $x_1 - x_0 = 1$ and $x_2 - x_1 = 1$ with weight 1, and a loop closure $x_2 - x_0 = 1.7$ with weight 4. Minimize the weighted sum of squared errors. Give $x_1$, $x_2$ and the final cost as fractions.

13. • In 1D, a prior $x_1 = 0$, an odometry factor $x_2 - x_1 = 1$, and two landmark factors $l - x_1 = 2$ and $l - x_2 = 1$, all with weight 1, define a quadratic cost. Write the $3 \times 3$ information matrix $\Lambda$ and the vector $\eta$ over $(x_1, x_2, l)$. Eliminate $l$ by the [Schur complement](/schur-complement/), as [GraphSLAM](/graphslam/) does, and give the reduced system. Which entry changed, and why?

14. • A factor graph has poses $x_1, x_2, x_3, x_4$ in a chain and one landmark $l$ seen from all four poses. Count the fill-in edges when you eliminate in the order $l, x_1, x_2, x_3, x_4$, and in the order $x_1, x_2, x_3, x_4, l$. What does this say about [square root SAM](/square-root-sam/)?

15. • A grid map clamps the log odds to $[-2, 2]$. One cell receives the increments $+1.5$, $+1.5$ and $-1.0$. Give its final value when they arrive in this order, and in the order $-1.0$, $+1.5$, $+1.5$. Compare with the unclamped sum and explain why clamping breaks the order independence of [occupancy grid mapping](/occupancy-grid-mapping/).

16. • A 1D scan has two points at offsets 0 and 3, and the lookup table is $T = (2, 0, 3, 1, 4, 5, 2, 0, 4, 1, 0)$. The score of shift $s$ is $T[s] + T[s + 3]$, for $s = 0, \dots, 7$. Build the coarse table $C[i] = \max(T[i], T[i+1])$, bound the blocks of shifts $\{0,1\}, \{2,3\}, \{4,5\}, \{6,7\}$, and run the best-first search of [correlative scan matching](/correlative-scan-matching/). Which shift wins, and how many shifts are scored?

17. • In [Wahba's problem](/wahba-problem/), take a single exact pair $r = b = e_3$ with weight 1. Build Davenport's matrix $K$ and find its eigenvalues. Describe the set of optimal quaternions and explain why one direction cannot fix the attitude.

18. • A state $x$ is 0 or 1 with probability $1/2$ each, and $y$ given $x$ is normal with mean $x$ and variance 1. To estimate $E[y]$ from $N$ samples, compare the variance of the plain average of the $y_i$ with that of the average of $E[y \mid x_i]$. By what factor does Rao-Blackwellization reduce the variance? Relate this to the [Rao-Blackwellized particle filter](/rao-blackwellized-particle-filter/).

19. • Under the [velocity motion model](/velocity-motion-model/) without noise, a robot at $(0, 0, 0)$ drives with $v = 1$ m/s and $\omega = 0.5$ rad/s for 2 s. Give the center and radius of its circle and its final pose to four decimals. Check that the chord from start to end has length $4 \sin 0.5$.

20. ★ Wahba's loss is $L(A) = \tfrac12 \sum_i a_i \lVert b_i - A r_i \rVert^2$ for unit vectors and weights $a_i > 0$. Prove that $L(A) = \lambda_0 - \operatorname{tr}(A B^\top)$ with $\lambda_0 = \sum_i a_i$ and $B = \sum_i a_i b_i r_i^\top$. Using $\operatorname{tr}(A(q) B^\top) = q^\top K q$, show that the least loss is $\lambda_0 - \lambda_{\max}(K)$. The [q-method](/davenport-q-method/) example has $a_1 = a_2 = 1$ and $\lambda_{\max} = 1.9996954$; what least loss does this predict?

21. ★ A robot stands still. Its pose $x$ has a prior of variance $P_0$, and two landmarks $m_1, m_2$ have no prior. It reads $z = m_j - x$ plus noise of variance $r$, $k$ times for each landmark. Find the posterior covariance of $(x, m_1, m_2)$ in closed form, and the variance of $m_1 - m_2$. Check your formulas at $P_0 = r = 1$, $k = 4$, and relate them to the [EKF SLAM convergence theorem](/ekf-slam-convergence-theorem/).

22. ★ In 1D information form, pose $x_1$ has a prior of information 1, and three landmarks $l_1, l_2, l_3$ are each linked to $x_1$ by one factor of information 1. The robot moves, adding a factor $x_2 - x_1 = u$ of information 1. Marginalize $x_1$ and give the information matrix over $(x_2, l_1, l_2, l_3)$. Explain why the [extended information filter](/extended-information-filter/) fills in, and what the [sparse extended information filter](/sparse-extended-information-filter/) does about it.

23. ★ Let a distribution over $k$ bins be sampled $n$ times independently, and assume that $2n K(\hat p, p)$ is chi-square with $k - 1$ degrees of freedom. Derive the particle count of KLD-sampling. Then give two reasons why, inside a localization filter, the bound is only an approximation.
