## What to remember

- $\mathrm{MOTA} = 1 - \sum_t (\mathrm{FN}_t + \mathrm{FP}_t + \mathrm{IDSW}_t) / \sum_t \mathrm{GT}_t$ counts errors and can be negative. $\mathrm{IDF1} = 2\,\mathrm{IDTP} / (\sum_o |o| + \sum_h |h|)$ matches whole trajectories once, and $\mathrm{HOTA}_\alpha = \sqrt{\mathrm{DetA}_\alpha \cdot \mathrm{AssA}_\alpha}$ weighs detection and association evenly.
- A gate keeps measurement $z$ for a track when $(z - \hat z)^\mathsf{T} S^{-1} (z - \hat z) \le \gamma$, with $S = H P H^\mathsf{T} + R$. For a Gaussian measurement in $p = 2$ dimensions it keeps the true one with probability $1 - e^{-\gamma/2}$.
- Data association in one frame is an assignment problem, solved exactly for its cost by the Hungarian algorithm in $O((n + m)^3)$ with dummy rows and columns for misses and new tracks. Over all frames with costs on consecutive links it is a min-cost flow, optimal for that cost model. With costs on three frames it is NP-hard, and the exact JPDA weights are #P-hard.
- The Kalman filter that predicts each track is exact only for linear motion with Gaussian noise. CONDENSATION drops it and approximates the posterior by $N$ weighted samples, which converge as $N \to \infty$.
- A correlation filter is ridge regression on all cyclic shifts of a patch. The data matrix is circulant, so the DFT solves it per frequency: $\hat w = \hat y \odot \overline{\hat x} / (|\hat x|^2 + \lambda)$ in $\Theta(P \log P)$. It is exact for cyclic shifts only; real motion is not cyclic.
- Local trackers climb a score from the last position. Mean shift tracking never accepts a step that lowers the Bhattacharyya coefficient $\sum_u \sqrt{p_u q_u}$, and the KLT step and inverse compositional alignment converge from a close start. None of them proves that the score's maximum is the target.
- Background models are heuristics with provable update rules. In the Stauffer-Grimson model, a component matched $t$ times in a row has weight $1 - (1 - w)(1 - \alpha)^t$; in ViBe a sample survives $k$ updates with probability $((N - 1)/N)^k$, whatever its age.
- Learned trackers, such as Siamese tracking and Deep SORT, are judged by benchmark measurements.

| Method | Time per frame | Online | Result |
|---|---|---|---|
| Mean shift tracking | $\Theta(k (j + 1)(m + B))$ | yes | coefficient never falls; local |
| CAMShift | $\Theta(W H + k m)$ | yes | local; size from moments |
| MOSSE | $\Theta(P \log P)$ | yes | exact minimizer of its weighted error |
| Kernelized correlation filter | $\Theta(P \log P)$ | yes | exact ridge regression on cyclic shifts |
| CONDENSATION | $\Theta(N (\log N + d^2 + M L))$ | yes | sample approximation of the posterior |
| Stauffer-Grimson | $O(P K \log K)$ | yes | heuristic |
| Global nearest neighbor | $O((n + m)^3)$ | yes | optimal in each frame for its cost |
| JPDA | $O(E n + n m p^2)$ | yes | exact weights over $E$ joint events |
| Multiple hypothesis tracking | $O(M^2 m^3 (n + m))$ | yes | best of the $M$ hypotheses kept |
| Network flow | $O(K n (n + L))$ for the video | no | optimal for pairwise costs |
| SORT | $O(n m (n + m))$ | yes | Hungarian optimal in each frame |

: Trackers of one target (top) and of many (bottom). $m$ is the window size for local trackers and the number of measurements for association; $P$ is the patch size, $N$ the samples, $n$ the tracks, $E$ the joint events, $M$ the hypotheses kept, $L$ the allowed links and $K$ the tracks found. Filter update terms are omitted.

## Choosing a method

With a fixed camera, subtract the background first. The Stauffer-Grimson mixture handles waves or leaves, and ViBe is simpler; both need tuning. For one target given by a box, a correlation filter is a fast baseline: MOSSE with gray values, the kernelized filter with HOG features. Mean shift and CAMShift suit a target with distinctive colors. When the target leaves the view and returns, use tracking-learning-detection. Siamese trackers need no online update but a network trained offline.

For many objects of known classes, track by detection. SORT is the baseline; ByteTrack adds the low-score boxes for occluded objects, and Deep SORT adds appearance against identity switches. When the whole video is available, network flow links all detections at once and is optimal for its pairwise costs. With radar-like measurements in clutter, gate first, then use GNN when targets are well apart, JPDA when gates overlap, MHT when decisions must wait for later scans, and the PHD filter when the number of targets is unknown and changes.
