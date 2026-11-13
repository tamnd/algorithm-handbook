A digital image is a grid of pixels, each holding an intensity or a colour. Image processing computes a new image from it, or extracts something: the edges, the regions, the corners to track, the faces. A phone camera denoises and sharpens every photo; a scanner thresholds a page before text recognition; a medical program segments an organ in a scan.

Most operations look at a window around each pixel, and the algorithms are about making one window cheap. A linear filter is a convolution: a $k \times k$ kernel costs $k^2$ operations per pixel, only $2k$ when the kernel is separable, and a box filter costs $O(1)$ per pixel with running sums or an integral image, whatever its size. Large kernels go through the fast Fourier transform. Nonlinear operators, such as the median filter, the bilateral filter and the morphological operators built from erosion and dilation, keep edges that linear smoothing blurs. Higher-level tasks turn into problems of other volumes: connected regions are graph search, segmentation is a minimum cut or clustering, and content-aware resizing is dynamic programming.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Images and point operations.** Colour spaces, gamma, histograms, histogram equalization and CLAHE, Otsu's thresholding, and the quality measures PSNR and SSIM.
2. **Filtering.** Separable, box and Gaussian filters, integral images, unsharp masking, median, bilateral and guided filters, and denoising by non-local means and total variation.
3. **Edges and features.** The Sobel and related operators, the Laplacian of Gaussian, Canny's detector, the Hough transform, Harris corners, SIFT and the Viola-Jones detector.
4. **Morphology and shape.** Structuring elements, erosion, dilation, opening and closing, the hit-or-miss transform, thinning, distance transforms, connected-component labelling and image moments.
5. **Segmentation.** Region growing, watershed, Felzenszwalb's graph method, mean shift, SLIC superpixels, active contours and GrabCut.
6. **Geometry, motion and restoration.** Resampling, pyramids, registration, optical flow by Lucas-Kanade and Horn-Schunck, Richardson-Lucy deblurring, inpainting, seam carving, dithering and colour quantization.

## What to read meanwhile

Chapter 28.1 defines the [pixel](/pixel/) and treats [reconstruction filters](/reconstruction-filter/) and the [mipmap](/mipmap/), a pyramid. For resampling, read [bilinear](/bilinear-interpolation/) and [bicubic interpolation](/bicubic-interpolation/) in Chapter 12.5. Filtering with large kernels uses [convolution via the FFT](/convolution-via-fft/) and the [multidimensional FFT](/multidimensional-fft/) of Chapter 11.3. The integral image is the table of [two-dimensional prefix sums](/two-dimensional-prefix-sums/), and a running median is the [sliding window median](/sliding-window-median/).

Region labelling is [flood fill](/flood-fill/) or [weighted union-find](/weighted-union-find/). [Graph cut segmentation](/image-segmentation-graph-cuts/) in Chapter 7.6 solves two-label segmentation exactly by one minimum cut. Chapter 25.2 has [k-means](/k-means/), [mean shift](/mean-shift/) and the [normalized cut](/normalized-cut/). The [medial axis](/medial-axis/) is the continuous skeleton. The [JPEG](/jpeg-compression/) and [lossy image compression](/lossy-image-compression/) entries of Volume 24 show how images are coded.
