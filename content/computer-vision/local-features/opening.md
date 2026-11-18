Two photographs show the same church, one taken from the square and one from a street corner a few metres to the left. A program that wants to know how the camera moved first finds, in each photograph, a few thousand small regions that it can find again: corners of windows, the dark centre of a rose window, the ends of a cornice. For each region it computes a vector, the descriptor, from the pixels around it. Say each image has 4000 regions and each descriptor has 128 numbers. Comparing every descriptor of the first image with every descriptor of the second costs $4000 \cdot 4000 \cdot 128 = 2.048 \times 10^9$ multiply-adds. With 256-bit binary descriptors it costs $1.6 \times 10^7$ comparisons of 256 bits, which is $6.4 \times 10^7$ population counts of 64-bit words. The nearest descriptor is often the wrong one, so the program keeps a match only when the nearest is clearly nearer than the second nearest.

Three questions run through the chapter. A detector must find the same physical point when the image is moved, turned, scaled or seen at a slant; this property is covariance, and [detector repeatability](/detector-repeatability/) measures how well it holds on real images. A descriptor must give close vectors for two views of one point and distant vectors for different points, and it must be quick to compare. A matcher must find near vectors among many, and must throw away the matches that are near by chance. None of the steps is exact. Invariance holds only for the class of maps a method is built for, and the quality of a detector, a descriptor or a matcher is a measured number on a test set. The matches that survive go on to the geometric tests of [RANSAC](/ransac/) in Chapter 38.3.

## What the chapter covers

1. **Features and matches.** The [feature descriptor](/feature-descriptor/) and [feature matching](/feature-matching/) as a search in descriptor space.
2. **Corner detectors.** The [Moravec detector](/moravec-corner-detector/) with four shifts, the [Shi-Tomasi detector](/shi-tomasi-corner-detector/) with the smaller eigenvalue of the structure tensor, and the [FAST](/fast-corner-detector/) segment test on a circle of 16 pixels.
3. **Scale space and blob detectors.** The [scale space](/scale-space-representation/), [automatic scale selection](/automatic-scale-selection/) by normalized derivatives, the [DoG detector](/difference-of-gaussians-detector/), the [determinant of Hessian detector](/determinant-of-hessian-detector/), [SURF](/surf/) with box filters on an integral image, and [KAZE](/kaze-features/) with nonlinear diffusion.
4. **Invariance and covariant regions.** [Covariant and invariant local features](/invariant-local-features/), repeatability as the fraction of features found again, the [Harris-Laplace](/harris-laplace-detector/) and [Harris-affine](/harris-affine-detector/) detectors, and [maximally stable extremal regions](/maximally-stable-extremal-regions/).
5. **Histogram descriptors.** [HOG](/histogram-of-oriented-gradients/), [RootSIFT](/rootsift/), [DAISY](/daisy-descriptor/), the [shape context](/shape-context/) and [local binary patterns](/local-binary-patterns/).
6. **Binary features.** [BRIEF](/brief-descriptor/), [ORB](/orb-features/) and [BRISK](/brisk-features/), all compared by the Hamming distance.
7. **Filtering matches and searching fast.** [Lowe's ratio test](/lowe-ratio-test/), the [mutual nearest neighbor check](/mutual-nearest-neighbor-matching/), [best bin first search](/best-bin-first-search/) and the [randomized k-d forest](/randomized-kd-forest/).
8. **Learned detectors and matchers.** [SuperPoint](/superpoint/), [SuperGlue](/superglue/) and [LoFTR](/loftr/), judged on benchmarks.

## A first reading

Read these 10 entries in order:

1. feature descriptor;
2. feature matching;
3. Shi-Tomasi corner detector;
4. FAST corner detector;
5. scale space;
6. automatic scale selection;
7. DoG detector;
8. covariant and invariant local features;
9. BRIEF descriptor;
10. Lowe's ratio test.

Then read ORB, which joins FAST and BRIEF, and the mutual check. Skip at first the affine detectors, KAZE, DAISY, the shape context, the two search structures and the learned methods. Come back to the search structures when the number of features grows into the millions, and to the affine detectors when the views differ by a large slant.

## Before you start

The chapter builds on the image processing of Volume 28: the [digital image](/digital-image/), [linear filtering](/linear-filtering/), the [Gaussian filter](/gaussian-filter/), [feature detection](/feature-detection/) and [corner detection](/corner-detection/), the [Harris corner detector](/harris-corner-detector/), the [Laplacian of Gaussian](/laplacian-of-gaussian/), the [Gaussian pyramid](/gaussian-pyramid/), the [integral image](/integral-image/) and [SIFT](/sift/), which this chapter uses but does not repeat. The matchers need [nearest neighbor search](/nearest-neighbor-search/) (Volume 5), the [k-d tree](/kd-tree/) and the [priority queue](/priority-queue/) (Volume 3), and the [Hamming distance](/hamming-distance/) (Volume 24). Shape context matching uses the [Hungarian algorithm](/hungarian-algorithm/) (Volume 7), and the Shi-Tomasi detector uses the [eigenvalues](/eigenvalue/) of a symmetric $2 \times 2$ matrix (Volume 12). Repeatability is measured through a known [homography](/homography/), defined in Chapter 38.3.

The roadmap below lists every entry of the chapter with its kind and level, and the figure after it shows which entries lean on which.
