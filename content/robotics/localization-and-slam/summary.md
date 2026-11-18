## What to remember

- Every method is a form of the **Bayes filter**: predict with $p(x_t \mid u_t, x_{t-1})$, then correct with $p(z_t \mid x_t, m)$ and normalize. On a finite state space the recursion is exact under the Markov assumption and costs $O(g^2)$ per step, or $O(gb)$ when one motion step reaches only $b$ cells. Dead reckoning is the prediction alone, and its error only grows.
- An **occupancy grid** keeps the log odds $l = \log(p/(1-p))$ of each cell and adds $\operatorname{logit}(p(m_i \mid z_t, x_t)) - l_0$ per reading. The cells are treated as independent, which is an approximation. Without clamping, the order of the readings does not matter.
- **Three filters, three beliefs.** A grid holds any belief at a cost linear in the number of cells. A Gaussian holds one peak. Particles hold several peaks at a cost of $O(N)$ sensor model evaluations. Only the grid and the particles can solve [global localization](/global-localization/), and for a fixed $N$ nothing guarantees a particle near the true pose.
- **EKF SLAM** keeps a joint Gaussian over $3 + 2m$ numbers in the plane and pays $O(m^2)$ time and memory per update. In the linear Gaussian case the map covariance never grows, the relative error of two landmarks shrinks with each observation, and the absolute error stays at least the initial pose error. With linearization the filter can become inconsistent.
- **Data association** chooses among $(n+1)^k$ pairings of $k$ readings with $n$ landmarks. Pairings that each pass their own gate can fail a joint test; [joint compatibility branch and bound](/joint-compatibility-branch-and-bound/) tests the set, and is exponential in the worst case.
- **Rao-Blackwellization**: given the path, the landmarks are independent. [FastSLAM](/fastslam/) samples the path and gives each particle $m$ small Kalman filters in a tree, at $O(\log m)$ per reading and particle.
- **Full SLAM** is sparse nonlinear least squares. Gauss-Newton and Levenberg-Marquardt reach a local minimum, and the elimination order sets the fill-in of the factor $R$. [SE-Sync](/se-sync/) certifies a global minimum when its relaxation is tight.
- **Wahba's problem** has a closed form: the optimal quaternion is the eigenvector of the largest eigenvalue $\lambda_{\max}$ of Davenport's $4 \times 4$ matrix $K$, and [QUEST](/quest-algorithm/) finds $\lambda_{\max}$ by Newton's method.

## The main estimators side by side

| Method | Belief | Time per step | Memory | Exact when |
|---|---|---|---|---|
| [Histogram filter](/histogram-filter/) | grid of $g$ cells | $O(g^2)$, banded $O(gb)$ | $O(g)$ | the state is discrete |
| [EKF localization](/ekf-localization/) | one Gaussian | $O(k)$, or $O(km)$ to associate | $O(1)$ | the model is linear Gaussian |
| [Monte Carlo localization](/monte-carlo-localization/) | $N$ particles | $O(ND)$ | $O(N)$ | never |
| [EKF SLAM](/ekf-slam/) | joint Gaussian | $O(km^2)$ | $O(m^2)$ | the model is linear Gaussian |
| [SEIF](/sparse-extended-information-filter/) | sparse information matrix | $O(k^3)$ | $O(n^2)$ | never |
| [FastSLAM](/fastslam/) | $N$ paths with their maps | $O(Nk \log m)$ | $O(Nm)$ | never |
| [GraphSLAM](/graphslam/) | batch least squares | $O(I(mp^2 + p^3 + k))$ in all | $O(p + k)$ | local minimum only |
| [iSAM2](/isam2/) | Bayes tree | $O(ws^2)$ for the changed top | $O((p+m)s)$ | linear, with no relinearization |

: The main estimators. Here $k$ is the number of readings per step (for SEIF, the bound on the active landmarks), $m$ or $n$ the number of landmarks, $p$ the number of poses, $D$ the cost of one sensor model evaluation, $I$ the number of iterations, $w$ the size of the re-eliminated top of the tree and $s$ the size of its largest clique.

## Choosing a method

- If the robot starts lost or can be carried away, use particles or a grid. [KLD-sampling](/kld-sampling/) adapts the number of particles. Random particles help after a kidnapping, but that rule is a heuristic.
- If the start pose is known and the landmarks are distinct, [EKF localization](/ekf-localization/) is cheap. Gate every pairing.
- For a small map of point landmarks, EKF SLAM is simple to write. Beyond a few hundred landmarks, use a graph.
- For a long run with loops, build a [pose graph](/pose-graph/), detect loops and optimize. Use [switchable constraints](/switchable-constraints/) or a robust cost if a wrong closure can enter, and [iSAM2](/isam2/) when the answer must stay current.
- For orientation from a gyro and two reference directions, the [complementary filter](/nonlinear-complementary-filter/) is small and converges from almost every start. Use the [error-state Kalman filter](/error-state-kalman-filter/) when you need a covariance or a bias estimate.
