## What to remember

- A detector is covariant with a class of maps $T$ when it finds $T(R)$ in the moved image wherever it found $R$, and a descriptor is invariant when it gives the same vector for both. Each method holds this only for the class it is built for, and [repeatability](/detector-repeatability/), the number of repeated features divided by $\min(n_1, n_2)$ under a known homography, is a measurement on test images.
- The [Shi-Tomasi](/shi-tomasi-corner-detector/) score $\lambda_{\min}$ of the structure tensor is the smallest change of the window over all unit shifts; [Moravec](/moravec-corner-detector/) takes the minimum over four shifts only. [FAST](/fast-corner-detector/) calls a pixel a corner when $n$ contiguous pixels of the 16 on a circle of radius 3 are all brighter than $I_p + t$ or all darker than $I_p - t$; the quick test on pixels 1, 5, 9 and 13 is valid for $n = 12$ only.
- [Automatic scale selection](/automatic-scale-selection/) multiplies a derivative of order $m$ by $t^{m\gamma/2}$, so a structure $s$ times larger is selected at a scale $s^2$ times larger. A Gaussian blob of variance $t_0$ is found by the normalized determinant of the Hessian at $t = t_0$. The [DoG detector](/difference-of-gaussians-detector/) with $s$ intervals per octave builds $s + 3$ Gaussian and $s + 2$ DoG images, and compares each point with 26 neighbours.
- [SURF](/surf/) replaces the Gaussian second derivatives by box filters on an [integral image](/integral-image/): a box sum costs 4 lookups at any size, and a filter of side $L$ corresponds to $\sigma = 1.2L/9$.
- [HOG](/histogram-of-oriented-gradients/) on a $64 \times 128$ window with $8 \times 8$ cells, $2 \times 2$ blocks of stride one cell and 9 bins has $7 \cdot 15 \cdot 36 = 3780$ values. [LBP](/local-binary-patterns/) with $P = 8$ has 59 uniform labels, 10 rotation invariant uniform labels and 36 rotation invariant codes.
- Binary descriptors are compared by the Hamming distance with an exclusive or and a population count. [BRIEF](/brief-descriptor/) is not invariant to rotation; [ORB](/orb-features/) turns the tests by the angle of the intensity centroid in steps of $12°$; [BRISK](/brisk-features/) uses 512 bits.
- [RootSIFT](/rootsift/) is the square root of the L1-normalized SIFT vector, and then the squared Euclidean distance is $2 - 2H$, where $H$ is the Hellinger kernel.
- [Lowe's ratio test](/lowe-ratio-test/) keeps a match when $d_1 < 0.8\, d_2$; the threshold is a tuned choice and its effect is measured, not proved. The [mutual check](/mutual-nearest-neighbor-matching/) has no parameter and keeps each feature in at most one pair.
- [Best bin first](/best-bin-first-search/) search with no limit on the leaves is exact; with a limit it has no error bound. The learned [SuperPoint](/superpoint/), [SuperGlue](/superglue/) and [LoFTR](/loftr/) are judged on benchmarks.

| Method | Kind | Covariant or invariant to | Output |
|---|---|---|---|
| Shi-Tomasi | corner detector | shift, rotation of the response | points |
| FAST | corner detector | shift, turns by multiples of $90°$ | points |
| DoG | blob detector | shift, rotation, scale (approximately) | points with a scale |
| SURF | detector and descriptor | shift, rotation, scale | 64 values |
| Harris-affine | region detector | affine maps (approximately) | ellipses |
| MSER | region detector | affine maps, monotone intensity changes | regions |
| HOG | descriptor | small shifts, contrast | 3780 values for $64 \times 128$ |
| BRIEF | descriptor | shift, small turns | 256 bits |
| ORB | detector and descriptor | shift, rotation | 256 bits |
| BRISK | detector and descriptor | shift, rotation, scale | 512 bits |
| SuperGlue | learned matcher | as measured on benchmarks | a partial assignment |

: The main methods of the chapter and the maps each is built to follow.

## Choosing a method

For tracking from frame to frame in a video, the views change little, and the [Shi-Tomasi detector](/shi-tomasi-corner-detector/) with a tracker or FAST with a binary descriptor is enough. When the camera turns or the scale changes, use a detector with a scale and an orientation: [ORB](/orb-features/) or BRISK when time and memory are short (32 bytes per descriptor against 512 for SIFT in single precision), and SIFT, RootSIFT or SURF when the matches must survive large changes of scale and blur. For wide baselines with a strong slant, use the [Harris-affine detector](/harris-affine-detector/) or [MSER](/maximally-stable-extremal-regions/).

Filter every set of candidates with the [ratio test](/lowe-ratio-test/) or the mutual check before a geometric test. With more than a few hundred thousand descriptors, use a [randomized k-d forest](/randomized-kd-forest/) or another approximate search, and measure the fraction of true neighbors it finds. On a GPU, with scenes like the training data, the learned matchers often give more correct matches; on other scenes only a test tells.
