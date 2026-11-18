A cleaning robot starts in a room it has never seen. Its wheels count turns, and a laser scanner measures the distance to the walls in a few hundred directions. From these numbers it must say where it is and draw a map good enough to come back to the dock. Neither number is exact. A wheel slips, a reading hits a chair leg, and a small error in heading turns into a large error in position after ten meters. The robot cannot know its pose; it can only keep a belief about it, and the belief must be updated many times a second.

The chapter treats this as a problem of probability. The pose $x_t$ and the map $m$ are unknown, the controls $u_{1:t}$ and the readings $z_{1:t}$ are known, and the goal is the posterior over the unknowns. When the map is given, the problem is localization. When it is not, the problem is simultaneous localization and mapping, SLAM. The same tools serve a car in a city, a drone that holds its attitude with a gyro and an accelerometer, and a phone that places virtual objects on a table.

Nearly all of the methods here are approximations, and the entries say so. A Kalman filter is exact only for a linear model with Gaussian noise; the extended Kalman filter linearizes and can become overconfident. A particle filter is right only in the limit of many particles. A graph optimizer finds a local minimum, and a single wrong loop closure can bend the whole map. Read each guarantee with its conditions.

## What the chapter covers

1. **Where am I.** [Mobile robot localization](/mobile-robot-localization/) states the problem, the [Bayes filter](/bayes-filter/) gives the recursion of prediction and correction, and [dead reckoning](/dead-reckoning/) shows why prediction alone fails.
2. **Motion and sensor models.** The [odometry motion model](/odometry-motion-model/) and the [velocity motion model](/velocity-motion-model/) give the prediction. The [landmark measurement model](/landmark-measurement-model/), the [beam range finder model](/beam-range-finder-model/) and the [likelihood field model](/likelihood-field-model/) give the correction.
3. **Maps.** The [occupancy grid map](/occupancy-grid-map/) stores log odds per cell, [occupancy grid mapping](/occupancy-grid-mapping/) fills it from scans, the [octree occupancy map](/octree-occupancy-map/) carries it to 3D, and the [topological map](/topological-map/) keeps a graph of places.
4. **Localization filters.** The [histogram filter](/histogram-filter/) and [Markov localization](/markov-localization/) on a grid, [EKF localization](/ekf-localization/) with one Gaussian, and [Monte Carlo localization](/monte-carlo-localization/) with particles. Then [global localization](/global-localization/), the [kidnapped robot problem](/kidnapped-robot-problem/) and [correlative scan matching](/correlative-scan-matching/).
5. **Attitude.** [Attitude estimation](/attitude-estimation/) from gyros and directions, [Wahba's problem](/wahba-problem/) with its solvers [TRIAD](/triad-method/), the [q-method](/davenport-q-method/) and [QUEST](/quest-algorithm/), and three filters: the [complementary filter](/nonlinear-complementary-filter/), the [error-state Kalman filter](/error-state-kalman-filter/) and the [invariant EKF](/invariant-extended-kalman-filter/).
6. **The SLAM problem.** The [problem](/slam-problem/) in its [online](/online-slam/) and [full](/full-slam/) forms, and its two discrete questions: [data association](/data-association-slam/) and [loop closure detection](/loop-closure-detection/).
7. **Gaussian filters for SLAM.** [EKF SLAM](/ekf-slam/) and its [convergence theorem](/ekf-slam-convergence-theorem/), [joint compatibility branch and bound](/joint-compatibility-branch-and-bound/), the [extended information filter](/extended-information-filter/) and its [sparse version](/sparse-extended-information-filter/), and [MonoSLAM](/monoslam/).
8. **Particle filters for SLAM.** The [Rao-Blackwellized particle filter](/rao-blackwellized-particle-filter/), [FastSLAM](/fastslam/) and [grid-based Rao-Blackwellized SLAM](/grid-based-rbpf-slam/).
9. **Graphs and smoothing.** The [pose graph](/pose-graph/) and [pose graph optimization](/pose-graph-optimization/), [GraphSLAM](/graphslam/), [square root SAM](/square-root-sam/), [iSAM](/isam/), the [Bayes tree](/bayes-tree/) and [iSAM2](/isam2/), the certifiable solver [SE-Sync](/se-sync/), and [switchable constraints](/switchable-constraints/) against wrong loop closures.
10. **Complete systems.** [Lidar odometry and mapping](/lidar-odometry-and-mapping/) and [ORB-SLAM](/orb-slam/).

## A first reading

For a first pass, read these in order:

1. [Mobile robot localization](/mobile-robot-localization/)
2. [Bayes filter](/bayes-filter/)
3. [Odometry motion model](/odometry-motion-model/)
4. [Likelihood field model](/likelihood-field-model/)
5. [Occupancy grid mapping](/occupancy-grid-mapping/)
6. [EKF localization](/ekf-localization/)
7. [Monte Carlo localization](/monte-carlo-localization/)
8. [SLAM](/slam-problem/)
9. [EKF SLAM](/ekf-slam/)
10. [FastSLAM](/fastslam/)
11. [Pose graph optimization](/pose-graph-optimization/)
12. [Loop closure detection](/loop-closure-detection/)

The attitude group can be read on its own, after [Wahba's problem](/wahba-problem/). The information filters, the Bayes tree, iSAM2, SE-Sync and the two complete systems can wait for a second pass.

## Before you start

The chapter assumes conditional probability, [Bayes' theorem](/bayes-theorem/) and [conditional independence](/conditional-independence/) from Volume 25, with [filtering](/filtering/), the [extended Kalman filter](/extended-kalman-filter/), the [particle filter](/particle-filter/) and the [factor graph](/factor-graph/). The [Kalman filter](/kalman-filter/) and [state estimation](/state-estimation/) are in Volume 28. From Volume 12 you need [least squares](/least-squares-problem/), the [QR decomposition](/qr-decomposition/) and the [Schur complement](/schur-complement/). [Nonlinear least squares](/nonlinear-least-squares/) and the [Gauss-Newton algorithm](/gauss-newton-algorithm/) are in Volume 38, with [bundle adjustment](/bundle-adjustment/). From this volume, read the [robot pose](/robot-pose/), the [special orthogonal group](/special-orthogonal-group/) and [uncertainty on Lie groups](/uncertainty-on-lie-groups/) in the first chapter of this volume. The [Kullback-Leibler divergence](/kullback-leibler-divergence/) and the [chi-squared test](/chi-squared-goodness-of-fit-test/) from Volume 33 appear in a few entries.
