Image processing computes something from a grid of samples: a cleaner or sharper image, a binary mask, a set of edges, regions or corners, the shift to a second image, a face. A phone camera denoises and sharpens each photo before it is stored. A scanner thresholds a page before text recognition. A microscope program labels and counts the cells in a picture, and a tracker follows corners from one video frame to the next.

Most operations look at a window around each pixel, and much of the chapter is about making one window cheap. A $k \times k$ kernel costs $k^2$ operations per pixel, a [separable](/separable-filter/) one $2k$, and a box costs $O(1)$ per pixel for any size, by running sums or by an [integral image](/integral-image/). Nonlinear operators use minima, maxima or value-dependent weights, and keep the edges that linear smoothing blurs. Higher-level tasks become problems of other volumes: labeling regions is connected components on the pixel grid, segmentation can be a minimum spanning forest or a minimum cut, and seam carving is a shortest path in a grid by dynamic programming.

A pixel has integer indices $(x, y)$, $x$ to the right and $y$ downward, and integer values in $\{0, \ldots, L-1\}$ or real values in $[0, 1]$. Each entry says whether the values are taken as stored (for most files, gamma encoded) or decoded to linear light, and which border rule it uses for reads outside the image: clamp, mirror, wrap, zero, or a window cut at the border. Costs are in terms of the width $W$, the height $H$, the number of pixels $N = WH$, the number of gray levels $L$ and the window or kernel size.

The guarantees are of three kinds, and the pages keep them apart. Some results are exact: [Otsu's method](/otsu-thresholding/) finds the threshold that maximizes its criterion, [connected component labeling](/connected-component-labeling/) finds the components, the [Felzenszwalb-Huttenlocher transform](/felzenszwalb-distance-transform/) gives the exact squared Euclidean distance, the [Laplacian pyramid](/laplacian-pyramid/) rebuilds its image in exact arithmetic, and [seam carving](/seam-carving/) finds a seam of least energy. Some are bounds, such as the error of the [chamfer distance](/chamfer-distance/). And many methods, among them the edge, corner and face detectors, the segmenters and the denoisers, depend on scales, thresholds and weights that are chosen by hand or learned, and their quality is measured on test images, by [PSNR](/psnr/), [SSIM](/structural-similarity-index/) or agreement with human judgments. For these the entries prove what the algorithm computes, not that the result is good.

## What the chapter covers

1. **Images, histograms and contrast.** The [digital image](/digital-image/), [gamma correction](/gamma-correction/), [color spaces](/color-spaces/), [noise](/image-noise/) and the [point spread function](/point-spread-function/), PSNR, the [histogram](/image-histogram/), and the point operations [contrast stretching](/contrast-stretching/), [histogram equalization](/histogram-equalization/) and [CLAHE](/clahe/).
2. **Thresholds, halftones and palettes.** [Thresholding](/image-thresholding/) and Otsu's method, [ordered dithering](/ordered-dithering/) and [Floyd-Steinberg dithering](/floyd-steinberg-dithering/), and [color quantization](/color-quantization/) by [median cut](/median-cut/) and [octrees](/octree-color-quantization/).
3. **Linear filters.** [Linear filtering](/linear-filtering/), separable kernels, the [box blur](/box-blur/), the integral image, the [Gaussian filter](/gaussian-filter/) and [unsharp masking](/unsharp-masking/).
4. **Edges and lines.** The [Sobel operator](/sobel-operator/) and its relatives, [non-maximum suppression](/non-maximum-suppression/), [hysteresis thresholding](/hysteresis-thresholding/), the [Canny edge detector](/canny-edge-detector/), the [Laplacian of Gaussian](/laplacian-of-gaussian/) and the [Hough transform](/hough-transform/).
5. **Mathematical morphology.** The [structuring element](/structuring-element/), [erosion](/morphological-erosion/), [dilation](/morphological-dilation/), [opening](/morphological-opening/), [closing](/morphological-closing/) and the [hit-or-miss transform](/hit-or-miss-transform/).
6. **Regions, distances and shape.** [Image labeling](/image-labeling/) and its two-pass algorithm, the [distance transform](/distance-transform/) by chamfer weights and by lower envelopes, [skeletons](/image-skeletonization/) by [Zhang-Suen thinning](/zhang-suen-thinning/), and [image moments](/image-moments/).
7. **Segmentation.** [Image segmentation](/image-segmentation/) by [region growing](/region-growing/), [watershed](/watershed-segmentation/), the [graph method](/felzenszwalb-segmentation/) of Felzenszwalb and Huttenlocher, [mean shift](/mean-shift-segmentation/), [SLIC](/slic-superpixels/), [GrabCut](/grabcut/) and [active contours](/active-contours/).
8. **Pyramids, features and detection.** The [Gaussian pyramid](/gaussian-pyramid/) and the Laplacian pyramid, the [Harris corner detector](/harris-corner-detector/), [SIFT](/sift/), [template matching](/template-matching/) and [normalized cross-correlation](/normalized-cross-correlation/), and the [Viola-Jones detector](/viola-jones-detector/).
9. **Geometry and motion.** [Resampling](/image-resampling/) and [warping](/image-warping/), [registration](/image-registration/) and [phase correlation](/phase-correlation/), [optical flow](/optical-flow/) by [Lucas-Kanade](/lucas-kanade-method/) and [Horn-Schunck](/horn-schunck-method/), and seam carving.
10. **Restoration, editing and quality.** [Image quality assessment](/image-quality-assessment/) and SSIM, [denoising](/image-denoising/) by the [bilateral filter](/bilateral-filter/), [non-local means](/non-local-means/) and [total variation](/total-variation-denoising/), [Richardson-Lucy deconvolution](/richardson-lucy-deconvolution/), [super-resolution](/super-resolution/), [inpainting](/image-inpainting/) and [Poisson image editing](/poisson-image-editing/).

## A first reading

Read these in order:

1. [Digital image](/digital-image/) and [gamma correction](/gamma-correction/)
2. [Image histogram](/image-histogram/) and [histogram equalization](/histogram-equalization/)
3. [Otsu's thresholding](/otsu-thresholding/)
4. [Linear filtering](/linear-filtering/) and [separable filtering](/separable-filter/)
5. [Box blur](/box-blur/) and [integral image](/integral-image/)
6. [Gaussian filter](/gaussian-filter/)
7. [Sobel operator](/sobel-operator/)
8. [Canny edge detector](/canny-edge-detector/), with non-maximum suppression and hysteresis thresholding
9. [Morphological erosion](/morphological-erosion/), [dilation](/morphological-dilation/) and [opening](/morphological-opening/)
10. [Connected component labeling](/connected-component-labeling/)
11. [Distance transform](/distance-transform/) and [chamfer distance](/chamfer-distance/)
12. [Watershed segmentation](/watershed-segmentation/) and [Felzenszwalb-Huttenlocher segmentation](/felzenszwalb-segmentation/)
13. [Gaussian pyramid](/gaussian-pyramid/) and [Laplacian pyramid](/laplacian-pyramid/)
14. [Harris corner detector](/harris-corner-detector/)
15. [PSNR](/psnr/) and [SSIM](/structural-similarity-index/)

Leave for later the color quantization entries, SIFT and Viola-Jones in detail, the optical flow methods and most of the restoration group.

## Before you start

A linear filter is a [discrete convolution](/discrete-convolution/) from the signal-processing chapter of this volume, and large kernels go through [convolution via the FFT](/convolution-via-fft/) and the [convolution theorem](/convolution-theorem/) of Volume 11, which phase correlation and deconvolution also use. The integral image is the table of [two-dimensional prefix sums](/two-dimensional-prefix-sums/) of Volume 6. From Volume 7 come [connected components](/connected-components/), [flood fill](/flood-fill/), [Kruskal's algorithm](/kruskal/) and [graph cut segmentation](/image-segmentation-graph-cuts/), and from Volume 3 the [disjoint-set forest](/disjoint-set/) and the [priority queue](/priority-queue/). [Bilinear interpolation](/bilinear-interpolation/), [least squares](/least-squares-problem/) and the [Poisson equation](/poisson-equation/) are in Volume 12, and [k-means](/k-means/), [mean shift](/mean-shift/) and [Gaussian mixtures](/gaussian-mixture-model/) in Volume 25. The [pixel](/pixel/) of Chapter 28.1 and [aliasing](/aliasing/) from the last chapter explain why an image must be smoothed before it is subsampled.
