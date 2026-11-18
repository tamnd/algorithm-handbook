## What to remember

- Intersection over union, $|A \cap B|/|A \cup B|$, scores the overlap of two regions, and $1 - \mathrm{IoU}$ is a metric. The threshold that calls a detection correct, 0.5 for PASCAL VOC and $0.50, 0.55, \ldots, 0.95$ for COCO, is a convention.
- Average precision is the area under the interpolated precision-recall curve of one class, with $p_{\mathrm{interp}}(r) = \max\{P_k : R_k \ge r\}$. VOC 2007 averages it at 11 recall points, later VOC uses all points, and COCO uses 101 points and averages over ten IoU thresholds. The three give different numbers for the same detections.
- Mean IoU for segmentation is the class average of $n_{ii}/(t_i + \sum_j n_{ji} - n_{ii})$ from the confusion matrix of all pixels in the data set. Small classes count as much as large ones.
- Greedy non-maximum suppression keeps the best box and drops every box with IoU above $t$ with it, in $\Theta(n^2)$ worst time. It is a rule, not the optimum of any stated cost. Soft-NMS multiplies scores by a decay such as $e^{-o^2/\sigma}$ instead of dropping boxes.
- Box regression predicts $t = ((x - x_a)/w_a, (y - y_a)/h_a, \log(w/w_a), \log(h/h_a))$ from a reference box, an exact and invertible map that does not change when the image is shifted or scaled.
- On a tree of parts with quadratic springs, the best placement of pictorial structures is exact by dynamic programming in $O(nh)$ with distance transforms; on a general graph the problem is NP-hard.
- Boykov-Jolly graph cuts give the global minimum of a binary energy with seeds by one s-t minimum cut; the random walker solves $L_U x^s_U = -B^T m^s$ for the probabilities of each label $s$; closed-form matting solves one sparse linear system in $\alpha$; intelligent scissors find an exact shortest path by Dijkstra's algorithm.
- Mean field in the dense CRF costs $O(LWH)$ per iteration with filtering. Sequential updates never raise the free energy, but the parallel update used in practice has no such guarantee in general.
- Learned detectors are judged by measurements. The entries report, for example, 58.5 percent mAP on VOC 2007 for R-CNN with box regression, 73.2 percent for Faster R-CNN at 5 frames per second, and 63.4 percent for YOLO at 45 frames per second.

| Method | Task | Time | Result |
|---|---|---|---|
| Greedy NMS | remove duplicates | $\Theta(n^2)$ worst | rule; keeps a maximal non-overlapping set |
| Dalal-Triggs | detection | $O(md + k^2)$ | linear SVM on HOG; measured |
| Deformable part model | detection | linear in the locations | exact part placement for a star |
| Faster R-CNN | detection | network plus $O(A \log A)$ | measured |
| DETR | detection | network plus Hungarian | exact matching in training; measured |
| Generalized Hough | shape detection | $O(em + WH)$ | exact accumulator |
| Boykov-Jolly | interactive cut | max flow | global minimum |
| Random walker | interactive labels | one sparse system | exact solution |
| Closed-form matting | soft matte | one sparse system | exact under the local color model |
| Dense CRF | refine labels | $O(NLWH)$ | approximate inference |
| Vocabulary tree | quantize a feature | $O(kLD)$ | approximate nearest word |

: Main methods of the chapter. $n$ is the number of boxes; $m$ the pixels and $d$ the HOG length; $A$ the anchors; $e$ and $m$ for the Hough transform the image and template edge points; $N$ the mean field iterations and $L$ the labels; $k$, $L$ and $D$ for the tree the branch factor, depth and descriptor length.

## Choosing a method

To report a detector, give AP with its version: VOC 11-point, VOC all-point or COCO, and the IoU thresholds. For segmentation give mIoU over the data set, not the mean of per-image scores. For a new detector, start from a two-stage network such as Faster R-CNN with a feature pyramid when accuracy matters, and from a one-pass detector such as SSD or YOLO when speed matters; check both on the benchmark that matches your images. Add Soft-NMS when objects stand close together. Use the Dalal-Triggs detector or the deformable part model when there is little training data or no GPU.

For cutting out one object, use Boykov-Jolly graph cuts when the user marks regions, intelligent scissors when the user traces the edge, and the random walker for several labels or weak edges. Use closed-form matting for hair and fur. For search in a large collection, use a bag of visual words with a vocabulary tree and spatial verification, then query expansion; use VLAD or Fisher vectors when memory per image must be small.
