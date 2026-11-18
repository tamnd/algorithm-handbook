## What to remember

- A point cloud has positions and no connections. Voxel grid downsampling replaces the points of each voxel by their centroid in $\Theta(n)$ expected time, and each point is within $s\sqrt3$ of its representative, but the result depends on where the grid starts.
- Statistical outlier removal deletes points whose mean $k$-neighbor distance exceeds $\mu + \alpha\sigma$. It removes at most $n/(1 + \alpha^2)$ points, and a few far outliers can hide themselves by raising $\sigma$.
- The normal of a point is the eigenvector of the least eigenvalue of its neighbors' covariance. Its sign is arbitrary; a viewpoint or propagation along a minimum spanning tree with costs $1 - |n_i \cdot n_j|$ fixes it.
- The chamfer distance $\sum_{x} \min_y |x - y|^2 + \sum_y \min_x |x - y|^2$ is symmetric and zero only for equal sets, but it breaks the triangle inequality and ignores density.
- ICP alternates closest-point matching and a Kabsch fit. Since $e_k \ge F(R_{k+1}, t_{k+1}, c_k) \ge e_{k+1}$, the mean squared error never rises and ICP stops after finitely many steps. The stopping pose depends on the start, and with tied closest points it need not even be a local minimum.
- Point-to-plane ICP takes a Gauss-Newton step on distances to tangent planes. It converges much faster near a good solution but is not monotone, and it fails when the target can slide on itself. Trimmed ICP keeps the fraction $\xi$ of shortest pairs, and its trimmed error never rises.
- Global methods need no start pose. RANSAC and 4PCS succeed with a probability that grows with the number of trials. FGR minimizes a robust cost from feature matches without a certificate. TEASER can certify its rotation when its relaxation is tight, and Go-ICP returns a pose within $\epsilon$ of the least ICP cost over its search box.

| Method | Time | Start pose | Result |
|---|---|---|---|
| ICP | $\Theta(Nnm)$ | needed | error never rises; local |
| Point-to-plane ICP | $\Theta(Nnm)$ | needed | local; fast near a solution |
| Trimmed ICP | $\Theta(Nnm)$ | needed | trimmed error never rises; local |
| Normal distributions transform | $O(n + Nm)$ | needed | local; basin about one cell |
| Coherent point drift | $\Theta(NKn)$ | needed, wide basin | likelihood never falls; local |
| Robust point matching | $\Theta(NKnm)$ | needed, wide basin | local, no guarantee |
| 4PCS | $O(N(n^2 + kn^2))$ | not needed | probabilistic |
| Fast global registration | $\Theta(Nm)$ | not needed | local in a robust cost |
| TEASER | $O(3^{m/3} + Nm^2)$ | not needed | certifiable when the relaxation is tight |
| Go-ICP | $O(KTnm)$ | not needed | within $\epsilon$ of the global minimum |

: Registration methods. For the ICP family and NDT, $n$ and $m$ are the source and target sizes and $N$ the iterations; $K$ is the number of centroids for CPD and of Sinkhorn sweeps per pose update for RPM; for 4PCS, $N$ is the number of trials and $k$ the candidates per trial; for FGR and TEASER, $m$ is the number of correspondences; for Go-ICP, $K$ and $T$ are the rotation and translation cubes examined.

## Choosing a method

Clean first: downsample with a voxel grid, remove outliers, estimate and orient normals. When the clouds come from a moving sensor with a good motion guess, ICP is enough, and point-to-plane ICP needs fewer iterations near the solution on smooth scenes; generalized ICP is less hurt by pairs that slide on flat patches. When only part of one cloud overlaps the other, use trimmed ICP. For laser scans matched to a map, NDT avoids the closest point search.

When there is no start pose, compute FPFH or SHOT descriptors, match them, and run RANSAC, FGR or TEASER on the matches; TEASER can certify its rotation, and its paper reports correct results with more than 99% wrong matches in its benchmarks. 4PCS works without descriptors on clouds with little local shape. Refine every global result with ICP. Use Go-ICP when a proved global optimum matters and the clouds are small. For shapes that bend, such as faces and organs, use coherent point drift or another non-rigid method.
