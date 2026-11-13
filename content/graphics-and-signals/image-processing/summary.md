## What to remember

- A pixel has integer indices $(x, y)$, $x$ to the right and $y$ downward. Each entry names whether values are used as stored (gamma encoded, for most files) or in linear light, and its border rule.
- Point operations read the [histogram](/image-histogram/) once: $\Theta(N + L)$ for $N$ pixels and $L$ gray levels. [Histogram equalization](/histogram-equalization/) maps level $k$ to the rounded value of $(L-1)c_k/N$, where $c_k$ is the cumulative count. The output histogram is close to flat, not flat. [Otsu's method](/otsu-thresholding/) returns the threshold of largest between-class variance in $\Theta(N + L)$; the entry proves it is the best two-group least-squares split of the gray values. Whether it separates objects is measured.
- [Ordered dithering](/ordered-dithering/) turns on exactly $k$ pixels of each $n \times n$ tile for the constant gray $k/n^2$. [Floyd-Steinberg](/floyd-steinberg-dithering/) passes each pixel's error to its four later neighbors with weights that sum to 1, so error is lost only at the image border. Choosing a palette is [k-means](/k-means/) on the colors; [median cut](/median-cut/) and [octrees](/octree-color-quantization/) are heuristics.
- A $k \times k$ kernel costs $k^2$ per pixel, a [separable](/separable-filter/) (rank-one) one $2k$. The [box blur](/box-blur/) costs $\Theta(WH + (W + H)r)$ for any radius $r$. The [integral image](/integral-image/) is the $(H+1) \times (W+1)$ table of [two-dimensional prefix sums](/two-dimensional-prefix-sums/), built in $\Theta(WH)$,, with any rectangle sum in four reads. Large kernels go through the [FFT](/convolution-via-fft/).
- [Sobel](/sobel-operator/), [Prewitt](/prewitt-operator/) and [Scharr](/scharr-operator/) estimate the gradient in $\Theta(WH)$. [Non-maximum suppression](/non-maximum-suppression/) and [hysteresis](/hysteresis-thresholding/) are $\Theta(WH)$. The [Canny detector](/canny-edge-detector/) is optimal only for its design criteria on a model step; its $\sigma$ and two thresholds are tuned.
- [Erosion](/morphological-erosion/) and [dilation](/morphological-dilation/) cost $\Theta(WHk)$ for $k$ offsets. [Opening](/morphological-opening/) and [closing](/morphological-closing/) are increasing and idempotent.
- [Connected component labeling](/connected-component-labeling/) is exact in $O(N\alpha(N))$ by two raster passes and union-find. The [Felzenszwalb-Huttenlocher transform](/felzenszwalb-distance-transform/) gives the exact squared Euclidean distance in $\Theta(WH)$; [chamfer](/chamfer-distance/) weights give a bounded approximation in two passes.
- The [Laplacian pyramid](/laplacian-pyramid/) rebuilds its image exactly in exact arithmetic, for any kernel. A [Gaussian pyramid](/gaussian-pyramid/) holds about $\tfrac43 WH$ samples; with sizes rounded up it can hold a little more.
- One [seam](/seam-carving/) of least energy is found exactly by dynamic programming; removing $k$ seams one at a time is greedy. [Phase correlation](/phase-correlation/) is exact for circular shifts. [Lucas-Kanade](/lucas-kanade-method/) solves a $2 \times 2$ system that is well posed only when the window has texture in two directions.
- Segmenters, detectors and denoisers prove what they compute, not that the result is good. Their parameters are tuned, and their quality is measured by [PSNR](/psnr/), [SSIM](/structural-similarity-index/) (in $(-1, 1]$, 1 only for equal images) or agreement with people.

| Method | Time | Guarantee |
|---|---|---|
| Histogram equalization, Otsu | $\Theta(N + L)$ | exact for the criterion |
| Box blur | $\Theta(WH + (W + H)r)$ | exact |
| Gaussian filter, unsharp mask | $\Theta(WHR)$ | exact for the cut kernel |
| Canny | $\Theta(WHr)$ | measured; tuned $\sigma$ and thresholds |
| Hough | $\Theta(NT + TD)$ | exact votes; peaks tuned |
| Erosion, dilation, opening | $\Theta(WHk)$ | exact |
| Labeling (two-pass) | $O(N\alpha(N))$ | exact |
| Chamfer 3-4 | $\Theta(WH)$ | bound on the error |
| Felzenszwalb-Huttenlocher DT | $\Theta(WH)$ | exact |
| Watershed (exact version) | $O(N^2 + G)$ | exact for its definition |
| Graph segmentation | $O(m \log m)$ | proved properties; tuned $k$ |
| Harris | $O(WHr)$ | measured; tuned $k$, threshold |
| Seam carving | $\Theta(kWH)$ | one seam exact; $k$ seams greedy |
| Phase correlation | $O(WH \log WH)$ | exact for circular shifts |
| Total variation (Chambolle) | $\Theta(nWH)$ | convex; duality gap stop |
| Bilateral, non-local means | $\Theta(WHR^2)$, $\Theta(WHS^2)$ | measured |

: The main methods. $N = WH$ pixels, $L$ levels; $r$, $R$, $S$ are radii, $k$ an element size or seam count, $m$ graph edges, $G$ the gray range, $n$ iterations.

## Choosing a method

For contrast, stretch between percentiles or equalize; use [CLAHE](/clahe/) when the light varies. For a bimodal histogram Otsu's threshold is the default; for uneven light use a local threshold.

For smoothing, use repeated boxes for speed and the Gaussian for a smooth response. When edges must stay sharp, use the [bilateral](/bilateral-filter/) or [guided filter](/guided-filter/), [non-local means](/non-local-means/) or [total variation](/total-variation-denoising/), and judge them on the images at hand.

For edges, Canny is the usual choice, with $\sigma$ set by the scale of the detail. Label a clean binary mask with two-pass labeling; otherwise segment with the [watershed](/watershed-segmentation/) from markers, the [graph method](/felzenszwalb-segmentation/), [SLIC](/slic-superpixels/) or [GrabCut](/grabcut/). Align pure shifts by phase correlation, and small local motion by Lucas-Kanade on a pyramid.
