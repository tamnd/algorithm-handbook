1. ◦ Compute the [intersection over union](/intersection-over-union/) of the boxes $a = (0, 0, 4, 4)$ and $b = (2, 1, 6, 5)$ in continuous coordinates. Then read the same numbers as PASCAL VOC boxes, with inclusive pixel indices, and compute the IoU again.

2. ◦ One class has $N = 4$ objects. The ranked detections are, from the highest score down: true positive, false positive, true positive, true positive, false positive. Compute the precision and recall after each detection, and the [average precision](/detection-mean-average-precision/) in the VOC 11-point, VOC all-point and COCO 101-point forms.

3. ◦ A segmentation with three classes has the confusion matrix, rows the true class and columns the predicted class,
$$n = \begin{pmatrix} 50 & 5 & 5 \\ 10 & 20 & 0 \\ 0 & 5 & 5 \end{pmatrix}.$$
Compute the IoU of each class, the [mean IoU](/mean-intersection-over-union/) and the pixel accuracy. Which class pulls the mean down?

4. ◦ For one class of a [panoptic segmentation](/panoptic-segmentation/), three predicted segments match true segments with IoU 0.9, 0.7 and 0.6, one predicted segment matches nothing, and two true segments are missed. Compute PQ, and its two factors, the segmentation quality and the recognition quality.

5. ◦ A reference box has center $(50, 50)$, width 20 and height 40, and its target box has center $(54, 46)$, width 30 and height 40. Compute the four [regression](/bounding-box-regression/) offsets and the IoU of the two boxes.

6. ◦ Three boxes have the scores 0.9, 0.8 and 0.7: $B_1 = (0, 0, 10, 10)$, $B_2 = (5, 0, 15, 10)$ and $B_3 = (1, 0, 11, 10)$. Run greedy [non-maximum suppression](/box-non-maximum-suppression/) with threshold 0.5, [Soft-NMS](/soft-nms/) with the linear rule and $N_t = 0.3$, and Soft-NMS with the Gaussian rule and $\sigma = 0.5$. Give the output order and the final scores.

7. ◦ Two images have the visual words $a$ and $b$ on a $2 \times 2$ grid. Image $X$ has $a$ twice in the top-left cell, $a$ once in the bottom-right cell and $b$ once in the top-right cell. Image $Y$ has $a$ once in the top-left cell, $a$ twice in the bottom-left cell and $b$ twice in the top-right cell. Compute the [spatial pyramid](/spatial-pyramid-matching/) kernel $\kappa^1$.

8. ◦ In a [generalized Hough transform](/generalized-hough-transform/), the template has four edge points around the reference point $c = (1, 1)$: $(0, 1)$ with gradient direction $180°$, $(2, 1)$ with $0°$, $(1, 0)$ with $270°$ and $(1, 2)$ with $90°$. Build the R-table. The image has the edge points $(5, 6)$ at $180°$, $(7, 6)$ at $0°$, $(6, 5)$ at $270°$, $(6, 7)$ at $90°$, $(2, 2)$ at $0°$ and $(9, 9)$ at $90°$. Which cells get votes, and where is the peak?

9. ◦ A feature map has the values $f(1, 2) = 4$, $f(2, 2) = 8$, $f(1, 3) = 6$ and $f(2, 3) = 2$ at integer points $(x, y)$. RoIAlign samples it at $(1.3, 2.6)$ by [bilinear interpolation](/bilinear-interpolation/). Compute the sample. What value does [RoI pooling](/roi-pooling/), which rounds to the nearest cell, use instead?

10. ◦ A foreground of color $F = (0.8, 0.4, 0.2)$ with $\alpha = 0.6$ is shot against a blue backing $B_1 = (0, 0, 1)$ and a green backing $B_2 = (0, 1, 0)$. Compute the two observed colors. Then recover $\alpha$ and $F$ from them by triangulation [matting](/image-matting/), using $\alpha = 1 - (I_1 - I_2) \cdot (B_1 - B_2) / |B_1 - B_2|^2$.

11. • Three boxes of height 1 have the $x$ ranges $B = [0, 2]$, $A = [0.5, 2.5]$ and $C = [1, 3]$. Compute their pairwise IoU. Run greedy NMS with threshold 0.5 when $A$ has the highest score, and again when $B$ has it. Show that the kept set is always a maximal set of boxes with pairwise IoU at most the threshold, but not always one of largest total score.

12. • One class has two objects. The detector finds the first object twice, with the two highest scores, and the second object with the third score. Compute the all-point AP. What is the AP if NMS removes the duplicate, and what is it if the duplicate is ranked last instead?

13. • A class appears in two images. In the first, the prediction has 90 true positive pixels, 10 false positive and none false negative. In the second, it has 1 true positive, no false positive and 9 false negative. Compare the mean of the per-image IoU with the IoU over the data set. Which one does the mIoU of PASCAL VOC use?

14. • A [random walker](/random-walker-segmentation/) graph has four pixels. Pixel 1 is a seed of label $A$ and pixel 4 a seed of label $B$. The edge weights are $w_{12} = 2$, $w_{13} = 1$, $w_{24} = 1$, $w_{34} = 2$ and $w_{23} = 1$. Compute the probabilities of label $A$ at pixels 2 and 3, and the labeling.

15. • A row of four pixels has an object seed at pixel 1 and a background seed at pixel 4. The neighbor weights are $w_{12} = 4$, $w_{23} = 1$ and $w_{34} = 3$. The region costs are $R_2(\mathrm{obj}) = 1$, $R_2(\mathrm{bkg}) = 2$, $R_3(\mathrm{obj}) = 2$ and $R_3(\mathrm{bkg}) = 0.5$. Build the s-t graph of [Boykov-Jolly graph cuts](/boykov-jolly-graph-cuts/), find the minimum cut and the labels. Then the user adds an object seed at pixel 3. What is the new cut?

16. • A child part has the match costs $f = (3, 0, 4, 1, 5)$ at positions $0$ to $4$ on a line. Compute the distance transform $D(x) = \min_{x'} f(x') + (x - x')^2$ for $x = 0, \ldots, 5$. A [pictorial structure](/pictorial-structures/) of two parts has the root costs $(3, 1, 3, 1, 2)$, and the child rests one step to the right of the root. Find the best placement of both parts and its cost.

17. • An [active shape model](/active-shape-model/) of two landmarks in the plane has the mean $\bar x = (0, 0, 2, 0)$ and one mode $p_1 = (0, 1, 0, -1)/\sqrt2$ with $\lambda_1 = 2$. The search finds the points $y = (0, 4, 2, -4)$ in the model frame. Compute $b_1$, clamp it to $\pm 3\sqrt{\lambda_1}$, and give the shape that the model returns.

18. • [DETR](/detr/) has three queries and two objects. The matching cost of query $i$ for object $j$ is
$$C = \begin{pmatrix} 0.2 & 0.3 \\ 0.4 & 0.9 \\ 0.8 & 0.95 \end{pmatrix}.$$
Find the matching of least total cost, and compare it with the greedy rule that takes the smallest entry first. What does the unmatched query learn?

19. • Show that [VLAD](/vlad/) is the mean part of the [Fisher vector](/fisher-vector/) with hard assignments, equal weights $w_k = 1/K$ and unit variances, up to a factor $\sqrt K/n$, so that both give the same vector after L2 normalization. How long is each for $K = 64$ centers and SIFT descriptors with $D = 128$, and for a Fisher vector with $K = 256$ and $D = 64$?

20. • Three training images give the differences $a_1 = (2, 0, 1, 0)$, $a_2 = (-1, 1, 0, 1)$ and $a_3 = -(a_1 + a_2)$ from the mean. Form the small matrix $A^T A$ of [eigenfaces](/eigenfaces/), find its eigenvalues, explain the zero eigenvalue, and give the fraction of the variance that the first eigenface explains.

21. • In an [ultrametric contour map](/ultrametric-contour-map/), three regions meet. The boundary between $A$ and $B$ has length 2 and mean strength 0.2, between $B$ and $C$ length 1 and strength 0.5, and between $A$ and $C$ length 3 and strength 0.4. Merge by the weakest mean boundary, and give the level of each merge and the value of the map on each boundary. Show that with the mean, merge levels never go down.

22. • [Intelligent scissors](/intelligent-scissors/) run on the grid of costs
$$\begin{pmatrix} 0 & 5 & 5 & 1 \\ 1 & 5 & 1 & 1 \\ 1 & 1 & 1 & 5 \end{pmatrix},$$
where a step into a pixel costs that pixel's value and moves go to the four neighbors. Find the least cost path from the top-left to the top-right pixel. Then add 2 to the cost of every step and find the path again.

23. ★ Let $A_{11}$ be the VOC 11-point AP and $A$ the all-point AP of the same ranked detections. Show that $|A_{11} - A| \le 1/11$, and give detections for which the difference comes as close to $1/11$ as you like. What is the bound for the COCO 101-point form?

24. ★ Prove that the Jaccard distance $1 - |A \cap B|/|A \cup B|$ satisfies the triangle inequality on finite sets. Conclude that if a detection has IoU at least $a$ with one true box and at least $b$ with another, the two true boxes have IoU at least $a + b - 1$.

25. ★ In one dimension and in the limit of a piecewise constant image, the [Mumford-Shah functional](/mumford-shah-functional/) becomes $\sum_i (u_i - g_i)^2 + \nu \cdot (\text{number of jumps of } u)$. Give a dynamic program that minimizes it exactly in $O(n^2)$ time, and run it on $g = (0, 0, 1, 1, 5)$ with $\nu = 2$ and with $\nu = 1/2$.

26. ★ Show that the random walker probabilities lie between 0 and 1 and that each is a weighted average of its neighbors. Then take a chain $s, a, b, c, t$ with seeds at $s$ and $t$ and the weights $2, 3, 3, 3$ in order. Show that thresholding the probabilities at $1/2$ cuts a different edge from the minimum cut, and give both costs.

27. ★ Two squares of side $w$ have centers that differ by $(\delta_x, \delta_y)$. Show that the set of offsets with IoU at least $1/2$ is convex and has area $\left(\tfrac43 - \tfrac83 \ln \tfrac32\right) w^2 \approx 0.252\, w^2$.
